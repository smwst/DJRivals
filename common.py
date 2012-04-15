"""Functions common to other modules."""
import os
import re


def _clean(name):
    """Strip all non-alphanumeric characters and convert to lowercase."""
    return re.sub(r"[^a-zA-Z0-9]", r"", name).lower()


def _dir_listing(path):
    """The contents of a directory."""
    return os.listdir(path)


def _file_exists(path):
    """Check to see if a file exists."""
    return True if os.path.exists(path) else False


def _link(name):
    """URLs and directory paths."""
    link = {
        "pop_ranking_page_url": "http://djmaxcrew.com/ranking/GetRankPopMixing.asp?p={}",
        "pop_ranking_disc_url": "http://djmaxcrew.com/ranking/GetRankPopMixingMusic.asp?c={}&pt={}&p={}",

        "disc_image_url": "http://img3.djmaxcrew.com/icon/disc/110/{}",
        "icon_image_url": "http://img3.djmaxcrew.com/icon/djicon/104/{}",

        "pop_database_directory": "./DJRivals/database/pop/",
        "dj_database_directory": "./DJRivals/database/dj/",

        "pop_html_directory": "./DJRivals/database/pop_html/",
        "dj_html_directory": "./DJRivals/database/dj_html/",

        "disc_image_directory": "./DJRivals/images/disc/",
        "icon_image_directory": "./DJRivals/images/icon/",

        "html_file": "./DJRivals/index.html",
        "index_file": "pop_index.json"
    }
    return link[name]


def _make_dir(path):
    """Create the given directory path if it doesn't already exist."""
    if not os.path.exists(path):
        os.makedirs(path)
    return path