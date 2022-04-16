import random , os ,requests
import json
import socket
import urllib.parse



from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
 
# print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
# print("date and time =", dt_string)


hostname_os=socket.getfqdn()
vversion="RENEW SQL TIME :"



def alias_send_msg(text):
	pol=emoji.emojize(""':man_genie:')
	mp=emoji.emojize(dt_string+" \n"'  :dizzy:'+"[ "+hostname_os +" ] "':dizzy:'+" \n"''+"  [ "+vversion+" ] "'')
	# msg_telegram=mp+" \n"+text+" ] \n "+pol+" [ "+""+" ] \n "+pol+"[ "+dt_string+" ] "
	msg_telegram=" [ "+hostname_os+" ]  "+"[ "+dt_string+" ] "
	# token = "2137513961:AAGENlwIUQnfvbKZX64-fZ72R_oStto8oFo"
	#-609247805
	# token=get_tokens()
	# token="5086890807:AAEEM2OhQaR9mB7KUZvwkE60mHvoSY4BhOQ"
	# token="5035848854:AAG9a-7bHDYTOXiNEdjXRsnM-gbkdw9TCfE"
	token="5351653833:AAEUeIwPT187sCG5vb33t_2JGHBlcLT-kNU"
	chat_id = "-723950994"
	# chat_id = "-1001616252735"
	url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + msg_telegram
	# url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + msg_telegram 

	results = requests.get(url_req)
	# print(results.json())

alias_send_msg(""+dt_string)