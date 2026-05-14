import os
import urllib.parse
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.request
import json

# Defina estes valores via export no terminal ou informe no código
CLIENT_ID = os.environ.get("LINKEDIN_CLIENT_ID", "")
CLIENT_SECRET = os.environ.get("LINKEDIN_CLIENT_SECRET", "")
REDIRECT_URI = "http://localhost:8000/callback"
SCOPE = "openid,profile,w_member_social,email"

class OAuthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(query)
        
        if "code" in params:
            code = params["code"][0]
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(b"<h1>Autenticacao OK!</h1><p>Olhe o terminal, fechando o servidor.</p>")
            
            # Trocar code pelo Access Token
            print("\n[!] Código recebido! Trocando pelo Access Token...")
            data = urllib.parse.urlencode({
                "grant_type": "authorization_code",
                "code": code,
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
                "redirect_uri": REDIRECT_URI
            }).encode('utf-8')
            
            req = urllib.request.Request("https://www.linkedin.com/oauth/v2/accessToken", data=data)
            try:
                with urllib.request.urlopen(req) as response:
                    res_body = response.read()
                    token_info = json.loads(res_body)
                    print("\n" + "="*50)
                    print("✅ SUCESSO! AQUI ESTA O SEU ACCESS TOKEN:")
                    print("="*50)
                    print(f"ACCESS_TOKEN: {token_info.get('access_token')}")
                    print(f"Expira em: {token_info.get('expires_in')} segundos (aprox 60 dias)")
                    print("="*50)
                    # Salva num arquivo pro Paulo Publicador depois
                    with open(".linkedin_token", "w") as f:
                        f.write(token_info.get('access_token'))
                    print("Token salvo no arquivo .linkedin_token\n")
            except Exception as e:
                print(f"Erro ao obter o token: {e}")
                
        else:
            self.send_response(400)
            self.end_headers()

def main():
    if not CLIENT_ID or not CLIENT_SECRET:
        print("Falta configurar CLIENT_ID ou CLIENT_SECRET!")
        return
        
    auth_url = f"https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id={CLIENT_ID}&redirect_uri={urllib.parse.quote(REDIRECT_URI)}&scope={urllib.parse.quote(SCOPE)}"
    
    print("\n" + "="*50)
    print("1. CLIQUE NESSE LINK PARA AUTORIZAR O CONCLAVE:")
    print("="*50)
    print(auth_url)
    print("\n[!] Esperando você fazer o login no navegador e autorizar...")
    
    server = HTTPServer(('localhost', 8000), OAuthHandler)
    server.handle_request() # Processa só uma requisição pra pegar o código e para
    
if __name__ == "__main__":
    main()
