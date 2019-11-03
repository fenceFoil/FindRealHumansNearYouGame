sudo pip install flask_apscheduler tensorflow transformers tqdm flask torch

# Run GPT2 API endpoint (port 5000)
cd ~/gamejam-2019/FindRealHumansNearYouGame/gpt2api/src && sudo flask run --host 0.0.0.0 --port 465 &

# Run Flask API for Game State (port 9283)
cd ~/gamejam-2019/FindRealHumansNearYouGame/flaskapi/src && sudo flask run --host 0.0.0.0 --port 443 &

# Run CRUD API (port 9620)
cd ~/gamejam-2019/FindRealHumansNearYouGame/api/python-flask-server && python3 -m swagger_server &

#Status Output
sleep 10
echo "Now Running all Servers"
sudo netstat -plnt

