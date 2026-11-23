"""SETEL (Secretaria de Telecomunicações): regras de classificação, lugar e países. Calibrado com os compromissos já classificados no painel."""
import re,unicodedata
def N(s):
    if s is None or s!=s: return ''
    return unicodedata.normalize('NFD',str(s)).encode('ascii','ignore').decode()

SEC=re.compile(r'(Agentes p[uú]blicos participantes:|Agentes privados participantes:|Representantes de governo estrangeiro ou organismo internacional:)',re.I)
def secoes(p):
    p=re.sub(r'\(CPF:[^)]*\)','',p or ''); d={'pub':'','priv':'','ext':''}; cur=None
    for x in SEC.split(p):
        xl=x.lower()
        if xl.startswith('agentes p'+'\u00fa'.lower()) or xl.startswith('agentes publicos'): cur='pub'
        elif xl.startswith('agentes privados'): cur='priv'
        elif xl.startswith('representantes de governo'): cur='ext'
        elif cur: d[cur]+=' '+x
    return d
def sem_mcom(pub):
    """tira da lista de agentes públicos as pessoas do próprio MCom (órgão 'Ministério das Comunicações'/MCOM/SETEL)"""
    out=[]
    for l in re.split(r'\n\s*-\s*|\s-\s(?=[A-Z])',pub):
        n=N(l)
        if re.search(r'ministerio das comunicacoes|\bMCOM\b|\bSETEL\b',n,re.I) and not re.search(r'anatel|telebras|camara|senado',n,re.I): continue
        out.append(l)
    return ' | '.join(out)
