data<-read.csv(file.choose())
str(data)
newdata <- data[which(data$age=='elder'),]
nrow(newdata)

tbc = table(newdata$Hypertension,newdata$Hyperlipidemia)
tbc                 # the contingency table

chisq.test(tbc, simulate.p.value = TRUE)

Phi<-sqrt(145.44/(nrow(newdata)))
Phi

#install.packages("GoodmanKruskal")
#library(GoodmanKruskal)
#varset1<- c("Hypertension","Hyperlipidemia")
#Frame1<- subset(data, select = varset1)
#GKmatrix1<- GKtauDataframe(Frame1)
#plot(GKmatrix1, corrColors = "blue")
#########################

     
tbl = table(newdata$Diabetes,newdata$Bronchitis)
tbl                 # the contingency table


chisq.test(tbl, simulate.p.value = TRUE)

Phic<-sqrt(4.50/(nrow(newdata)))
