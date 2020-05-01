"""
Minimal user interface

.. image:: https://imgs.xkcd.com/comics/everyones_an_epidemiologist.png
   :alt: cli-xkcd-epi-remote


.. image:: ../docs/source/images/everyones_an_epidemiologist.png
   :alt: cli-xkcd-epi-local


"""
def get_user_input():
    return input("Type something and press enter: ")


def echo_user_input(user_input):
    print(f"I heard, '{user_input}'")

