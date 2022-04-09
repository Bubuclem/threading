import threading
import json
from urllib.request import urlopen
import time

BASE_URL = 'https://random-data-api.com/api/{}'
Vehicles = []

class Vehicle(object):
    '''
    id
    uid
    vin
    make_and_model
    color
    transmission
    drive_type
    fuel_type
    car_type
    car_options[]
    specs[]
    doors
    mileage
    kilometrage
    license_plate
    '''
    def __init__(self, data):
	    self.__dict__ = json.loads(data)

def add_vehicle() -> None : 
    json_url = urlopen(BASE_URL.format('vehicle/random_vehicle'))
    data = json_url.read()

    vehicle = Vehicle(data)
    Vehicles.append(vehicle)

def print_vehicle():
    for vehicle in Vehicles:
        print(vehicle.make_and_model)

def print_time(start : time):
    end = time.time()
    print('{} sec'.format(end - start))

def sync():
    Vehicles.clear()
    start = time.time()

    for i in range(0,100):
        add_vehicle()

    print_time(start)

def thread():
    Vehicles.clear()
    start = time.time()

    threads = [None] * 100
    for i in range(0,100):
        threads[i] = threading.Thread(target=add_vehicle)
        threads[i].start()

    for i in range(len(threads)):
        threads[i].join()

    print_time(start)

if __name__=='__main__':
    sync()
    thread()