import os
import requests
import pandas as pd
import lxml.html as lh
from bs4 import BeautifulSoup
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.88 Safari/537.36"
}


def get_categories_and_items(url):
    """Fetches categories, their associated items, descriptions, prices, and images from the webpage"""
    response = requests.get(url, headers=headers)

    # Force the correct encoding
    response.encoding = "utf-8"

    webpage_content = (
        response.text
    )  # Get the text content after setting the correct encoding

    tree = lh.fromstring(webpage_content)

    categories = []
    items = []

    section_number = 2
    while True:
        category_xpath = f'//*[@id="root"]/div/main/div/section[4]/section/section[2]/section[{section_number}]/h4/text()'
        category = tree.xpath(category_xpath)
        if not category:
            break
        categories.append(category[0])

        item_xpath_base = f'//*[@id="root"]/div/main/div/section[4]/section/section[2]/section[{section_number}]/div[2]/div'
        item_count = len(tree.xpath(item_xpath_base))

        for i in range(1, item_count + 1):
            # XPath for the div containing item name, description, price, and image
            item_div_xpath = f"{item_xpath_base}[{i}]/div/div/div[2]/div/div"

            # Extract item name
            item_name_xpath = f"{item_div_xpath}/h4/text()"
            item_name = tree.xpath(item_name_xpath)

            # Initialize price variable
            item_price = "N/A"

            # Handle price extraction
            price_divs = tree.xpath(f"{item_div_xpath}/div")
            if len(price_divs) == 1:
                # Single div, price in the only div
                price_xpath = f"{item_div_xpath}/div/span/text()"
                if tree.xpath(price_xpath):
                    item_price = tree.xpath(price_xpath)[0]
            elif len(price_divs) > 1:
                # Multiple divs, price in the second div
                price_xpath = f"{item_div_xpath}/div[2]/span/text()"
                if tree.xpath(price_xpath):
                    item_price = tree.xpath(price_xpath)[0]
                else:
                    # Fallback for other potential locations if needed
                    price_xpath_fallback = f"{item_div_xpath}/div/span/text()"
                    if tree.xpath(price_xpath_fallback):
                        item_price = tree.xpath(price_xpath_fallback)[0]

            # Print the raw price before cleaning for debugging
            item_price = str(item_price)

            # Extract item description
            description_xpath = f"//*[@id='root']/div/main/div/section[4]/section/section[2]/section[{section_number}]/div[2]/div[{i}]/div/div/div[2]/p/text()"
            item_description = tree.xpath(description_xpath)
            item_description_text = item_description[0] if item_description else ""

            # Extract the full <img> element as a string
            image_xpath = f"//*[@id='root']/div/main/div/section[4]/section/section[2]/section[{section_number}]/div[2]/div[{i}]/div/div/div[1]/div[1]/img"
            img_element = tree.xpath(image_xpath)

            if img_element:
                item_image_element = etree.tostring(
                    img_element[0], pretty_print=True, encoding="unicode"
                )
                print(f"Full <img> element: {item_image_element}")
            else:
                item_image_element = "No Image"
                print("No Image found")

            # Append item details to the list
            print(item_price)
            price = str(str(item_price))
            if item_name:
                items.append(
                    {
                        "Category": category[0],
                        "Item_Name": item_name[0],
                        "Item_Description": item_description_text,
                        "Price": price,
                        "Image Element": item_image_element,
                    }
                )

        section_number += 1

    df = pd.DataFrame(items)
    return df


def save_df(name, df):
    """Save the dataframe, replacing if file already exists"""
    if not os.path.exists("Menu"):
        os.makedirs("Menu")
    file_path = f"Menu/{name}.csv"

    # Specify encoding when saving to CSV
    df.to_csv(file_path, index=True)


def get_menu(url, save=True):
    """Get all Menu Items from the passed url"""
    url += "/order"

    webpage = requests.get(url, headers=headers, timeout=5)
    restaurant_name = BeautifulSoup(webpage.text, "lxml").head.find("title").text[:-22]

    df = get_categories_and_items(url)

    if save:
        save_df(restaurant_name, df)
    return df


if __name__ == "__main__":
    link = "https://www.zomato.com/mumbai/grandmamas-cafe-juhu"
    dframe = get_menu(link, save=True)
