from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import time
import os

driver = None

@given('que eu acesso o site "{url}"')
def step_acessar_site(context, url):
    global driver
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(0.3)

@when('eu preencho o formulário de Practice Form')
def step_preencher_formulario(context):
    botao_1 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[2]/div/div[3]')
    botao_1.click()
    time.sleep(2)
    elemento = driver.find_element(By.XPATH, "//span[text()='Practice Form']")
    driver.execute_script("arguments[0].click();", elemento)
    time.sleep(2)

    campo_nome = driver.find_element(By.ID, "firstName")
    campo_nome.click()
    campo_nome.send_keys("teste")
    time.sleep(1)

    pyautogui.press('tab')
    pyautogui.write('last')
    time.sleep(0.5)

    pyautogui.press('tab')
    pyautogui.write('email@email.com')
    time.sleep(0.5)

    pyautogui.press('tab')
    pyautogui.press('right')
    time.sleep(0.5)

    pyautogui.press('tab')
    pyautogui.write('1234567890')
    time.sleep(0.5)

    pyautogui.press('tab')
    pyautogui.write('13 dec 2002')
    pyautogui.press('enter')
    time.sleep(0.5)

    pyautogui.press('tab')
    pyautogui.write('art')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(1)

    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('space')
    pyautogui.press('tab')
    pyautogui.press('space')
    time.sleep(1)

    arquivo = os.path.join(os.path.dirname(__file__), "arq.txt")
    upload = driver.find_element(By.ID, "uploadPicture")
    upload.send_keys(arquivo)
    time.sleep(1)

    campo_endereco = driver.find_element(By.ID, "currentAddress")
    campo_endereco.click()
    time.sleep(1)
    pyautogui.write('Sao Paulo - SP')

    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('down')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('down')
    pyautogui.press('down')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(5)

@then('devo ver o modal de confirmação')
def step_ver_modal(context):
    modal_titulo = driver.find_element(By.ID, "example-modal-sizes-title-lg")
    assert modal_titulo.is_displayed(), "Modal não apareceu"
    driver.quit()
