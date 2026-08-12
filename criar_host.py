from zabbix_utils import ZabbixAPI

ZABBIX_URL = "http://192.168.15.11/zabbix"
USUARIO = "Admin"
SENHA = "zabbix"  # Altere caso tenha mudado a senha do Admin no painel

try:
    # Autenticação direta com Usuário/Senha Admin
    zbx = ZabbixAPI(url=ZABBIX_URL, user=USUARIO, password=SENHA)

    # 1. Busca um grupo de hosts válido
    grupos = zbx.hostgroup.get({'output': ['groupid'], 'limit': 1})
    id_grupo = grupos[0]['groupid']

    # 2. Cria o host
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