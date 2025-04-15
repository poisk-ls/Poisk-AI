#!/bin/bash

# Colors
GREEN='\033[0;32m'
CYAN='\033[0;36m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${CYAN}Starting Package Installation...${NC}"
sleep 1

# Update and Upgrade
echo -e "${GREEN}Updating package list...${NC}"
pkg update -y && pkg upgrade -y

# Array of packages
packages=("sl" "screenfetch" "neofetch" "cmatrix" "neofetch" "libcaca" "termux-api" "cowsay")

# Install each package
for pkg in "${packages[@]}"
do
    echo -e "${GREEN}Installing ${pkg}...${NC}"
    pkg install -y "$pkg"
    if [ $? -eq 0 ]; then
        echo -e "${CYAN}${pkg} installed successfully!${NC}"
    else
        echo -e "${RED}Failed to install ${pkg}${NC}"
    fi
    sleep 0.5
done

echo -e "${GREEN}All done! Enjoy your new tools.${NC}"