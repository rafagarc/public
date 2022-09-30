# ---------------------------------------------------
# BRFY PACK FOR PYTHON
# ---------------------------------------------------


help_menu = """
FUNCTIONS
format_number(): formata número para notação brasileira (99.999,99)
comma_dot_swap(): converte notação americana (99,999.99) para brasileira (99.999,99)
date_conv(): Converte formato de data dia/mês/ano para ano-mês-dia 
date_conv_br(): Converte ano-mês-dia para dia/mês/ano
De_to_de(): Coloca preposições em caixa baixa (Ex: 'Zé Da Silva' > 'Zé da Silva')
iso3_pais(): Converte sigla ISO3 para nome do país em português
desacentua(): Remove acentos, cedilhas e outros sinais não-ASCII
cores(): Retorna lista de cores com tamanho especificado
paleta(): Recebe lista e retorna combinação de cores
estado_to_UF(): Nome do estado > Sigla

DICTIONARIES
country_to_pais: Países EN>PT
ESTADO_to_UF: NOME DO ESTADO > Sigla
state_to_UF: Nome do estado (EN) > Sigla
uf_to_estado: Sigla > Nome do estado
UF_to_estado: SIGLA > Nome do estado
week_to_semana: Dia da semana EN > PT
week_dic: Dia da semana (0:6) > PT
UF_to_code: UF para código IBGE
estado_to_code: estado para código IBGE

LISTS
UF_list: Siglas de estados
capitais: Capitais do Brasil (Capital-UF)
"""

# ---------------------------------------------------


def help():
    print(help_menu)

# ---------------------------------------------------


# Converte número para string formato brasileiro

