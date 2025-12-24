# SIMULAÇÃO DE FLUXO DE VALIDAÇÃO DE IDENTIDADE

# Simulando extração de dados da CNH
nome_cnh = "JOÃO DA SILVA"
cpf_cnh = "12345678900"

# Simulando extração do nome de um comprovante
texto_comprovante = """
COMPANHIA DE LUZ
FATURA REFERENTE AO MÊS DE MAIO/2025
JOÃO DA SILVA
RUA EXEMPLO, 123 - CENTRO
SÃO PAULO - SP
CEP: 01000-000
"""

# Simulando comparação facial (DeepFace seria aqui, mas vamos simular)
match_facial = True
distancia_simulada = 0.32

# Validar se o nome da CNH está no texto do comprovante
nome_valido = nome_cnh in texto_comprovante.upper()

# Mostrar resultados simulados
print("=== VALIDAÇÃO DE IDENTIDADE (PoC Simulada) ===")
print(f"Nome extraído da CNH: {nome_cnh}")
print(f"CPF extraído da CNH: {cpf_cnh}")
print(f"Match Facial: {'Sim' if match_facial else 'Não'}")
print(f"Distância Simulada: {distancia_simulada}")
print(f"Nome presente no comprovante: {'Sim' if nome_valido else 'Não'}")

# Veredito final (simulação de regra)
if match_facial and distancia_simulada < 0.4 and nome_valido:
    status = "APROVADO"
else:
    status = "REPROVADO"

print("\nResultado Final:", status)