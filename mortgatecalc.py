


def convert_interest_rate(apr):
    return apr * .01 / 12


def mortgage(homecost, apr):
    interest_rate = convert_interest_rate(apr)
    term_fifteen = (15 * 12)
    term_thirty = (30 * 12)
    thirty_discount_rate = (interest_rate * ((1 + interest_rate) ** term_thirty)) / \
                                          (((1 + interest_rate) ** term_thirty) - 1)

    fifteen_discount_rate = (interest_rate * ((1 + interest_rate) ** term_fifteen)) / \
                                          (((1 + interest_rate) ** term_fifteen) - 1)
    fifteen_year = homecost * fifteen_discount_rate
    thirty_year = homecost * thirty_discount_rate
    return("15-Year Mortgage Monthly Payment is ${:.2f}\n".format(fifteen_year) +
           "30-Year Mortgage Monthly Payment is ${:.2f}".format(thirty_year))


if __name__ == '__main__':
    # code to be run directly
