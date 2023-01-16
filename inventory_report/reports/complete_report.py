from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, file):
        report = super().generate(file)
        stock_products = cls.company_filter(file)
        report += "\nProdutos estocados por empresa:\n"
        for company, times in stock_products.items():
            report += f"- {company}: {times}\n"

        return report
