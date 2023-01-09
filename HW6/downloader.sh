#!/bin/bash
read -p "link: " link
wget $link
echo $link >> log.txt

