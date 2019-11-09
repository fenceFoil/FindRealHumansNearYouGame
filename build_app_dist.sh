rootDir=`pwd`
echo $rootDir
cd $rootDir/app/findrealhumansapp && npm run build && rm -rf $rootDir/flaskapi/src/static/app/ && yes | cp -R $rootDir/app/findrealhumansapp/dist/ $rootDir/flaskapi/src/static/app/
