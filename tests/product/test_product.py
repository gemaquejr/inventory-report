from inventory_report.inventory.product import Product


def test_cria_produto():
    mockProduct = Product(
        123,
        "newspaper",
        "gemaque's Diary",
        "15/01/2023",
        "16/01/2023",
        123321,
        "seco e conservado",
    )

    assert mockProduct.id == 123
    assert mockProduct.nome_da_empresa == "gemaque's Diary"
    assert mockProduct.nome_do_produto == "newspaper"
    assert mockProduct.data_de_fabricacao == "15/01/2023"
    assert mockProduct.data_de_validade == "16/01/2023"
    assert mockProduct.numero_de_serie == 123321
    assert mockProduct.instrucoes_de_armazenamento == "seco e conservado"
