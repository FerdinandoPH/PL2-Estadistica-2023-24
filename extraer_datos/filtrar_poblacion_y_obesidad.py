with open('poblacion_y_obesidad_original.csv', 'r') as f:
  lineas = f.readlines()
  for n,linea in enumerate(lineas):
    lineasep=linea.replace("\"","").split(',')
    valoresdelista=[lineasep[4],lineasep[1],lineasep[-1]]
    valoresdelista=map(str,valoresdelista)
    lineaAescribir=",".join(valoresdelista)
    print(lineaAescribir)
    with open ("poblacion_y_obesidad_limpio.csv","a") as a:
      a.write(lineaAescribir)
      a.close()
  f.close()