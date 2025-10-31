import pytest
from taxcalculator import TaxCalculator


@pytest.fixture
def calculate_employment():
    calc = TaxCalculator(1000, "E")
    return calc


def test_social_contributions(calculate_employment):
    income_after = calculate_employment.calculate_social_contributions()
    assert round(calculate_employment.socialSecurityRetirement, 2) == 97.60
    assert round(calculate_employment.socialSecurityDisability, 2) == 15.00
    assert round(calculate_employment.socialSecuritySickness, 2) == 24.50
    assert round(income_after, 2) == 862.90


def test_health_contributions(calculate_employment):
    income_after = calculate_employment.calculate_social_contributions()
    calculate_employment.calculate_health_contributions(income_after)
    assert round(calculate_employment.healthContributionPaid, 2) == 77.66
    assert round(calculate_employment.healthContributionDeductedFromTax, 2) == 66.87


def test_tax_parameters(calculate_employment):
    income_after = calculate_employment.calculate_social_contributions()
    calculate_employment.calculate_tax_parameters(True, income_after)
    assert calculate_employment.deductibleExpenses == 111.25
    assert calculate_employment.reducedTax == 46.33


def test_tax_summary_employment(calculate_employment):
    income_after = calculate_employment.calculate_social_contributions()
    calculate_employment.calculate_health_contributions(income_after)
    calculate_employment.calculate_tax_parameters(True, income_after)
    taxed, taxed_rounded = calculate_employment.calculate_tax_summary(income_after)

    assert round(taxed, 2) == 751.65
    assert taxed_rounded == 752
    assert round(calculate_employment.taxBeforeDeductions, 2) == 135.36
    assert round(calculate_employment.taxAfterDeductions, 2) == 22.16


def test_net_income_employment(calculate_employment):
    income_after = calculate_employment.calculate_social_contributions()
    calculate_employment.calculate_health_contributions(income_after)
    calculate_employment.calculate_tax_parameters(True, income_after)
    calculate_employment.calculate_tax_summary(income_after)
    net = calculate_employment.calculate_net_income()

    assert round(net, 2) == 763.24


def test_tax_summary_civil():
    calc = TaxCalculator(1000, "C")

    income_after = calc.calculate_social_contributions()
    calc.calculate_health_contributions(income_after)
    calc.calculate_tax_parameters(False, income_after)

    taxed, taxed_rounded = calc.calculate_tax_summary(income_after)

    assert round(income_after, 2) == 862.90
    assert round(calc.deductibleExpenses, 2) == 172.58

    assert round(taxed, 2) == 690.32
    assert taxed_rounded == 690

    assert round(calc.taxBeforeDeductions, 2) == 124.20
    assert round(calc.taxAfterDeductions, 2) == 57.33


def test_net_income_civil():
    calc = TaxCalculator(1000, "C")

    income_after = calc.calculate_social_contributions()
    calc.calculate_health_contributions(income_after)
    calc.calculate_tax_parameters(False, income_after)
    calc.calculate_tax_summary(income_after)

    net = calc.calculate_net_income()

    assert round(net, 2) == 728.24


def test_negative_income():
    with pytest.raises(ValueError):
        TaxCalculator(-1000, "E")


def test_invalid_contract_type():
    with pytest.raises(ValueError):
        TaxCalculator(1000, "X")
