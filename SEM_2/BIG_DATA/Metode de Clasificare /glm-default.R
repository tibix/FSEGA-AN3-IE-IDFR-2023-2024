library(tidyverse)
library(modelr)
library(ISLR)
library(caret)
library(rsample)

data(Default)
names(Default)


#vizualizarea datelor
ggplot(Default) +
  geom_point(aes(x = balance, y = income, color = default, shape = default)) + 
  scale_shape_manual(values = c(1, 4)) +
  theme(text = element_text(size=20))

ggplot(Default) +
  geom_boxplot(aes(x = default, y = balance, fill = default)) +
theme(text = element_text(size=20))

ggplot(Default) +
  geom_boxplot(aes(x = default, y = income, fill = default)) +
  theme(text = element_text(size=20))


by_default <- group_by(Default, default)
summarize(by_default, count = n())

# crearea unui model simplu de regresie logistica: default in fct de balanta
mod <- glm(data = Default, default ~ balance, family = binomial)
summary(mod)

grid <- Default %>%
  data_grid(balance = seq_range(balance, 100)) %>%
    add_predictions(mod, "prob_default", type="response")

ggplot() +
  geom_line(data = grid, aes(balance, prob_default), color = "red", size = 2) 

nd <- tribble(~balance, 1000, 2000)
predicted <- predict(mod, newdata = nd, type = "response")

mod_income <- glm(data = Default, default ~ income, family = binomial)
summary(mod_income)

mod_student <- glm(data = Default, default ~ student, family = binomial)
summary(mod_student)

nd <- tribble(~student, "Yes", "No")
predicted <- predict(mod_student, newdata = nd, type = "response")

mod_all <- glm(data = Default, default ~ balance + income + student, family = binomial)
summary(mod_all)

mod_balance_student <- glm(data = Default, default ~ balance + student, family = binomial)
summary(mod_balance_student)

grid_students_yes <- Default %>%
  data_grid(balance = seq_range(balance, 100)) %>%
  mutate(student = "Yes") %>%
  add_predictions(mod_balance_student, "prob_default", type = "response")

grid_students_no <- Default %>%
  data_grid(balance = seq_range(balance, 100)) %>%
  mutate(student = "No") %>%
  add_predictions(mod_balance_student, "prob_default", type = "response")


ggplot(grid_students_yes, aes(balance, prob_default)) +
  geom_line(color = "blue", size = 2) +
  geom_line(data = grid_students_no, color = "orange", size = 2)

ggplot(Default, aes(x=student, y=balance, fill=student)) +
  geom_boxplot()

#realizarea unui task complet pentru rezolvarea problemei de clasificare
# pe baza setului de date disponibil

set.seed(123)
split <- initial_split(Default, prop = 0.7, strata = "default")
train <- training(split)
test <- testing(split)

mod_balance_student_train <- glm(data = train, default ~ balance + student, family = binomial)
summary(mod_balance_student_train)

pred_test <- predict(mod_balance_student_train, newdata = test, type = "response")
table(pred_test > 0.2, test$default)  #we identify just 25 defaulters from more than 100 in the test set


#perform classification analysis with caret
set.seed(123)
split <- initial_split(Default, prop = 0.7, strata = "default")
train <- training(split)
test <- testing(split)
table(test$default)
table(train$default)

features <- setdiff(names(Default),  "default")
x <- train[, features]
y <- train$default

fitControl <- trainControl(
  method = "cv",
  number = 10
)
modGLM_all <- train(
  x=x,
  y=y,
  method = "glm",
  family = "binomial",
  trControl = fitControl
)
modGLM_all
confusionMatrix(modGLM_all)
pred_all = predict(modGLM_all, newdata = test, type = "raw")
confusionMatrix(pred_all, test$default)

summary(modGLM_all)

xNoIncome <- x %>% select(-income)
modGLM_NoIncome <- train(
  x=xNoIncome,
  y=y,
  method = "glm",
  family = "binomial",
  trControl = fitControl
)
confusionMatrix(modGLM_NoIncome)
summary(modGLM_NoIncome)
pred_noIncome <- predict(modGLM_NoIncome, test)
confusionMatrix(pred_noIncome, test$default)
