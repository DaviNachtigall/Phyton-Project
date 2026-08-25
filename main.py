import requests
from bs4 import BeautifulSoup
import time

#Variaveis Globais
TOKEN = '8724511737:AAGGCJfn-7qVOl8ozjMc-L-YyEDaR3uVLt4'
CHAT_ID = '8920592138'
URL = 'https://www.amazon.com.br/Adaptador-Display-Wireless-Espelhamento-Celular/dp/B0H85CZKQ8/ref=sr_1_3?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=5NH7EO6X7I8O&dib=eyJ2IjoiMSJ9.ShOQnT7pcli9bQdNFc2Ah2p2jo_NUnV4yKv3bU1LsPaQLBnRdFZbz9rCKA9lFharQtbYy7rYPLMsFRJ-wtnx_m8wvaD5_-9vklSJe-n9Uf-LRUgT7k7QAwBS862roiLQH_j4B_c1BpGXXd6jQUukR7hjdSyege615H8qVYt4N7dwSs-tANLbcVGnoldggzhXugWF4GYTlP0c0F6RyG8YuB_YsDfPx-uDxMg8BX_QKbnMDjsnihRV85rgIm4ynuCbnQljVmIxRQYiU3Fss09s3J-OPoN_YE2iT40xijTz4SE.Bi7QsjUfXY1vAfm6AuCmm5I1Vi-E8ry01SeI_HMyAtA&dib_tag=se&keywords=hdmi+wireless&qid=1787630580&sprefix=hdmi+wirele%2Caps%2C242&sr=8-3&ufe=app_do%3Aamzn1.fos.db68964d-7c0e-4bb2-a95c-e5cb9e32eb12'
PrecoDesejavel = 280

def telegramMensage(mensagem):
    url =  'https://api.telegram.org/bot%s/sendMessage' % TOKEN
    dados = {'chat_id': CHAT_ID, 'text': mensagem}
    requests.post(url, data=dados)

def conferir_preco():
    headers = {'UserAgent': 'Mobizilla/5.0 (X11; Linux x86_64)'}

    #baixa o conteudo e coloca na variavel respota
    resposta = requests.get(URL, headers=headers)

    #organiza o texto html de resposta e armazena em soup
    soup = BeautifulSoup(resposta.text, "html.parser")

    # procura (soup.find) o preco nas linhas(div) com tipo(classe) especifico do Mercado Livre
    elemento_preco = soup.find("div", class_="ui-pdp-price__second-line")

    if not elemento_preco:
        # jeito alternativo do primeiro
        elemento_preco = soup.find("span", class_="andes-money-amount--main")

    if elemento_preco:

        # pega o texto de elemento_preco e o trata para virar um float
        texto_limpo = elemento_preco.text.replace(".", "").replace(",", ".").strip()

        #transforma em float
        preco_atual = float(texto_limpo)

        print('Preço checado: R$ %s' %preco_atual)


        if preco_atual <= PrecoDesejavel:
            telegramMensage(f" ALERTA DE PROMOÇÃO!\nO produto baixou para R$ {preco_atual}\nLink: {URL}")
            return True  # Sinaliza que encontrou a promoção

    else:
        print('Não foi possivel localizar a página')

    return False

def main():
    print('Funcionou a main')
    achou_promocao = False

    while achou_promocao == False:
        achou_promocao = conferir_preco()

        if achou_promocao:
            print('Promoção encontrada!')

        else:
            print("Ainda caro... Checando novamente em 1 hora.")
            time.sleep(3600)  # Pausa por 1 hora (3600 segundos)

#ponto de entrada com IF para poder importar parte do código em outro projeto
if __name__ == "__main__":
    main()