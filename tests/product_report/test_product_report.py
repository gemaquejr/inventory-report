from inventory_report.inventory.product import Product


def test_relatorio_produto():
    mockProduct = Product(
        123,
        "newspaper",
        "gemaque's Diary",
        "15/01/2023",
        "16/01/2023",
        123321,
        "seco e conservado",
    )

    assert repr(mockProduct) == (
        f"O produto {mockProduct.nome_do_produto}"
        f" fabricado em {mockProduct.data_de_fabricacao}"
        f" por {mockProduct.nome_da_empresa}"
        f" com validade até {mockProduct.data_de_validade}"
        f" precisa ser armazenado {mockProduct.instrucoes_de_armazenamento}."
    )
