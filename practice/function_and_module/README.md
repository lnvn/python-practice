## Function and Module

#### Build and install a package
```bash
cd ./practice/function_and_module

# create a source distribution package
python3 setup.py sdist

# install distribution into your local copy of python
python3 setup.py install
```

#### Test
```python
# you already build a module called "nester"
import nester
fav_movies = ["abc", "def", ["ghi", "jkl"]]

# all code in python associated with a namespace
# when you put code into it own module, python automatically create a 
# namespace with the same name as your module => the code in your module (this case is "nester") is associated with a namespace call "nester"
# Page 45 - Head First Python 2nd version
# this case you need to call print_lol function base on that namespace
nester.print_lol(fav_movies)

# or you can add the function to current namespace by use
from nester import print_lol
fav_movies = ["abc", "def", ["ghi", "jkl"]]
# Code in your main program is associated with a namespace called __main__
# dont need to specify namespace because the function is added into the __main__ namespace
print_lol(fav_movies)

```

#### Upload code to PyPI
```python
python3 setup.py sdist
pip3 install twine
twine upload dist/* --repository testpypi
```

#### What we have learned in this session
- Use function to reuse the cose
- Build and upload a python module
- Recursive function

example
```python
def print_lol(the_list, level=0):
    for item in the_list:
        if isinstance(item, list):
            # here we have recursive function
            print_lol(item, level+1)
        else:
            for tab_stop in range(level):
                print("\t", end='')
            print(item)
```