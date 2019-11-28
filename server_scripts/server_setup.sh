sudo apt-get update
sudo apt-get install gcc g++ make

# Install Nodejs & npm
curl -sL https://deb.nodesource.com/setup_13.x | sudo -E bash -
sudo apt-get install -y nodejs

# Install YARN
curl -sL https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
sudo apt-get update && sudo apt-get install yarn

sudo ln -s /usr/bin/nodejs /usr/bin/node
sudo npm install --no-optional -g @vue/cli

# Install npm dependencies
cd ~/FindRealHumansNearYouGame/app/findrealhumansapp && npm install

#  @vue/cli-service @vue/cli-plugin-babel @vue/cli-service-global
# sudo npm install --no-optional -g vue eslint @vue/cli @vue/cli-service @vue/cli-plugin-babel @vue/cli-service-global @vue/cli-plugin-eslint vue-template-compiler eslint-plugin-vue^C
# sudo apt-get remove -y npm node yarn