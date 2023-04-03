#!/bin/bash
# Script that sends POST to URL
curl -sX POST -d "email=test@gmail.com&subject=I am okay" "$1"
