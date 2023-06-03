#!/bin/bash

url=""
num_visits=0

read -p "Enter the URL you want to visit: " url
read -p "Enter the number of times to visit the URL: " num_visits

for ((i=0; i<$num_visits; i++))
do
    wget -O /dev/null "$url"
    echo "Visited URL: $url"

    sleep 1  # Wait for 1 second before making the next request
done

echo "Finished visiting the URL $num_visits times."
