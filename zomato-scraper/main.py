from info_scraper import get_restaurant_info
from review_scraper import get_reviews
from menu_scraper import get_menu


def scrape_all_data(url_list):
    """Scrapes all data from the urls passed """

    get_restaurant_info(url_list=url_list, file_name="Restaurants.csv")
    for url in url_list:
        get_reviews(url=url, max_reviews=50, sort="popular", save=True)
        get_menu(url)


if __name__ == '__main__':
    urls = [
        # "https://www.zomato.com/mumbai/pizza-bites-1-hill-road-bandra-west",
        "https://www.zomato.com/SmokeHouseDeli-Pali",
    ]
    scrape_all_data(urls)
