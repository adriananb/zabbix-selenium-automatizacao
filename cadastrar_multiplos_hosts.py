import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ==========================================================
# LISTA COM OS 4 HOSTS PARA CADASTRAR AUTOMATICAMENTE
# ==========================================================
novos_hosts = [
    {
        "nome": "Servidor-WEB-01",
        "visivel": "Servidor Web Nginx 01",
        "grupo": "Discovered hosts",
        "ip": "192.168.15.60"
    },
    {
        "nome": "Servidor-DB-01",
        "visivel": "Servidor Banco PostgreSQL",
        "grupo": "Discovered hosts",
        "ip": "192.168.15.61"
    },
    {
        "nome": "Servidor-APP-01",
        "visivel": "Servidor Aplicacao Node",
        "grupo": "Discovered hosts",
        "ip": "192.168.15.62"
    },
    {
        "nome": "Servidor-BKUP-01",
        "visivel": "Servidor de Backup Storage",
        "grupo": "Discovered hosts",
        "ip": "192.168.15.63"
    }
]

# 1. Configura e abre o Chrome
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.maximize_window()

espera = WebDriverWait(navegador, 15)

try:
    # 2. Acessa o Zabbix
    print("Acessando o Zabbix...")
    navegador.get("http://192.168.15.11/zabbix")

    # 3. Efetuando Login
    print("Efetuando login...")
    campo_usuario = espera.until(EC.presence_of_element_located((By.ID, "name")))
    campo_usuario.clear()
    campo_usuario.send_keys("Admin")

    campo_senha = navegador.find_element(By.ID, "password")
    campo_senha.clear()
    campo_senha.send_keys("zabbix")

    botão_entrar = navegador.find_element(By.ID, "enter")
    botão_entrar.click()

    # 4. Acessar a página de Hosts
    print("Acessando a página de Hosts...")
    time.sleep(2)
    link_hosts = espera.until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'zabbix.php?action=host.list')]"))
    )
    navegador.execute_script("arguments[0].click();", link_hosts)

    # 5. Loop para cadastrar os 4 hosts
    for indice, host in enumerate(novos_hosts, start=1):
        print(f"\n Cadastrando Host [{indice}/4]: {host['nome']}...")

        # A) Comando para criar host
        btn_criar_host = espera.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Criar host') or contains(@title, 'Criar host')]"))
        )
        btn_criar_host.click()

        # B) Preenche nome e nome visível
        campo_hostname = espera.until(EC.presence_of_element_located((By.ID, "host")))
        campo_hostname.clear()
        campo_hostname.send_keys(host["nome"])

        campo_visivel = navegador.find_element(By.ID, "visiblename")
        campo_visivel.clear()
        campo_visivel.send_keys(host["visivel"])

        # C) Preencher o grupo de hosts
        campo_grupo = navegador.find_element(By.XPATH, "//div[@id='groups_']//input")
        campo_grupo.send_keys(host["grupo"])
        time.sleep(1)
        campo_grupo.send_keys(Keys.ENTER)
        time.sleep(1)

        # D) Adiciona interface do agente
        btn_add_interface = espera.until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'js-add-interface') or text()='Adicionar'] | //a[contains(@class, 'js-add-interface') or text()='Adicionar']"))
        )
        navegador.execute_script("arguments[0].click();", btn_add_interface)
        time.sleep(1)

        try:
            opcao_agente = navegador.find_element(By.XPATH, "//a[contains(text(),'Agente') or contains(text(),'Agent')]")
            navegador.execute_script("arguments[0].click();", opcao_agente)
            time.sleep(1)
        except:
            pass

        # E) Preenche o IP
        campo_ip = espera.until(
            EC.presence_of_element_located((By.XPATH, "//input[contains(@id, 'interfaces_0_ip') or contains(@id, 'ip')]"))
        )
        campo_ip.clear()
        campo_ip.send_keys(host["ip"])

        # F) Clicar em 'adicionar' para salvar o host
        btn_salvar = espera.until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'overlay-dialogue-footer')]//button[contains(text(), 'Adicionar') or @id='add']"))
        )
        navegador.execute_script("arguments[0].click();", btn_salvar)

        # G) Aguarda a confirmação de salvamento antes de ir pro próximo
        espera.until(EC.presence_of_element_located((By.CLASS_NAME, "msg-good")))
        print(f" Host '{host['nome']}' cadastrado com sucesso!")
        time.sleep(1.5)

    print("\n FORAM CADASTRADOS COM SUCESSO!")
    
    # Mostrar resultado provando os 4 cadastrados na lista
    navegador.save_screenshot("resultado_4_hosts.png")
    print("Print final salvo como 'resultado_4_hosts.png'")

    time.sleep(3)

except Exception as e:
    print(f" Ocorreu um erro no processo: {e}")

finally:
    navegador.quit()