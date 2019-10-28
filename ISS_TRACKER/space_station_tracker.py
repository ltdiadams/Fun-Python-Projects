import requests
import webbrowser
import time
import turtle


astronaut_data = 'http://api.open-notify.org/astros.json'

results = requests.get(astronaut_data).json()
print(results)

print('People in space {}'.format(results['number']))

for person in results['people']:
    print(person['name'] + ' in ' + person['craft'])

#
iss_location = 'http://api.open-notify.org/iss-now.json'

while True:
    result = requests.get(iss_location).json()
    #print(result)

    timestamp = result['timestamp']
    lat = result['iss_position']['latitude']
    long = result['iss_position']['longitude']
    print(str(timestamp) + ' ' + lat + ' ' + long)

    screen = turtle.Screen()
    screen.setup(720,360)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.bgpic('NASA_World_Map.gif')
    screen.register_shape('ISS.gif')
    iss = turtle.Turtle(visible=False)
    iss.shape('ISS.gif')
    iss.penup()
    iss.goto(float(long), float(lat))
    iss.showturtle()
    # google_maps_iss = "http://maps.google.com/?q={},{}".format(lat, long)
    # webbrowser.open_new_tab(google_maps_iss)

    #turtle.mainloop()

    time.sleep(.1)



