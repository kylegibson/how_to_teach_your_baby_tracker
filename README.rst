********************************
How to teach your baby (tracker)
********************************

The book
`How to teach your baby to read
<http://www.amazon.com/Teach-Your-Gentle-Revolution-Series/dp/0757001858>`_
offers an exciting way
to introduce
young children
to the wonderful world
of reading.

One challenge
in following the
program outlined in the book
is keeping track
of the number of times
each word has been seen.
This is critical,
because words
need to be retired
after being viewed
a certain number of times.
Retired words
are then replaced with
new words.

This application
provides a web interface
for managing words.
You can add words,
retire words
and mark words as viewed.

This application
can also be used
for tracking
quantities
in the book
`How to teach your baby math
<http://www.amazon.com/Teach-Your-Gentle-Revolution-Series/dp/075700184X>`_.

=============================
Mobile-friendly web interface
=============================

.. image:: https://github.com/kylegibson/how_to_teach_your_baby_tracker/raw/master/tracker.png
    :alt: How to teach your baby (tracker)
    :width: 300
    :height: 533
    :align: center

Clicking on a word
in the above interface
causes the word
view count
to be incremented
by one.
Clicking
``Mark All``
will increment
the view count
for all words
in the group.

In the administrator
interface
(browse to ``/admin``)
you can configure
as many ``WordGroupings``
as you'd like,
each with as many
``Words``
as you want.

==============================
Installation and configuration
==============================

#. Download
   `master.zip
   <https://github.com/kylegibson/how_to_teach_your_baby_tracker/archive/master.zip>`_
   and extract it.
#. Create a new virtualenv
   and install the requirements:

   .. code-block:: shell-session

       virtualenv env
       source env/bin/activate
       pip install -r how_to_teach_your_baby_tracker-master/requirements.txt

#. Change directory
   into the application
   directory.
#. Initialize the database

   .. code-block:: shell-session

       ./manage.py migrate

#. Create a
   superuser account
   that you can use
   for managing words.

   .. code-block:: shell-session

       ./manage.py createsuperuser

=====
Usage
=====

#. Start the server.

   .. code-block:: shell-session

       ./manage.py runserver 0.0.0.0:30000

#. Navigate your browser to
   ``http://localhost:30000/admin``
   and log in
   as the superuser
   you created above.
#. Create your ``Words``
   and
   ``WordGroupings``
   as desired.
