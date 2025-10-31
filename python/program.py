from taxcalculator import TaxCalculator
from taxprinter import TaxPrinter


class Program:
    def __init__(self):
        self.calculator = None
        self.printer = TaxPrinter()

    def get_users_input(self):
        try:
            income = float(input("Enter income: "))
            contract_type = input("Contract Type: (E)mployment, (C)ivil")[0].upper()
            self.calculator = TaxCalculator(income, contract_type)
            self.printer = TaxPrinter()
            return True
        except ValueError:
            print("Incorrect")
            return False

    def process_employment_contract(self):
        print("EMPLOYMENT")
        self.calculate_and_display_full_summary(deductible_expenses_fixed=True)

    def process_civil_contract(self):
        print("CIVIL")
        self.calculate_and_display_full_summary(deductible_expenses_fixed=False)

    def calculate_and_display_full_summary(self, deductible_expenses_fixed=True):
        calc = self.calculator
        pr = self.printer

        pr.print_income(calc.income)

        income_after_social_contributions = calc.calculate_social_contributions()
        pr.print_social_contributions(calc, income_after_social_contributions)

        calc.calculate_health_contributions(income_after_social_contributions)
        pr.print_health_contributions(calc)

        calc.calculate_tax_parameters(deductible_expenses_fixed, income_after_social_contributions)
        pr.print_tax_parameters(calc)

        taxed_income, taxed_income_rounded = calc.calculate_tax_summary(income_after_social_contributions)
        pr.print_tax_summary(calc, deductible_expenses_fixed, taxed_income, taxed_income_rounded)

        net_income = calc.calculate_net_income()
        pr.print_net_income(net_income)

    def run(self):
        if not self.get_users_input():
            return
        if self.calculator.contractType == "E":
            self.process_employment_contract()
        elif self.calculator.contractType == "C":
            self.process_civil_contract()
        else:
            print("Unknown type of contract!")
