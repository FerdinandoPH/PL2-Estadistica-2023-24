with open("big_mac_index_original.csv","r") as f:
  lineas=f.readlines()
  with open("big_mac_index_2023_limpio.csv","a") as a:
    a.write("name,adj_price\n")
    a.close()
  for linea in lineas:
    lineasep=linea.split(',')
    if "2023-07" in lineasep[0]:
      print(linea)
      with open("big_mac_index_2023_limpio.csv","a") as a:
        a.write(lineasep[3]+","+lineasep[8]+"\n")
        a.close()
  f.close()