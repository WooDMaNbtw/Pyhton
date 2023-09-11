import time
import undetected_chromedriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import json


def get_data(url="https://www.avito.ru/moskva/kvartiry/prodam-ASgBAgICAUSSA8YQ?context"
                       "=H4sIAAAAAAAA_0q0MrSqLraysFJKK8rPDUhMT1WyLrYyNLNSKk5NLErOcMsvyg3PTElPLVGyrgUEAAD__xf8iH4tAAAA"
                       "&p="):
    # options = webdriver.ChromeOptions()
    # options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
    #                      f'Chrome/114.0.0.0 Safari/537.36')
    # options.add_argument("--disable-blink-features=AutomationControlled")
    # # options.headless = True
    #
    # service = Service(executable_path="/chromedriver/chromedriver")
    # driver = webdriver.Chrome(options=options, service=service)

    driver = undetected_chromedriver.Chrome(headless=True)

    try:
        for page in range(1, 2):
            driver.get(url=f"{url}{page}")
            time.sleep(5)
            result = {}

            src = driver.page_source
            soup = BeautifulSoup(src, "lxml")
            container = soup.find("div", class_="items-items-kAJAg")
            items = container.find_all("div", class_="iva-item-root-_lk9K")

            count = 0
            for item in items:
                count += 1
                print(f"Process # {count}/{len(items)}")

                href = title = price = description = address = metro = img = "Not found"

                try:
                    href = f'https://www.avito.ru{item.find("div", class_="iva-item-title-py3i_").find("a").get("href")}'
                except Exception as ex:
                    pass

                try:
                    title = item.find("div", class_="iva-item-title-py3i_").find("h3").text
                except Exception as ex:
                    pass

                try:
                    price = item.find("div", class_="iva-item-priceStep-uq2CQ").find("span").find("p", class_="styles-module-root-_KFFt").text
                except Exception as ex:
                    pass

                try:
                    address = item.find("div", class_="geo-root-zPwRk").find("p").find("span").text
                    metro = item.find("div", class_="geo-root-zPwRk").find("p", class_="styles-module-margin-top_0-_usAN").find("span", class_="geo-icons-uMILt").find_next("span").text
                except Exception as ex:
                    pass
                print(metro)
                try:
                    description = item.find("div", class_="iva-item-descriptionStep-C0ty1").find("p").text
                except Exception as ex:
                    pass

                try:
                    img = item.find("div", class_="photo-slider-photoSlider-Eyzg_").find("li", class_="photo-slider-list-item-h3A51").get("data-marker").replace("slider-image/image-", "")
                except Exception as ex:
                    pass

                res = {
                    "href": href,
                    "title": title.strip().replace(" ", ""),
                    "price": price.strip().replace(" ", " "),
                    "address": address,
                    "metro": metro,
                    "description": description.rstrip().replace("\n", ""),
                    "img": img
                }

                result[f"item_{count}"] = res

                print(f"Appartment: {title} was parsed successfully!")
                print("Next item...")
                print("_"*25)
                time.sleep(0.2)

                if count == len(items):
                    break

            with open("result_json.json", "a", encoding="utf-8") as file:
                json.dump([result], file, indent=4, ensure_ascii=False)


            break

    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()



def main():
    get_data()


if __name__ == '__main__':
    main()