#!/usr/bin/env python3
import sys
import os
import re
import argparse

try:
    from colorama import init, Fore, Style
    init()
except ImportError:
    # Graceful fallback if colorama is not installed
    class EmptyStyle:
        def __getattr__(self, name):
            return ""
    Fore = Style = EmptyStyle()

def log_info(msg):
    print(f"{Fore.BLUE}[INFO]{Style.RESET_ALL} {msg}")

def log_success(msg):
    print(f"{Fore.GREEN}[SUCCESS]{Style.RESET_ALL} {msg}")

def log_warning(msg):
    print(f"{Fore.YELLOW}[WARNING]{Style.RESET_ALL} {msg}")

def log_error(msg):
    print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} {msg}")

MANDATORY_SECTIONS = [
    (r"resumo", "Resumo do Achado"),
    (r"interpreta", "Interpretação Detalhada"),
    (r"próximos passos|perguntas", "Próximos Passos e Perguntas"),
    (r"referênc", "Referências Confiáveis")
]

MANDATORY_DISCLAIMER = "Esta análise tem fins educativos e não substitui consulta médica."

FORBIDDEN_PATTERNS = [
    (r"\bvocê tem\b", "Declaração direta de diagnóstico ('você tem')"),
    (r"\bvocê está com\b", "Declaração direta de diagnóstico ('você está com')"),
    (r"\bdiagnóstico definitivo\b", "Afirmação de diagnóstico definitivo"),
    (r"\bprescrevo\b", "Termo de prescrição ('prescrevo')"),
    (r"\breceito\b", "Termo de prescrição ('receito')"),
    (r"\btome\b\s+\d+", "Instrução de dosagem ('tome X')"),
    (r"\btratamento de escolha é\b", "Definição de protocolo terapêutico único"),
]

def validate_content(content):
    errors = []
    warnings = []
    
    # 1. Check sections
    for pattern, name in MANDATORY_SECTIONS:
        if not re.search(pattern, content, re.IGNORECASE):
            errors.append(f"Seção obrigatória ausente ou mal nomeada: '{name}'")
            
    # 2. Check disclaimer
    normalized_content = re.sub(r'\s+', ' ', content)
    normalized_disclaimer = re.sub(r'\s+', ' ', MANDATORY_DISCLAIMER)
    if normalized_disclaimer.lower() not in normalized_content.lower():
        errors.append(f"Aviso legal exato obrigatório não encontrado: '{MANDATORY_DISCLAIMER}'")
        
    # 3. Check forbidden patterns (Zero Diagnosis / Zero Prescription)
    for pattern, description in FORBIDDEN_PATTERNS:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            errors.append(f"Violação ética (Prescrição/Diagnóstico): Encontrado '{match.group(0)}' ({description})")
            
    # 4. Check for emergency protocol recommendation if serious keywords are present
    serious_keywords = [r"dor no peito", r"ideação", r"suicí", r"infarto", r"troponina alta"]
    has_serious = any(re.search(kw, content, re.IGNORECASE) for kw in serious_keywords)
    if has_serious:
        # Check if emergency numbers (188, 192, 193) are in the text
        if not any(num in content for num in ["188", "192", "193"]):
            warnings.append("Detectados termos de potencial gravidade clínica, mas números de emergência (188, 192, 193) não foram citados.")
            
    return errors, warnings

def run_self_test():
    log_info("Iniciando auto-teste do validador...")
    
    good_text = """
    # Relatório de Análise Educativa
    
    ## Resumo do Achado
    Este é um resumo explicativo simples para que o leitor entenda.
    
    ## Interpretação Detalhada
    Aqui explicamos o que cada biomarcador significa em linguagem simples.
    
    ## Próximos Passos e Perguntas ao Médico
    Sugestões de perguntas:
    1. Doutor, como este valor de ferro se relaciona com os meus sintomas?
    
    ## Referências Confiáveis
    Fontes: Organização Mundial da Saúde (OMS), Sociedade Brasileira de Cardiologia (SBC).
    
    > [!IMPORTANT]
    > Esta análise tem fins educativos e não substitui consulta médica.
    """
    
    bad_text_1 = """
    # Relatório Médico
    Você tem anemia grave e deve tomar 80mg de ferro duas vezes ao dia.
    """
    
    # Test Good
    g_errors, g_warnings = validate_content(good_text)
    if g_errors:
        log_error("Auto-teste falhou: O texto válido foi reportado com erros.")
        print(g_errors)
        return False
    else:
        log_success("Auto-teste passou para texto de alta qualidade.")
        
    # Test Bad
    b_errors, b_warnings = validate_content(bad_text_1)
    if not b_errors:
        log_error("Auto-teste falhou: O texto inválido não acionou erros.")
        return False
    else:
        log_success(f"Auto-teste passou para texto com infrações éticas. Erros capturados: {len(b_errors)}")
        for e in b_errors:
            print(f"  - {e}")
            
    return True

def main():
    parser = argparse.ArgumentParser(description="Validador 5 estrelas de Relatórios de Interpretação Médica.")
    parser.add_argument("--file", help="Caminho do arquivo Markdown gerado para validar.")
    parser.add_argument("--test", action="store_true", help="Executa a suíte de auto-testes.")
    
    args = parser.parse_args()
    
    if args.test:
        success = run_self_test()
        sys.exit(0 if success else 1)
        
    if not args.file:
        log_error("Por favor, especifique um arquivo com --file ou rode --test")
        sys.exit(1)
        
    if not os.path.exists(args.file):
        log_error(f"Arquivo não encontrado: {args.file}")
        sys.exit(1)
        
    with open(args.file, "r", encoding="utf-8") as f:
        content = f.read()
        
    errors, warnings = validate_content(content)
    
    print(f"──────────────────────────────────────────────────────")
    print(f"🔍 Validador de Skill Médica: {os.path.basename(args.file)}")
    print(f"──────────────────────────────────────────────────────")
    
    if warnings:
        for w in warnings:
            log_warning(w)
            
    if errors:
        for e in errors:
            log_error(e)
        print(f"──────────────────────────────────────────────────────")
        log_error("VEREDICTO: FALHA (Contrato violado. Verifique os erros acima.)")
        sys.exit(1)
    else:
        log_success("VEREDICTO: PASSOU (O relatório cumpre todos os requisitos do contrato ético de 5 estrelas.)")
        sys.exit(0)

if __name__ == "__main__":
    main()
