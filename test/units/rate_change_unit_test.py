################################################################################
#
#  Copyright (C) 2019 Garrett Brown
#  This file is part of pyqudt - https://github.com/eigendude/pyqudt
#
#  pyqudt is derived from jQUDT
#  Copyright (C) 2012-2013  Egon Willighagen <egonw@users.sf.net>
#
#  SPDX-License-Identifier: BSD-3-Clause
#  See the file LICENSE for more information.
#
################################################################################

from qudt.units.ratechange import RateChangeUnit
from qudt.quantity import Quantity

import unittest


class RateChangeUnitTest(unittest.TestCase):
    def test_ft3s(self) -> None:
        per_sec = Quantity(250, RateChangeUnit.PERCENT_PER_SEC)

        per_wk = per_sec.convert_to(RateChangeUnit.PERCENT_PER_WK)
        self.assertAlmostEqual(per_wk.value, 250*60*60*24*7, 1)


if __name__ == '__main__':
    unittest.main()
