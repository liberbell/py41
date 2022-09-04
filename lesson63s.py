from xmlrpc.server import SimpleXMLRPCServer

with SimpleXMLRPCServer(("127.0.0.1", "8000")) as server:

    def add_num(x, y):
        return x + y