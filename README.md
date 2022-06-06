# Scraping Real Estate Data

O projeto tem como objetivo fornecer um script para coleta personalizada de dados de imóveis a partir de scraping do site **vivareal.com** (um dos maiores sites de imóveis do Brasil). Esse projeto contém caráter exclusivamente educacional.

#########

É possível rodar o arquivo na máquina local a partir do comando "python 3 real_estate_scraper.py" no terminal direcionando a pasta destino dos arquivos. Para garantir que todas dependências estejam rodando com a mesma versão, é aconselhável criação de ambiente virtual e instalação dos pacotes contidos no requirements.txt.

Ao executar o arquivo será inicializado a caixa de diálogo que tomará os seguintes inputs:

**Cidade**: sempre digitada em letra minúscula, separada por "-" em caso de nomes compostos e sempre sem acento. Por exemplo: belo-horizonte, campinas, sao-paulo, etc;

**UF (estado)**: sempre digitada em letra minúscula contendo a sigla do estado em questão ou nome composto do estado separado por "-" a depender do caso. Exemplo: minas-gerais, sp, rj, pr, etc;

**Tipo do imóvel**: o input desse campo se trata de qual modalidade se deseja consultar na busca. As opções são: casa, apartamento, condominio e chacara;

**Transação**: aqui dizemos a respeito da transação desejada em relação ao imóvel, se desejamos comprar ou alugar. Portanto as opções são: venda e aluguel;

**Volume de dados**: e finalmente: quantas páginas devemos buscar? Esse input dirá qual é o tamanho do conjunto de dados aproximado que desejamos.

#########

Após a execução, o conjunto de dados será salvo em formato Excel no diretório do script.

As colunas da tabela final são:

'nome_imovel' = descrição do imóvel. Ex: casa n° 1314 ou apartamento xyz;
'endereço_imovel' = endereço do imóvel;
'preco_imovel' = preço de venda ou aluguel do imóvel;
'metros_imovel' = metragem do imóvel em metros quadrados;
'quartos_imovel' = número de quartos do imóvel;
'banheiros_imovel' = número de banheiros do imóvel;
'vagas_imovel' = número de vaga de veículos do imóvel;
'data_extracao' = data de coleta dos dados do imóvel;

#########

Melhorias futuras: coluna com o link do imóvel redirecionando para o site e criação de diretório contendo imagens do imóvel;

**Disclaimers**: registros de aluguel e venda virão misturados em alguns casos por conta da listagem no Viva Real.
