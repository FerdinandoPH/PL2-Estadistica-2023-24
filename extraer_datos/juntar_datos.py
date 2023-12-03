with open("numero_de_McDonalds.csv","r") as f:
  lineas=f.readlines()
  with open("datos_finales_sin_traducir.csv","w") as a:
    a.write("country,mcnumber,Population,PersonPerMc,BigMacAdjusted,Obesity\n")
    a.close()
  lineas=sorted(lineas[1:])
  for linea in lineas:
    lineasep=linea.split(',')
    lineasep[1]=lineasep[1].replace('\n','')
    popu="NA"
    ppmc="NA"
    obesidad="NA"
    bigmac="NA"
    with open("poblacion_y_obesidad_limpio.csv","r") as o:
      lineaso=o.readlines()[1:]
      encontrado=False
      for lineao in lineaso:
        lineaosep=lineao.split(',')
        if lineasep[0]==lineaosep[0]:
          encontrado=True
          popu=lineaosep[1]
          ppmc=str(round(int(lineaosep[1])/int(lineasep[1]),2))
          obesidad=lineaosep[2].replace('\n','')
          break
      if not encontrado:
        print("INDICE DE OBESIDAD NO ENCONTRADO PARA", lineasep[0])
      o.close()
    with open("big_mac_index_2023_limpio.csv","r") as p:
      lineasp=p.readlines()[1:]
      encontrado=False
      for lineap in lineasp:
        lineapsep=lineap.split(',')
        if lineasep[0]==lineapsep[0]:
          encontrado=True
          bigmac=str(round(float(lineapsep[1].replace('\n','')),2))
          break
      if not encontrado:
        print("BIG MAC NO ENCONTRADO PARA", lineasep[0])
      p.close()
    with open("datos_finales_sin_traducir.csv","a") as a:
      a.write(lineasep[0]+","+lineasep[1]+","+popu+","+ppmc+","+bigmac+","+obesidad+"\n")
      a.close()
  f.close()