R={}
R['min']=r'ministro(\(a\))? de estado / minist[a-z]+ das comunicacoes|ministro de estado das comunicacoes|ministro das comunicacoes|ministro da comunicacao|frederico de siqueira|frederico siqueira|jose juscelino|gabinete do ministro|com o ministro|ministro frederico|ministro juscelino'
R[1]=r'anatel|agencia nacional de telecomunicacoes'
R[2]=r'embaixad|\bUIT\b|\bITU\b|uniao internacional|uniao europeia|delegacao|governo (do|da|de) |republica d|\bBID\b|banco mundial|banco interamericano|\bONU\b|\bOEA\b|\bCAF\b|\bOCDE\b|unesco|japao|\bMIC\b|\bJICA\b|\bKOICA\b|\bUSTDA\b|\bCEPAL\b|\bCITEL\b|international|internacional|mercosul|ministerio .{0,30}(china|coreia|japao|portugal|franca|italia|alemanha|india|estados unidos|uruguai|argentina|paraguai|chile|colombia|mexico|peru|equador)'
R[3]=r'conexis|telcomp|abrint|abdc|brasscom|\bsindicato|federacao nacional|\bSENAR\b|\bCNI\b|\bFIESP\b|\bAbramulti\b|\bAbrafix\b|\bAbrasat\b|\bSindisat\b|\bABINEE\b|\bFEBRATEL\b|\bAPTEL\b|\bALAI\b|\bP&D Brasil\b|\bInternetSul\b|associacao (brasileira|nacional|de |das |dos )|\bAIAB\b'
R[4]=r'\bclaro\b|\bvivo\b|telefonica|\btim\b|\boi\b|algar|brisanet|v\.?tal|americanet|desktop|sercomtel|unifique|\bsky\b|nextel|operadora|\bnet\b|copel telecom|ligga|giga mais|\bISP\b|provedor|\bTelemar\b|\bEmbratel\b|\bAlloha\b|\bWorld ?Net\b'
R[5]=r'huawei|ericsson|nokia|google|\bmeta\b|facebook|microsoft|amazon|\baws\b|spacex|starlink|samsung|\bzte\b|padtec|qualcomm|intelbras|\boppo\b|\bapple\b|\bcisco\b|\bIBM\b|oracle|\bdell\b|\bintel\b|nvidia|mediatek|tiktok|\bx corp|twitter|netflix|\bxiaomi\b|\bmotorola\b|\blenovo\b|\bpositivo\b|\bascenty\b|\bequinix\b|\bodata\b|\bkuiper\b|\boneweb\b'
R[6]=r'telebras|\bEAF\b|entidade administradora da faixa|faixa de 3[,\.]?5|\bGAISPI\b|\bGIRED\b'
R[7]=r'deputad|senador|senado|camara dos deputados|camara municipal|prefeit|governador|assembleia|vereador|secretari[ao] (de estado|municipal|estadual)|governo do estado|governo estadual|\bFPA\b|bancada|frente parlamentar|comissao de |congresso nacional|secretari[ao] de estado da|secretaria (municipal|estadual)|controladoria geral'
T={}
T[0]=r'escolas? conectad|\bEACE\b|entidade administradora da conectividade|conectividade (de|das|nas) escolas|conectividade escolar|\bENEC\b|escola'
T[1]=r'rodovia|4g|5g|\b700 ?mhz\b|leilao|cobertura movel|telefonia movel|torres?\b|antena|\bblitz\b|\bsmp\b|estrada|cobertura rodoviaria|\bBR-?\d{2,3}'
T[2]=r'inclusao digital|\bPNID\b|\bGTI-?PNID\b|pontos? de inclusao|computadores|\bCRC\b|recondicionamento|\bchips?\b|internet brasil|\bPDDE\b|politica nacional de inclusao|conectividade significativa|letramento|formatura'
T[3]=r'satelite|espacial|\bleo\b|orbita|starlink|spacex|kuiper|oneweb|\bagencia espacial\b|\bAEB\b|spacesail|hispasat|viasat|\bSGDC\b|eutelsat|telesat|\bNTN\b'
T[4]=r'3[,\.]5 ?ghz|3[,\.]5ghz|\bgaispi\b|\bgired\b|\btv digital\b|\btv 3\.?0\b|radiodifusao|faixa de 3|interferencia|\bTV aberta\b|banda c\b|parabolica|\b600 ?mhz\b'
T[5]=r'\bfust\b|fundo de universalizacao|conselho gestor do fust|conselho gestor do fundo'
T[6]=r'norte conectado|infovia|programa norte|amazonia conectada|cabos? (fluvia|subfluvia)|\bPNC\b|rios? (amazonas|negro|solimoes)|madeira|tapajos'
T[7]=r'data ?cent|\bnuvem\b|\bcloud\b|\bredata\b|\bhyperscal|\bDC\b'
T[8]=r'ciberseguranca|seguranca cibernetica|\bcyber|cibernetic|ciberespaco|\bCNCiber\b|\bGSI\b|\bCTIR\b|ataque ciberne|lgpd|protecao de dados|\bCiber\b|e-?ciber'
T[9]=r'inteligencia artificial|\bIA\b|\bDiG\.?IA\b|\bAI\b|\bia generativa\b|llm|chatgpt|openai'
T[10]=r'cabos? submarin|\bsubmarin|ellalink|\bmonet\b|\bmalbec\b|atlantico sul|cabo transatl'
def classificar(reg):
    subj=N(reg.get('assunto')); loc=N(reg.get('local')); obj=N(reg.get('objetivos')); info=N(reg.get('info'))
    s=secoes(reg.get('participantes')); pub=N(sem_mcom(s['pub'])); priv=N(s['priv']); ext=N(s['ext'])
    pubfull=N(s['pub'])
    f=lambda k,txt,fl=re.I: re.search(R[k],txt,fl) is not None
    cats=set()
    if re.search(R['min'],' | '.join([subj,loc,pubfull,info]),re.I): cats.add(0)
    if f(1,' | '.join([subj,pub,priv,ext,info,obj,loc])): cats.add(1)
    if ext.strip() or f(2,' | '.join([subj,ext,priv,info,obj,loc])): cats.add(2)
    if f(3,' | '.join([subj,priv,ext,pub,info])): cats.add(3)
    if f(4,' | '.join([subj,priv,pub,info])): cats.add(4)
    if f(5,' | '.join([subj,priv,ext,pub,info])): cats.add(5)
    if f(6,' | '.join([subj,priv,pub,info,obj])): cats.add(6)
    if f(7,' | '.join([subj,pub,priv,ext,info])): cats.add(7)
    tx=' | '.join([subj,info,obj,loc])
    tem=set(k for k,r in T.items() if re.search(r,tx,re.I))
    return sorted(cats),sorted(tem)


