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
    c=achar_cidade(loc) or achar_cidade(reg.get('assunto',''))
    if c and c[0]!='DF': return f'{c[0]}:{c[1]}',False
    exl=achar_exterior(loc)
    if exl: return exl,False
    if len(set(uf_trip))==1: return uf_trip[0],False
    if uf_trip:
        return uf_trip[0],False
    return 'DF:Brasília',True

# ---------------------------------------------------------------------------------------------
# Países (mapa-múndi do painel): código ISO3 -> nome, aliases (sem acento, minúsculas), latitude, longitude
# A posição no mapa é linear: x = 500.1 + 2.779*lon ; y = 277.8 - 3.304*lat
# ---------------------------------------------------------------------------------------------
PAISES=[
 ("ARG","Argentina",[],-34.6,-58.4),("BOL","Bolívia",[],-16.5,-68.1),("CHL","Chile",[],-33.4,-70.7),("COL","Colômbia",[],4.7,-74.1),
 ("ECU","Equador",[],-0.2,-78.5),("PRY","Paraguai",[],-25.3,-57.6),("PER","Peru",[],-12.0,-77.0),("URY","Uruguai",[],-34.9,-56.2),
 ("VEN","Venezuela",[],10.5,-66.9),("GUY","Guiana",[],6.8,-58.2),("SUR","Suriname",[],5.9,-55.2),("PAN","Panamá",[],9.0,-79.5),
 ("CRI","Costa Rica",[],9.9,-84.1),("CUB","Cuba",[],23.1,-82.4),("DOM","República Dominicana",["dominicana"],18.5,-69.9),
 ("MEX","México",[],19.4,-99.1),("GTM","Guatemala",[],14.6,-90.5),("HND","Honduras",[],14.1,-87.2),("SLV","El Salvador",[],13.7,-89.2),
 ("NIC","Nicarágua",[],12.1,-86.3),("HTI","Haiti",["haiti"],18.5,-72.3),("JAM","Jamaica",[],18.0,-76.8),("TTO","Trinidad e Tobago",[],10.7,-61.5),
 ("USA","Estados Unidos",["estados unidos da america","eua","usa"],38.9,-77.0),("CAN","Canadá",[],45.4,-75.7),
 ("PRT","Portugal",[],38.7,-9.1),("ESP","Espanha",[],41.4,2.2),("FRA","França",[],48.9,2.35),("DEU","Alemanha",[],52.5,13.4),
 ("ITA","Itália",[],41.9,12.5),("GBR","Reino Unido",["inglaterra","reino unido da gra-bretanha"],51.5,-0.1),("IRL","Irlanda",[],53.3,-6.3),
 ("NLD","Países Baixos",["holanda"],52.4,4.9),("BEL","Bélgica",[],50.85,4.35),("LUX","Luxemburgo",[],49.6,6.1),("CHE","Suíça",[],46.2,6.1),
 ("AUT","Áustria",[],48.2,16.4),("SWE","Suécia",[],59.3,18.1),("NOR","Noruega",[],59.9,10.75),("FIN","Finlândia",[],60.2,24.9),
 ("DNK","Dinamarca",[],55.7,12.6),("POL","Polônia",[],52.2,21.0),("CZE","República Tcheca",["tchequia","republica checa"],50.1,14.4),
 ("HUN","Hungria",[],47.5,19.0),("ROU","Romênia",[],44.4,26.1),("GRC","Grécia",[],38.0,23.7),("TUR","Turquia",[],39.9,32.9),
 ("UKR","Ucrânia",[],50.45,30.5),("RUS","Rússia",["russia"],55.75,37.6),("HRV","Croácia",[],45.8,16.0),("SRB","Sérvia",[],44.8,20.5),
 ("AZE","Azerbaijão",[],40.4,49.9),("CHN","China",[],39.9,116.4),("JPN","Japão",[],35.7,139.7),("KOR","Coreia do Sul",["coreia","republica da coreia"],37.6,127.0),
 ("IND","Índia",[],28.6,77.2),("THA","Tailândia",[],13.75,100.5),("VNM","Vietnã",["vietna","viet nam"],21.0,105.85),("IDN","Indonésia",[],-6.2,106.8),
 ("MYS","Malásia",[],3.1,101.7),("PHL","Filipinas",[],14.6,121.0),("ARE","Emirados Árabes Unidos",["emirados arabes"],25.2,55.3),
 ("QAT","Catar",["qatar"],25.3,51.5),("SAU","Arábia Saudita",[],24.7,46.7),("ISR","Israel",[],31.8,35.2),("JOR","Jordânia",[],31.95,35.9),
 ("KAZ","Cazaquistão",[],51.2,71.4),("MAR","Marrocos",[],34.0,-6.8),("EGY","Egito",[],30.0,31.2),("ZAF","África do Sul",[],-25.7,28.2),
 ("AGO","Angola",[],-8.8,13.2),("MOZ","Moçambique",[],-25.95,32.6),("NGA","Nigéria",[],9.1,7.5),("KEN","Quênia",["kenia"],-1.3,36.8),
 ("ETH","Etiópia",[],9.0,38.75),("GHA","Gana",[],5.6,-0.2),("SEN","Senegal",[],14.7,-17.45),("TUN","Tunísia",[],36.8,10.2),
 ("DZA","Argélia",[],36.75,3.05),("AUS","Austrália",[],-35.3,149.1),("NZL","Nova Zelândia",[],-41.3,174.8),("TLS","Timor-Leste",["timor leste"],-8.55,125.6),
]
def _nk(s):
    return re.sub(r"[^a-z0-9 ]"," ",N(s).lower()).strip()
_IDX={}
for _i,_n,_al,_la,_lo in PAISES:
    for _k in [_n]+_al: _IDX[_nk(_k)]=(_i,_n,_la,_lo)
def pais_info(nome):
    """nome do país como vem do Portal -> (iso3, nome, x, y) ou None"""
    k=_nk(nome)
    if k in _IDX:
        i,n,la,lo=_IDX[k]; return i,n,round(500.1+2.779*lo,1),round(277.8-3.304*la,1)
    for kk,(i,n,la,lo) in _IDX.items():
        if len(kk)>4 and (kk in k or k in kk): return i,n,round(500.1+2.779*lo,1),round(277.8-3.304*la,1)
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
