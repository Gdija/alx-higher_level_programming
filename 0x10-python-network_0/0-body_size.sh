#!/bin/bash
#displays the size of the body of the response
curl -s "http://www.google.com/" | wc --bytes
