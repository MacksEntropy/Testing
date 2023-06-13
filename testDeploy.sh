#! /bin/bash

health_check () {
    echo "Checking health of production webapi..."
    health="$(curl -I "https://stag.ai-snips.io" 2>&1 | awk '/HTTP\// {print $2}')" 
    if [ -v health ] 
        then echo "Something went wrong, curl request returned null" 
        exit 1
    fi
    if [ $health -eq 200 ]
        then 
            echo "Webapi returned status code $health, looks good!"
    elif [ $health -gt 399 ]
        then 
            echo "Something went wrong, Webapi returned status code $health"
    fi 
}
health_check