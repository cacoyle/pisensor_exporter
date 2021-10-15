#!env/bin/python

from math import ceil
from time import sleep

from prometheus_client.core import GaugeMetricFamily, REGISTRY
from prometheus_client import start_http_server, Summary, Gauge

import Adafruit_DHT

def c_to_f(celcius):
    return float("%.2lf" % ((celcius * 9/5 + 32)))

config = {
    'sensors': [
        {
            'name': 'fridge_center',
            'pin': 24,
            'type': Adafruit_DHT.AM2302
        }
    ]
}

REQUEST_TIME = Summary(
    'request_processing_seconds',
    'Time spent processing request'
)

class PiSensors(object):
    def collect(self):
        for sensor in config['sensors']:
            t = GaugeMetricFamily(
                'temp_sensor',
                'Temperature Sensor',
                labels=['name', 'type']
            )

            h = GaugeMetricFamily(
                'humidity_sensor',
                'Humidity Sensor',
                labels=['name', 'type']
            )
           
            humidity, temperature = Adafruit_DHT.read_retry(
                sensor['type'],
                sensor['pin']
            )

            t.add_metric([sensor['name'], str(sensor['type'])], c_to_f(temperature))
            h.add_metric([sensor['name'], str(sensor['type'])], ceil(humidity))


            yield t
            yield h

if __name__ == '__main__':
    REGISTRY.register(PiSensors())
    start_http_server(8888)

    while True:
        sleep(60)