UFS='AC AL AP AM BA CE DF ES GO MA MT MS MG PA PB PR PE PI RJ RN RS RO RR SC SP SE TO'.split()
CAPITAIS={'rio branco':'AC','maceio':'AL','macapa':'AP','manaus':'AM','salvador':'BA','fortaleza':'CE','brasilia':'DF','vitoria':'ES','goiania':'GO','sao luis':'MA','cuiaba':'MT','campo grande':'MS','belo horizonte':'MG','belem':'PA','joao pessoa':'PB','curitiba':'PR','recife':'PE','teresina':'PI','rio de janeiro':'RJ','natal':'RN','porto alegre':'RS','porto velho':'RO','boa vista':'RR','florianopolis':'SC','sao paulo':'SP','aracaju':'SE','palmas':'TO'}
OUTRAS={'campinas':'SP','gramado':'RS','petrolina':'PE','juazeiro':'BA','campina grande':'PB','foz do iguacu':'PR','canela':'RS','londrina':'PR','santos':'SP','niteroi':'RJ','uberlandia':'MG','ribeirao preto':'SP','sao jose dos campos':'SP','joinville':'SC','blumenau':'SC','caxias do sul':'RS','maraba':'PA','santarem':'PA','timon':'MA','imperatriz':'MA'}
NOMES={}  # nome sem acento -> nome com acento (preenchido pelo uso: viagens e lista abaixo)
for n in ('Rio Branco','Maceió','Macapá','Manaus','Salvador','Fortaleza','Brasília','Vitória','Goiânia','São Luís','Cuiabá','Campo Grande','Belo Horizonte','Belém','João Pessoa','Curitiba','Recife','Teresina','Rio de Janeiro','Natal','Porto Alegre','Porto Velho','Boa Vista','Florianópolis','São Paulo','Aracaju','Palmas','Campinas','Gramado','Petrolina','Juazeiro','Campina Grande','Foz do Iguaçu','Canela','Londrina','Santos','Niterói','Uberlândia','Ribeirão Preto','São José dos Campos','Joinville','Blumenau','Caxias do Sul','Marabá','Santarém','Timon','Imperatriz'):
    NOMES[N(n).lower()]=n
DF_FORTE=(r"minist[eé]rio|mist[eé]rio|esplanada|bras[ií]lia|planalto|\bDF\b|anatel|ag[eê]ncia nacional|senado|c[aâ]mara dos|congresso nacional|pal[aá]cio|distrito federal|"
          r"\bTCU\b|\bCGU\b|\bSTF\b|itamaraty|\bEBC\b|telebras|\bSCS\b|\bSAUS\b|\bSHIS\b|\bSGAN\b|\bSBN\b|\bSBS\b|\bSEPN\b|\bSAIN\b|\bCLN\b|\bCLS\b|\bW3\b|asa (sul|norte)|\bGM\b|"
          r"gabinete|\bMCom\b|\bMCOM\b|\bUnB\b|Finatec|Royal Tulip|\bCICB\b|Centro Internacional de Convenções|Ulysses Guimar|Lago (Sul|Norte)|Setor de Clubes|\bMME\b|\bMGI\b|Kubitschek|Complexo Brasil 21|Casa Civil")
