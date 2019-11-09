# FindRealHumansNearYouGame
49er Game Jam November 2019. The humans are not robots, come on in!

## Deployment instructions

### Server

* Create a server like an Amazon EC2 instance
  * AMI: Deep Learning AMI (Ubutnu 16.04) Version 25.0 has been tested
  * Recc. g4dn.xlarge (on 11.7.2019 in my favorite region it's 0.52USD/hr)
  * Open port 80 to http traffic incoming and ssh traffic incoming on 22.
    * OPTIONAL: Open port 8080 to ping gpt2 server directly. Note that there's an endpoint we open up through port 80 to run prompts through gpt2 and the pickup line cropper already, so it's not useful outside of testing the 8080 server itself.
  * Log into it over SSH

##### INITIAL INSTALL
  * One liner:
    * run `git clone https://github.com/fenceFoil/FindRealHumansNearYouGame.git && cd FindRealHumansNearYouGame/server_scripts/ && ./server_setup.sh && ./build_app_dist.sh && ./monitor.sh`
  * Mostly Automated Steps (Same as One Liner)
    * run `git clone https://github.com/fenceFoil/FindRealHumansNearYouGame.git`
    * run `cd FindRealHumansNearYouGame/server_scripts/`
    * run `./server_setup.sh`
    * run `./build_app_dist.sh` (Builds the app into static files)
    * run `./run_all.sh` (original script) or `./monitor.sh` (for split_planel dashboard)
  
##### UPDATE INSTALL
  * run `cd FindRealHumansNearYouGame/server_scripts/`
  * run `update.sh` (will force pull latest and rebuild vue app's dist
  * run `./stop_all.sh` or `./run_all.sh` as needed

##### Server Script Descriptions:
  * `update.sh` - force pull latest and rebuild vue app's static dist files
  * `monitor.sh` - Split terminal dashboard for monitoring servers
  * `server_setup.sh` - Install all base dependencies including vue app's npm dependencies
  * `stop_all.sh` - stop all servers automatically
  
* Manually build static app files:
  * Nav to 'app/findrealhumansapp'
  * `npm install`
  * `npm run build`
  * Copy `dist/` to `FindRealHumansNearYouGame/flaskapi/src/static/app/`
  
### Hot Reloading Dev Client

Okay, so the above works for the server app.

To connect a hot reloading dev client to a server running in AWS:

Go to `/app/src/findrealhumansapp/` in this repo and run `npm run serve`. Then uncomment the URL setting line in `main.js` and set it to the URL of your AWS server.

There's probably a way to do this automatically depending on whether you're running your Vue app in prod or dev.

### Testing API with Postman

We have a Postman collection you can import which hits most of the endpoints in the server. Look for it in the repo.
