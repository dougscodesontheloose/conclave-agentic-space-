import os
import urllib.parse
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.request
import json
import sys

CLIENT_ID = "77jkpqncli74jq"
CLIENT_SECRET = "<linkedin_client_secret>"
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
            self.wfile.write(b"<h1>Autenticacao OK!</h1><p>Pode fechar esta aba.</p>")
            
            print("\n[!] Código recebido! Trocando pelo Access Token...", flush=True)
            data = urllib.parse.urlencode({
                "grant_type": "authorization_code",
                "code": code,
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
                "redirect_uri": REDIRECT_URI
            }).encode('utf-8')
            
            req = urllib.request.Request("https://www.linkedin.com/oauth/v2/accessToken", data=data)
            req.add_header('Content-Type', 'application/x-www-form-urlencoded')
            try:
                with urllib.request.urlopen(req) as response:
                    res_body = response.read()
                    token_info = json.loads(res_body)
                    print("✅ SUCESSO!", flush=True)
                    with open(".linkedin_token", "w") as f:
                        f.write(token_info.get('access_token', 'ERROR_NO_TOKEN'))
                    print("Token salvo no arquivo .linkedin_token\n", flush=True)
            except urllib.error.HTTPError as e:
                print(f"Erro HTTP: {e.code} - {e.read().decode('utf-8')}", flush=True)
            except Exception as e:
                print(f"Erro: {e}", flush=True)
                
        else:
            self.send_response(400)
            self.end_headers()

def main():
    print("Servidor ouvindo...", flush=True)
    server = HTTPServer(('localhost', 8000), OAuthHandler)
    server.handle_request() # Processa só uma requisição
    
if __name__ == "__main__":
    main()
