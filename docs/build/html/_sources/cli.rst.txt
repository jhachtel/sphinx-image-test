==========
CLI Module
==========


**--cli rst file image directives--**
'''''''''''''''''''''''''''''''''''''


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
   :alt: cli-rst-xkcd-cq-local


images_docs
-----------

.. image:: ../images_docs/code_quality.png
   :alt: cli-rst-xkcd-cq-local


images_root
-----------

.. image:: ../../images_root/code_quality.png
   :alt: cli-rst-xkcd-cq-local


images_app
----------

.. image:: ../../app/images_app/code_quality.png
   :alt: cli-rst-xkcd-cq-local


|


**--End cli rst file image directives--**
'''''''''''''''''''''''''''''''''''''''''



CLI Module in app Package
-------------------------

.. note::
   This is where the cli module is linked into the cli.rst file. 
   It should show the same as above, 
   only the image is being linked from the app package, 
   specifically the cli module.


.. automodule:: app.cli
   :members:


