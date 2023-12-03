from googletrans import Translator
translator= Translator()
with open("LocomotoraFinal.csv","r") as f:
  lineas=f.readlines()[1:]
  with open("LocomotoraFinalTraducida.csv","a") as a:
    a.write("Pais,Numeromc,Poblacion,PersonaporMc,BigMacAjustado,Obesidad\n")
    a.close()
  for linea in lineas:
    lineasep=linea.split(',')
    trad=translator.translate(lineasep[0],src="en",dest="es").text
    print(trad)
    with open("LocomotoraFinalTraducida.csv","a") as a:
      a.write(trad+","+lineasep[1]+","+lineasep[2]+","+lineasep[3]+","+lineasep[4]+","+lineasep[5])
      a.close()
  f.close()