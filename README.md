# FindRealHumansNearYouGame
49er Game Jam November 2019. The humans are not robots, come on in!

## Deployment instructions

* Create a server like an Amazon EC2 instance
  * Minimum specs: needs a gpu? maybe?
  * Recc. g4dn.xlarge (on 11.7.2019 in my favorite region it's 0.52USD/hr)
  * Open port 80 to http traffic incoming and ssh traffic incoming on 22.
    * OPTIONAL: Open port 8080 to ping gpt2 server directly. Note that there's an endpoint we open up through port 80 to run prompts through gpt2 and the pickup line cropper already, so it's not useful outside of testing the 8080 server itself.
* Log into it
* `git clone https://github.com/fenceFoil/FindRealHumansNearYouGame.git`
* ON DEV MACHINE: Build the /app/ project using `npm install` then `npm run build` and copy the contents of `/dist/` up to the server under `~/FindRealHumansNearYouGame/flaskapi/src/static/app/`
* `chmod +x run_all.sh`
* `./run_all.sh`

