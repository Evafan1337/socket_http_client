from socket_handler.socket_handler import SocketHandler

handler = SocketHandler()
handler.setPort(80)
handler.setUrl("http://www.airwar.ru/enc/fighter/yak28.html")
handler.setFilename("upload/t4.txt")


handler.sendHTTPGetRequest()