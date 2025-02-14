from dlms_cosem.security import NoSecurityAuthentication
from dlms_cosem.client import DlmsClient
from dlms_cosem.io import BlockingTcpIO, TcpTransport


class TestDlmsClient:
    def test_client_invocation_counter_property(self):
        transport = TcpTransport(
            io=BlockingTcpIO(host="localhost", port=4059),
            client_logical_address=1,
            server_logical_address=1,
        )
        client = DlmsClient(
            client_initial_invocation_counter=500,
            transport=transport,
            authentication=NoSecurityAuthentication(),
        )

        assert client.client_invocation_counter == 500

    def test_client_invocation_counter_setter(self):
        transport = TcpTransport(
            io=BlockingTcpIO(host="localhost", port=4059),
            client_logical_address=1,
            server_logical_address=1,
        )
        client = DlmsClient(
            client_initial_invocation_counter=500,
            transport=transport,
            authentication=NoSecurityAuthentication(),
        )
        client.client_invocation_counter = 1000
        assert client.client_invocation_counter == 1000
        assert client.dlms_connection.client_invocation_counter == 1000
