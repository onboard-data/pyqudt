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

from qudt.units.energy import EnergyUnit, PowerUnit
from qudt.quantity import Quantity

import unittest


class PowerUnitTest(unittest.TestCase):
    def test_kbtu_per_hr(self) -> None:
        kbtus = Quantity(2500, PowerUnit.KBTU_PER_HR)

        btus = kbtus.convert_to(PowerUnit.THM_US_PER_HR)
        self.assertAlmostEqual(btus.value, 25, 1)


if __name__ == '__main__':
    unittest.main()
