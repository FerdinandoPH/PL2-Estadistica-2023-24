datos <- read.csv("datos_finales.csv", header = TRUE)
headers <- colnames(datos)
titulos <- c("Personas por McDonalds", "Precio del Big Mac ajustado a la RPC", "Porcentaje de obesidad (IMC>30)")
print("#####ESTADISTICAS UNIDIMENSIONALES#####")
for (i in 4:length(headers)) {
  categoria <- titulos[i - 3]
  print(paste("# Columna:", categoria, "#"))
  datos_sin_na <- datos[, headers[i]][!is.na(datos[, headers[i]])]
  print("Datos de la columna (excluyendo NA):")
  print(datos_sin_na)
  print(noquote("---Medidas---"))
  resumen <- summary(datos[, headers[i]])
  tabla <- data.frame("NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA")
  colnames(tabla) <- c("Mínimo", "1er Cuartil", "Mediana", "Media", "Varianza,", "D.típica", "3er Cuartil", "Máximo", "Rango")
  for (i in 1:4){
    tabla[i] <- round(resumen[i], 2)
  }
  tabla[5] <- round(var(datos_sin_na) * (length(datos_sin_na) - 1) / length(datos_sin_na), 2)
  tabla[6] <- round(sd(datos_sin_na) * sqrt((length(datos_sin_na) - 1) / length(datos_sin_na)), 2)
  for (i in 7:8){
    tabla[i] <- round(resumen[i - 2], 2)
  }
  tabla[9] <- round(diff(range(datos_sin_na)), 2)
  hist(datos_sin_na, main = categoria, xlab = categoria, ylab = "Frecuencia", col = "yellow", border = "red", breaks = 10)
  boxplot(datos_sin_na, main = categoria, xlab = categoria, ylab = "Frecuencia", col = "yellow", border = "red")
  print(tabla)
}
print("#####ESTADISTICAS BIDIMENSIONALES#####")
print("#Personas por Mcdonalds frente al porcentaje de obesidad#")
plot(datos$PersonasporMc, datos$Obesidad, xlab = "Personas por Mcdonalds", ylab = "Porcentaje de obesidad", main = "Porcentaje de obesidad frente al número de personas por Mcdonalds", col = "red", pch = "+")
lm_po <- lm(datos$Obesidad ~ datos$PersonasporMc)
lm_po
paste(noquote("Correlación entre el porcentaje de obesidad y el número de personas por Mcdonalds de cada país:"), cor(datos$PersonasporMc[!is.na(datos$PersonasporMc)], datos$Obesidad[!is.na(datos$Obesidad)]))
abline(lm_po, col = "#fcc706")
print("#Big Mac Ajustado frente al porcentaje de obesidad#")
plot(datos$BigMacAjustado, datos$Obesidad, xlab = "Big Mac Ajustado", ylab = "Porcentaje de obesidad", main = "Precio del Big Mac Ajustado a la RPC frente al porcentaje de obesidad", col = "red", pch = "+")
lm_bo <- lm(datos$Obesidad ~ datos$BigMacAjustado)
lm_bo
noquote(paste(noquote("Correlación entre el porcentaje de obesidad y el precio del Big Mac ajustado a la RPC de cada país:"), cor(datos$BigMacAjustado[!is.na(datos$BigMacAjustado)], datos$Obesidad[!is.na(datos$Obesidad)])))
abline(lm_bo, col = "#fcc706")
print("#Personas por Mcdonalds frente al precio del Big Mac Ajustado#")
plot(datos$BigMacAjustado, datos$PersonasporMc, xlab = "Precio del Big Mac ajustado", ylab = "Personas por Mcdonalds", main = "Precio del Big Mac ajustado a la RPC vs  personas por McDonalds", col = "red", pch = "+")
lm_bp <- lm(datos$PersonasporMc ~ datos$BigMacAjustado)
lm_bp
noquote(paste(noquote("Correlación entre el número de personas por Mcdonalds y el precio del Big Mac ajustado de cada país:"), cor(datos$BigMacAjustado[!is.na(datos$BigMacAjustado)], datos$PersonasporMc[!is.na(datos$PersonasporMc)])))
abline(lm_bp, col = "#fcc706")
print("#####ESTADISTICAS MULTIDIMENSIONALES#####")
#Obesidad: variable dependiente, Personas por Mcdonalds y Big Mac Ajustado: variables independientes
reg_lin_multiple <- lm(formula = datos$Obesidad ~ datos$PersonasporMc + datos$BigMacAjustado)
summary(reg_lin_multiple)
