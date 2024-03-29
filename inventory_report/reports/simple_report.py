from datetime import datetime
from collections import Counter


class SimpleReport:
    @classmethod
    def company_filter(cls, file):
        company = [item["nome_da_empresa"]for item in file]
        return Counter(company)

    @classmethod
    def generate(cls, file):
        # https://www.programiz.com/python-programming/datetime
        now = datetime.now()
        oldest_date = min([item["data_de_fabricacao"] for item in file])
        close_to_expiration = min(
            [
                item["data_de_validade"] for item in file
                if item["data_de_validade"] > now.strftime("%Y-%m-%d")
            ]
        )

        more_products = cls.company_filter(file).most_common()[0][0]

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {close_to_expiration}\n"
            f"Empresa com mais produtos: {more_products}"
        )
