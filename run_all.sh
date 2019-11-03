# Run GPT2 API endpoint (port 5000)
cd ~/gamejam-2019/FindRealHumansNearYouGame/gpt2api/src && flask run --host 0.0.0.0 &

# Run Flask API for Game State (port 9283)
cd ~/gamejam-2019/FindRealHumansNearYouGame/flaskapi/src && flask run --host 0.0.0.0 --port 9283 &

# Run CRUD API (port 9620)
cd ~/gamejam-2019/FindRealHumansNearYouGame/api/python-flask-server && python3 -m swagger_server &

#Status Output
sleep 10
echo "Now Running all Servers"
sudo netstat -plnt

