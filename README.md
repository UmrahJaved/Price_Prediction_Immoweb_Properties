# **Price_Prediction_Immoweb_Properties**

Creating a live server using Flash API for Price Prediction of Houses in Belgium. The data was scrapped from Immoweb.be, cleaned, explored and used Machine Learning to predict the price of the houses.

## Scrapping Dataset

With ´BeautifulSoup´, we extracted data from different URLs collected from Immoweb.be and stored all the informations in a csv file.
* Link for Repo: `https://github.com/UmrahJaved/challenge-collecting-data`.
But for Price Prediction model we use different dataset from different team for learning purpose.
* Link for Repo: `https://github.com/adityachugh02/challenge-collecting-data`

## Data Analysis

The scrapped data was cleaned and analysed to gain insights about the dataset. The codes for data cleaning and analysis are shared below:
* Data Cleaning : `https://github.com/UmrahJaved/challenge-data-analysis`
* Data Analysis : `https://github.com/adityachugh02/challenge-data-analysis`

## Price Prediction

Using 'Linear Regression', we predict the price of house property in Belgium. Th model is taken as an input in Flask API and predicted price is the JSON output. Finally, the API is deployed  on 'Heroku' with the help of 'Docker Container'. You can find the code in `challenge-api-deployment` folder. 


Link for the live server on Heroku : `https://prediction-umrah.herokuapp.com/predict`
