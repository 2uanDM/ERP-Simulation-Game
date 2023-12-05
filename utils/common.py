import polars as pl


def product_info() -> pl.DataFrame:
    data = [{'Code': 1, 'Name': '500g Nut Muesli'},
            {'Code': 2, 'Name': '500g Blueberry Muesli'},
            {'Code': 3, 'Name': '500g Strawberry Muesli'},
            {'Code': 4, 'Name': '500g Raisin Muesli'},
            {'Code': 5, 'Name': '500g Original Muesli'},
            {'Code': 6, 'Name': '500g Mixed Muesli'},
            {'Code': 11, 'Name': '1kg Nut Muesli'},
            {'Code': 12, 'Name': '1kg Blueberry Muesli'},
            {'Code': 13, 'Name': '1kg Strawberry Muesli'},
            {'Code': 14, 'Name': '1kg Raisin Muesli'},
            {'Code': 15, 'Name': '1kg Original Muesli'},
            {'Code': 16, 'Name': '1kg Mixed Muesli'},]

    return pl.DataFrame(data)
