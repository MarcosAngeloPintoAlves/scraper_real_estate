from selenium import webdriver
from selenium.common import exceptions
import pandas as pd
from datetime import date
import time

options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--disable-notifications")
options.add_argument("disable-infobars")
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36")

#input de características do imóvel
cidade = str(input('Deseja olhar casas de qual cidade?'))
estado = str(input('Essa UF do país se encontra a cidade? Digite a sigla em letras minúsculas: sp, rj, minas-gerais, etc:'))
tipo_imovel = str(input('Qual o tipo do imóvel? Lista: casa, apartamento, condominio ou chacara:'))
transacao = str(input('Compra ou aluguel de imoveis? Lista: venda e aluguel:'))
pages = int(input('Quantas páginas de dados deseja? Cada página contém cerca de 30 registros:'))

driver = webdriver.Chrome(options=options)

print(f'https://www.vivareal.com.br/{transacao}/{estado}/{cidade}/{tipo_imovel}_residencial/')

driver.get(f'https://www.vivareal.com.br/{transacao}/{estado}/{cidade}/{tipo_imovel}_residencial/')

driver.find_element_by_xpath('//*[@id="cookie-notifier-cta"]').click()

#definindo listas que vão receber o valor dos elementos xpath
nome_list=[]
endereco_list=[]
preco_list=[]
metros_list=[]
quartos_list=[]
banheiros_list=[]
vagas_list=[]

for i in range(1, pages+1):
    print(i)
    try:                                                                                                                                                                                                                                            
        nome = driver.find_elements_by_xpath('//a[@class="property-card__content-link js-card-title"]/div[@class="property-card__content"]/h2[@class="property-card__header"]/span[@class="property-card__title js-cardLink js-card-title"]') 
        endereco = driver.find_elements_by_xpath('//a[@class="property-card__content-link js-card-title"]/div[@class="property-card__content"]/h2[@class="property-card__header"]/span[@class="property-card__address-container js-property-card-address  js-see-on-map "]/span[@class="property-card__address"]')
        preco = driver.find_elements_by_xpath('//a[@class="property-card__content-link js-card-title"]/div[@class="property-card__content"]/section[@class="property-card__values  "]/div[@class="property-card__price js-property-card-prices js-property-card__price-small"]/p[@style="display: block;"]')
        metros = driver.find_elements_by_xpath('//a[@class="property-card__content-link js-card-title"]/div[@class="property-card__content"]/ul[@class="property-card__details"]/li[@class="property-card__detail-item property-card__detail-area"]/span[@class="property-card__detail-value js-property-card-value property-card__detail-area js-property-card-detail-area"]')
        quartos = driver.find_elements_by_xpath('//a[@class="property-card__content-link js-card-title"]/div[@class="property-card__content"]/ul[@class="property-card__details"]/li[@class="property-card__detail-item property-card__detail-room js-property-detail-rooms"]/span[@class="property-card__detail-value js-property-card-value"]')
        banheiros = driver.find_elements_by_xpath('//a[@class="property-card__content-link js-card-title"]/div[@class="property-card__content"]/ul[@class="property-card__details"]/li[@class="property-card__detail-item property-card__detail-bathroom js-property-detail-bathroom"]/span[@class="property-card__detail-value js-property-card-value"]')
        vagas = driver.find_elements_by_xpath('//a[@class="property-card__content-link js-card-title"]/div[@class="property-card__content"]/ul[@class="property-card__details"]/li[@class="property-card__detail-item property-card__detail-garage js-property-detail-garages"]/span[@class="property-card__detail-value js-property-card-value"]')

        for i in range(len(nome)):                                                                                      
            nome_list.append(nome[i].text)

        for j in range(len(endereco)):
            endereco_list.append(endereco[j].text)

        for h in range(len(preco)):
            preco_list.append(preco[h].text)

        for m in range(len(metros)):
            metros_list.append(metros[m].text)

        for q in range(len(quartos)):
            quartos_list.append(quartos[q].text)
        
        for b in range(len(banheiros)):
            banheiros_list.append(banheiros[b].text)

        for v in range(len(vagas)):
            vagas_list.append(vagas[v].text)

        if i < pages:
            try:
                driver.find_element_by_xpath('//*[@id="js-site-main"]/div[2]/div[1]/section/div[2]/div[2]/div/ul/li[9]/a').click()
            except:
                print("Erro.")
                pass
        else:
            pass
        time.sleep(10)
    except exceptions.StaleElementReferenceException:
        pass

driver.quit()

#zipando listas dentro de uma lista, passando em dataframe e salvando arquivo em .csv
dados_casa = list(zip(nome_list, endereco_list, preco_list, metros_list, 
quartos_list, banheiros_list, vagas_list))

dataset_residencial = pd.DataFrame(dados_casa, columns=['nome_imovel','endereço_imovel', 'preco_imovel',
 'metros_imovel', 'quartos_imovel', 'banheiros_imovel', 'vagas_imovel'])

dataset_residencial['data_extracao'] = str(date.today())

dataset_residencial.to_excel(f'real_estate_{cidade}_{estado}_{tipo_imovel}_{transacao}_{pages}_{str(date.today())}.xlsx',
 index=False, header=True)