A: && pushd \users\bj\documents\gamejamnov2019\botornot\findrealhumansnearyougame\app\findrealhumansapp\
call npm run build
ssh -i "A:\Users\BJ\Downloads\gamejamkeypair.pem" ubuntu@44.224.175.124 "rm -rf ~/FindRealHumansNearYouGame/flaskapi/src/static/api/*"
scp -pCr -i "A:\Users\BJ\Downloads\gamejamkeypair.pem" dist/* ubuntu@44.224.175.124:~/FindRealHumansNearYouGame/flaskapi/src/static/app/
popd

