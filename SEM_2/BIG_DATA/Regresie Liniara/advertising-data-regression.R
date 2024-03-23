library(tidyverse)
library(modelr)
library(scatterplot3d)

Advertising <- read_csv("Advertising.csv")  # reads the data from the csv file

Advertising <- select(Advertising, TV:sales) # drop out the first column from the dataset

Advertising %>%
  ggplot(aes(TV, sales)) + geom_point() 

Advertising %>%
  ggplot(aes(radio, sales)) + geom_point() + geom_smooth()

Advertising %>%
  ggplot(aes(newspaper, sales)) + geom_point() + geom_smooth()

#learn the linear regression of sales on TV spendings 
mod_sales_TV <- lm(data = Advertising, sales ~ TV)    
summary(mod_sales_TV)

#plot the data against the learned regression line
grid_TV <- Advertising %>%  # builds a novel grid with 100 points, adding predictions
  data_grid(TV = seq_range(TV, 100)) %>%
  add_predictions(mod_sales_TV, "sales")

ggplot(Advertising, aes(TV, sales)) + 
  geom_point() +  # plot the advertising data
  geom_line(data = grid_TV, color = "red", size = 1) # plot the predictions

confint(mod_sales_TV)  # confidende interval for regression parameters

mod_sales_radio <- lm(data = Advertising, sales ~ radio)    
summary(mod_sales_radio)

mod_sales_newspaper <- lm(data = Advertising, sales ~ newspaper)    
summary(mod_sales_newspaper)

confint(mod_sales_newspaper)

grid_radio <- Advertising %>%  # builds a novel grid with 100 points, adding predictions
  data_grid(radio = seq_range(radio, 100)) %>%
  add_predictions(mod_sales_radio, "sales")
ggplot(Advertising, aes(radio, sales)) + 
  geom_point() +  # plot the advertising data
  geom_line(data = grid_radio, color = "blue", size = 1) # plot the predictions


grid_newspaper <- Advertising %>%  # builds a novel grid with 100 points, adding predictions
  data_grid(newspaper = seq_range(newspaper, 100)) %>%
  add_predictions(mod_sales_newspaper, "sales")
ggplot(Advertising, aes(newspaper, sales)) + 
  geom_point() +  # plot the advertising data
  geom_line(data = grid_newspaper, color = "yellow", size = 2) # plot the predictions

mod_sales_all <- lm(data = Advertising, sales ~ TV + radio + newspaper) 
summary(mod_sales_all)

mod_sales_TV_radio <- lm(data = Advertising, sales ~ TV + radio)
summary(mod_sales_TV_radio)

s3d <- scatterplot3d(Advertising$TV, Advertising$radio, Advertising$sales, type="p") 
s3d$plane3d(mod_sales_TV_radio, lty.box = "solid")

newspendings <- tibble(
  TV = 100,
  radio = 20
)
predict(mod_sales_TV_radio, newdata = newspendings, interval = "confidence")
predict(mod_sales_TV_radio, newdata = newspendings, interval = "prediction")

mod_sales_TV_radio_interaction <- lm(data = Advertising, sales ~ TV * radio)
summary(mod_sales_TV_radio_interaction)
