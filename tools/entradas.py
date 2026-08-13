"""Pontos de entrada de script, com os tipos que NAO sao bytecode respeitados.

O byte de funcao de um bg_event e o de um object_event decidem o que o
ponteiro e.  Andar sobre um ponteiro que aponta para dados desmonta os bytes
como se fossem comandos, segue o salto que o ruido acaba soletrando, e produz
tanto as travadas de "opcode desconhecido" quanto o lixo kana no texto.

Isto espelha RomExtractorGen2:extractScriptsAndText.
"""

MAP_LENGTH = 9
WARP_LENGTH, COORD_LENGTH, BG_LENGTH, OBJECT_LENGTH = 5, 8, 5, 13

BGEVENT_ITEM = 7                       # aponta para `hiddenitem item, flag`
OBJECTTYPE_ITEMBALL, OBJECTTYPE_TRAINER = 1, 2

PB, PA = 37, 0x40ED                    # MapGroupPointers


def ok(bank, addr):
    return addr is not None and addr != 0 and (addr >= 0x4000 or bank == 0)


def coletar(usa, br, groups, somente=None):
    """`somente` = (grupo, indice) restringe a um unico mapa.

    Sem isso, pedir um mapa varre todos os indices do grupo ate ele, e a
    contagem por local sai inflada com o que veio dos vizinhos.
    """
    return _coletar(usa, br, groups, somente)


def _coletar(usa, br, groups, somente=None):
    """-> (starts, textos)

    starts : [(bank, addr)]              scripts para andar
    textos : [(bank, addr_usa, addr_br)] texto lido direto, sem andar
    """
    starts, textos = [], []

    def texto(bank, a_usa, a_br):
        if ok(bank, a_usa) and ok(bank, a_br):
            textos.append((bank, a_usa, a_br))

    for group, nmaps in sorted(groups.items()):
        gp = usa.word(PB, PA + (group - 1) * 2)
        if gp is None:
            continue
        for mi in range(1, nmaps + 1):
            if somente and (group, mi) != somente:
                continue
            entry = gp + (mi - 1) * MAP_LENGTH
            ab, aa = usa.byte(PB, entry), usa.word(PB, entry + 3)
            if not ab or not aa or aa < 0x4000:
                continue
            bank = usa.byte(ab, aa + 6)          # banco dos scripts do mapa
            sa = usa.word(ab, aa + 7)
            ea = usa.word(ab, aa + 9)
            if not bank:
                continue

            # cabecalho de scripts: db cenas; {dw script, dw filler} xN;
            #                       db callbacks; {db tipo, dw script} xM
            if sa and sa >= 0x4000:
                n = usa.byte(bank, sa)
                if n is not None and n < 32:
                    for si in range(n):
                        s = usa.word(bank, sa + 1 + si * 4)
                        if ok(bank, s):
                            starts.append((bank, s))
                    cb = sa + 1 + n * 4
                    m = usa.byte(bank, cb)
                    if m is not None and m <= 5:   # NUM_MAPCALLBACK_TYPES
                        for ci in range(m):
                            s = usa.word(bank, cb + 1 + ci * 3 + 1)
                            if ok(bank, s):
                                starts.append((bank, s))

            if not (ea and ea >= 0x4000):
                continue
            c = ea + 2                              # db 0, 0 ; filler
            nw = usa.byte(bank, c) or 0
            c += 1 + nw * WARP_LENGTH

            nc = usa.byte(bank, c) or 0
            c += 1
            for _ in range(nc):
                s = usa.word(bank, c + 4)
                if ok(bank, s):
                    starts.append((bank, s))
                c += COORD_LENGTH

            nb = usa.byte(bank, c) or 0
            c += 1
            for _ in range(nb):
                kind = usa.byte(bank, c + 2)
                p_usa = usa.word(bank, c + 3)
                p_br = br.word(bank, c + 3)
                if kind == BGEVENT_ITEM:
                    pass                            # item oculto: nao e bytecode
                elif kind in (5, 6):                # conditional_event: dw ev, dw script
                    if p_usa and p_usa >= 0x4000:
                        s_u = usa.word(bank, p_usa + 2)
                        if ok(bank, s_u):
                            starts.append((bank, s_u))
                elif ok(bank, p_usa):
                    starts.append((bank, p_usa))
                c += BG_LENGTH

            no = usa.byte(bank, c) or 0
            c += 1
            for _ in range(no):
                palType = usa.byte(bank, c + 7) or 0
                otype = palType % 16
                s_u = usa.word(bank, c + 9)
                s_b = br.word(bank, c + 9)
                if otype == OBJECTTYPE_ITEMBALL:
                    pass                            # dois bytes crus
                elif otype == OBJECTTYPE_TRAINER:
                    # struct `trainer`: os ponteiros de texto ficam em +5, +7
                    # e +9 (visto / vitoria / derrota).  O script propriamente
                    # dito vem depois; aqui interessa o dialogo.
                    if s_u and s_u >= 0x4000 and s_b and s_b >= 0x4000:
                        for off in (5, 7, 9):
                            texto(bank, usa.word(bank, s_u + off),
                                  br.word(bank, s_b + off))
                elif ok(bank, s_u):
                    starts.append((bank, s_u))
                elif s_u and s_u < 0x4000:
                    starts.append((0, s_u))         # ObjectEventText, em ROM0
                c += OBJECT_LENGTH

    # StdScripts
    for i in range(64):
        s = usa.word(64, 0x4000 + i * 2)
        if ok(64, s):
            starts.append((64, s))

    return starts, textos
