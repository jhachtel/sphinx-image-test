===========================
Sphinx Image Directive Test
===========================

------------
Introduction
------------

**This project exists to figure out why images do not display in 
documentation when using reStructuredText image directives for 
some users.**

There is an index, cli, and broken_images rst file, 
and a docstring in the cli module. 
The same image is linked from various locations to various locations 
to demonstrate proper pathing. 

The broken_images.rst file has a few examples 
of how the image directive can be broken. 
**Feel free to add more.**


------------------------
Application Instructions
------------------------

The virtual environment is `imgtest`.

Activate the environment on Windows by typing: 

.. code-block::

   imgtest\Scripts\activate


Deactivate on Windows by typing:

.. code-block::

   deactivate


Feel free to add instructions for Mac and Linux if you know them.

The entry point for the app is run.py in the root folder. 
It simply takes command line input and echoes back, 
telling you what it received as input from you. 



XKCD 'Image URL (for hotlinking/embedding):'
--------------------------------------------

.. image:: https://imgs.xkcd.com/comics/code_quality.png
   :alt: index-xkcd-cq-remote


images_source
-------------

`sphinx_image_test\\docs\\source\\images_source\\code_quality.png`

**This is where I expect the image to be, and where it is in my production project. 
The images directory in the source directory of the docs directory.**

.. note::
   I am on a Windows 10 machine. 


.. image:: images_source/code_quality.png
   :alt: index-xkcd-cq-local


images_docs
-----------

.. image:: ../images_docs/code_quality.png
   :alt: index-xkcd-cq-local


images_root
-----------

.. image:: ../../images_root/code_quality.png
   :alt: index-xkcd-cq-local


images_app
----------

.. image:: ../../app/images_app/code_quality.png
   :alt: index-xkcd-cq-local



.. toctree::
   :maxdepth: 1
   :caption: Contents:
   
   cli
   broken_images


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`




