#!/usr/bin/env bash

sudo apt update
sudo apt upgrade -y
# Install Python3 pip
sudo apt install -y python3-pip

# Install Nginx
sudo apt install -y nginx

# Install Virtualenv
sudo apt install -y virtualenv