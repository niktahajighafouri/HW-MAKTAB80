#!/bin/bash
current_directory=$(pwd)
echo $current_directory
read -p "file name:" file_name
if [ $(find . -name $file_name) ]; then
	head $file_name
else
	echo "there is not such a file in the current directory"
fi

