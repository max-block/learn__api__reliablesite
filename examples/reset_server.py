from pprint import pprint

from zeep.helpers import serialize_object

from examples import API_KEY, API_PASSWORD, SERVER_ID, get_server_service


def main():
    service = get_server_service()
    res = service.SendIPMICommand(API_KEY, API_PASSWORD, SERVER_ID, "Reset")
    pprint(serialize_object(res))


if __name__ == "__main__":
    main()
