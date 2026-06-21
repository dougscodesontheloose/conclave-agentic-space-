import os
import json
import urllib.request
import sys

def get_person_id(token):
    req = urllib.request.Request("https://api.linkedin.com/v2/userinfo")
    req.add_header('Authorization', f'Bearer {token}')
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            return data.get('sub')
    except Exception as e:
        print(f"Erro ao buscar User ID: {e}")
        return None

def publish_post(token, person_id, text):
    url = "https://api.linkedin.com/v2/ugcPosts"
    payload = {
        "author": f"urn:li:person:{person_id}",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": text
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }
    
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data)
    req.add_header('Authorization', f'Bearer {token}')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-Restli-Protocol-Version', '2.0.0')
    
    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 201:
                return True, response.read().decode('utf-8')
            return False, response.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        return False, e.read().decode('utf-8')
    except Exception as e:
        return False, str(e)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 linkedin_publisher.py path/to/content.md")
        sys.exit(1)
        
    content_path = sys.argv[1]
    if not os.path.exists(content_path):
        print(f"Arquivo não encontrado: {content_path}")
        sys.exit(1)
        
    token_path = os.environ.get("LINKEDIN_TOKEN_PATH", "legacy/linkedin-auth/.linkedin_token")
    with open(token_path, "r") as f:
        token = f.read().strip()
        
    with open(content_path, "r") as f:
        # Extrai o corpo do post ignorando possíveis headers do Markdown de tarefa
        full_content = f.read()
        if "## Texto Final Revisado" in full_content:
            text = full_content.split("## Texto Final Revisado")[1].strip()
        else:
            text = full_content.strip()
            
    person_id = get_person_id(token)
    if not person_id:
        print("Falha ao obter Person ID.")
        sys.exit(1)
        
    success, res = publish_post(token, person_id, text)
    if success:
        print(f"✅ SUCESSO! Post publicado. ID: {res}")
    else:
        print(f"❌ FALHA: {res}")
