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

from qudt.unit import Unit
from qudt.ontology.unit_factory import UnitFactory


class EnergyUnit(object):
    """
    """
    EV: Unit = UnitFactory.get_qudt('EV')
    JOULE: Unit = UnitFactory.get_qudt('J')
    BTU: Unit = UnitFactory.get_qudt('BTU_IT')
    KBTU: Unit = UnitFactory.get_qudt('KiloBTU_IT')
    KWH: Unit = UnitFactory.get_qudt('KiloW-HR')

    NM3_GAS: Unit = UnitFactory.get_qudt('NM3-NAT-GAS')
    SCM_GAS: Unit = UnitFactory.get_qudt('SCM-NAT-GAS')
    SFT3_GAS: Unit = UnitFactory.get_qudt('SFT3-NAT-GAS')


class PowerUnit(object):
    BTU_PER_HR: Unit = UnitFactory.get_qudt('BTU_IT-PER-HR')
    KBTU_PER_HR: Unit = UnitFactory.get_qudt('KiloBTU_IT-PER-HR')
    THM_US_PER_HR: Unit = UnitFactory.get_qudt('THM_US-PER-HR')
