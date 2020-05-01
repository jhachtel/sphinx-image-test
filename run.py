"""
Entry point/main module for the app.

.. image:: https://imgs.xkcd.com/comics/everyones_an_epidemiologist.png
   :alt: run-xkcd-epi-remote


.. image:: docs/source/images/everyones_an_epidemiologist.png
   :alt: run-xkcd-epi-local


"""
import sys

from app.cli import get_user_input
from app.cli import echo_user_input


if __name__ == '__main__':
    user_input = get_user_input()
    echo_user_input(user_input)
    sys.exit()

