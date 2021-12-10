# Financial Analysis Web App
https://share.streamlit.io/mayurk1/fin-web-app-final-project/webApp.py 

# 1. Project Description
This project is a technical analysis web app made using the Streamlit framework. It allows for a user to perform various analysis methods given a ticker and input parameters. The following indicators are supported: Moving Average, Exponential Moving Average, and Moving Average Convergence Divergence. Additionally, a function to plot Moving Average crossovers of user provided windows is also provided (extra credit?). The app allows for charts with the range of current date and up to 999 days in the past.

# 2. Project Selection
I chose this project as I enjoy analyzing stock data and wanted to learn more about making a web app with visualizations. Through making this app, I learned the basics of web app development and how to use various frameworks. Additionally, I leveraged Python libraries and APIs to collect stock data. I learned how to develop a data collection and analysis pipeline using a stock data API. Finally, I learned how to apply Classes to a real world application through this project.

# 3. Future Considerations
If I had an opportunity to redo this project, I would make the visualizations more robust by allowing for user manipulation. Further, in order to improve performance and memory, I would implement a caching feature to prevent unnecessary API calls. These changes would be made in order to improve the quality of the data visualizations and provide a long term solution for this web app given the limitations of the free API. Further, I would use a more robust API as the current one is limited in number of calls and does not adjust historic data for stock split prices.

# 4. How to Run the Web App
The web app is currently hosted on the Streamlit servers at the following URL:

https://share.streamlit.io/mayurk1/fin-web-app-final-project/webApp.py

No additional setup or changes should be needed in order for the app to run.
## How to Use the Web App
To start, enter a ticker in the text box in the sidebar (if the sidebar is not visible, press the arrow in the top left corner). SPY is set as the default value if no input is provided. Next, select the type of Technical Analysis you would like to do. Depending on the selection, a set of parameters will be provided below. Next, provide the delta value, which is the number of days from the current day to collect data on. The application will pull the daily adjusted closing values of the provided ticker. Next, adjust the sliders for the given Technical Analysis selection. There are default values for some TAs. In order to revert them, select a different dropdown item and select the original again.

Please wait ~1 second after hitting 'Run' for the app the update.

API Limitations: due to the limitations of the (free) API, historic stock price data is NOT retroactively updated for stock splits.

NOTE: please enter logical selections, if a specific chart is not possible, the system will not graph the line. Hit 'Run' to create a new graph after updating the inputs. 

If an incorrect ticker is provided, the system will display an error message. In order to clear this, provide valid inputs in the sidebar and hit 'Run' again.

# 5. Challenges 
The main challenge of this project was finding and using an appropriate framework. Having tried Flask and Django before settling on Streamlit, the process of creating a web app can be very tedious. Further, creating and setting up the proper logic was difficult as I had to account for various user inputs and selections, without having the entire page crash. One of the biggest issues I faced was a proper implementation of updating the sidebar fields given the user selection. I overcame these issues by implementing a Streamlit form in order to prevent user inputs from conflicting with each other.

# 6. Cited Sources
The official documentations of the Streamlit, Alpaca, and numpy APIs were extensively used. The Streamlit documentation greatly helped in the formulation of the web app elements and implementation of the logic. The Alpaca Markets API and documentation was used in order to pull market data. Finally, the third resource was used to assist in the creation of moving average plots from stock data.

https://docs.streamlit.io/ 
https://alpaca.markets/docs/
https://www.datacamp.com/community/tutorials/moving-averages-in-pandas

# Description of Files
### webApp.py
Main web app driver file. Contains the page objects and form logic.

### tradingMethods.py
Class to perform the technical analysis functions. Takes in ticker, deltas, and related features.

### config.py
Holds references to API keys.

### requirements.txt
Necessary Python libraries.