rootDir=`cd .. && pwd`
echo $rootDir
cd $rootDir/app/findrealhumansapp && npm install && npm run build && rm -rf $rootDir/flaskapi/src/static/app/ && yes | cp -R $rootDir/app/findrealhumansapp/dist/ $rootDir/flaskapi/src/static/app/
