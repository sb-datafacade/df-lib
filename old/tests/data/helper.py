class ProductProperties:
    def __init__(self, price, base_sale_number, sales_drop_trend,
                 case_distribution, marketing_campaign_distribution, competing_price_drop_rate=1):
        self.price = price
        self.base_sale_number = base_sale_number
        self.sales_drop_trend = sales_drop_trend
        self.case_distribution = case_distribution
        self.marketing_campaign_distribution = marketing_campaign_distribution
        self.competing_price_drop_rate = competing_price_drop_rate
