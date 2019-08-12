[![Build Status](https://travis-ci.org/reason-for-risen/geocode.svg?branch=dev)](https://travis-ci.org/reason-for-risen/geocode)
# geocode
Geocode is a simple desktop app that can easily find any location from queries like "red square" or "Nevsky prospect 4". It can also return the address of the clicked spot on the map! 

## Installation

**NOTE**: Python 3.6 or higher is required.

```bash
# clone the repo
$ git clone https://github.com/reason-for-risen/geocode.git

# change the working directory to geocode
$ cd geocode

# install python3 and python3-pip if they are not installed

# install the requirements via pipenv
$ bash install_pipenv.sh
```

## Usage
```bash
# run via pipenv
$ pipenv run python3 src/geomap.py
```

## Tests
```bash
# run pytest via pipenv
$ pipenv run pytest
```
