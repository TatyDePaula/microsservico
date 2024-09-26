import requests

def get_cep_info(cep):
    cep = ''.join(filter(str.isdigit, cep))
    
    if len(cep) != 8 or not cep.isdigit():
        raise ValueError("CEP inválido. Deve conter 8 dígitos numéricos.")
    
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    
    if response.status_code == 400:
        raise ValueError("CEP inválido. Formato incorreto.")
    
    data = response.json()
    
    if 'erro' in data and data['erro']:
        raise ValueError("CEP não encontrado.")
    
    return data

print(get_cep_info("13181292"))