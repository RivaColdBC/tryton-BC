# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import test_view, test_depends


class ProjectRevenueTestCase(unittest.TestCase):
    'Test ProjectRevenue module'

    def setUp(self):
        trytond.tests.test_tryton.install_module('project_revenue')

    def test0005views(self):
        'Test views'
        test_view('project_revenue')

    def test0006depends(self):
        'Test depends'
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        ProjectRevenueTestCase))
    return suite
