#!/bin/bash

cd $1
/usr/local/bin/scrapy crawl calendar -a login=$2 -a password=$3
mv calendar.ics $4
