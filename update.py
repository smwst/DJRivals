"""DJRivals database updater."""
from collections import OrderedDict
from time import localtime, sleep, strftime, time
import json

from common import _link
import pop
import dj
import image
import html


def database():
    """database() -> None

    Continuous incremental updates of the DJRivals database.

    """
    pop_index_file = _link("pop_index_file")
    while(True):
        print("Beginning new cycle...\n")
        disc_list = pop.index()
        disc_list = sorted(disc_list.keys(), key=lambda x: disc_list[x]["timestamp"])
        interval = int(36 * 60 * 60 / len(disc_list))
        for disc in disc_list:
            pop.database([disc])
            with open(pop_index_file, "rb") as f:
                data = json.loads(f.read().decode(), object_pairs_hook=OrderedDict)
            data[disc]["timestamp"] = int(time())
            with open(pop_index_file, "wb") as f:
                f.write(json.dumps(data, indent=4).encode())
            print("\nNext incremental update at: " + strftime("%H:%M:%S", localtime(time() + interval)))
            print("Ctrl-C to quit.\n")
            sleep(interval)
        print("\nFull database update complete.\n")


def djs():
    """djs() -> None

    Update the DJ database and retrieve any necessary icons.

    """
    dj.database()
    image.icons()


def index():
    """index() -> None

    Update the index file, generate the html for DJRivals, and retrieve new disc
    images if available.

    """
    pop.index(True)
    html.html()
    image.discs()
