#!/bin/bash

echo 'motion detected!'
DATE=$(date +"Y-%m-%d_%H%M")

#fswebcam -r 800x600 -d /dev/video1 $DATE.jpg
fswebcam -r 800x600 -d /dev/video1 ../images/cita.jpg
