# 17tracker
17Track.net Python API (Unnoficial)

# Description

This small tool can be used to track mail packages from about anywhere on the world thanks to 17track.net service. 
Just call it passing the packages as arguments separated by spaces. By default it returns a JSON object for each package containing all its tracking history, but you can ge ta human readable text of the last event occurred with --format last_only.

## Supported Carriers

A non-exaustive list includes:

- Canada Post
- Correios Brazil
- FedEx
- UPS
- USPS

For a full list of supported carriers, alongside with their package naming patterns, check http://www.17track.net/en/carrier

## Usage

```
usage: 17tracker.py [-h] [--verbose] [--format {json,last_only}] packages

Track any package on 17Track.net

positional arguments:
  packages              packages to track

optional arguments:
  -h, --help            show this help message and exit
  --verbose
  --format {json,last_only}
```
