'''
Script para Gerar um Token JWT a partir de uma lista de Key IDs.
'''

import jwt
import os
import random
import time

os.system('clear')
# Comandos para criar CHAVE e SECRET para teste
# OBS: A Chave e o Secret devem ser iguais aos do Json Args da Function JWT

# OSX:
#  echo -n 'qualquer_string_aqui...' | md5 -r | tr '[:lower:]' '[:upper:]'

# Linux:
#  echo -n 'qualquer_string_aqui...' | md5sum | tr '[:lower:]' '[:upper:]'

# Exemplo: 

#  echo -n 'chave_pic_pay_2023' | md5 -r | tr '[:lower:]' '[:upper:]'
#  echo -n 'secret_pic_pay_2023' | md5 -r | tr '[:lower:]' '[:upper:]'

##########################################################################

# formato do dic 
# CHAVE_MD5 : SECRET_MD5

# chave_pic_pay_2023 (string) = 0AC4C3DEDB9B9263BEC8FF929D750D8A (MD5)
# secret_pic_pay_2023 (string) = 92E7D28F180A5BFC12139B1EA76FA897 (MD5)

kids_and_secrets = {
    '0AC4C3DEDB9B9263BEC8FF929D750D8A' : '92E7D28F180A5BFC12139B1EA76FA897'
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