ESTADOS={'acre':'AC','alagoas':'AL','amapa':'AP','amazonas':'AM','bahia':'BA','ceara':'CE','espirito santo':'ES','goias':'GO','maranhao':'MA','mato grosso do sul':'MS','mato grosso':'MT','minas gerais':'MG','para':'PA','paraiba':'PB','parana':'PR','pernambuco':'PE','piaui':'PI','rio de janeiro':'RJ','rio grande do norte':'RN','rio grande do sul':'RS','rondonia':'RO','roraima':'RR','santa catarina':'SC','sao paulo':'SP','sergipe':'SE','tocantins':'TO'}
def cidade_estado_extenso(txt):
    """'Parintins - Amazonas' / 'Sobral, Ceará' -> ('AM','Parintins'); só vale com separador antes do nome do estado"""
    t=N(txt or '')
    for nome in sorted(ESTADOS,key=len,reverse=True):
        m=re.search(r"([A-Z][\w'.]+(?: (?:de|da|do|dos|das|e|[A-Z][\w'.]+))*)\s*(?:/|-|,)\s*"+re.escape(nome)+r"\b",t,re.I)
        if m and ESTADOS[nome]!='DF': return ESTADOS[nome],m.group(1).strip()
    return None
def cidade_uf(txt):
    """acha 'Cidade/UF' ou 'Cidade - UF' no texto"""
    m=re.search(r"([A-ZÁÉÍÓÚÂÊÔÃÕÇ][\wÁÉÍÓÚÂÊÔÃÕÇáéíóúâêôãõç'.]+(?: (?:de|da|do|dos|das|e|[A-ZÁÉÍÓÚÂÊÔÃÕÇ][\wáéíóúâêôãõç'.]+))*)\s*(?:/|-|–|,)\s*(%s)\b"%'|'.join(UFS),txt or '')
    if m: return m.group(2),m.group(1).strip()
    return None
def achar_cidade(txt):
    t=' '+re.sub(r'[^a-z0-9 ]',' ',N(txt).lower())+' '
    for nome in sorted(list(CAPITAIS)+list(OUTRAS),key=len,reverse=True):
        if ' '+nome+' ' in t:
            uf=CAPITAIS.get(nome) or OUTRAS[nome]; return uf,NOMES.get(nome,nome.title())
    return None
def decidir_lugar_setel(reg,vgs):
    """reg: dict(local, assunto, virtual, iso). vgs: viagens [ini,fim,..,lugares[]] (campo 8). Retorna (lugar, pendencia_bool)"""
    if reg['virtual']: return 'VI:Virtual',False
    loc=reg.get('local') or ''
    trip=[v for v in vgs if v[0]<=reg['iso']<=v[1]]
    lugares=[l for v in trip for l in v[8]]
    ex=[l for l in lugares if l.startswith('EX:')]
    br_local=bool(cidade_uf(loc)) and cidade_uf(loc)[0] in UFS or bool(achar_cidade(loc))
    if ex and not re.search(DF_FORTE,loc,re.I) and not br_local:
        t=N(loc+' '+reg.get('assunto','')).lower()
        for l in ex:
            cid=re.sub(r'^EX:|\s*\(.*\)$','',l)
            if N(cid).lower() in t: return l,False
        return ex[0],False
    if re.search(DF_FORTE,loc,re.I): return 'DF:Brasília',False
    uf_trip=[l for l in lugares if not l.startswith('EX:') and not l.startswith('DF:')]
    cu=cidade_uf(loc) or cidade_uf(reg.get('assunto',''))
    if cu and cu[0] in UFS and cu[0]!='DF': 
        return f'{cu[0]}:{NOMES.get(N(cu[1]).lower(),cu[1])}',False
    ce=cidade_estado_extenso(loc) or cidade_estado_extenso(reg.get('assunto',''))
    if ce: return f'{ce[0]}:{ce[1]}',False
    c=achar_cidade(loc) or achar_cidade(reg.get('assunto',''))
    if c and c[0]!='DF': return f'{c[0]}:{c[1]}',False
    exl=achar_exterior(loc)
    if exl: return exl,False
    if len(set(uf_trip))==1: return uf_trip[0],False
    if uf_trip:
        return uf_trip[0],False
    return 'DF:Brasília',True

