import os

from dotenv import load_dotenv
from zeep import Client

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_PASSWORD = os.getenv("API_PASSWORD")
SERVER_ID = os.getenv("SERVER_ID")
WSDL = "http://api.reliablesite.net/dedicated-servers.svc?wsdl"


def get_server_service():
    client = Client(WSDL)
    return client.bind("DedicatedServerApi", "BasicHttpBinding_Server")
