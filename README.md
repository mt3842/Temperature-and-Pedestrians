# Temperature and Pedestrians

This project is a data analysis project that aims to understand how temperature affects the pedestrian volume in Melbourne, Australia. In particular, we want to find out if a city’s maximum daily temperatures have an effect on the foot traffic in Melbourne. With data on pedestrian volumes gathered by sensors from all over the city in the years 2023 and 2024, we try to assess the effect of temperature on the pedestrian counts. Initial analyses through simple linear regression indicates that while temperature is indeed an important variable, it has only a small degree of explanatory power. A regression model with quadratic terms, which was selected via cross-validation, fit the data somewhat better and indicates that there is a peak in pedestrian traffic at 25 degrees Celsius with a decrease in both extreme heat and cold. Unfortunately, even the model with the quadratic terms explained only a small portion of the variation in the pedestrian volume which suggests that temperature is only a solitary variable of many that need to be considered in outdoor activity. More analysis and more variables need to be incorporated to explain the phenomenon of pedestrian activity better.


## Relevant Technologies

- Python
- R
- Statistical Methods: Linear Regression, Polynomial Regression, Cross-Validation
Data Visualization: Scatterplots, Descriptive Statistics

## Abstract 

Does the temperature affect if people choose to go outside and how long they spend outside? Using Melbourne, Australia as a test case, we find and model the relationship between the temperature and the number of pedestrians recorded by sensors within Melbourne. First, we performed a simple linear regression, finding that the temperature is a significant variable in predicting the number of pedestrians on a given day; yet, a simple linear model explains only a little of the variance of the number of pedestrians. Thus, we next explored a polynomial regression model, using cross-validation to choose the degree of the polynomial. As such, we fit a quadratic regression model, which better aligns with the scatterplot of the two variables than a linear model. This resulted in a slightly more promising model, yet still explaining a small percentage of the variance in the number of pedestrians recorded. While temperature is a factor, more is needed to explain more fully the number of pedestrians per day.
