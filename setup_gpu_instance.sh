#=======================================================================
# need to get git, pip, ansible installed
#=======================================================================

apt-get update
apt-get install python-setuptools
apt-get install git

easy_install pip

git clone git://github.com/ansible/ansible.git --recursive

cd ./ansible

source ./hacking/env-setup

pip install paramiko PyYAML Jinja2 httplib2 six

pip install ansible

pip install --upgrade pip

sudo apt-get install libatlas-base-dev gfortran

pip install scipy