# ---------------------------------------------------------------------------------------------
# Países do mapa-múndi do painel: (código ISO3, nome, outros nomes aceitos, x, y)
#   - os 173 países com polígono no mapa usam um ponto DENTRO do próprio país (capital ou ponto interno);
#   - ilhas e cidades-estado sem polígono (Cingapura, Hong Kong, Cabo Verde, Malta...) só têm o ponto.
# O nome vem do Portal como "Cidade/País"; a comparação ignora acento, maiúscula e pontuação.
# Se aparecer um país que não está aqui, ele vai para 'pendencias_de_pais' no JSON: basta incluir uma linha.
# ---------------------------------------------------------------------------------------------
PAISES=[
 ("FJI","Fiji",[],994.5,337.0),
 ("TZA","Tanzânia",["republica unida da tanzania"],596.5,298.8),
 ("ESH","Saara Ocidental",[],466.2,197.7),
 ("CAN","Canadá",[],289.7,127.8),
 ("USA","Estados Unidos",["estados unidos da america", "eua", "usa"],286.1,149.3),
 ("KAZ","Cazaquistão",[],698.5,108.6),
 ("UZB","Uzbequistão",[],675.4,139.8),
 ("PNG","Papua-Nova Guiné",["papua nova guine"],900.7,299.9),
 ("IDN","Indonésia",[],796.9,298.3),
 ("ARG","Argentina",[],319.1,394.6),
 ("CHL","Chile",[],303.6,388.2),
 ("COD","República Democrática do Congo",["congo kinshasa", "rd congo", "republica democratica do congo"],565.5,287.4),
 ("SOM","Somália",[],626.9,262.4),
 ("KEN","Quênia",["kenia"],602.4,282.1),
 ("SDN","Sudão",[],583.0,225.1),
 ("TCD","Chade",[],551.7,227.3),
 ("HTI","Haiti",["haiti"],299.2,216.7),
 ("DOM","República Dominicana",["dominicana"],305.8,216.7),
 ("RUS","Rússia",["russia"],604.6,93.6),
 ("BHS","Bahamas",[],283.4,196.7),
 ("FLK","Ilhas Malvinas",["ilhas falkland", "malvinas"],334.7,449.1),
 ("NOR","Noruega",[],530.0,79.9),
 ("GRL","Groenlândia",[],384.9,30.6),
 ("ATF","Terras Austrais Francesas",[],693.3,441.2),
 ("TLS","Timor-Leste",["timor leste"],849.7,307.1),
 ("ZAF","África do Sul",[],578.5,362.7),
 ("LSO","Lesoto",[],578.2,376.1),
 ("MEX","México",[],224.7,213.7),
 ("URY","Uruguai",[],343.9,393.1),
 ("BRA","Brasil",[],352.6,313.8),
 ("BOL","Bolívia",[],310.9,332.3),
 ("PER","Peru",[],286.1,317.4),
 ("COL","Colômbia",[],294.2,262.3),
 ("PAN","Panamá",[],279.2,248.1),
 ("CRI","Costa Rica",[],266.4,245.1),
 ("NIC","Nicarágua",[],260.3,237.8),
 ("HND","Honduras",[],257.8,231.2),
 ("SLV","El Salvador",[],252.2,232.5),
 ("GTM","Guatemala",[],248.6,229.6),
 ("BLZ","Belize",[],253.6,221.1),
 ("VEN","Venezuela",[],314.2,243.1),
 ("GUY","Guiana",["guiana guiana inglesa", "guiana inglesa"],338.4,255.3),
 ("SUR","Suriname",[],344.7,264.4),
 ("FRA","França",[],506.6,116.2),
 ("ECU","Equador",[],281.9,278.5),
 ("PRI","Porto Rico",[],314.9,217.7),
 ("JAM","Jamaica",[],286.7,218.3),
 ("CUB","Cuba",[],281.5,206.5),
 ("ZWE","Zimbábue",["zimbabue"],582.8,340.6),
 ("BWA","Botsuana",["botswana"],566.1,351.1),
 ("NAM","Namíbia",[],547.7,351.2),
 ("SEN","Senegal",[],451.6,229.2),
 ("MLI","Mali",[],490.2,221.0),
 ("MRT","Mauritânia",[],471.3,211.2),
 ("BEN","Benin",["benim"],506.5,245.9),
 ("NER","Níger",[],526.0,220.7),
 ("NGA","Nigéria",[],520.9,247.7),
 ("CMR","Camarões",[],535.0,259.3),
 ("TGO","Togo",["republica togolesa"],502.9,250.4),
 ("GHA","Gana",[],499.5,259.3),
 ("CIV","Costa do Marfim",[],484.4,253.1),
 ("GIN","Guiné",[],469.3,243.6),
 ("GNB","Guiné-Bissau",["guine bissau"],458.1,238.5),
 ("LBR","Libéria",[],473.9,256.8),
 ("SLE","Serra Leoa",[],467.2,249.9),
 ("BFA","Burkina Faso",["burkina fasso"],495.0,237.3),
 ("CAF","República Centro-Africana",[],556.6,256.3),
 ("COG","Congo",["republica do congo"],542.1,281.0),
 ("GAB","Gabão",[],532.5,280.0),
 ("GNQ","Guiné Equatorial",[],528.9,272.6),
 ("ZMB","Zâmbia",[],577.0,322.4),
 ("MWI","Malaui",["malawi"],595.0,321.7),
 ("MOZ","Moçambique",[],598.6,334.8),
 ("SWZ","Essuatíni",["eswatini", "suazilandia"],587.1,365.6),
 ("AGO","Angola",[],536.8,306.9),
 ("BDI","Burundi",[],582.9,289.0),
 ("ISR","Israel",[],597.1,173.9),
 ("LBN","Líbano",[],599.8,165.8),
 ("MDG","Madagascar",[],629.6,342.4),
 ("PSE","Palestina",["estado da palestina"],597.9,172.4),
 ("GMB","Gâmbia",[],456.8,233.3),
 ("TUN","Tunísia",[],526.4,165.0),
 ("DZA","Argélia",[],507.3,184.8),
 ("JOR","Jordânia",[],599.9,172.2),
 ("ARE","Emirados Árabes Unidos",["emirados arabes"],653.8,194.5),
 ("QAT","Catar",["qatar"],643.2,194.2),
 ("KWT","Kuwait",["cuaite"],632.2,180.9),
 ("IRQ","Iraque",[],621.5,168.6),
 ("OMN","Omã",[],655.8,209.9),
 ("VUT","Vanuatu",[],963.6,328.3),
 ("KHM","Camboja",[],791.5,235.9),
 ("THA","Tailândia",[],779.4,232.4),
 ("LAO","Laos",[],788.3,217.0),
 ("MMR","Mianmar",["myanmar"],768.1,208.3),
 ("VNM","Vietnã",["viet nam", "vietna"],794.3,208.4),
 ("PRK","Coreia do Norte",[],853.1,145.1),
 ("KOR","Coreia do Sul",["coreia", "republica da coreia"],853.0,153.6),
 ("MNG","Mongólia",[],785.8,123.0),
 ("IND","Índia",[],714.6,183.3),
 ("BGD","Bangladesh",[],750.7,199.2),
 ("BTN","Butão",[],751.4,187.5),
 ("NPL","Nepal",[],733.4,184.6),
 ("PAK","Paquistão",[],692.7,178.9),
 ("AFG","Afeganistão",[],683.5,165.8),
 ("TJK","Tadjiquistão",["tajiquistao"],697.3,150.3),
 ("KGZ","Quirguistão",["quirguizistao"],707.3,140.7),
 ("TKM","Turcomenistão",[],664.8,148.6),
 ("IRN","Irã",["ira"],650.7,170.4),
 ("SYR","Síria",[],606.8,162.3),
 ("ARM","Armênia",[],624.9,144.8),
 ("SWE","Suécia",[],546.1,70.1),
 ("BLR","Belarus",["bielorrussia"],577.6,100.9),
 ("UKR","Ucrânia",[],584.9,111.1),
 ("POL","Polônia",[],558.5,105.3),
 ("AUT","Áustria",[],545.7,118.5),
 ("HUN","Hungria",[],552.9,120.9),
 ("MDA","Moldávia",["moldova"],578.7,121.5),
 ("ROU","Romênia",[],572.6,131.1),
 ("LTU","Lituânia",[],566.4,95.1),
 ("LVA","Letônia",[],568.9,90.0),
 ("EST","Estônia",[],571.8,83.8),
 ("DEU","Alemanha",[],537.3,104.3),
 ("BGR","Bulgária",[],570.3,136.5),
 ("GRC","Grécia",[],566.0,152.2),
 ("TUR","Turquia",[],591.5,146.0),
 ("ALB","Albânia",[],555.6,141.8),
 ("HRV","Croácia",[],544.6,126.5),
 ("CHE","Suíça",[],522.7,123.0),
 ("LUX","Luxemburgo",[],516.4,113.5),
 ("BEL","Bélgica",[],512.2,109.8),
 ("NLD","Países Baixos",["holanda"],513.7,104.7),
 ("PRT","Portugal",[],474.8,149.9),
 ("ESP","Espanha",[],506.2,141.0),
 ("IRL","Irlanda",[],482.6,101.7),
 ("NCL","Nova Caledônia",[],960.4,349.2),
 ("SLB","Ilhas Salomão",[],945.0,309.8),
 ("NZL","Nova Zelândia",[],985.9,414.3),
 ("AUS","Austrália",[],914.4,394.4),
 ("LKA","Sri Lanka",[],724.1,252.7),
 ("CHN","China",[],823.6,146.0),
 ("TWN","Taiwan",[],836.2,199.4),
 ("ITA","Itália",[],534.8,139.4),
 ("DNK","Dinamarca",[],535.1,93.8),
 ("GBR","Reino Unido",["inglaterra", "reino unido da gra-bretanha"],499.8,107.6),
 ("ISL","Islândia",[],447.9,62.6),
 ("AZE","Azerbaijão",["azerbaidjao"],638.8,144.3),
 ("GEO","Geórgia",[],620.9,138.6),
 ("PHL","Filipinas",[],836.4,229.6),
 ("MYS","Malásia",[],782.7,267.6),
 ("BRN","Brunei",[],819.2,262.7),
 ("SVN","Eslovênia",[],541.4,125.3),
 ("FIN","Finlândia",[],569.3,78.9),
 ("SVK","Eslováquia",["republica eslovaca"],554.3,116.7),
 ("CZE","República Tcheca",["republica checa", "tchequia"],540.1,112.3),
 ("ERI","Eritreia",["eritrea"],607.4,226.9),
 ("JPN","Japão",[],888.3,159.8),
 ("PRY","Paraguai",[],340.0,361.4),
 ("YEM","Iêmen",["iemen"],631.9,225.3),
 ("SAU","Arábia Saudita",[],629.9,196.2),
 ("CYP","Chipre",[],592.0,162.4),
 ("MAR","Marrocos",[],481.2,165.5),
 ("EGY","Egito",[],586.8,178.7),
 ("LBY","Líbia",[],549.9,188.7),
 ("ETH","Etiópia",[],607.8,248.1),
 ("DJI","Djibuti",[],618.0,239.1),
 ("UGA","Uganda",[],589.9,273.8),
 ("RWA","Ruanda",[],582.9,284.8),
 ("BIH","Bósnia e Herzegovina",["bosnia herzegovina", "bosnia-herzegovina"],549.5,131.8),
 ("MKD","Macedônia do Norte",["macedonia"],560.4,140.3),
 ("SRB","Sérvia",[],557.1,129.8),
 ("MNE","Montenegro",[],553.6,136.6),
 ("TTO","Trinidad e Tobago",[],329.2,242.4),
 ("SSD","Sudão do Sul",[],583.9,253.9),
 ("SGP","Cingapura",["singapura"],788.6,273.3),
 ("HKG","Hong Kong",[],817.5,204.1),
 ("MAC","Macau",[],815.5,204.5),
 ("CPV","Cabo Verde",[],434.8,228.6),
 ("STP","São Tomé e Príncipe",[],518.7,276.8),
 ("MLT","Malta",[],540.4,159.2),
 ("BRB","Barbados",[],334.5,234.5),
 ("MUS","Maurício",["mauricio"],659.9,344.5),
 ("GRD","Granada",[],328.6,237.8),
 ("KNA","São Cristóvão e Névis",["sao cristovao e nevis"],325.9,220.6),
 ("TUV","Tuvalu",[],998.1,305.9),
 ("MCO","Mônaco",[],520.7,133.4),
 ("SMR","San Marino",[],534.6,132.8),
 ("MDV","Maldivas",[],704.4,263.9),
 ("BHR","Bahrein",["bareine"],640.7,191.2),
 ("VAT","Vaticano",["santa se"],534.7,139.4),
 ("LIE","Liechtenstein",[],526.5,122.2),
 ("AND","Andorra",[],504.3,137.4),
 ("SYC","Seychelles",[],654.3,293.0),
 ("COM","Comores",[],620.4,316.5),
 ("WSM","Samoa",[],22.7,323.4),
 ("TON","Tonga",[],13.2,347.5),
 ("KIR","Kiribati",[],980.9,273.2),
 ("DMA","Dominica",[],329.5,227.2),
 ("LCA","Santa Lúcia",[],330.6,231.5),
 ("VCT","São Vicente e Granadinas",[],330.0,234.2),
 ("ATG","Antígua e Barbuda",[],328.4,221.3),
 ("ATA","Antártica",["antartida"],337.8,462.0),
 ("KOS","Kosovo",[],559.0,136.7),
 ("GUF","Guiana Francesa",[],354.8,261.6),
]
def _nk(s):
    return re.sub(r"\s+"," ",re.sub(r"[^a-z0-9 ]"," ",N(s).lower())).strip()
