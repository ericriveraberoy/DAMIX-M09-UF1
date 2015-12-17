''' Python SSL Client '''
import ssl
import socket
import pprint

CONTEXT = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
CONTEXT.verify_mode = ssl.CERT_REQUIRED
CONTEXT.check_hostname = True
CONTEXT.load_verify_locations("/etc/ssl/certs/ca-certificates.crt")

S = "frontal.ies-sabadell.cat"
CONN = CONTEXT.wrap_socket(socket.socket(socket.AF_INET), server_hostname=S)
CONN.connect(("frontal.ies-sabadell.cat", 443))

CERT = CONN.getpeercert()
pprint.pprint(CERT)
