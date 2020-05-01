===========================
Sphinx Image Directive Test
===========================

Introduction
------------

This project exists to figure out why images do not display in 
documentation when using reStructuredText image directives for 
some users.

.. image:: https://imgs.xkcd.com/comics/everyones_an_epidemiologist.png
   :alt: index-xkcd-epi-remote


Images_source
-------------

This is where I expect the image to be, and where it is in my production project. 
The images directory in the source directory of the docs directory. 
`\\sphinx_image_test\\docs\\source\\images\\everyones_an_epidemiologist.png`, 
only `images` is named `images_source` here to help folks troubleshoot 
pathing issues. 

.. note::
   I am on a Windows 10 machine. 


.. image:: images_source/everyones_an_epidemiologist.png
   :alt: index-xkcd-epi-local


Images_source
-------------

.. image:: images_source/everyones_an_epidemiologist.png
   :alt: index-xkcd-epi-local


Images_source
-------------

.. image:: images_source/everyones_an_epidemiologist.png
   :alt: index-xkcd-epi-local


















.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   cli


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`




