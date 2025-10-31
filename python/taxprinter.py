class TaxPrinter:
    def print_income(self, income):
        print("Income", income)

    def print_social_contributions(self, tax_case, income_after):
        print("Social security tax: " + "{0:.2f}".format(tax_case.socialSecurityRetirement))
        print("Health social security tax: " + "{0:.2f}".format(tax_case.socialSecurityDisability))
        print("Sickness social security tax  " + "{0:.2f}".format(tax_case.socialSecuritySickness))
        print("Income for calculating health security tax: ", income_after)

    def print_health_contributions(self, tax_case):
        print("Health security tax: 9% = " + "{0:.2f}".format(tax_case.healthContributionPaid)
              + " 7,75% = " + "{0:.2f}".format(tax_case.healthContributionDeductedFromTax))

    def print_tax_parameters(self, tax_case):
        print("Tax deductible expenses = ", tax_case.deductibleExpenses)

    def print_tax_base(self, taxed_income, taxed_income_rounded):
        print("Income to be taxed: ", taxed_income, " rounded: " + "{0:.0f}".format(taxed_income_rounded))

    def print_tax_before_deductions(self, tax_case, deductible_expenses_fixed):
        print("Advance tax 18% =", tax_case.taxBeforeDeductions)
        if deductible_expenses_fixed:
            taxPaid = tax_case.taxBeforeDeductions - tax_case.reducedTax
            print("Reduced tax = " + "{0:.2f}".format(taxPaid))
        else:
            taxPaid = tax_case.taxBeforeDeductions
            print("Already paid tax = " + "{0:.2f}".format(taxPaid))

    def print_tax_after_deductions(self, tax_case, deductible_expenses_fixed):
        label = "Advance paid tax " if deductible_expenses_fixed \
            else "Advance tax "
        print(label + "{0:.2f}".format(tax_case.taxAfterDeductions)
              + " rounded " + "{0:.0f}".format(tax_case.taxAfterDeductionsRounded))

    def print_tax_summary(self, tax_case, deductible_expenses_fixed, taxed_income, taxed_income_rounded):
        self.print_tax_base(taxed_income, taxed_income_rounded)
        self.print_tax_before_deductions(tax_case, deductible_expenses_fixed)
        self.print_tax_after_deductions(tax_case, deductible_expenses_fixed)

    def print_net_income(self, net_income):
        print("\nNet income = " + "{0:.2f}".format(net_income))
