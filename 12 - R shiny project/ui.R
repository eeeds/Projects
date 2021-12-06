# Load libraries
library(shiny)
library(tidyverse)

# Application Layout
shinyUI(
  fluidPage(
    br(),
    #Application title
    titlePanel("Trends in Demographics and Income"),
    p("Explore the difference between people who earn less than 50K and more than 50K. You can filter the data by country, then explore various demogrphic information."),
    
    # Add first fluidRow to select input for country
    fluidRow(
      column(12, 
             wellPanel(
               selectInput("country", "Select a country",
                              choices = c("United-States", "Canada", "Mexico", "Germany", "Philippines"))
             )  # add select input 
             )
    ),
    
    # Add second fluidRow to control how to plot the continuous variables
    fluidRow(
      column(3, 
             wellPanel(
               p("Select a continuous variable and graph type (histogram or boxplot) to view on the right."),
               radioButtons("continuous_variable","Select a continuous variable: ", choices = c("age", "hours_per_week")),   # add radio buttons for continuous variables
               radioButtons("graph_type", "Select a graph type: ", choices = c("histogram","boxplot") )    # add radio buttons for chart type
               )
             ),
      column(9,
             plotOutput("p1"))  # add plot output
    ),
    
    #  Add third fluidRow to control how to plot the categorical variables
    fluidRow(
      column(3, 
             wellPanel(
               p("Select a categorical variable to view bar chart on the right. Use the check box to view a stacked bar chart to combine the income levels into one graph. "),
               radioButtons("categorial_variables", "Select categorical variables: ", choices = c("education", "workclass")),    # add radio buttons for categorical variables
               checkboxInput("is_stacked", "Bar is stacked or not. ", value = FALSE)     # add check box input for stacked bar chart option
               )
             ),
      column(9, plotOutput("p2"))  # add plot output
    )
  )
)