import xmlrpc.client

with xmlrpc.client.ServerProxy("http://127.0.0.1") as proxy:
    print(proxy.add_num(10, 20))