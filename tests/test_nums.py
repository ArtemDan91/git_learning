import pytest
from first.nums import div


@pytest.mark.parametrize("division, divider, expected_result", [(10, 2, 5),
                                                   (20, 10, 2),
                                                   (30, -3, -10),
                                                   (5, 2, 2.5)])
def test_division_good(division, divider, expected_result):
    assert div(division, divider) == expected_result


@pytest.mark.parametrize("expected_exception, division, divider",
                         [(ZeroDivisionError, 10, 0),
                          (TypeError, 20, "2")])
def test_division_with_error(expected_exception, division, divider):
    with pytest.raises(expected_exception):
        div(division, divider)


