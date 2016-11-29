Overview
--------

The Movie Website Project is the first assignment for the Udacity Full Stack Web Development Nanodegree.
It creates a static html page showing a list of movies, including the title, poster and trailer, using object-oriented Python.

Contents
--------

* **media.py**: where a class named *Movie* is defined.
* **entertainment_center.py**: where a list of movies is stored as instances of the class *Movie*, including box art imagery and a trailer url.
* **fresh_tomatoes.py**: a program that takes as imputs the information stored in **entertainment_center.py** and returns an HTML page.

Requirements
------------

* Python 2.7 or superior.
* Web browser (such as Chrome, Firefox or Safari)

Installation
------------

1. Download **media.py**, **entertainment_center.py** and **fresh_tomatoes.py**.
2. Save **media.py**, **entertainment_center.py** and **fresh_tomatoes.py** in the same folder.

Usage
-----

This project comes with six movies stored by default. Check them out, by the way, they are awesome. To create a Movie Website with these six movies, all you need to do is run **entertainment_center.py** on a Python shell.
If you want to customize it with your favorite movies, edit **entertainment_center.py** and add your own instances of Movie, including the title, storyline, poster image url and youtube trailer url. Here is an example:
```python
movie_name = media.Movie(
    "title",
    "storyline", 
    "poster image url", 
    "youtube trailer url"
    )
```
After you have added your movies, run **entertainment_center.py** on a Python shell, and watch your very own Movie Website come to life.
If you want to change the look of the page, you can modify the HTML, CSS and JavaScript in **fresh_tomatoes.py**
If an error message shows up on the HTML file, check any changes you have made for typos and make sure that all the files are in the same directory.

Acknowledgements
----------------

My special thanks go to **Kunal**, Udacity Instructor of *Programming Foundations with Python*, and to [**Adarsh**](https://github.com/adarsh0806), creator of **fresh_tomatoes.py**.

