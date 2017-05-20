#!/bin/bash

docker run -it --net=host -v ${PWD}:/var/www/localhost/htdocs s4ros/apache2 /bin/ash

