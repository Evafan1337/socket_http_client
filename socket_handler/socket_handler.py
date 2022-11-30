import socket
from helper import Helper
from urllib import parse

class SocketHandler():

    PORT = None
    URL = None
    FILENAME = None
    CHARSET = "windows-1251"

    sock = None

    def getUrl(self):
        return self.URL

    def getPort(self):
        return self.PORT

    def getFilename(self):
        return self.FILENAME

    def setUrl(self, url):
        if(Helper.validate_url(url)):
            self.URL = url
        else:
            raise Exception("URL is not correct")

    def setPort(self, port):
        if(Helper.validate_port(port)):
            self.PORT = port
        else:
            raise Exception("PORT is not correct")

    def setFilename(self, filename):
        self.FILENAME = filename

    def setCharset(self,value):
        self.CHARSET = value

    def getCharset(self):
        return self.CHARSET

    def prepareUrl(self):
        return parse.urlparse(self.URL)

    def createSocket(self):
        return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def sendHTTPGetRequest(self):
        sock = self.createSocket()
        url = self.prepareUrl()
        port = self.getPort()

        sock.connect((url.netloc, port))
        m = 'GET '+ url.path + ' HTTP/1.1\r\nHost: '+url.netloc+'\r\n\r\n'

        m = m.encode()
        sock.send(m)

        response = []
        end_flag = False
        while True: 
            chunk = sock.recv(8192)
            response.append(chunk)
            output = chunk.decode("windows-1251")
            if("</html>" in output):
                break

        arr = b''.join(response)

        filename = self.getFilename()
        charset = self.getCharset()

        arr = arr.decode(charset)
        with open(filename, 'w') as f:
            f.writelines(arr)
        sock.close()