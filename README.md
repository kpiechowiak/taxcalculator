# taxcalculator
TaxCalculator - a kata for a Clean Code exercise

The first step was improving clarity. Several variables in the original implementation had cryptic or shortened names that did not fully describe their purpose, such as t_health1, t_socialSecurity, or t_advance. I renamed them to more descriptive identifiers like healthContributionPaid, socialSecurityRetirement and taxBeforeDeductions. This makes the code self-explanatory without relying on comments. I also aligned the naming style with Python conventions - using snake_case for functions and attributes.

While restructuring the code, I also broke down the logic into small, focused methods, each responsible for a single, well-defined task. Instead of long procedures that handled multiple steps, each calculation is now isolated in its own function, which aligns with clean code principles.

I then separated concerns by splitting responsibilities into three classes: one dedicated to performing all tax calculations ("TaxCalculator"), another responsible for output formatting and printing ("TaxPrinter"), and a "Program" class that manages input and the overall application flow. This follows the single responsibility principle - each class now has a clear purpose instead of mixing logic.

The original code printed values as it calculated them, which made it difficult to test the logic without reading console output. Now the calculator only returns values, and all printing is handled separately. This change enabled me to introduce unit tests covering the key calculation paths, including both employment and civil contracts, as well as invalid input cases (negative income and unsupported contract types).