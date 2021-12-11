# Load libraries
library(shiny)
library(tidyverse)

# Read in data
adult <- read_csv("adult.csv")
# Convert column names to lowercase for convenience 
names(adult) <- tolower(names(adult))

# Define server logic
shinyServer(function(input, output) {
  
  df_country <- reactive({
    adult %>% filter(native_country == input$country)
  })

  #Create logic to plot histogram or boxplot
  output$p1 <- renderPlot({
    if (input$graph_type == "histogram") {
      # histogram
      ggplot(df_country(), aes_string(x =input$continuous_variable)) +
        geom_histogram(bins = 100, fill = "dodgerblue3") +  # histogram geom
        labs(y = "Number of adults", title = paste("Trend of", input$continuous_variable )) +  # labels
        facet_wrap(~prediction)    # facet by prediction
    }
    else {
      # boxplot
      ggplot(df_country(), aes_string(y = input$continuous_variable)) +
        geom_boxplot() +  # boxplot geom
        coord_flip()+  # flip coordinates
        labs(title = paste("How", input$continuous_variable,"value is spread")) +  # labels
        facet_wrap(~prediction)    # facet by prediction
    }

  })

  #Create logic to plot faceted bar chart or stacked bar chart
  output$p2 <- renderPlot({
    # Bar chart
    p <- ggplot(df_country(), aes_string(x =input$categorial_variables)) +
      labs(x="Categorial variables",y="Output") +  # labels
      theme(axis.text.x = element_text(angle = 45))    # modify theme to change text angle and legend position
    
    if (input$is_stacked) {
      p+geom_bar(aes(fill = prediction))   # add bar geom and use prediction as fill
    }
    else{
      p + 
        geom_bar(aes_string(fill=input$categorical_variables)) + # add bar geom and use input$categorical_variables as fill 
        facet_wrap(~prediction)   # facet by prediction
    }
  })
  
})