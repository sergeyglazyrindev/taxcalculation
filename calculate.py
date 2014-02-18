#!/usr/bin/env python

import datetime
import time

from tax.tasks import calculate
import config


def run():
    calculate_customs(config.get_config_for_calculations())


if __name__ == '__main__':
    run()
