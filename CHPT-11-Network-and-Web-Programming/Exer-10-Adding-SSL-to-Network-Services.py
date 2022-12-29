# Exer-10-Adding-SSL-to-Network-Services

from socket import socket, AF_INET, SOCK_STREAM
import ssl

KEYFILE = "server_key.pem"  # Private key of the server
CERTFILE = "server_cert.pem"  # Server certificate (given to client)


def echo_client(s):
    while True:
        data = s.recv(8192)
        if data == b"":
            break
        s.send(data)
    s.close()
    print("Connection closed")


def echo_server(address):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(1)

    # Wrap with an SSL layer requiring client certs
    s_ssl = ssl.wrap_socket(s, keyfile=KEYFILE, certfile=CERTFILE, server_side=True)
    # Wait for connections
    while True:
        try:
            c, a = s_ssl.accept()
            print("Got connection", c, a)
            echo_client(c)
        except Exception as e:
            print("{}: {}".format(e.__class__.__name__, e))


echo_server(("", 20000))

###

from socket import socket, AF_INET, SOCK_STREAM
import ssl

s = socket(AF_INET, SOCK_STREAM)
s_ssl = ssl.wrap_socket(s, cert_reqs=ssl.CERT_REQUIRED, ca_certs="server_cert.pem")
s_ssl.connect(("localhost", 20000))
s_ssl.send(b"Hello World?")
s_ssl.recv(8192)

###

import ssl


class SSLMixin:
    """
    Mixin class that adds support for SSL to existing servers based
    on the socketserver module.
    """

    def __init__(
        self,
        *args,
        keyfile=None,
        certfile=None,
        ca_certs=None,
        cert_reqs=ssl.NONE,
        **kwargs
    ):
        self._keyfile = keyfile
        self._certfile = certfile
        self._ca_certs = ca_certs
        self._cert_reqs = cert_reqs
        super().__init__(*args, **kwargs)

    def get_request(self):
        client, addr = super().get_request()
        client_ssl = ssl.wrap_socket(
            client,
            keyfile=self._keyfile,
            certfile=self._certfile,
            ca_certs=self._ca_certs,
            cert_reqs=self._cert_reqs,
            server_side=True,
        )
        return client_ssl, addr


###

# XML-RPC server with SSL

from xmlrpc.server import SimpleXMLRPCServer


class SSLSimpleXMLRPCServer(SSLMixin, SimpleXMLRPCServer):
    pass


###

import ssl
from xmlrpc.server import SimpleXMLRPCServer
from sslmixin import SSLMixin


class SSLSimpleXMLRPCServer(SSLMixin, SimpleXMLRPCServer):
    pass


class KeyValueServer:
    _rpc_methods_ = ["get", "set", "delete", "exists", "keys"]

    def __init__(self, *args, **kwargs):
        self._data = {}
        self._serv = SSLSimpleXMLRPCServer(*args, allow_none=True, **kwargs)
        for name in self._rpc_methods_:
            self._serv.register_function(getattr(self, name))

    def get(self, name):
        return self._data[name]

    def set(self, name, value):
        self._data[name] = value

    def delete(self, name):
        del self._data[name]

    def exists(self, name):
        return name in self._data

    def keys(self):
        return list(self._data)

    def serve_forever(self):
        self._serv.serve_forever()


if __name__ == "__main__":
    KEYFILE = "server_key.pem"
    CERTFILE = "server_cert.pem"
    kvserv = KeyValueServer(("", 15000), keyfile=KEYFILE, certfile=CERTFILE)
    kvserv.serve_forever()

###

from xmlrpc.client import ServerProxy

s = ServerProxy("https://localhost:15000", allow_none=True)
s.set("foo", "bar")
s.set("spam", [1, 2, 3])
s.keys()
s.get("foo")
s.get("spam")
s.delete("spam")
s.exists("spam")

###

from xmlrpc.client import SafeTransport, ServerProxy
import ssl


class VerifyCertSafeTransport(SafeTransport):
    def __init__(self, cafile, certfile=None, keyfile=None):
        SafeTransport.__init__(self)
        self._ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        self._ssl_context.load_verify_locations(cafile)
        if cert:
            self._ssl_context.load_cert_chain(certfile, keyfile)
        self._ssl_context.verify_mode = ssl.CERT_REQUIRED

    def make_connection(self, host):
        s = super().make_connection((host, {"context": self._ssl_context}))

        return s


# Create the client proxy
s = ServerProxy(
    "https://localhost:15000",
    transport=VerifyCertSafeTransport("server_cert.pem"),
    allow_none=True,
)

###

if __name__ == "__main__":
    KEYFILE = "server_key.pem"  # Private key of the server
    CERTFILE = "server_cert.pem"  # Server certificate
    CA_CERTS = "client_cert.pem"  # Certificates of accepted clients

    kvserv = KeyValueServer(
        ("", 15000),
        keyfile=KEYFILE,
        certfile=CERTFILE,
        ca_certs=CA_CERTS,
        cert_reqs=ssl.CERT_REQUIRED,
    )
    kvserv.serve_forever()

# Create the client proxy
s = ServerProxy(
    "https://localhost:15000",
    transport=VerifyCertSafeTransport(
        "server_cert.pem", "client_cert.pem", "client_key.pem"
    ),
    allow_none=True,
)

###

"""
bash % openssl req -new -x509 -days 365 -nodes -out server_cert.pem \
    -keyout server_key.pem
"""