def format_number(raw_n):
    turn = 3
    offset = 0
    num_str = str(raw_n).replace('.',',')
    comma_slot = num_str.find(',')
    if comma_slot > turn:
        for i in range(comma_slot//3):
            num_str = num_str[:comma_slot-turn] + '.' + num_str[comma_slot-turn:]
            turn += 3
    elif comma_slot == -1 and len(str(raw_n)) > turn:
        for i in range(len(str(raw_n))//3):
            num_str = num_str[:-turn-offset] + '.' + num_str[-turn-offset:]
            turn += 3
            offset += 1
    else:
        pass
    if num_str[0] == '.':
        num_str = num_str[1:]
    else:
        pass
    return num_str

# ---------------------------------------------------


# Converte string com vírgula e número para formato brasileiro e vice-versa

def comma_dot_swap(raw_n):
    num_str = raw_n.replace(',','#sep#').replace('.','#dec#').replace('#sep#','.').replace('#dec#',',')
    return num_str

# Converte data brasileira para formato YYYY-MM-DD

def date_conv(my_date):

    day_sep = my_date.find('/')
    month_sep = my_date.rfind('/')
    day = my_date[0:day_sep]
    month = my_date[day_sep+1:month_sep]
    year = my_date[-4:]
    
    if len(day) == 1:
        day = '0' + day
    else:
        pass
    
    if len(month) == 1:
        month = '0' + month
    else:
        pass
    
    ymd_date = f'{year}-{month}-{day}'
    return ymd_date

# ---------------------------------------------------


def date_conv_br(my_date):

    day_sep = my_date.find('-')
    month_sep = my_date.rfind('-')
    year = my_date[0:day_sep]
    month = my_date[day_sep+1:month_sep]
    day = my_date[-2:]
    
    if len(day) == 1:
        day = '0' + day
    else:
        pass
    
    if len(month) == 1:
        month = '0' + month
    else:
        pass
    
    ymd_date = f'{day}/{month}/{year}'
    return ymd_date    

def De_to_de(x):
    prep_dic = {' Do ':' do ', ' Da ':' da ', ' Dos ':' dos ', ' Das ':' das ', ' De ':' de ', ' E ': ' e '}
    for i in prep_dic:
        x = x.replace(i,prep_dic[i])
    return x

# ---------------------------------------------------


def iso3_pais(x):
    
    iso_dic = {'AFG': 'Afeganistão', 'ZAF': 'África do Sul', 'ALB': 'Albânia', 'DEU': 'Alemanha', 'AND': 'Andorra', 'AGO': 'Angola', 'ATG': 'Antígua e Barbuda', 'SAU': 'Arábia Saudita', 'DZA': 'Argélia', 'ARG': 'Argentina', 'ARM': 'Armênia', 'AUS': 'Austrália', 'AUT': 'Áustria', 'AZE': 'Azerbaijão', 'BHS': 'Bahamas', 'BGD': 'Bangladesh', 'BRB': 'Barbados', 'BHR': 'Barém', 'BEL': 'Bélgica', 'BLZ': 'Belize', 'BEN': 'Benim', 'BLR': 'Bielorrússia', 'BOL': 'Bolívia', 'BIH': 'Bósnia e Herzegovina', 'BWA': 'Botswana', 'BRA': 'Brasil', 'BRN': 'Brunei', 'BGR': 'Bulgária', 'BFA': 'Burkina Faso', 'BDI': 'Burundi', 'BTN': 'Butão', 'CPV': 'Cabo Verde', 'KHM': 'Camboja', 'CMR': 'Camarões', 'CAN': 'Canadá', 'QAT': 'Catar', 'KAZ': 'Cazaquistão', 'CAF': 'República Centro-Africana', 'TCD': 'Chade', 'CZE': 'República Tcheca', 'CHL': 'Chile', 'CHN': 'China', 'CYP': 'Chipre', 'COL': 'Colômbia', 'COM': 'Comores', 'COG': 'República do Congo', 'COD': 'República Democrática do Congo', 'KOR': 'Coreia do Sul', 'PRK': 'Coreia do Norte', 'CIV': 'Costa do Marfim', 'CRI': 'Costa Rica', 'HRV': 'Croácia', 'CUB': 'Cuba', 'DNK': 'Dinamarca', 'DJI': 'Djibouti', 'DMA': 'Dominica', 'DOM': 'República Dominicana', 'EGY': 'Egito', 'SLV': 'El Salvador', 'ARE': 'Emirados Árabes', 'ECU': 'Equador', 'ERI': 'Eritreia', 'SVK': 'Eslováquia', 'SVN': 'Eslovênia', 'ESP': 'Espanha', 'USA': 'Estados Unidos', 'EST': 'Estônia', 'SWZ': 'Essuatíni', 'ETH': 'Etiópia', 'FJI': 'Fiji', 'PHL': 'Filipinas', 'FIN': 'Finlândia', 'FRA': 'França', 'GAB': 'Gabão', 'GMB': 'Gâmbia', 'GHA': 'Gana', 'GEO': 'Geórgia', 'GRC': 'Grécia', 'GRD': 'Granada', 'GTM': 'Guatemala', 'GUY': 'Guiana', 'GNB': 'Guiné-Bissau', 'GIN': 'Guiné', 'GNQ': 'Guiné Equatorial', 'HTI': 'Haiti', 'HND': 'Honduras', 'HUN': 'Hungria', 'YEM': 'Iêmen', 'IND': 'Índia', 'IDN': 'Indonésia', 'IRQ': 'Iraque', 'IRN': 'Irão', 'IRL': 'Irlanda', 'ISL': 'Islândia', 'ISR': 'Israel', 'ITA': 'Itália', 'JAM': 'Jamaica', 'JPN': 'Japão', 'JOR': 'Jordânia', 'KIR': 'Kiribati', 'KWT': 'Kuwait', 'LAO': 'Laos', 'LSO': 'Lesoto', 'LVA': 'Letônia', 'LBN': 'Líbano', 'LBR': 'Libéria', 'LBY': 'Líbia', 'LIE': 'Liechtenstein', 'LTU': 'Lituânia', 'LUX': 'Luxemburgo', 'MKD': 'Macedônia do Norte', 'MDG': 'Madagascar', 'MYS': 'Malásia', 'MWI': 'Malawi', 'MDV': 'Maldivas', 'MLI': 'Mali', 'MLT': 'Malta', 'MAR': 'Marrocos', 'MHL': 'Ilhas Marshall', 'MUS': 'Maurícia', 'MRT': 'Mauritânia', 'MEX': 'México', 'MMR': 'Mianmar', 'FSM': 'Estados Federados da Micronésia', 'MOZ': 'Moçambique', 'MDA': 'Moldávia', 'MCO': 'Mónaco', 'MNG': 'Mongólia', 'MNE': 'Montenegro', 'NAM': 'Namíbia', 'NRU': 'Nauru', 'NPL': 'Nepal', 'NIC': 'Nicarágua', 'NER': 'Níger', 'NGA': 'Nigéria', 'NOR': 'Noruega', 'NZL': 'Nova Zelândia', 'OMN': 'Omã', 'NLD': 'Holanda', 'PLW': 'Palau', 'PAN': 'Panamá', 'PNG': 'Papua-Nova Guiné', 'PAK': 'Paquistão', 'PRY': 'Paraguai', 'PER': 'Peru', 'POL': 'Polônia', 'PRT': 'Portugal', 'KEN': 'Quênia', 'KGZ': 'Quirguistão', 'GBR': 'Reino Unido', 'ROU': 'Romênia', 'RWA': 'Ruanda', 'RUS': 'Rússia', 'WSM': 'Samoa', 'SLB': 'Ilhas Salomão', 'SMR': 'San Marino', 'LCA': 'Santa Lúcia', 'KNA': 'São Cristóvão e Névis', 'STP': 'São Tomé e Príncipe', 'VCT': 'São Vicente e Granadinas', 'SEN': 'Senegal', 'SLE': 'Serra Leoa', 'SRB': 'Sérvia', 'SYC': 'Seicheles', 'SGP': 'Singapura', 'SYR': 'Síria', 'SOM': 'Somália', 'LKA': 'Sri Lanka', 'SDN': 'Sudão', 'SSD': 'Sudão do Sul', 'SWE': 'Suécia', 'CHE': 'Suíça', 'SUR': 'Suriname', 'THA': 'Tailândia', 'TJK': 'Tajiquistão', 'TZA': 'Tanzânia', 'TLS': 'Timor-Leste', 'TGO': 'Togo', 'TON': 'Tonga', 'TTO': 'Trinidad e Tobago', 'TUN': 'Tunísia', 'TKM': 'Turcomenistão', 'TUR': 'Turquia', 'TUV': 'Tuvalu', 'UKR': 'Ucrânia', 'UGA': 'Uganda', 'URY': 'Uruguai', 'UZB': 'Uzbequistão', 'VUT': 'Vanuatu', 'VEN': 'Venezuela', 'VNM': 'Vietnã', 'ZMB': 'Zâmbia', 'ZWE': 'Zimbábue'}
    try: 
        a = iso_dic[x.upper()]
    except:
        a = ''
    
    return a

# ---------------------------------------------------


def cores(size):
    
    colors = ['#3395ea', '#fc4f71', '#F1CF00', '#125d9d', '#ffc0ce', '#4EC4B2', '#d14664', '#F2895A', '#f8c694', '#9575ed']
    
    wheel = 0
    count = 0 
    palette = []
    
    while count < size:
        if wheel > 9:
            wheel = 0
        else:
            pass
        palette.append(colors[wheel])
        count += 1
        wheel +=1
    return palette

def paleta(iterable):
    this_palette = cores(len(iterable))
    count = 0
    for i in iterable:
        print(f'{i}: {this_palette[count]}')
        count += 1

# ---------------------------------------------------


def desacentua(x):
    normalMap = {'À': 'A', 'Á': 'A', 'Â': 'A', 'Ã': 'A', 'Ä': 'A',
             'à': 'a', 'á': 'a', 'â': 'a', 'ã': 'a', 'ä': 'a', 'ª': 'A',
             'È': 'E', 'É': 'E', 'Ê': 'E', 'Ë': 'E',
             'è': 'e', 'é': 'e', 'ê': 'e', 'ë': 'e',
             'Í': 'I', 'Ì': 'I', 'Î': 'I', 'Ï': 'I',
             'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i',
             'Ò': 'O', 'Ó': 'O', 'Ô': 'O', 'Õ': 'O', 'Ö': 'O',
             'ò': 'o', 'ó': 'o', 'ô': 'o', 'õ': 'o', 'ö': 'o', 'º': 'O',
             'Ù': 'U', 'Ú': 'U', 'Û': 'U', 'Ü': 'U',
             'ù': 'u', 'ú': 'u', 'û': 'u', 'ü': 'u',
             'Ñ': 'N', 'ñ': 'n',
             'Ç': 'C', 'ç': 'c',
             '§': 'S',  '³': '3', '²': '2', '¹': '1'}
    normalize = str.maketrans(normalMap)
    return x.translate(normalize)
    
# ---------------------------------------------------

def estado_to_UF(x):
    estado_UF = {'ACRE':'AC', 'ALAGOAS':'AL', 'AMAPA':'AP', 'AMAZONAS':'AM', 'BAHIA':'BA', 'CEARA':'CE', 'DISTRITO FEDERAL':'DF', 'ESPIRITO SANTO':'ES', 'GOIAS':'GO', 'MARANHAO':'MA', 'MATO GROSSO':'MT', 'MATO GROSSO DO SUL':'MS', 'MINAS GERAIS':'MG', 'PARA':'PA', 'PARAIBA':'PB', 'PARANA':'PR', 'PERNAMBUCO':'PE', 'PIAUI':'PI', 'RIO DE JANEIRO':'RJ', 'RIO GRANDE DO NORTE':'RN', 'RIO GRANDE DO SUL':'RS', 'RONDONIA':'RO', 'RORAIMA':'RR', 'SANTA CATARINA':'SC', 'SAO PAULO':'SP', 'SERGIPE':'SE', 'TOCANTINS':'TO'}
    
    normalMap = {'À': 'A', 'Á': 'A', 'Â': 'A', 'Ã': 'A', 'Ä': 'A',
             'à': 'a', 'á': 'a', 'â': 'a', 'ã': 'a', 'ä': 'a', 'ª': 'A',
             'È': 'E', 'É': 'E', 'Ê': 'E', 'Ë': 'E',
             'è': 'e', 'é': 'e', 'ê': 'e', 'ë': 'e',
             'Í': 'I', 'Ì': 'I', 'Î': 'I', 'Ï': 'I',
             'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i',
             'Ò': 'O', 'Ó': 'O', 'Ô': 'O', 'Õ': 'O', 'Ö': 'O',
             'ò': 'o', 'ó': 'o', 'ô': 'o', 'õ': 'o', 'ö': 'o', 'º': 'O',
             'Ù': 'U', 'Ú': 'U', 'Û': 'U', 'Ü': 'U',
             'ù': 'u', 'ú': 'u', 'û': 'u', 'ü': 'u',
             'Ñ': 'N', 'ñ': 'n',
             'Ç': 'C', 'ç': 'c',
             '§': 'S',  '³': '3', '²': '2', '¹': '1'}

    normalize = str.maketrans(normalMap)

    y = x.translate(normalize).upper()

    try:
        a = estado_UF[y]
    except:
        a = x

    return a

# ---------------------------------------------------



country_to_pais = {'Afghanistan':'Afeganistão', 'Albania':'Albânia', 'Algeria':'Argélia', 'Andorra':'Andorra', 'Angola':'Angola', 'Antigua and Barbuda':'Antígua e Barbuda', 'Argentina':'Argentina', 'Armenia':'Armênia', 'Australia':'Austrália', 'Austria':'Áustria', 'Azerbaijan':'Azerbaijão', 'Bahamas':'Bahamas', 'Bahrain':'Bahrain', 'Bangladesh':'Bangladesh', 'Barbados':'Barbados', 'Belarus':'Belarus', 'Belgium':'Bélgica', 'Belize':'Belize', 'Benin':'Benin', 'Bhutan':'Butão', 'Bolivia':'Bolívia', 'Bosnia and Herzegovina':'Bósnia e Herzegovina', 'Botswana':'Botswana', 'Brazil':'Brasil', 'Brunei':'Brunei', 'Bulgaria':'Bulgária', 'Burkina Faso':'Burkina Faso', 'Burma':'Burma', 'Burundi':'Burundi', 'Cabo Verde':'Cabo Verde', 'Cambodia':'Camboja', 'Cameroon':'Camarões', 'Canada':'Canadá', 'Central African Republic':'República Centro-Africana', 'Chad':'Chade', 'Chile':'Chile', 'China':'China', 'Colombia':'Colômbia', 'Comoros':'Comores', 'Congo (Brazzaville)':'República do Congo', 'Congo (Kinshasa)':'República   Democrática do Congo', 'Costa Rica':'Costa Rica', 'Cote d\'Ivoire':'Costa do Marfim', 'Croatia':'Croácia', 'Cuba':'Cuba', 'Cyprus':'Chipre', 'Czechia':'República Tcheca', 'Faroe Islands':'Ilhas Faroe', 'Greenland':'Groenlândia', 'Denmark':'Dinamarca', 'Diamond Princess':'Diamond Princess', 'Djibouti':'Djibouti', 'Dominica':'Dominica', 'Dominican Republic':'República Dominicana', 'Ecuador':'Equador', 'Egypt':'Egito', 'El Salvador':'El Salvador', 'Equatorial Guinea':'Guiné Equatorial', 'Eritrea':'Eritrea', 'Estonia':'Estônia', 'Eswatini':'Eswatini', 'Ethiopia':'Etiópia', 'Fiji':'Fiji', 'Finland':'Finlândia', 'French Guiana':'Guiana Francesa', 'French Polynesia':'Polinésia Francesa', 'Guadeloupe':'Guadalupe', 'Martinique':'Martinica', 'Mayotte':'Mayotte', 'New Caledonia':'Nova Caledônia', 'Reunion':'Ilhas Reunião', 'Saint Barthelemy':'Saint Barthelemy', 'Saint Pierre and Miquelon':'Saint Pierre e Miquelon', 'St Martin':'St Martin', 'France':'França', 'Gabon':'Gabão', 'Gambia':'Gâmbia', 'Georgia':'Geórgia', 'Germany':'Alemanha', 'Ghana':'Gana', 'Greece':'Grécia', 'Grenada':'Grenada', 'Guatemala':'Guatemala', 'Guinea':'Guiné', 'Guinea-Bissau':'Guiné-Bissau', 'Guyana':'Guiana', 'Haiti':'Haiti', 'Holy See':'Vaticano', 'Honduras':'Honduras', 'Hungary':'Hungria', 'Iceland':'Islândia', 'India':'Índia', 'Indonesia':'Indonésia', 'Iran':'Irã', 'Iraq':'Iraque', 'Ireland':'Irlanda', 'Israel':'Israel', 'Italy':'Itália', 'Jamaica':'Jamaica', 'Japan':'Japão', 'Jordan':'Jordânia', 'Kazakhstan':'Cazaquistão', 'Kenya':'Quênia', 'Korea, South':'Coreia do Sul', 'Kosovo':'Kosovo', 'Kuwait':'Kuwait', 'Kyrgyzstan':'Quirguistão', 'Laos':'Laos', 'Latvia':'Letônia', 'Lebanon':'Líbano', 'Lesotho':'Lesoto', 'Liberia':'Libéria', 'Libya':'Líbia', 'Liechtenstein':'Liechtenstein', 'Lithuania':'Lituânia', 'Luxembourg':'Luxemburgo', 'Madagascar':'Madagascar', 'Malawi':'Malawi', 'Malaysia':'Malásia', 'Maldives':'Maldivas', 'Mali':'Mali', 'Malta':'Malta', 'Marshall Islands':'Ilhas Marshall', 'Mauritania':'Mauritânia', 'Mauritius':'Ilhas Maurício', 'Mexico':'México', 'Moldova':'Moldova', 'Monaco':'Mônaco', 'Mongolia':'Mongólia', 'Montenegro':'Montenegro', 'Morocco':'Marrocos', 'Mozambique':'Moçambique', 'Namibia':'Namíbia', 'Nepal':'Nepal', 'Aruba':'Aruba', 'Bonaire, Sint Eustatius and Saba':'Bonaire, Santo Eustáquio e Saba', 'Curacao':'Curaçao', 'Sint Maarten':'Sint Maarten', 'Netherlands':'Holanda', 'New Zealand':'Nova Zelândia', 'Nicaragua':'Nicarágua', 'Niger':'Níger', 'Nigeria':'Nigéria', 'North Macedonia':'Macedônia do Norte', 'Norway':'Noruega', 'Oman':'Omã', 'Pakistan':'Paquistão', 'Panama':'Panamá', 'Papua New Guinea':'Papua Nova Guiné', 'Paraguay':'Paraguai', 'Peru':'Peru', 'Philippines':'Filipinas', 'Poland':'Polônia', 'Portugal':'Portugal', 'Qatar':'Catar', 'Romania':'Romênia', 'Russia':'Rússia', 'Rwanda':'Ruanda', 'Saint Kitts and Nevis':'São Cristóvão e Nevis', 'Saint Lucia':'Santa Lúcia', 'Saint Vincent and the Grenadines':'São Vicente e Granadinas', 'San Marino':'San Marino', 'Sao Tome and Principe':'São Tomé e Príncipe', 'Saudi Arabia':'Arábia Saudita', 'Senegal':'Senegal', 'Serbia':'Sérvia', 'Seychelles':'Seychelles', 'Sierra Leone':'Serra Leoa', 'Singapore':'Cingapura', 'Slovakia':'Eslováquia', 'Slovenia':'Eslovênia', 'Solomon Islands':'Ilhas Salomão', 'Somalia':'Somália', 'South Africa':'África do Sul', 'South Sudan':'Sudão do Sul', 'Spain':'Espanha', 'Sri Lanka':'Sri Lanka', 'Sudan':'Sudão', 'Suriname':'Suriname', 'Sweden':'Suécia', 'Switzerland':'Suíça', 'Syria':'Síria', 'Taiwan*':'Taiwan', 'Tajikistan':'Tadjiquistão', 'Tanzania':'Tanzânia', 'Thailand':'Tailândia', 'Timor-Leste':'Timor-Leste', 'Togo':'Togo', 'Trinidad and Tobago':'Trinidad e Tobago', 'Tunisia':'Tunísia', 'Turkey':'Turquia', 'US':'EUA', 'Uganda':'Uganda', 'Ukraine':'Ucrânia', 'United Arab Emirates':'Emirados Árabes', 'Anguilla':'Anguilla', 'Bermuda':'Bermudas', 'British Virgin Islands':'Ilhas Virgens Britânicas', 'Cayman Islands':'Ilhas Cayman', 'Channel Islands':'Ilhas do Canal', 'Falkland Islands (Malvinas)':'Ilhas Falkland (Malvinas)', 'Gibraltar':'Gibraltar', 'Isle of Man':'Ilha de Man', 'Montserrat':'Montserrat', 'Turks and Caicos Islands':'Ilhas Turcas e Caicos', 'United Kingdom':'Reino Unido', 'Uruguay':'Uruguai', 'Uzbekistan':'Uzbequistão', 'Vanuatu':'Vanuatu', 'Venezuela':'Venezuela', 'Vietnam':'Vietnã', 'West Bank and Gaza':'Cisjordânia e Gaza', 'Western Sahara':'Saara Ocidental', 'Yemen':'Iémen', 'Zambia':'Zâmbia', 'Zimbabwe':'Zimbábue', 'American Samoa':'Samoa Americana', 'Guam':'Guam', 'Northern Mariana Islands':'Ilhas Marianas do Norte', 'Puerto Rico':'Porto Rico', 'Virgin Islands':'Ilhas Virgens'}

# ---------------------------------------------------

UF_to_code = {'AC': '12', 'AL': '27', 'AP': '16', 'AM': '13', 'BA': '29', 'CE': '23', 'DF': '53', 'ES': '32', 'GO': '52', 'MA': '21', 'MT': '51', 'MS': '50', 'MG': '31', 'PA': '15', 'PB': '25', 'PR': '41', 'PE': '26', 'PI': '22', 'RN': '24', 'RS': '43', 'RJ': '33', 'RO': '11', 'RR': '14', 'SC': '42', 'SP': '35', 'SE': '28', 'TO': '17'}

estado_to_code = {'Acre': '12', 'Alagoas': '27', 'Amapá': '16', 'Amazonas': '13', 'Bahia': '29', 'Ceará': '23', 'Distrito Federal': '53', 'Espírito Santo': '32', 'Goiás': '52', 'Maranhão': '21', 'Mato Grosso': '51', 'Mato Grosso do Sul': '50', 'Minas Gerais': '31', 'Pará': '15', 'Paraíba': '25', 'Paraná': '41', 'Pernambuco': '26', 'Piauí': '22', 'Rio Grande do Norte': '24', 'Rio Grande do Sul': '43', 'Rio de Janeiro': '33', 'Rondônia': '11', 'Roraima': '14', 'Santa Catarina': '42', 'São Paulo': '35', 'Sergipe': '28', 'Tocantins': '17'}

UF_to_estado = {'AC':'Acre', 'AL':'Alagoas', 'AP':'Amapá', 'AM':'Amazonas', 'BA':'Bahia', 'CE':'Ceará', 'DF':'Distrito Federal', 'ES':'Espírito Santo', 'GO':'Goiás', 'MA':'Maranhão', 'MS':'Mato Grosso do Sul', 'MT':'Mato Grosso', 'MG':'Minas Gerais', 'PA':'Pará', 'PB':'Paraíba', 'PR':'Paraná', 'PE':'Pernambuco', 'PI':'Piauí', 'RJ':'Rio de Janeiro', 'RN':'Rio Grande do Norte', 'RS':'Rio Grande do Sul', 'RO':'Rondônia', 'RR':'Roraima', 'SC':'Santa Catarina', 'SP':'São Paulo', 'SE':'Sergipe', 'TO':'Tocantins'}

capitais = ['Brasília-DF', 'Rio Branco-AC', 'Maceió-AL', 'Macapá-AP', 'Manaus-AM', 'Salvador-BA', 'Fortaleza-CE', 'Vitória-ES', 'Goiânia-GO', 'São Luís-MA', 'Cuiabá-MT', 'Campo Grande-MS', 'Belo Horizonte-MG', 'Belém-PA', 'João Pessoa-PB', 'Curitiba-PR', 'Recife-PE', 'Teresina-PI', 'Rio de Janeiro-RJ', 'Natal-RN', 'Porto Alegre-RS', 'Porto Velho-RO', 'Boa Vista-RR', 'Florianópolis-SC', 'São Paulo-SP', 'Aracajú-SE', 'Palmas-TO']

week_to_semana = {'Sunday':'domingo', 'Monday':'segunda-feira', 'Tuesday':'terça-feira', 'Wednesday':'quarta-feira', 'Thursday':'quinta-feira', 'Friday':'sexta-feira', 'Saturday':'Sábado'}

week_dic = {6:'domingo', 0:'segunda-feira', 1:'terça-feira', 2:'quarta-feira', 3:'quinta-feira', 4:'sexta-feira', 5:'sábado'}

UF_list = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MS', 'MT', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']