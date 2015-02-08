# I am CAT: A simple python picture carroussel

This repository contains a simple python wsgi file and settings to automatically create a bootstrap caroussel from a directory containing pictures. 

* [iamcat.py](iamcat.py) is a simply wsgi application that reads a directory and makes a twitter bootstrap caroussel with all pictures from that directory
* The [uwsgi configuration](upstart_iamcat_uwsgi.conf) starts a uwsgi process that serves [iamcat.py]. It also defines the DOCUMENT_ROOT to point to a hosted folder that contains the picture folder
* The [nginx configuration](nginx_iamcat.conf) sets up nginx to redirect "/" to the uwsgi server, and simply serve all other files in the DOCUMENT_ROOT. 

Installation
----

The following assumes a ubuntu linux server:

0. Install nginx, uwsgi, python, and mako
1. Create a folder somewhere, e.g. DOCUMENT_ROOT, and put a folder of pictures in it 
2. Copy upstart_iamcat_uwsgi.conf to /etc/init/iamcat.conf and adjust the paths in the file
3. Copy nginx_iamcat.conf to /etc/nginx/sites-available and adjust the document root
4. Start 'iamcat' and restart nginx

With a bit of luck, you should now see a caroussel at the web site of your server that looks like [i.amcat.nl](http://i.amcat.nl). All files in the document root will be served as normal. 
