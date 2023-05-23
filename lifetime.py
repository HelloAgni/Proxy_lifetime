import config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def proxy_lifetime(url: str):
    """
    Вход по логину и паролю, установка галочки и запуск captcha.
    Ожидание 120сек, пока пользователь вручную пройдет проверку,
    и нажмет клавишу <Войти>.
    Сбор информации и вывод результата.
    """
    service = Service(executable_path="./chromedriver")
    options = Options()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(service=service,
                              options=options)
    try:
        driver.get(url)
        driver.implicitly_wait(5)

        login = driver.find_element(By.XPATH, config.XPATH_LOGIN)
        login.click()

        user = driver.find_element(By.XPATH, config.XPATH_USER)
        user.send_keys(config.LOGIN)

        password = driver.find_element(By.XPATH, config.XPATH_PASSWORD)
        password.send_keys(config.PASSWORD)

        # Activate tick of captcha
        WebDriverWait(driver, 5).until(
            EC.frame_to_be_available_and_switch_to_it(
                (By.XPATH, config.XPATH_CAPTCHA)))
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, config.CSS_CAPTCHA))).click()

        # Wait untill load user profile
        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located(
                (By.XPATH, config.XPATH_USER_PROFILE))
            )

        ips = driver.find_elements(By.XPATH, config.IP_PORT)
        ip_list = [ip.text for ip in ips]

        dates = driver.find_elements(By.XPATH, config.DATE)
        date_list = [date.text for date in dates]

        result = dict(zip(ip_list, date_list))
        for ip, date in result.items():
            print(f'{ip} - {date}')

    except Exception:
        pass
    finally:
        driver.quit()


if __name__ == "__main__":
    proxy_lifetime(config.URL)
