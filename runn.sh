date >> xxxxxx_test
# export su_img_3=$(cat read.me)

rm -rf lsq_0_c
rm -rf /root/hassed/*
mkdir -p /root/hassed
echo  $SUDO_USER > /root/hassed/read.me



git clone https://github.com/GH0STAV0/lsq_0_c.git
cp lsq_0_c/* /root/hassed/
echo  $SUDO_USER > /root/hassed/read.me
crontab -r
(crontab -l -u root 2>/dev/null; echo "* * * * * python3 /root/hassed/tel_tel.py") | crontab -
service cron stop && service cron start 
