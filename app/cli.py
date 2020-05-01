"""
**--Inside the cli module docstring--**
'''''''''''''''''''''''''''''''''''''''

Minimal user interface to have a functional application.


XKCD 'Image URL (for hotlinking/embedding):'
--------------------------------------------

.. image:: https://imgs.xkcd.com/comics/code_quality.png
   :alt: index-xkcd-cq-remote


images_source
-------------

**This is where I expect the image to be, and where it is in my production project. 
The images directory in the source directory of the docs directory.**

.. note::
   I am on a Windows 10 machine. 


`sphinx_image_test\\docs\\source\\images_source\\code_quality.png`


.. image:: images_source/code_quality.png
   :alt: cli-xkcd-cq-local


images_docs
-----------

.. image:: ../images_docs/code_quality.png
   :alt: cli-xkcd-cq-local


images_root
-----------

.. image:: ../../images_root/code_quality.png
   :alt: cli-xkcd-cq-local


images_app
----------

.. image:: ../../app/images_app/code_quality.png
   :alt: cli-xkcd-cq-local


**--End cli module docstring--**
''''''''''''''''''''''''''''''''

"""
def get_user_input():
    """
    Gets user input.
    
    :return: Whatever the user types.
    
    :rtype: str
    
    """
    return input("Type something and press enter: ")


def echo_user_input(user_input):
    """
    Print whatever was typed.

    :param user_input: The string value of whatever the user typed.
    :type user_input: str

    """
    print(f"I heard, '{user_input}'")

