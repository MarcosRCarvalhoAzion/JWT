'''
Script para Gerar um Token JWT a partir de uma lista de Key IDs.
'''

import jwt
import os
import random
import sys
import time

os.system('clear')

kids_and_secrets = {
    f'{sys.argv[1]}' : f'{sys.argv[2]}'
}

# get a random kid with secret
selected_kid, selected_secret = random.choice(list(kids_and_secrets.items()))

current_time = int(time.time())
_10_minutes_in_seconds = 10 * 60
expiration = current_time + _10_minutes_in_seconds

payload = {'exp': expiration, 'iat': current_time, 'my_data_1': 'x', 'my_data_2': 'y'}

headers = {'kid': selected_kid}

generated_jwt = jwt.encode(payload, selected_secret, algorithm='HS256', headers=headers)

authorization_token = f'Bearer {generated_jwt}'

msg = f'''
      --------------------------
      - AZION MOVE TO THE EDGE -
      -------------------------- 
      
      [+] [JWT] Gerado com sucesso!
      
      [!] CHAVE selecionada para gerar o JWT: {selected_kid}
      [!] SECRET selecionado para gerar o JWT: {selected_secret}
      
      -------------------------------------------------------------
      
      Adicione o Header abaixo na Request:
      
      ---------------------------
      Header Name: Authorization
      ---------------------------
      
      ---------------------------
      
      Header Value: {authorization_token}
      
      ---------------------------    
'''

# Salva o resultado num arquivo de texto: information.txt

with open('information.txt', 'w', encoding='utf-8') as _file:
    _file.write(msg)
print(msg)