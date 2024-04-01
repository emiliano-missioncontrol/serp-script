from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
from urllib.parse import urlparse


TARGET_DOMAIN = "missioncontrol.com.mx"


keywords = [
    "mission control",
    "yamaha yc61 precio",
    "mcintosh rs150",
    "tornamesa mcintosh",
    "mision control",
    "blue microphones",
    "yamaha hs7",
    "missioncontrol",
    "stagepas 600bt",
    "yamaha yc61",
    "dali spektor 2",
    "mcintosh mt5",
    "tornamesa mcintosh mt5",
    "yamaha hs5",
    "yamaha hs8",
    "mission control switch",
    "amplificador mcintosh",
    "mcintosh ma12000",
    "blue spark",
    "chandler limited",
    "microfonos blue",
    "monitores yamaha hs5",
    "amplificador carver",
    "mcintosh mc275",
    "mcintosh tornamesa",
    "cambridge cxn 100",
    "cambridge cxn v2",
    "blue mics",
    "mcintosh mha50",
    "tocadiscos mcintosh",
    "blue dragonfly mic",
    "yamaha revstar rss02t",
    "blue spark sl",
    "blue mouse microphone",
    "dynaudio lyd 7",
    "mcintosh mt5-6",
    "dynaudio lyd 8",
    "misioncontrol",
    "anthem mrx 1140",
    "anthem avr",
    "audifonos mcintosh",
    "yamaha mg10xu",
    "mcintosh audio",
    "mx123",
    "mc intosh",
    "yamaha ck61",
    "dali 3",
    "marantz",
    "rs150"
]


def isTargetDomain(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc == TARGET_DOMAIN


def scrape_serp_data(kw):
    options = Options()
    options.add_argument('--headless=new') # comentar para probar en modo visible (abre el navegador)

    driver = webdriver.Chrome(service=Service(), options=options)
    driver.get("https://google.com/")

    try:
        cookie_dialog = driver.find_element(By.CSS_SELECTOR, "[role='dialog']")
        accept_button = cookie_dialog.find_element(
            By.XPATH, ".//button[contains(., 'Accept')]")
        if accept_button is not None:
            accept_button.click()
    except NoSuchElementException:
        pass

    search_form = driver.find_element(
        By.CSS_SELECTOR, "form[action='/search']")
    search_textarea = search_form.find_element(By.CSS_SELECTOR, "textarea")
    search_textarea.send_keys(kw)
    print("Buscando: " + kw)
    search_form.submit()

    search_div = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#search')))

    serp_divs = search_div.find_elements(
        By.CSS_SELECTOR, "div[jscontroller][jsaction][data-hveid][data-ved]")

    serp_elements = []
    rank = 1

    for serp_div in serp_divs:
        try:
            serp_title_h3 = serp_div.find_element(By.CSS_SELECTOR, "h3")
            title = serp_title_h3.text
            serp_title_a = serp_title_h3.find_element(By.XPATH, './..')
            url = serp_title_a.get_attribute("href")
        except NoSuchElementException:
            continue
        if isTargetDomain(url):
            serp_element = {
                'rank': rank,
                'url': url,
                'title': title,
                'keyword': kw
            }
            serp_elements.append(serp_element)

        rank += 1

    driver.quit()
    return serp_elements


# Scraping de datos SERP para cada palabra clave
all_serp_data = []
for kw in keywords:
    serp_data = scrape_serp_data(kw)
    all_serp_data.extend(serp_data)

# Exportar los datos a un archivo CSV
csv_file = "serp_results.csv"
header = ['keyword', 'rank', 'url', 'title']
with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    writer.writerows(all_serp_data)

print("Scraping completado. Datos guardados en", csv_file)
