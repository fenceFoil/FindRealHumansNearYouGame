rootDir=`cd .. && pwd`
echo $rootDir

cd $rootDir/gpt2api/src && flask run --host 0.0.0.0 --port 8080 &

echo "GPT-2 API now running"