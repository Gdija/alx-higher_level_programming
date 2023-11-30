#!/bin/bash
#sends a DELETE request to the URL and displays the body of the response
curl -sXl DELETE "$1"
