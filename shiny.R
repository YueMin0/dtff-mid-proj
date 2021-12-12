library(shiny)

ui = fluidPage(
  titlePanel("Does our wealth grow with our life span?"),
  sidebarLayout(
    sidebarPanel(
      sliderInput(inputId = "year",
                  label = "Range of Year:",
                  min = 1952,
                  max = 2007,
                  value = c(1952,2007)),
      checkboxGroupInput(inputId = "contin",
                         label = "Continent",
                         choices = list("Africa",
                                        "America",
                                        "Asia",
                                        "Europe",
                                        "Oceania"),
                         selected = c("Africa",
                                      "America",
                                      "Asia",
                                      "Europe",
                                      "Oceania"))
    ),
    mainPanel(
      plotOutput(outputId = "plot"),
      textOutput(outputId = "select")
    )
  )
  
)


server = function(input, output) {

  output$plot = renderPlot({
    library(gapminder) 
    library(ggplot2)
    
    df = gapminder
    levels(df$continent) = c("Africa",
                             "America",
                             "Asia",
                             "Europe",
                             "Oceania")
    
    subdf = df[as.character(df$continent) %in% input$contin, ]
    subdf = subdf[subdf$year >= input$year[1], ]
    subdf = subdf[subdf$year <= input$year[2], ]
    
    g <- ggplot(subdf) + 
      geom_point(aes(x = gdpPercap, y = lifeExp, 
                     color = continent)) + 
      xlim(range(df$gdpPercap)) + ylim(range(df$lifeExp))
    
    g1 <- g + 
      labs(x =  'GDP per capita', 
           y = 'life expectancy',
           color = "",
           title = 'Life expectancy and GDP per capita',
           caption = 'dataset: gapminder') 
    g1
  }
    
  )
}

shinyApp(ui, server)
