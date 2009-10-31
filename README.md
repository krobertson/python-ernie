Python-Ernie
=====

By Ken Robertson (ken@invalidlogic.com)

Python-Ernie is a port of the Ruby-based Ernie server by Tom Preston-Werner.  Python-Ernie is the Python server implementation for the BER-RPC specification.

See the full BERT-RPC specification at [bert-rpc.org](http://bert-rpc.org).


Installation
------------

To install Python-Ernie, you will also need to install the Python port of BERT serializers and Erlastic.

    $ git clone git://github.com/samuel/python-erlastic.git
    $ sudo python python-erlastic/setup.py install
    
    $ git clone git://github.com/samuel/python-bert.git
    $ sudo python python-bert/setup.py install

To install python-ernie itself, run:

    $ sudo ./setup.py install


Example Handler
---------------

from ernie import mod, start

    from ernie import mod, start
    
    def calc_add(a, b):
        return a + b
    mod('calc').fun('add', calc_add)
    
    if __name__ == "__main__":
        start()


Contribute
----------

If you'd like to hack on Python-Ernie, start by forking my repo on GitHub:

http://github.com/krobertson/python-ernie

Just create your own fork, hack on it, and then send me a pull request once done.


Todo
---------

I'll be the first to admin I am still new to Python.  So if I am way off on best practices in Python, let me know!

1. Update exception handling to return traceback
1. Ensure correct handling around read operations
1. See if I can clean up the way you define your modules
1. Test


License
---------

Copyright (c) 2009 Ken Robert

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.