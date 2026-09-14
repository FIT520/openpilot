import unittest

from opendbc.car.honda.values import CAR, HondaFlags


class TestHondaFingerprint(unittest.TestCase):
  def test_tja_bosch_only(self):
    for car_model in CAR:
      if car_model.config.flags & HondaFlags.BOSCH_TJA_CONTROL:
        assert car_model.config.flags & HondaFlags.BOSCH, "Nidec car found with TJA control"

  def test_fit4g_tja_test_config(self):
    flags = CAR.HONDA_FIT_4G.config.flags
    assert flags & HondaFlags.BOSCH
    assert flags & HondaFlags.BOSCH_RADARLESS
    assert flags & HondaFlags.BOSCH_TJA_CONTROL
    assert not flags & HondaFlags.LKAS_MINSPEED_CUTOFF

