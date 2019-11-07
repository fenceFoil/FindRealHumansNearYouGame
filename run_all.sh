source activate tensorflow_p36
pip install flask_apscheduler tqdm torch transformers

# Run GPT2 API endpoint (port 5000)
cd ~/FindRealHumansNearYouGame/gpt2api/src && flask run --host 0.0.0.0 --port 8080 &

# Run Flask API for Game State (port 9283)
sudo iptables -t nat -I PREROUTING -p tcp --dport 80 -j REDIRECT --to-ports 3000
cd ~/FindRealHumansNearYouGame/flaskapi/src && flask run --host 0.0.0.0 --port 3000 &

# Run CRUD API (port 9620)
#cd ~/gamejam-2019/FindRealHumansNearYouGame/api/python-flask-server && python3 -m swagger_server &

# ADMIN DASHBOARD (80)
# cd ~/gj/FindRealHumansNearYouGame/admindashboard/admin && sudo python2 -m SimpleHTTPServer 80 &

#Status Output
sleep 10
echo "Now Running all Servers"
netstat -plnt

