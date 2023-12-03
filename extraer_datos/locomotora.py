with open('obeso.csv', 'r') as f:
  lineas = f.readlines()
  for n,linea in enumerate(lineas):
    lineasep=linea.replace("\"","").split(',')
    valoresdelista=[lineasep[4],lineasep[1],lineasep[-1]]
    valoresdelista=map(str,valoresdelista)
    lineaAescribir=",".join(valoresdelista)
    print(lineaAescribir)
    with open ("obesofiltrado.csv","a") as a:
      a.write(lineaAescribir)
      a.close()
  f.close()