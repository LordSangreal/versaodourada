"""Decodificador de texto Gen 2, fiel a RomExtractorGen2:decodeGen2Text."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
_MF = json.load(open(os.path.join(HERE, "repo", "tools", "rom_manifest_gold.json"),
                     encoding="utf-8"))
CHARMAP = {int(k): v for k, v in _MF["charmap"].items()}

# acentos que a traducao BR acrescentou, lidos dos glifos da fonte da ROM
BR_ACCENTS = {
    0xBA: "á", 0xBB: "â", 0xBC: "ã", 0xBD: "à", 0xBE: "ê", 0xBF: "í",
    0xC0: "ó", 0xC1: "ô", 0xC2: "õ", 0xC3: "ú", 0xC4: "ç", 0xEA: "é",
    0xCB: "Á", 0xCD: "Í", 0xCE: "Â", 0xD0: "Ê", 0xD5: "Ã", 0xD6: "Õ",
    0xD7: "É", 0xCC: "Ó",
    # Mais tres que a traducao BR tomou de ligaduras inglesas pouco uteis em
    # portugues.  Deduzidos por contexto, com o validador de 18 colunas
    # apontando as palavras quebradas:
    0xD4: "Ç",   # era "'s".  COMUNICA+C+OES, ESTA+C+AO, DAN+C+A, CABE+C+ADA
    0xD1: "Ô",   # era "'l".  M+O+NICA
    0xC5: "º",   # era "ü".   4+o+ ANDAR, {STRBUF}+o+ premio
    # Macros e ligaduras que a traducao BR redefiniu para caber nas 18
    # colunas.  Nao sao glifos: cada byte expande para varios caracteres.
    # Cada um foi deduzido cruzando o ingles alinhado com o portugues:
    0x5C: "TA",        # RO+TA, BICICLE+TA, FLORES+TA
    0x5B: "ÃO",        # GR+AO / GR+AO+S, onde o ingles diz BERRY
    0x5D: "POKéMON",   # "CENTRO _", "GINASIO _", "seus _S"
    # Os dois bytes de LIGADURA do charmap original -- um byte so que ja
    # valia dois glifos, e que a traducao BR reaproveitou:
    0x4A: "DO",        # era <PK><MN>.  GYARA+DO+S, "LABORATORIO DO PROFESSOR"
    0x24: "QU",        # era <PO><KE>.  +QU+EM, PSI+QU+ICO, E+QU+IPE
    0x56: "DADE",      # era <……>.  CI+DADE NEW BARK, na placa da cidade
    # NAO mapear 0xE1/0xE2 (<PK>/<MN>) nem 0x70/0x71 (<PO>/<KE>): sao glifos
    # legitimos e distintos.  Quem aparece no texto BR e a ligadura acima.
}
BR_CHARMAP = dict(CHARMAP)
BR_CHARMAP.update(BR_ACCENTS)

TEXT_NO_GLYPH = {0x05, 0x07, 0x0A, 0x0B, 0x0D, 0x0E, 0x0F, 0x10, 0x11, 0x12,
                 0x13, 0x15}


def decode(rom, bank, address, br=False):
    """Devolve (texto, ok). rom e um objeto com .byte(bank, addr)."""
    cm = BR_CHARMAP if br else CHARMAP
    out = []
    i = 0
    hops = 0
    in_string = False
    while i < 4096:
        b = rom.byte(bank, address + i)
        if b is None:
            return "".join(out), False
        # Um byte que a traducao BR reaproveitou vale mais que qualquer caso
        # especial daqui de baixo.  Sem esta precedencia, a cadeia de elifs
        # atropelava o mapa BR: 0x56 virava reticencias antes de alguem
        # perguntar ao charmap, e a placa de New Bark saia "CI...... NEW BARK"
        # em vez de "CIDADE NEW BARK".
        if br and b in BR_ACCENTS:
            out.append(BR_ACCENTS[b])
            i += 1
            continue
        if b == 0x50:
            if not in_string:
                break
            in_string = False
        elif b in (0x57, 0x58):
            break
        elif b == 0x00:
            in_string = True
        elif b == 0x16 and not in_string:
            far_addr = rom.word(bank, address + i + 1)
            far_bank = rom.byte(bank, address + i + 3)
            hops += 1
            if (hops > 8 or not far_bank or far_bank > 0x7F
                    or far_addr is None or far_addr < 0x4000 or far_addr >= 0x8000):
                break
            bank, address, i = far_bank, far_addr, -1
        elif b == 0x01:
            out.append("{STRBUF}")
            i += 2
        elif b in (0x4E, 0x4F):
            out.append("\n")
        elif b == 0x51:
            out.append("\f")
        elif b == 0x55:
            out.append("\v")
        elif b == 0x52:
            out.append("{PLAYER}")
        elif b == 0x53:
            out.append("{RIVAL}")
        elif b == 0x54:
            out.append("POKé")
        elif b == 0x06:
            pass
        elif b == 0x09 and not in_string:
            out.append("{NUM}")
            i += 3
        elif b == 0x14 and not in_string:
            out.append("{STRBUF}")
            i += 1
        elif b == 0x0C and not in_string:
            i += 1
        elif (not in_string) and b in TEXT_NO_GLYPH:
            pass
        else:
            ch = cm.get(b)
            if ch and not ch.startswith("<"):
                out.append(ch)
            elif ch == "<……>" or b == 0x56:
                out.append("……")
            elif ch:
                out.append(ch)
        i += 1
    return "".join(out), True


def is_texty(s, minlen=3):
    if len(s) < minlen:
        return False
    letters = sum(1 for c in s if c.isalpha())
    return letters >= max(2, int(len(s) * 0.4))


def key(bank, addr):
    return "%02x:%04x" % (bank, addr)
