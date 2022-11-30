### CONDA ENVIORNMENT
# Create Conda Enviornment
# through yaml file.

conda env list
conda create -n <env-name>
conda activate <env-name>
conda install (package)
conda remove (package)

# version number
conda --version

# create an enviornment from environemnt.yml file
conda env create --file environment.yml

conda env remove -n <env-name>

# create an environment file from environment
conda env export > environment.yml
conda env export --file environment.yml


### install redis on ubuntu 22.04
sudo apt update && sudo apt upgrade

sudo apt-get install redis-server -y

# update
sudo nano /etc/redis/redis.conf
# bind 192.168.1.200 ....
# change this to local ip
# bind 192.168.2.1 ::1  (::1 is for ipv6 on localhost)

# supervised no (change this to)
# supervised systemd

sudo systemctl start redis-server
sudo systemctl restart redis-server
sudo systemctl stop redis-server
sudo systemctl status redis-server

sudo systemctl enable redis-server  (automatic start on boot)


### Virtual Environment
pip install virtualenv
virtualenv -version
virtualenv <env-name>
source <env-name>/bin/activate
deactivate