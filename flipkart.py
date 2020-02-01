import requests,pprint,time,random
from bs4 import BeautifulSoup 
for i in range(12):
	a=requests.get('https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy%2C4io&otracker=nmenu_sub_Electronics_0_Mi&page='+str(i+1))
	time.sleep(random.randint(1,4))

	# print(i)
	b=BeautifulSoup(a.text,'html.parser')
	phone=b.find('div',class_='bhgxx2 col-12-12')
	if phone!=None:
		phone=phone.find_next('div',class_='bhgxx2 col-12-12')
	details={'name':'','ram':'','rom':'','price':''}
	for j in range(24):
		if phone!=None:
			phone=phone.find_next('div',class_='bhgxx2 col-12-12')
			if phone!=None:
				phone_name=phone.find('div',class_='_3wU53n')
				if phone_name != None:
					details['name']=phone_name.text
				phone_ram=phone.find('li',class_='tVe95H')	
				if phone_ram != None:
					details['ram'] =(phone_ram.get_text()[0:8])
					details['rom'] =phone_ram.get_text().rstrip()[11:21]	
				phone_price = phone.find('div',class_='_1vC4OE _2rQ-NK')
				if phone_price != None:
					details['price'] =(phone_price.text)
				pprint.pprint (details)
	