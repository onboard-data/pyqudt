from qudt.unit import Unit
from qudt.ontology.unit_factory import UnitFactory

class RateChangeUnit(object):
    """
    """
    PERCENT_PER_SEC: Unit = UnitFactory.get_qudt('PERCENT-PER-SEC')
    PERCENT_PER_WK: Unit = UnitFactory.get_qudt('PERCENT-PER-WK')
    PERCENT_PER_YR: Unit = UnitFactory.get_qudt('PERCENT-PER-YR')

