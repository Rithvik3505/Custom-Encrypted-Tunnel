import ssl

def create_ssl_context(is_server=False):
    if is_server:
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")
    else:
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
    return context

def wrap_socket(sock, is_server=False, server_hostname=None):
    context = create_ssl_context(is_server)
    return context.wrap_socket(sock, server_side=is_server, server_hostname=server_hostname if not is_server else None)

