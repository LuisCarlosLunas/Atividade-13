CalcEua={34:5,35:5.5,36:6,37:7,38:8.5,39:8,40:8.5,41:9.5,42:10.5,43:11.5,44:12.5}
def Conversor(numCalc):
  if numCalc<34 or numCalc>44:
    return "Número de calçado inválido!"
  else:
     return f"Tamanho BR:{numCalc}\nTamanho EUA:{CalcEua.get(numCalc)}\nTamanho Europa:{numCalc+2}\n"