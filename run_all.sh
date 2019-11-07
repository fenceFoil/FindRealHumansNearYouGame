sudo pip install flask_apscheduler tensorflow transformers tqdm flask torch

# Run GPT2 API endpoint (port 5000)
cd ~/FindRealHumansNearYouGame/gpt2api/src && sudo flask run --host 0.0.0.0 --port 8080 &

# Run Flask API for Game State (port 9283)
cd ~/FindRealHumansNearYouGame/flaskapi/src && sudo flask run --host 0.0.0.0 --port 80 &

# Run CRUD API (port 9620)
#cd ~/gamejam-2019/FindRealHumansNearYouGame/api/python-flask-server && python3 -m swagger_server &

# ADMIN DASHBOARD (80)
# cd ~/gj/FindRealHumansNearYouGame/admindashboard/admin && sudo python2 -m SimpleHTTPServer 80 &

#Status Output
sleep 10
echo "Now Running all Servers"
sudo netstat -plnt

