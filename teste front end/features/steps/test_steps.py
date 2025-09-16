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

@when('navego no meu e clico em new windows')
def step_entrar_browserWindows(context):
    # clica no card alerts, frame e windows
    botao_alerts = driver.find_element(By.XPATH, "//h5[text()='Alerts, Frame & Windows']")
    botao_alerts.click()
    time.sleep(2)
    
    # clica aba browser windows
    elemento = driver.find_element(By.XPATH, "//span[text()='Browser Windows']")
    driver.execute_script("arguments[0].click();", elemento)
    time.sleep(2)

    driver.find_element(By.ID, "windowButton").click()
    time.sleep(2)

    driver.switch_to.window(driver.window_handles[1])
    time.sleep(1)
    
@then('devo ver nova janela com uma mensagem e fechar')
def step_valida_newWindow(context):
    texto = driver.find_element(By.ID, "sampleHeading").text
    print("Texto encontrado:", texto)
    time.sleep(2)

    if texto == "This is a sample page":
        print("Texto validado com sucesso!")
    else:
        print("Texto não corresponde!")
    
    time.sleep(2)
    driver.close()
    driver.quit()


@when('crio um elemento')
def criando_elemento(context):
    botao = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]/div/div[3]/h5')
    botao.click()
    time.sleep(2)
    
    elemento = driver.find_element(By.XPATH, "//span[text()='Web Tables']")
    driver.execute_script("arguments[0].click();", elemento)
    time.sleep(2)

    driver.find_element(By.XPATH, '//*[@id="addNewRecordButton"]').click()
    time.sleep(2)

    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write('ss')
    pyautogui.press('tab')
    pyautogui.write('last teste')
    pyautogui.press('tab')
    pyautogui.write('email@email.com')
    pyautogui.press('tab')
    pyautogui.write('99')
    pyautogui.press('tab')
    pyautogui.write('90999')
    pyautogui.press('tab')
    pyautogui.write('admin')
    pyautogui.press('tab')
    pyautogui.press('space')
    time.sleep(3)

@when('edito um elemento')
def editando_elemento(context):
    # filtra por 'ss'
    input_element = driver.find_element(By.XPATH, "//input[@id='searchBox']")
    input_element.send_keys("ss")
    time.sleep(2)
    
    # clica no editar
    elemento = driver.find_element(By.ID, "edit-record-4")
    driver.execute_script("arguments[0].click();", elemento)
    time.sleep(2)

    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write('sss')
    time.sleep(2)

    driver.find_element(By.ID, 'submit').click()
    time.sleep(2)

@then('devo deletar o elemento criado')
def deletando_elemento(context):
    time.sleep(2)

    elemento = driver.find_element(By.ID, "delete-record-4")
    driver.execute_script("arguments[0].click();", elemento)

    time.sleep(2)
    driver.close()
    driver.quit()

@when('clico em start e a barra de progresso deve parar com valor menor ou igual a 25')
def start_progress_bar(context):
    time.sleep(2)
    elemento = driver.find_element(By.XPATH, "//h5[text()='Widgets']")
    driver.execute_script("arguments[0].click();", elemento)
    time.sleep(3)

    elemento1 = driver.find_element(By.XPATH, '//span[text()="Progress Bar"]/parent::li')
    elemento1.click()
    time.sleep(2)

    start = driver.find_element(By.ID, 'startStopButton')
    start.click()
    time.sleep(2)
    
    # espera os 25%
    while True:
        progress_text = driver.find_element(By.CSS_SELECTOR, '#progressBar .progress-bar').text
        progresso = int(progress_text.replace('%', ''))
        if progresso > 24:
            break
        time.sleep(0.01) 
    
    start.click()  # para a barra
    time.sleep(2)

    # pega o valor final da barra
    final_progress_text = driver.find_element(By.CSS_SELECTOR, '#progressBar .progress-bar').text
    final_progress = int(final_progress_text.replace('%', ''))
    assert final_progress <= 25, f"Erro: progresso final foi {final_progress}%"

@then('Deve clicar no botao restart depois de 100 porcento')
def aguarda_cem_porcento(context):
    time.sleep(2)

    driver.find_element(By.ID, 'startStopButton').click()
    
    # continua ate 100%
    while True:
        progress_text = driver.find_element(By.CSS_SELECTOR, '#progressBar .progress-bar').text
        progresso = int(progress_text.replace('%', ''))
        if progresso >= 100:
            break
        time.sleep(0.1)

    time.sleep(3)
    reset_button = driver.find_element(By.ID, 'resetButton')
    reset_button.click()

    time.sleep(4)
    driver.close()
    driver.quit()



