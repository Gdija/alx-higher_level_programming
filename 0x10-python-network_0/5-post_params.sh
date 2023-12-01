#!/bin/bash
#sends a POST request with a values
curl -s -H -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
