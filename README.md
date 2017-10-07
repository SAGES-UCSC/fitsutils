# fitsutils
random fits file utilities not already in astropy scripts

## fitscrop
Crop a fits file to a rectangle with the given bottom left corner and top right corner.
```
usage: fitscrop [-h] fitsin fitsout xlow ylow xhigh yhigh

Crop a fits file.

positional arguments:
  fitsin      input fits file
  fitsout     output fits file
  xlow        lower x-axis cutoff (inclusive)
  ylow        lower y-axis cutoff (inclusive)
  xhigh       higher x-axis cutoff (exclusive)
  yhigh       higher y-axis cutoff (exclusive)

optional arguments:
  -h, --help  show this help message and exit
```

## fitscphdr
Copy the header from one fits file to another fits file, warning if there are any overwrites.
```
usage: fitscphdr [-h] [--clobber] sourcefits targetfits newfits

Copy a fits header.

positional arguments:
  sourcefits  source fits header file
  targetfits  target fits header file
  newfits     name for new fits file

optional arguments:
  -h, --help  show this help message and exit
  --clobber   overwrite existing fits header entries
```
