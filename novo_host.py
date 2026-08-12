from zabbix_utils import ZabbixAPI

ZABBIX_URL = "http://192.168.15.11/zabbix"
USUARIO = "Admin"
SENHA = "zabbix"

try:
    # 1. Conecta e autentica no Zabbix
    zbx = ZabbixAPI(url=ZABBIX_URL, user=USUARIO, password=SENHA)

    # 2. Busca dinamicamente o ID do primeiro grupo de hosts existente
    grupos = zbx.hostgroup.get(output=['groupid'], limit=1)
    if not grupos:
        raise Exception("Nenhum grupo de hosts encontrado no Zabbix.")
    
    id_grupo = grupos[0]['groupid']

    # 3. Cria o host com a sintaxe nativa do zabbix_utils
    novo_host = zbx.host.create(
        host="Servidor-Automacao-Python",
        name="Servidor Automacao Python",
        interfaces=[{
            "type": 1,
            "main": 1,
            "useip": 1,
            "ip": "192.168.15.50",
            "dns": "",
            "port": "10050"
        }],
        groups=[{"groupid": id_grupo}]
    )

    print(f"✅ Host criado com sucesso! ID do Host: {novo_host['hostids'][0]}")

except Exception as e:
    print(f"❌ Erro na API do Zabbix: {e}")