class TaxCalculator(object):
    def __init__(self, income, contract_type):
        if income < 0:
            raise ValueError()
        if contract_type not in ("E", "C"):
            raise ValueError("Contract type must be 'E' or 'C'")
        self.income = income
        self.contractType = contract_type

        self.socialSecurityRetirement = 0  # 9,76% of the income
        self.socialSecurityDisability = 0  # 1,5% of the income
        self.socialSecuritySickness = 0  # 2,45% of the income

        self.deductibleExpenses = 111.25
        self.healthContributionPaid = 0  # 9% of the income
        self.healthContributionDeductedFromTax = 0  # 7,75% of the income
        self.taxBeforeDeductions = 0  # advance tax = 18% PIT
        self.reducedTax = 46.33  # tax-free income 46,33 PLN
        self.taxAfterDeductions = 0
        self.taxAfterDeductionsRounded = 0

    def calculate_social_contributions(self):
        self.socialSecurityRetirement = (self.income * 9.76) / 100
        self.socialSecurityDisability = (self.income * 1.5) / 100
        self.socialSecuritySickness = (self.income * 2.45) / 100
        income_after = self.income - \
            (self.socialSecurityRetirement
             + self.socialSecurityDisability
             + self.socialSecuritySickness)
        return income_after

    def calculate_health_contributions(self, income_after):
        self.healthContributionPaid = (income_after * 9) / 100
        self.healthContributionDeductedFromTax = (income_after * 7.75) / 100

    def calculate_tax_parameters(self, deductible_expenses_fixed, income_after):
        if deductible_expenses_fixed:
            self.deductibleExpenses = 111.25
            self.reducedTax = 46.33
        else:
            self.deductibleExpenses = (income_after * 20) / 100
            self.reducedTax = 0

    def calculate_tax_base(self, income_after):
        taxed_income = income_after - self.deductibleExpenses
        taxed_income_rounded = float("{0:.0f}".format(taxed_income))
        return taxed_income, taxed_income_rounded

    def calculate_tax_before_deductions(self, income):
        self.taxBeforeDeductions = (income * 18) / 100

    def calculate_tax_after_deductions(self):
        self.taxAfterDeductions = self.taxBeforeDeductions \
            - self.healthContributionDeductedFromTax \
            - self.reducedTax
        self.taxAfterDeductionsRounded = float("{0:.0f}".format(self.taxAfterDeductions))

    def calculate_tax_summary(self, income_after):
        taxed_income, taxed_income_rounded = self.calculate_tax_base(income_after)
        self.calculate_tax_before_deductions(taxed_income_rounded)
        self.calculate_tax_after_deductions()
        return taxed_income, taxed_income_rounded

    def calculate_net_income(self):
        return self.income - \
            (self.socialSecurityRetirement
                + self.socialSecurityDisability
                + self.socialSecuritySickness
                + self.healthContributionPaid
                + self.taxAfterDeductionsRounded)
