import scrapy
import sys
from scrapy.http import FormRequest
from icalendar import Calendar, Alarm



class CalendarSpider(scrapy.Spider):
    name = "calendar"
    start_urls = ["https://sso.smile.fr/cas/login?service=https%3A%2F%2Fbluemind.smile.fr%2Fcal%2Fcalendar%2Fexport"]

    def parse(self, response):
        
        if not(hasattr(self, "login")) or not(hasattr(self, "password")):
            raise Exception('Missing -a login=value (or password)')
        
        self.log('Now login post')
        return FormRequest.from_response(
            response,
            formxpath="//form",
            formdata={'username':self.login, 'password':self.password},
            callback=self.check_login_response
        )

    def check_login_response(self, response):
        self.log('Add reminder')

        gcal = Calendar.from_ical(response.body)
        for component in gcal.walk():
            if component.name == "VEVENT":
                a = Alarm({'ACTION':'DISPLAY', 'TRIGGER':'-PT15M'})
                component.add_component(a)

        self.log('Save to file')
        f = open('calendar.ics', 'wb')
        f.write(gcal.to_ical())
        f.close()