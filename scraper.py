from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import csv

def get_chrome_driver():
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')  # Start the browser maximized
    chrome_options.add_experimental_option("detach", True)  # Keep the browser open after the script finishes
    
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=chrome_options)

driver = get_chrome_driver()

reviews_list = []

base_url = "https://www.amazon.in/Apple-iPhone-15-128-GB/product-reviews/B0CHX1W1XY/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber="
for i in range(1, 11):
    url = base_url + f"{i}"
    print(f"Scraping page {i}")
    driver.get(url)
    driver.implicitly_wait(2)
    
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(2)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    soup = BeautifulSoup(driver.page_source, "html.parser")
    field = soup.find("div", class_="a-section a-spacing-none review-views celwidget")
    if field:
        reviews_elements = field.find_all("div", class_="a-section review aok-relative")
        print(f"Found {len(reviews_elements)} reviews on this page")

        for count, element in enumerate(reviews_elements):
            soup2 = BeautifulSoup(str(element), "html.parser")
            date = soup2.find("span", class_="a-size-base a-color-secondary review-date")
            reviewer_name = soup2.find("div", class_="a-profile-content")
            review = soup2.find("span", class_="a-size-base review-text review-text-content")
            stars = soup2.find("span", class_="a-icon-alt")
            model = soup2.find('a', class_="a-size-mini a-link-normal a-color-secondary")

            reviews_list.append([
                reviewer_name.text if reviewer_name else "",
                date.text if date else "",
                model.text if model else "",
                stars.text if stars else "",
                review.text.strip() if review else ""
            ])
    else:
        print(f"No reviews found on page {i}")

with open('Amazon_reviews_iphone15.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Reviewer Name', 'Date', 'Package(s)/model(s)', 'Stars', 'Reviews'])

    for review in reviews_list:
        writer.writerow(review)

print("CSV file created successfully!")
print(f"Total reviews scraped: {len(reviews_list)}")