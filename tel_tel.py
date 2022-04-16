import random , os ,requests
import json
import socket
import urllib.parse
from datetime import datetime
import mysql.connector



l05_00="/root/hassed/read.me"
# datetime object containing current date and time
now = datetime.now()
 
# print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
# print("date and time =", dt_string)


hostname_os=socket.getfqdn()
vversion="RENEW SQL TIME"

#############################################################################################
def read_current_l0g():
	final_msg=''
	with open(l05_00,'r') as file:
		lines = file.readlines()
		for i in lines:
			final_msg=final_msg + i
		print(final_msg)
	return final_msg
#######################



#################################################################################################






def alias_send_msg(text):
	# pol=emoji.emojize(""':man_genie:')
	hoost=read_current_l0g()
	count_used=str(counting_used_config_config())
	# mp=emoji.emojize(dt_string+" \n"'  :dizzy:'+"[ "+hostname_os +" ] "':dizzy:'+" \n"''+"  [ "+vversion+" ] "'')
	# msg_telegram=mp+" \n"+text+" ] \n "+pol+" [ "+""+" ] \n "+pol+"[ "+dt_string+" ] "
	msg_telegram="  [ "+hoost+" ]  [ "+count_used+" ] \n [ "+vversion+ " ] ["+dt_string+" ] "
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


###############################################################################################

# def set_table(typ0):
# 	# vpn_type=cnf_bvb.vpn_type
# 	if "N" in typ0:
# 		print("NORD VPN")
# 		tab_list_1='nord_list2'
# 		# vpn_folder=pwd+"/N0RD/WORKING_CONFIG/"
# 		# typ0="N"
# #       ######################################################          
# 	elif "C" in typ0:
# 		print(" NAME_CHEAP")
# 		tab_list_1='name_cheap'
# 		# vpn_folder=pwd+"/CHEAP_VPN/"
# 		# typ0="C"
# 	return tab_list_1


def counting_used_config_config():
	this_table='nord_list2'
	# set_table(typ0)
	mydb = mysql.connector.connect(host="remotemysql.com",user="f6V3kVwxvH",passwd="sOVnW1130i",database="f6V3kVwxvH")
	# print(" counting_used_config_config  : ",end='',flush=True)
	mycursor = mydb.cursor()
	sql = "SELECT * FROM `"+this_table+"`  WHERE `used` LIKE 'y'"
	mycursor.execute(sql)
	record = mycursor.fetchall()
	count=mycursor.rowcount
	# print(str(count))
	# for row in record:
	# 	fresh_config=str(row[1])
	return count

#################################################################################################











counting_used_config_config()

alias_send_msg(dt_string)