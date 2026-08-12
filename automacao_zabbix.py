import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Configura e abre o Chrome
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.maximize_window()

espera = WebDriverWait(navegador, 15)

try:
    # 2. Acessa o Zabbix
    print("🌐 Acessando o Zabbix...")
    navegador.get("http://192.168.15.11/zabbix")

    # 3. Efetuando Login
    print("🔑 Efetuando login...")
    campo_usuario = espera.until(EC.presence_of_element_located((By.ID, "name")))
    campo_usuario.clear()
    campo_usuario.send_keys("Admin")

    campo_senha = navegador.find_element(By.ID, "password")
    campo_senha.clear()
    campo_senha.send_keys("zabbix")

    botão_entrar = navegador.find_element(By.ID, "enter")
    botão_entrar.click()

    # 4. Navega para a página de Hosts
    print("🖥️ Navegando para a página de Hosts...")
    time.sleep(2)
    link_hosts = espera.until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'zabbix.php?action=host.list')]"))
    )
    navegador.execute_script("arguments[0].click();", link_hosts)

    # 5. Clica no botão 'Criar host'
    print("➕ Clicando no botão 'Criar host'...")
    btn_criar_host = espera.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Criar host') or contains(@title, 'Criar host')]"))
    )
    btn_criar_host.click()

    # 6. Preenche Nome e Nome Visível
    print("📝 Preenchendo Nome e Nome Visível...")
    campo_hostname = espera.until(EC.presence_of_element_located((By.ID, "host")))
    campo_hostname.clear()
    campo_hostname.send_keys("Servidor-Selenium-Automation")

    campo_visivel = navegador.find_element(By.ID, "visiblename")
    campo_visivel.clear()
    campo_visivel.send_keys("Servidor Selenium Automation")

    # 7. Preenche o Grupo de Hosts
    print("🏷️ Preenchendo o Grupo de Hosts...")
    campo_grupo = navegador.find_element(By.XPATH, "//div[@id='groups_']//input")
    campo_grupo.send_keys("Discovered hosts")
    time.sleep(1)
    campo_grupo.send_keys(Keys.ENTER)  # Pressiona Enter para confirmar a seleção do grupo
    time.sleep(1)

    # 8. Adiciona Interface de Agente
    print("🔌 Adicionando Interface...")
    # Clica no link/botão Adicionar na seção de interfaces
    btn_add_interface = espera.until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'js-add-interface') or text()='Adicionar'] | //a[contains(@class, 'js-add-interface') or text()='Adicionar']"))
    )
    navegador.execute_script("arguments[0].click();", btn_add_interface)
    time.sleep(1)

    # Clica na opção 'Agente'
    try:
        opcao_agente = navegador.find_element(By.XPATH, "//a[contains(text(),'Agente') or contains(text(),'Agent')]")
        navegador.execute_script("arguments[0].click();", opcao_agente)
        time.sleep(1)
    except:
        pass # Se a interface de agente já for adicionada por padrão

    # Preenche o IP
    print("🌐 Preenchendo IP...")
    campo_ip = espera.until(
        EC.presence_of_element_located((By.XPATH, "//input[contains(@id, 'interfaces_0_ip') or contains(@id, 'ip')]"))
    )
    campo_ip.clear()
    campo_ip.send_keys("192.168.15.55")

    # 9. Clica no botão azul 'Adicionar' (para salvar o host no modal)
    print("💾 Salvando o Host...")
    btn_salvar = espera.until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'overlay-dialogue-footer')]//button[contains(text(), 'Adicionar') or @id='add']"))
    )
    navegador.execute_script("arguments[0].click();", btn_salvar)

    # 10. Aguarda o feedback verde de sucesso
    print("⏳ Confirmando criação...")
    espera.until(EC.presence_of_element_located((By.CLASS_NAME, "msg-good")))
    print("🎉 SUCESSO ABSOLUTO! Host cadastrado com sucesso no Zabbix!")

    # Tira o print oficial do projeto
    navegador.save_screenshot("resultado_zabbix.png")
    print("📸 Print salvo como 'resultado_zabbix.png'")

    time.sleep(3)

except Exception as e:
    print(f"❌ Ocorreu um erro: {e}")

finally:
    navegador.quit()