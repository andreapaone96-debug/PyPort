import socket

host = socket.gethostbyname('127.0.0.1')

def tcp_connection(host):
        connections = []
        for port in range(1, 10000):
            try:
                connection = socket.create_connection((host, port), timeout=.2)
                connections.append((host, port, connection))
                connection.close()
                

            except ConnectionRefusedError:
                continue
                

            except PermissionError:
                continue
                

            except TimeoutError:
                continue

        return connections


connect = tcp_connection(host)

for port in connect:
    try:
        servizio = socket.getservbyport(port[1], "tcp")

    except OSError:
        servizio = "Non registrato"

    print(f"Porta {port[1]}: APERTA | Servizio: {servizio}")