_IDX={}
for _i,_n,_al,_x,_y in PAISES:
    for _k in [_n]+list(_al): _IDX[_nk(_k)]=(_i,_n,_x,_y)
IGNORAR_PAIS={"informacoes protegidas por sigilo","sem informacao","su a"}
def pais_ignorar(nome):
    """destinos que não são país (sigilo, sem informação)"""
    return _nk(nome) in IGNORAR_PAIS or not _nk(nome)
def pais_info(nome):
    """nome do país como vem do Portal -> (iso3, nome, x, y) ou None. Só aceita nome exato (sem adivinhar)."""
    k=_nk(nome)
    if k in _IDX:
        i,n,x,y=_IDX[k]; return i,n,x,y
    return None

CIDADES_EX={'washington':'USA','nova york':'USA','new york':'USA','las vegas':'USA','san francisco':'USA','miami':'USA','orlando':'USA','houston':'USA',
 'barcelona':'ESP','madri':'ESP','madrid':'ESP','lisboa':'PRT','paris':'FRA','londres':'GBR','london':'GBR','genebra':'CHE','geneva':'CHE','bruxelas':'BEL',
 'berlim':'DEU','roma':'ITA','toquio':'JPN','tokyo':'JPN','pequim':'CHN','beijing':'CHN','xangai':'CHN','shanghai':'CHN','shenzhen':'CHN','seul':'KOR',
 'dubai':'ARE','doha':'QAT','riade':'SAU','cidade do mexico':'MEX','buenos aires':'ARG','santiago':'CHL','bogota':'COL','montevideu':'URY','assuncao':'PRY',
 'quito':'ECU','antalya':'TUR','istambul':'TUR','amsterda':'NLD','amsterdam':'NLD','luxemburgo':'LUX','viena':'AUT'}
def achar_exterior(loc):
    """local que é, por inteiro, um país ou uma cidade estrangeira conhecida (ex.: 'TURQUIA', 'Washington, D.C.') -> 'EX:...' ou None"""
    t=re.sub(r'[^a-z0-9 ]',' ',N(loc).lower()); t=re.sub(r'\s+',' ',t).strip()
    if not t: return None
    iso_nome={i:n for i,n,_,_,_ in PAISES}
    if t in _IDX:
        return 'EX:'+_IDX[t][1]
    for cid,iso in CIDADES_EX.items():
        if t==cid or t.startswith(cid+' '):
            nome=iso_nome.get(iso)
            if not nome: continue
            nome_cid=cid.title() if cid!=N(nome).lower() else nome
            return 'EX:'+nome if cid==N(nome).lower() else f'EX:{nome_cid} ({nome})'
    return None
