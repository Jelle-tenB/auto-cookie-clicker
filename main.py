from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-search-engine-choice-screen")
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")
stop = 300
timeout_start = time.time()

def find_data():
    global money
    money = int(driver.find_element(By.CSS_SELECTOR, value="#money").text.strip().replace(',', ''))

    cursor = driver.find_element(By.CSS_SELECTOR, value="#buyCursor")
    grandma = driver.find_element(By.CSS_SELECTOR, value="#buyGrandma")
    mine = driver.find_element(By.CSS_SELECTOR, value="#buyFactory")
    shipment = driver.find_element(By.CSS_SELECTOR, value="#buyShipment")
    alchemylab = driver.find_element(By.CSS_SELECTOR, value="#buyAlchemy\\ lab")
    portal = driver.find_element(By.CSS_SELECTOR, value="#buyPortal")
    timemachine = driver.find_element(By.CSS_SELECTOR, value="#buyTime\\ machine")

    costs = {
        cursor: int(cursor.text.strip().split()[2].replace(',', '')),
        grandma: int(grandma.text.strip().split()[2].replace(',', '')),
        mine: int(mine.text.strip().split()[2].replace(',', '')),
        shipment: int(shipment.text.strip().split()[2].replace(',', '')),
        alchemylab: int(alchemylab.text.strip().split()[3].replace(',', '')),
        portal: int(portal.text.strip().split()[2].replace(',', '')),
        timemachine: int(timemachine.text.strip().split()[3].replace(',', ''))
    }
    return costs

def buying():
    costs = find_data()
    lowest_item = min(costs, key=costs.get)
    lowest_cost = costs[lowest_item]
    try:
        affordable_item = max((item for item, cost in costs.items() if cost <= money), key=costs.get)
        affordable_item.click()
        # time.sleep(0.1)
        # costs = find_data()
        # lowest_item = min(costs, key=costs.get)
        # lowest_cost = costs[lowest_item]
        # if money > lowest_cost:
        #     buying()
        # else:
        #     auto_click()
    except Exception as e:
        print(f"Exception occurred: {e}")
        auto_click()
    auto_click()


def auto_click():
    timeout = 5
    repeating = time.time()
    while time.time() < repeating + timeout:
        cookie.click()
    if timeout_start + stop < time.time():
        pass
    else:
        buying()

auto_click()
print(driver.find_element(By.ID, value="cps").text)
driver.quit()
