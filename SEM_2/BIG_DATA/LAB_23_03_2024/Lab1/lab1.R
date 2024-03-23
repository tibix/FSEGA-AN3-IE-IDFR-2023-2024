#variabile
A<-12
15->z
z
B=17
A
A[1] #orice variabila e un vector cu index pornind de la 1
class(A)
a=1
B=12L
class(B)

#operatori
2^3

3L/2L
8%/%3 #catul impartirii intregi
8%%3 #restul impartirii

a=5/+0 #infinit - calcul simbolic
a

exp(a)
exp(-a)

#vectori
a = 1:10

a
a[5]
a[-5]
a[2:5]
a[-(2:5)]

1:10 - 1
1:10*2
#pentru secvente reale 
seq(1,5,0.5) # sequence
rep(1,10) #vector de elemente identice - replicate

is.numeric(A)
is.integer(A)
is.integer(B)
is.numeric(B) #mostenire "integer" is "numeric"

#conversie de tip spre string
as.character(A)

#variabilele mediului
ls()

#variabile plus valoare
ls.str()
str(a)
z = NULL

#sterge variabila 
rm(z)
rm(list=ls())

#VECTORI
studenti = c("Ana","Cristina", "Bob")
studenti[1]
length(studenti)
#vector de indexi
studenti[c(1,3)]
studenti[1:2]
studenti[c(3,3)]

studenti[rep(2,10)]

#vectori etichetati
note = c(10,6,7,8,6)
discipline= c("informatica", "matematica", "engleza",
              "contabilitate", "finante")

names(note) = discipline
note
str(note)
note["informatica"]
note[c("informatica","engleza")]
note[]
note[TRUE]#asteapta un filtru pe indecsi
note[1==1]
1:5%%2==1
note[1:5%%2==1] #elementele de pe pozitii impare
note[2:3]
note[1:5%%2==0]

#variabilele sunt vectori
is.vector(studenti)
is.vector(note)
is.vector(A)
length(A)

note - 1

#MATRICE (tipuri de date omogene ca tip)
d = matrix(1:6,nrow=2)
d

matrix(1:6,nrow=2, byrow = TRUE)

matrix(1:3,nrow=2, ncol=3, byrow = TRUE)

cbind(1:3, 1:3)
rbind(1:3, 1:3)

m = rbind(matrix(1:6,nrow=2, byrow = TRUE), 1:3)
m

rownames(m) = c("x1","x2","x3")
m
colnames(m) = c("y1","y2","y3")
m
m[1,1]
m["x1",1]
m["x1", "y1"]
m[1,] #prima linie
m[,1] #prima coloana
t(t(m[,1]))
m["x1",]
m[,"y1"]
m[,1]

t(t(m[,1]))#prima coloana prin dubla transpunere
m
m[7]
length(m)
m[1:length(m)]
dim(m) #linii si coloane
dim(m)[1] #linii
dim(m)[2] #coloane
m[dim(m)[1]*dim(m)[2]] #ultimul element din matrice, colt dreapta jos
m[length(m)]

m
m[1:2,1:2]
m[c(TRUE,TRUE,FALSE), c(TRUE,TRUE,FALSE)]
m[2:3, c(TRUE,TRUE,FALSE)]
#sau
1:3
1:3>1
1:3<3
m[1:3>1, 1:3<3]
m[1:3!=2, 1:3!=2] #nu vrem a doua linie si a doua coloana

m
colSums(m)
t(t(rowSums(m)))
sum(colSums(m))
sum(rowSums(m))
sum(m)

length(m)
m
m*2
m
m - c(1,2,3)
m-c(1,2)


#FACTORI
days = c("Luni", "Marti", "Miercuri", "Joi", "Vineri", "Sambata", "Duminica")
days_factor = factor(days)
levels(days_factor)
str(days_factor)
days_factor2<-factor(days, levels=c("Luni","Marti","Miercuri", "Joi", "Vineri", "Sambata", "Duminica"))
levels(days_factor2)
days_factor3<-factor(days, levels=c("Luni","Marti","Miercuri", "Joi", "Vineri", "Sambata", "Duminica"), labels=c("L","Ma", "Mi",
                                                                                                                 "J", "V", "S", "D"))                     
