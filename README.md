# Code review

A "technical test" done in a Django Rest Framework project

# Which files should you look for to check my code review and my own take on the subject?

* src/myuser/views_original.py: The original file, available at the given [gist](https://gist.githubusercontent.com/jbma/3b7e26c595f2e4c05525b0d70f4b3605/raw/ca54b46d8df6694daab596fe246a5cd404b3c30a/views.py)
* src/myuser/views_code_review.py: The original file, but with my comments for each code snippet that deserved my evaluation.
* src/myuser/views.py: My take on it, displaying how I would write the views module

## To run project (with docker):

#### Dependencies needeed: docker

    $ git clone <repo_url>
    $ cd <project_dir>
    
    # Will setup the django webserver on http://0.0.0.0:8000
    $ docker-compose up 
    # To access the container shell
    $ docker-compose exec web bash

## To run project (with local computer):

#### Dependencies needeed: python 3 and pipenv.

    $ git clone <repo_url>
    $ cd <project_dir>
    $ pipenv install
    $ pipenv shell

    # To start django webserver on http://127.0.0.1:8000
    $ cd src && ./manage.py runserver

### To login, use the already available user: "admin" and password: "admin"

# MIT License

Copyright (c) [2019] [Nuno Diogo da Silva diogosilva.nuno@gmail.com]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
