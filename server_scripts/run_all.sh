source activate tensorflow_p36
pip install flask_apscheduler tqdm torch transformers

#eventually only stop servers that had updated files
./stop_all.sh && ./stop_all.sh 

# Run GPT2 API endpoint (port 5000)
./start_gpt2_api.sh &

# Run Flask API for Game State (port 9283)
./start_flask_api.sh &

# Run CRUD API (port 9620)
#cd ~/gamejam-2019/FindRealHumansNearYouGame/api/python-flask-server && python3 -m swagger_server &

# ADMIN DASHBOARD (80)
# cd ~/gj/FindRealHumansNearYouGame/admindashboard/admin && sudo python2 -m SimpleHTTPServer 80 &

#Status Output
sleep 10
echo "Now Running all Servers"
netstat -plnt

