import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import time
import urllib3

# You can leave this bit out if you're using a paid PythonAnywhere account
proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))
# end of the stuff that's only needed for free accounts

bot = telepot.Bot('####')
# geolocation request keyboard
kb_geo_req = ReplyKeyboardMarkup(
		keyboard=[
				[KeyboardButton(text="Отправить локацию", request_location=True)]
		],
		resize_keyboard=True,
		one_time_keyboard=True
)

kb_remove = ReplyKeyboardRemove()

def handle(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
#	print(msg)
# cheking for new user
	with open('users.txt', 'r') as f:
		new_user = True
		for line in f:
			if int(line.split('\t')[0]) == chat_id:
				new_user = False
# request geolocation
	if content_type == 'text' and new_user:
		bot.sendMessage(
				308032530,
				'Чтобы отобразить пролеты, мне необходимо знать вашу геолокацию',
				reply_markup=kb_geo_req
		)
# adding new user
	if content_type == 'location' and new_user:
		with open('users.txt', 'a') as f:
			f.write(str(msg['chat']['id'])+'\t'+msg['chat']['first_name']+'\t'+str(msg['location']['latitude'])+'\t'+str(msg['location']['longitude'])+'\n')

bot.message_loop(handle)

print ('Listening ...')

#Keep the program running.
while 1:
time.sleep(10)
