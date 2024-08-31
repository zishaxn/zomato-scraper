# Zomato-Scraper
A script that can scrape Restaurant information, menu items, and reviews using the restaurant link.

### Zomato

Zomato (/zoʊmɑːtoʊ/) is an Indian multinational restaurant aggregator and food delivery company founded by Pankaj Chaddah and Deepinder Goyal in 2008.

Zomato provides information, menus and user-reviews of restaurants as well as food delivery options from partner restaurants in select cities. 
The service is available in over 24 countries and in more than 10,000 cities. 

### Details of the Scraped data
This scraped dataset contains many attributes of the restaurant, such as:

- Name, Weblink, Open Hours, Address, Phone no, Price Range, Cuisine type.
- The Rating, Number of Ratings.
- Reviews - You can specify the max number of reviews to scrape for.
- Menu items - Description, Price and Tags.

### Ideas on how to use the data

- The Information can be used to form a catalogue of all restaurant in a given area.
- Create Geographical maps with the most famous cusine in a geo-location.
- The Menu items can be analysed to find which items are popular and gain insights to help to manage a restaurant.
- The Review data can be used to build a classification or sentiment-analysis algorithm.

### How to Run

- Clone the repo in your local machine
    `git clone `
- Install all the dependencies
    `pip3 install requirements.txt`
- Navigate to zomato-scraper
    `cd zomato-scraper`
- If you want to get specific data like only info,reviews or menu you can simply go to a specific file and run it.
    `python menu_scraper.py`

    ### Output

    - For reviews and menu a folder will be created as Menu and Reviews and CSV file will be stored with the name
        of the place.
    - For info a main CSV will be created, that will have info data of all the cafes / restaurants.

