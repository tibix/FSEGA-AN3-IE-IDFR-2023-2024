
library(rsample)
library(tidyverse)
library(caret)
library(corrplot)

data(attrition)
#draw distributions of numeric attributes

attrition %>%
  select_if(is.numeric)

attrition %>%
  ggplot(aes(Age)) +
  geom_density(show.legend = TRUE)

attrition %>%
  select_if(is.numeric) %>%
  gather(metric, value) %>%
  ggplot(aes(value, fill=metric)) +
  geom_density(show.legend = FALSE) +
  facet_wrap(~metric, scales = "free")

#convert some numerical attributes to factors
attrition <- attrition %>%
  mutate(
    JobLevel = factor(JobLevel),
    StockOptionLevel = factor(StockOptionLevel),
    TrainingTimesLastYear = factor(TrainingTimesLastYear)
  )

attrition <- attrition %>%
mutate(
  Attrition = factor(Attrition),
  BusinessTravel = factor(BusinessTravel),
  Department = factor(Department)
)


attrition <- attrition %>%
  mutate(
    Education = factor(Education),
    EducationField = factor(EducationField),
    EnvironmentSatisfaction = factor(EnvironmentSatisfaction),
    Gender = factor(Gender),
    JobInvolvement = factor(JobInvolvement),
    JobRole = factor(JobRole),
    JobSatisfaction = factor(JobSatisfaction),
    OverTime = factor(OverTime),
    PerformanceRating = factor(PerformanceRating),
    RelationshipSatisfaction= factor(RelationshipSatisfaction),
    WorkLifeBalance = factor(WorkLifeBalance)
  )

attrition <- attrition %>%
  mutate(
    MaritalStatus = factor(MaritalStatus)
  )
    

attrition %>%
  filter(Attrition == "No") %>%    # filter rows with Attrition == Yes
  select_if(is.numeric) %>%         # select numeric attributes
  cor() %>%
  corrplot::corrplot()

set.seed(123)
#initial_split comes from rsample package
split <- initial_split(attrition, prop = 0.7, strata = "Attrition") # the training and testing will be stratified according with Attrition
train <- training(split)
test  <- testing(split)

# to see that the divion of the data was done with stratification
table(train$Attrition)
table(test$Attrition)
table(attrition$Attrition)

features <- setdiff(names(train), "Attrition")
x <- train[,features]
y <- train$Attrition


fitControl <- trainControl(
  method = "cv",
  number= 10
)

modNbSimpleCV <- train(
  x = x,
  y = y,
  method = "nb",
  trControl = fitControl
)
modNbSimpleCV
confusionMatrix(modNbSimpleCV)

searchGrid <- expand.grid(
  usekernel = c(TRUE, FALSE),
  fL = 0.5,
  adjust = seq(0, 5, by = 1)
)

modNbCVSearch <- train(
  x = x,
  y = y,
  method = "nb",
  trControl = fitControl,
  tuneGrid = searchGrid
)
modNbCVSearch
confusionMatrix(modNbCVSearch)

modNbCVSearch$results %>%
  top_n(5, wt = Accuracy) %>%
  arrange(desc(Accuracy))

predSimple <- predict(modNbSimpleCV, test)
predProbSimple <- predict(modNbSimpleCV, test, type = "prob")
confusionMatrix(predSimple, test$Attrition)

pred <- predict(modNbCVSearch, test)
predProb <- predict(modNbCVSearch, test, type = "prob")
confusionMatrix(pred, test$Attrition)

library(pROC)
dataset <- data.frame(
  actual.class <- test$Attrition,
  probability <- predProb[,1]
  )
roc.val <- roc(actual.class ~ probability, dataset)
adf <- data.frame(  # creem un data frame nou pentru a putea face grafic cu ggplot
  specificity <- roc.val$specificities, 
  sensitivity <- roc.val$sensitivities)

datasetSimple <- data.frame(
  actual.class <-test$Attrition,
  probability <- predProbSimple[,1]
)
rocSimple.val <- roc(actual.class ~ probability, datasetSimple)
adfSimple <- data.frame(  # creem un data frame nou pentru a putea face grafic cu ggplot
  specificity <- rocSimple.val$specificities, 
  sensitivity <- rocSimple.val$sensitivities)


ggplot() + 
  geom_line(data=adfSimple, aes(specificity, sensitivity), color = 'blue') + 
  scale_x_reverse() + 
  theme(text = element_text(size=20))


#apply the hold-out procedure:
# train one model on the training set and apply it on the test set

searchOne <- expand.grid(
  usekernel = TRUE,
  fL = 0.5,
  adjust = 4
)
fitControlNone <- trainControl(
  method = "none"
)

modNbNone <- train(
  x = x,
  y = y, 
  method = "nb",
  trControl = fitControlNone,
  tuneGrid = searchOne
)
modNbNone
summary(modNbNone)

ggplot(modNbCVSearch)
ggplot(modNbCVSearch, metric = "Accuracy")





#pana in acest moment, Caret a incercat sa gaseasca cel mai bun model folosind acuraterea ca si metrica pentru compararea modelelor
#mai jos, putem schimba aceasta metrica si sa o inlocuim cu aria de sub curba ROC
fitControlROC <- trainControl(
  method = "cv",
  number= 10,
  classProbs = TRUE,
  summaryFunction = twoClassSummary,
  savePredictions = TRUE
)


modNbCVSearchROC = train(
  x = x,
  y = y, 
  method = "nb",
  trControl = fitControlROC,
  tuneGrid = searchGrid,
  metric = "ROC"
)
modNbCVSearchROC
confusionMatrix(modNbCVSearchROC)
modNbCVSearchROC$results %>%
  top_n(5, wt = ROC) %>%
  arrange(desc(ROC))

ggplot(modNbCVSearchROC, metric = "ROC")
