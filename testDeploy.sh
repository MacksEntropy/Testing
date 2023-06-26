#! /bin/bash

health_check () {
    echo "Checking health of production webapi..."
    health="$(curl -I "https://api.ai-snips.io/api/manage/healthcheck" 2>&1 | awk '/HTTP\// {print $2}')"
    if [ $health -eq 200 ]
        then 
            echo "Webapi returned status code $health, looks good!"
    elif [ $health -gt 399 ]
        then 
            echo "Something went wrong, Webapi returned status code $health"
    fi 
}
health_check