# FindRealHumansNearYouGame
49er Game Jam November 2019. The humans are not robots, come on in!

## Deployment instructions

### Server

* Create a server like an Amazon EC2 instance
  * AMI: Deep Learning AMI (Ubutnu 16.04) Version 25.0 has been tested
  * Recc. g4dn.xlarge (on 11.7.2019 in my favorite region it's 0.52USD/hr)
  * Open port 80 to http traffic incoming and ssh traffic incoming on 22.
    * OPTIONAL: Open port 8080 to ping gpt2 server directly. Note that there's an endpoint we open up through port 80 to run prompts through gpt2 and the pickup line cropper already, so it's not useful outside of testing the 8080 server itself.
* Log into it
* `git clone https://github.com/fenceFoil/FindRealHumansNearYouGame.git`
* ON DEV MACHINE: Build the /app/ project using `npm install` then `npm run build` and copy the contents of `/dist/` up to the server under `~/FindRealHumansNearYouGame/flaskapi/src/static/app/`
* `./run_all.sh`

### Hot Relaoding Dev Client

Okay, so the above works for the server app. Building the vue app for prod takes too long.

To connect a hot reloading dev client to a server running in AWS:

Go to `/app/src/findrealhumansapp/` in this repo and run `npm run serve`. Then uncomment the URL setting line in `main.js` and set it to the URL of your AWS server.

There's probably a way to do this automatically depending on whether you're running your Vue app in prod or dev.

### Testing API with Postman

We have a Postman collection you can import which hits most of the endpoints in the server. Look for it in the repo.