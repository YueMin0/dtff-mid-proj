##--------------------------------------------------------------------
## Heatmap table
##--------------------------------------------------------------------

library(ztable)
library(magrittr)

temp = read.csv("C:\\Users\\yuema\\MidProj\\text\\presentation\\dataset\\1871_2020_temperature.csv")
decade = temp[,1]

temp = temp[,-1]
row.names(temp) = decade

options(ztable.type = "html")
z = ztable(temp)
z = vlines(z, 1)
z = hlines(z, 1)


z %>% makeHeatmap() %>% print(caption="Table 1. Switzerland Temperature - Monthly Average")


##--------------------------------------------------------------------
## Line plot
##--------------------------------------------------------------------

df = as.data.frame(cbind(1960:1980, JohnsonJohnson[1:21], JohnsonJohnson[22:42], JohnsonJohnson[43:63], JohnsonJohnson[64:84]))
colnames(df) = c("Year", "Q1", "Q2", "Q3", "Q4")


library(ggplot2)


cbPalette <- c("Q1" = "#009E73", "Q2" = "#0072B2", "Q3" = "#D55E00", "Q4" = "#CC79A7")


p = ggplot(data = df, aes(x = Year)) + 
  geom_line(aes(y = Q1, color = "Q1")) + 
  geom_line(aes(y = Q2, color = "Q2")) +
  geom_line(aes(y = Q3, color = "Q3")) +
  geom_line(aes(y = Q4, color = "Q4"))

p + labs(title = "Johnson & Johnson Quarterly Earnings Per Share 1960-1980", y = "Earnings ($)", color = "") +
  scale_color_manual(values = cbPalette) + 
  theme(legend.position = "bottom", legend.key = element_rect(fill = "white"))
  
