""" extensions of lizard """

from __future__ import print_function

from .auto_open import auto_open, auto_read
from .csvoutput import csv_output
from .htmloutput import html_output
from .version import version
from .xmloutput import xml_output


def print_xml(results, options, _, total_factory):
    print(xml_output(total_factory(list(results)), options.verbose))
    return 0


def print_csv(results, options, _, total_factory):
    csv_output(total_factory(list(results)), options)
    return 0
