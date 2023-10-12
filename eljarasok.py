def hanyados(a:int=1, b:int=1):
   if  b== 0:
      print(" 0-val nem lehet osztani kulonben pedig csinalja ugyan azt amit eddig")
   else:
      c: float = a / b
      print(f"{a} / {b} = {c: .2f}")