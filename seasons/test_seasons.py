from seasons import time_from_birth_in_text
import pytest
from datetime import date
import datetime

def test_valid():
    assert time_from_birth_in_text(datetime.date(2024, 8, 24)) == "Five hundred twenty-five thousand, six hundred minutes"
    assert time_from_birth_in_text(datetime.date(2023, 8, 24)) == "One million, fifty-two thousand, six hundred forty minutes"
