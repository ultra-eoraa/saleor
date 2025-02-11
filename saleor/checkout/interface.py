from dataclasses import dataclass

from prices import Money, TaxedMoney


@dataclass
class TaxedPricesData:
    """Store a prices data with applied taxes.

    'price' includes discount from sale if any valid exists.
    'price_with_discounts' includes voucher discount and sale discount if any valid
    exists.
    'undiscounted_price' is a price without any sale and voucher.
    """

    undiscounted_price: TaxedMoney
    price_with_discounts: TaxedMoney
    price_with_sale: TaxedMoney


@dataclass
class PricesData:
    """Store a prices data without applied taxes.

    'price' includes discount from sale if any valid exists.
    'price_with_discounts' includes voucher discount and sale discount if any valid
    exists.
    'undiscounted_price' is a price without any sale and voucher.
    """

    undiscounted_price: Money
    price_with_discounts: Money
    price_with_sale: Money
