-- Pagina de glifos que este mod acrescenta.
-- base 0x100 e espaco livre acima das paginas $60/$80 da ROM,
-- entao isto ADICIONA um alfabeto em vez de trocar o existente.
return {
  latin = {
    image = "assets/font/latin.png",
    base = 0x100,
    glyphsPerRow = 16,
  },
}
