import socket
import threading


class ClientHandler(threading.Thread):
    '''A thread to handle one client request'''

    def __init__(self, client_socket, client_address):
        super().__init__()
        self._client_socket = client_socket
        self._client_address = client_address

    def run(self):  # the function that the thread runs
        request = self._client_socket.recv(1024)  # read from the client (bytes, not str)

        reply = request.upper()[::-1]  # create reply to send to client

        self._client_socket.sendall(reply)  # send the reply to the client
        self._client_socket.close()  # close the connection


def setup():
    '''Initialize the server socket'''
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # close the socket
    serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # set some socket options
    # serv.setblocking(0)

    serv.bind((socket.gethostname(), 7777))  # bind to local host and port 7777
    serv.listen(5)  # start listening

    return serv


def main():
    '''Main program.'''
    serv = setup()
    while True:  # loop until program is killed
        (csock, addr) = serv.accept()  # sleep until client request arrives
        handler = ClientHandler(csock, addr)  # create new thread to handle client
        handler.start()  # start the new thread


if __name__ == '__main__':
    main()
