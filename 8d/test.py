#!/usr/bin/env python

import coverage
COV = coverage.coverage(branch=True, include='app/*')
COV.set_option('report:show_missing', True)
COV.start()

import unittest
suite = unittest.TestLoader().discover('tests')
unittest.TextTestRunner(verbosity=2).run(suite)

COV.stop()
COV.report()