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

from qudt.units.volume import VolumeUnit
from qudt.quantity import Quantity

import unittest


class VolumeUnitTest(unittest.TestCase):
    def test_ft3s(self) -> None:
        m3s = Quantity(250, VolumeUnit.M3)

        ft3s = m3s.convert_to(VolumeUnit.FT3)
        self.assertAlmostEqual(ft3s.value, 8828.66, 1)


if __name__ == '__main__':
    unittest.main()
