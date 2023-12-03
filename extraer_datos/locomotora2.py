with open("obesofiltrado.csv","r") as f:
  
  lineas = f.readlines()
  lineaprimera=lineas[0]
  restodelinas=sorted(lineas[1:])
  with open ("obesofiltradoordenado.csv","w") as a:
    a.write(lineaprimera)
    a.writelines(restodelinas)
    a.close()
  f.close()