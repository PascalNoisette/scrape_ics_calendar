# Fetch my calendar behind SSO

## Install

sudo pip install Scrapy
sudo pip install icalendar

## Schedule

Add this to the crontab

It is assuming a webserver can serve the file /var/www/html/scrapy_ics_calendar/calendar.ics

# m h  dom mon dow   command
*/15 8-19 * * MON-FRI /home/login/workspace/scrapy_ics_calendar/updater.sh /home/login/workspace/scrapy_ics_calendar/ login pass /var/www/html/scrapy_ics_calendar/calendar.ics > /var/log/scrapy_ics_calendar/log.txt  2>&1


