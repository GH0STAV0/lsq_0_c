import random , os ,requests
import json
import socket
import urllib.parse
from datetime import datetime
import mysql.connector



# HOST="zzroiqlkjzv2.eu-west-2.psdb.cloud"
# USERNAME="c4cz3k2azim8"
# PASSWORD="pscale_pw_SZsOhzZm6AVnde53meT3ygRRh7zSjXdZ4dawwURylQo"
# DATABASE="plan"

HOST="remotemysql.com"
USERNAME="f6V3kVwxvH"
PASSWORD="sOVnW1130i"
DATABASE="f6V3kVwxvH"


vversion="RENEW SQL TIME V_FINAL "


l05_00="/root/hassed/read.me"
# datetime object containing current date and time
now = datetime.now()
 
# print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
# print("date and time =", dt_string)


hostname_os=socket.getfqdn()

#############################################################################################
def read_current_l0g():
	final_msg=''
	with open(l05_00,'r') as file:
		lines = file.readlines()
		for i in lines:
			final_msg=final_msg + i
		final_msg=final_msg.replace("\n", "")
		# print(final_msg)
	return final_msg
#######################
# lommmmp="re"


# print(lommmmp)

#################################################################################################






def alias_send_msg(text):

	count_used=str(counting_used_config_config())
	global lommmmp
	lommmmp="jhj"
	# pol=emoji.emojize(""':man_genie:')
	# print(lommmmp)
	hoost=read_current_l0g()
	lommmmp=count_used
	# print(lommmmp)
	###################################################
	

	# mp=emoji.emojize(dt_string+" \n"'  :dizzy:'+"[ "+hostname_os +" ] "':dizzy:'+" \n"''+"  [ "+vversion+" ] "'')
	# msg_telegram=mp+" \n"+text+" ] \n "+pol+" [ "+""+" ] \n "+pol+"[ "+dt_string+" ] "
	msg_telegram="    [ "+hoost+" ]                [ "+count_used+" ] \n[ "+vversion+ " ]   [ "+dt_string+" ] "
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
	check_tolerance(count_used)
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
	print(" [  VPN USED  ] ..... ", end='',flush=True)

	this_table='vanish_tb'
	# set_table(typ0)
	mydb = mysql.connector.connect(host=HOST,user=USERNAME,passwd=PASSWORD,database=DATABASE)
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


def check_tolerance(count_used):

	
	# count_used=str(counting_used_config_config())
	# print(" [  VPN USED  ]",type(count_used))
	int_count=int(count_used)
	# print(" [  VPN USED  ]",type(int_count))
	
	if int_count >= 3780 :
		print(int_count)
		# print(" Reset ")
		
		restored_fresh_sql_table()
	else :
		print(int_count)




def drop_sql_table():
	print(" Reset  OF TABLE USED  : ",end='',flush=True)
	mydb = mysql.connector.connect(host=HOST,user=USERNAME,passwd=PASSWORD,database=DATABASE)
	mycursor = mydb.cursor()
	sql = "UPDATE `nord_list2` SET  `used` = 'n';"
	mycursor.execute(sql)
	print("[ SUCCED ] ")


def restored_fresh_sql_table():

	print(" Drop_sql_table  OF  : ",end='',flush=True)
	mydb = mysql.connector.connect(host=HOST,user=USERNAME,passwd=PASSWORD,database=DATABASE)
	mycursor = mydb.cursor()
	sql = "UPDATE `nord_list2` SET    `used` = 'n'"
	mycursor.execute(sql)
	mydb.commit()
	print("[ SUCCED ] ")
	# UPDATE `nord_list2` SET    `used` = 'n';
	# drop_sql_table()
	# print(" restored_fresh_sql_table  OF nord_list2 nord_list2.sql : ",end='',flush=True)
	# os.system("mysql -h remotemysql.com -u f6V3kVwxvH -psOVnW1130i f6V3kVwxvH < nord_list2.sql")
	# print("[ SUCCED ] ")
	alias_send_msg(dt_string)













# counting_used_config_config()


alias_send_msg(dt_string)
# print(lommmmp)
