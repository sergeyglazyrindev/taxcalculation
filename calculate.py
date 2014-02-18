#!/usr/bin/env python

import datetime
import time

from customs.tasks import calculate_customs
import config


def run():
    calculate_customs(config.get_config_for_calculations())


if __name__ == '__main__':
    run()
