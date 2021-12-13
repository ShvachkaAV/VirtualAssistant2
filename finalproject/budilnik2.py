import datetime
import time
import pyglet


def budilnik_main(day, month, year, hour, minutes):
    music_budilnik = pyglet.resource.media("budilnik.wav")
    then = datetime.datetime(int(year), int(month), int(day), int(hour), int(minutes))
    now = datetime.datetime.now()
    delta = then - now
    time.sleep(delta.seconds)
    return music_budilnik.play(), pyglet.app.run()