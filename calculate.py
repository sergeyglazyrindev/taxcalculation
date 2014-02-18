#!/usr/bin/env python

from tax.tasks import calculate
import config


def run():
    calculate(config.get_config_for_calculations())


if __name__ == '__main__':
    run()
