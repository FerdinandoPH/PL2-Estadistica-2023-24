from googletrans import Translator
translator= Translator()
with open("Locomotora.csv","r") as f:
  lineas=f.readlines()[1:]
  with open("LocomotoraTraducida.csv","a") as a:
    a.write("country,mcnumber\n")
    a.close()
  for linea in lineas:
    lineasep=linea.split(',')
    trad=translator.translate(lineasep[0],src="es",dest="en").text
    print(trad)
    with open("LocomotoraTraducida.csv","a") as a:
      a.write(trad+","+lineasep[1])
      a.close()
  f.close()