rootDir=`cd .. && pwd`
echo $rootDir

sudo iptables -t nat -I PREROUTING -p tcp --dport 80 -j REDIRECT --to-ports 3000
cd $rootDir/flaskapi/src && flask run --host 0.0.0.0 --port 3000 &

echo "FLASK API now running"