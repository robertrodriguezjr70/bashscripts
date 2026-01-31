#!/bin/bash

# Exit immediately if a command fails
set -e

# Update package index
sudo apt update -y

# Install Apache
sudo apt install -y apache2

# Start Apache service
sudo systemctl start apache2

# Enable Apache to start on boot
sudo systemctl enable apache2
