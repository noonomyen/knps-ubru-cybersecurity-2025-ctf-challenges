#!/usr/bin/bash

set -e

echo "Acquire::http::Proxy \"http://192.168.1.11:3142\";" | sudo tee /etc/apt/apt.conf.d/00aptproxy
sudo apt update -y
sudo apt upgrade -y
