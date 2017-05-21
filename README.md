# ulp is a Location Picker

Ulp is a command-line tool that can be used to find and interact with URLs from a given input. 

Think of something like Facebook's [PathPicker](https://github.com/facebook/pathpicker), but for URLs.

## Installing

Ulp is a python package and as such it can be installed via pip. You can install the latest released version with 

```
pip install -U ulp
```

and, if you want to install a fresh version from the latest source code *(good luck)*, you can run 

```
pip install git+https://github.com/victal/ulp.git@master
```

For systems where Python 2.x is the default version, you might need to run the commands above using **pip3** as the executable instead of **pip**.

## Requirements

Ulp is being developed/used with Python 3.5, but it might just work with **Python > 3.0**

*Copy to clipboard* functionality depends on [Pyperclip](https://github.com/asweigart/pyperclip) and as such you might need to install additional modules for it to work. Check Pyperclip's Readme for details.


## Usage

Simply pipe or redirect the input from which you want to pick the URLs into **ulp**. Yes, just like PathPicker. Yes, it's on purpose.

**Example:**

If you're pushing to a BitBucket repository, for example, the output of `hg push` will give you the URL where you can create a new PR from the branch you just pushed to, so you can do

```
hg push | ulp
```

and open the given URL in a browser or copy it for later.

If you just want to list the URLs in a given input, you can use the **ulp_extract** helper script, like this:

```
cat huge_text_with_lots_of_urls | ulp_extract
```

## License

Ulp is licensed with the [MIT License](https://github.com/victal/ulp/blob/master/LICENSE)

## TODO

* Add a 'filter' option within the UI
* Add an example image/gif in this readme
* Tidy up - clean up code, ad a --help, tests and clean up code
