import requests
from bs4 import BeautifulSoup
import time

#Variaveis Globais
TOKEN = '8724511737:AAGGCJfn-7qVOl8ozjMc-L-YyEDaR3uVLt4'
CHAT_ID = '8920592138'
URL = 'https://www.mercadolivre.com.br/transmissor-receptor-hdmi-sem-fio-wireless-1080p-full-hd-50m-metros-transmite-espelha-tv-ps5-video-pc-notebook-d-densen/p/MLB61595839?pdp_filters=item_id%3AMLB5893429854&matt_tool=38524122&ua=zUF5Kr1tsCPn0P6jze0r7uRlRhA0_liH2A23_N_LhO6W4jE#origin=whatsapp&sid=whatsapp&wid=MLB5893429854'
PrecoDesejavel = 240

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

    #procura (soup.find) o preco nas linhas(span) com tipo(classe) especifico do Mercado Livre
    elemento_preco = soup.find("span", class_="andes-money-amount__fraction")

    if elemento_preco:

        # pega o texto de elemento_preco e o trata para virar um float
        texto_limpo = elemento_preco.text.replace(".", "").replace(",", ".").strip()

        #transforma em float
        preco_atual = float(texto_limpo)

        print('Preço checado: R$ %s' %preco_atual)


        if preco_atual <= PrecoDesejavel:
            telegramMensage(f" ALERTA DE PROMOÇÃO!\nO produto baixou para R$ {preco_atual}\nLink: {URL}")
            return True  # Sinaliza que encontrou a promoção

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