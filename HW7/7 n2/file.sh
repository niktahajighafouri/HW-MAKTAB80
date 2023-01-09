#!/bin/bash
read -p 'Enter file name: ' file_name
find ./ -name $file_name
tail -n 11 $file_name
