from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field
from zeep.helpers import serialize_object

from examples import API_KEY, API_PASSWORD, get_server_service


class ServerListItem(BaseModel):
    id: int = Field(..., alias="Server_Id")
    label: str = Field(..., alias="Server_Label")
    status: str = Field(..., alias="Status")
    name: Optional[str] = Field(..., alias="User_Name")


class ServerDetails(BaseModel):
    ip: str
    name: str
    processor: str

    @staticmethod
    def from_zeep_object(data) -> ServerDetails:
        data = serialize_object(data)
        ip = data["IPBlockDetailsList"]["IPBlock_Details"][0]["IP_Description"]
        name = data["ServerDetails"]["Server_Name"]
        processor = data["ServerDetails"]["Processor"]
        return ServerDetails(ip=ip, name=name, processor=processor)


def main():
    service = get_server_service()
    res = service.GetListAllServers(API_KEY, API_PASSWORD)

    servers_list = res["UsersServerDetailsList"]["Users_Server_Details"]
    servers_list = [ServerListItem(**serialize_object(s)) for s in servers_list]

    for server_item in servers_list:
        res = service.GetServersDetails(API_KEY, API_PASSWORD, server_item.id)
        details = ServerDetails.from_zeep_object(res)
        print(details)


if __name__ == "__main__":
    main()