levels(days_factor3)
days_factor[1]<days_factor[2]
days_factor4<-factor(days, ordered=TRUE, labels=c("L","Ma", "Mi", "J", "V", "S", "D"))
days_factor4[1]<days_factor4[2]
days_factor4[1]


#LISTE
Avatar<-list("James Cameron",2009,237)
names(Avatar)<-c("regizor", "an", "buget")
Avatar$regizor
is.character(Avatar$regizor)
is.vector(Avatar)
Avatar["regizor"]
Avatar[["regizor"]]
is.list(Avatar[1])
Avatar[[1]]

Passengers<-list(regizor="Morten Tyldum", an=2016, budget=150)
filmeUSA <-list(Avatar, Passengers, origine="USA")
filmeUSA[[3]]
is.list(filmeUSA[3])
filmeUSA$origine
filmeUSA[[3]]
filmeUSA["origine"]
filmeUSA[["origine"]]
filmeUSA$origine

filmeUSA[[c(1,1)]]
filmeUSA[[1]][[1]]

filmeUSA$subtitrare<-"Engleza"
length(filmeUSA)

filmeUSA[[5]]<-"Sci-Fi"
filmeUSA[[5]]<-NULL

#Data Frames
nume<-c("Ana","Bob", "Andrei", "Lucia", "Alex")
varsta<-c(30,32,28,27,29)
fumator<-c(FALSE,FALSE,FALSE,TRUE,TRUE)
df<-data.frame(nume,varsta,fumator)
View(df)
names(df)<-c("Nume", "Varsta", "Fumator")
df[3,]

View(df[c(3,5),c("Varsta", "Fumator")])

df$Varsta
df[["Varsta"]]
df[[2]]

greutate<-c(63,97,87,60,70)
df$Greutate <-greutate
df[["Greutate"]]<-greutate

Inaltime<-c(173,197,189,160,170) 
cbind(df,Inaltime)
df<- cbind(df,Inaltime)

ted<-data.frame(Nume="Ted", Varsta=67,Fumator=TRUE,Greutate=66,Inaltime=175)
df<-rbind(df,ted)
df

seq(10,1,-1)
sort(seq(10,1,-1))

sort(df$Nume)
sort(df$Varsta)
sort(df$Greutate, decreasing=TRUE)

df
poz<-order(df$Varsta)
poz
df[poz,]
order(df$Varsta, df$Nume)
df[3,2] <-32
df[order(df$Varsta, df$Nume),]

#TIBBLES
install.packages("tidyverse")
library(tidyverse)
tib = tibble(df)
tib

view(tib)

#Operatii de agregare
mean(tib$Varsta)
min(tib$Inaltime)

filter(tib, Varsta == 32)

tib %>% 
  filter(Varsta >= 32)

tib %>% 
  filter(Varsta >= 32) %>% 
  arrange(Inaltime)

tib %>% 
  filter(Varsta >= 32) %>% 
  arrange(desc(Inaltime)) %>%
  select(-Fumator)

tib %>% 
  filter(Varsta >= 32, Varsta <= 70) %>% 
  arrange(desc(Inaltime)) %>%
  select(-Fumator) %>%
  group_by(Varsta) %>%
  count()


tib %>% 
  filter(Varsta >= 32) %>% 
  arrange(desc(Inaltime)) %>%
  select(Varsta)

tib %>% 
  filter(Varsta >= 32) %>% 
  arrange(desc(Inaltime)) %>%
  select(Varsta) %>%
ggplot(aes(x=Varsta)) + geom_histogram()

table (tib %>% 
         filter(Varsta >= 32) %>% 
         arrange(desc(Inaltime)) %>%
         select(Varsta)) #tabela de frecvente

table (tib %>% 
         filter(Varsta >= 32) %>% 
         arrange(desc(Inaltime)) %>%
         select(Varsta))  #tabela de frecvente 
   
tib %>% 
  filter(Varsta >= 32) %>% 
  arrange(desc(Inaltime)) %>%
  select(-Fumator) %>%
  group_by(Varsta) %>%
  summarize(medie=mean(Inaltime))
