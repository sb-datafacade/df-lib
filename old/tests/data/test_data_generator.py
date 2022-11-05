import csv
from datetime import date, timedelta
import random
import numpy as np

from tests.data.helper import ProductProperties

start_date = date(2022, 1, 1)
end_date = date(2022, 6, 30)

from datetime import date, timedelta

sale_count_by_month_Product1 = [97, 100, 99, 90, 75, 40]  # Bad Review
bad_case_count_by_month_Product1 = [5, 50, 100, 200, 400, 1000]

sale_count_by_month_Product2 = [100, 95, 90, 87, 75, 60]  # Marketing Campaign stopped and dropped over the period
marketing_campaign_stopped = [150, 180, 50, 40, 30, 30]
marketing_campaign_normal = [150, 150, 150, 150, 150, 150]

sale_count_by_month_Product3 = [100, 95, 90, 85, 80, 75]  # Competitor kept decreasing price
sale_count_by_month_Product4 = [97, 100, 99, 80, 55,
                                20]  # Increased number of bad product review and competing product decreased the price
sale_count_by_month_Product5 = [97, 100, 103, 106, 107, 110]  # All okay
sale_count_by_month_Product6 = [97, 100, 103, 106, 107, 110]  # All okay
sale_count_by_month_Product7 = [97, 100, 103, 106, 107, 110]  # All okay
sale_count_by_month_Product8 = [97, 100, 103, 106, 107, 110]  # All okay
sale_count_by_month_Product9 = [97, 100, 103, 106, 107, 110]  # All okay
sale_count_by_month_Product10 = [97, 100, 103, 106, 107, 110]  # All okay
normal_cases = [1, 1, 1, 1, 1, 1]

product_properties_map = {
    "Product1": ProductProperties(price=88, base_sale_number=1000, sales_drop_trend=sale_count_by_month_Product1,
                                  case_distribution=bad_case_count_by_month_Product1,
                                  marketing_campaign_distribution=marketing_campaign_normal),
    "Product2": ProductProperties(price=67, base_sale_number=500, sales_drop_trend=sale_count_by_month_Product2,
                                  case_distribution=normal_cases,
                                  marketing_campaign_distribution=marketing_campaign_stopped),
    "Product3": ProductProperties(price=80, base_sale_number=600, sales_drop_trend=sale_count_by_month_Product3,
                                  case_distribution=normal_cases,
                                  marketing_campaign_distribution=marketing_campaign_normal,
                                  competing_price_drop_rate=0.98),
    "Product4": ProductProperties(price=40, base_sale_number=400, sales_drop_trend=sale_count_by_month_Product4,
                                  case_distribution=normal_cases,
                                  marketing_campaign_distribution=marketing_campaign_normal,
                                  competing_price_drop_rate=0.98),
    "Product5": ProductProperties(price=60, base_sale_number=300, sales_drop_trend=sale_count_by_month_Product5,
                                  case_distribution=normal_cases,
                                  marketing_campaign_distribution=marketing_campaign_normal),
    "Product6": ProductProperties(price=99, base_sale_number=900, sales_drop_trend=sale_count_by_month_Product6,
                                  case_distribution=normal_cases,
                                  marketing_campaign_distribution=marketing_campaign_normal),
    "Product7": ProductProperties(price=100, base_sale_number=600, sales_drop_trend=sale_count_by_month_Product7,
                                  case_distribution=normal_cases,
                                  marketing_campaign_distribution=marketing_campaign_normal),
    "Product8": ProductProperties(price=66, base_sale_number=450, sales_drop_trend=sale_count_by_month_Product8,
                                  case_distribution=normal_cases,
                                  marketing_campaign_distribution=marketing_campaign_normal),
    "Product9": ProductProperties(price=55, base_sale_number=770, sales_drop_trend=sale_count_by_month_Product9,
                                  case_distribution=normal_cases,
                                  marketing_campaign_distribution=marketing_campaign_normal),
    "Product10": ProductProperties(price=78, base_sale_number=850, sales_drop_trend=sale_count_by_month_Product10,
                                   case_distribution=normal_cases,
                                   marketing_campaign_distribution=marketing_campaign_normal),
}
sales_reps = ["Nancy", "Sam", "Raj", "Paul", "David"]
regions = ["US_WA", "US_CA", "US_NY", "US_OR"]
issue_types = ["Issue1", "Issue2", "Issue3", "Issue4", "Issue5", "Issue6"]
campaign_types = ["email", "google_ads", "facebook_ads", "other_ads"]

"""
    # id_sales => Incremental (1-100000)
    # id_customer => Random integer from range (1-10000)
    # sales_rep => Random selection of a fixed set of string
    # id_product => Random selection of a fixes set of string
    # dim_region => Random Selection from a fixed set of string
    # m_amound => Decima ?
    # ds => range for a year
    Loop through date range
        Loop through all product -
        figure out number sales on that day. From the total montly sales and randomize it. Sort it to decreaseing order.
        Randomly choose sales person, customer
        Fixed price per product.
"""


def calculate_randomized_items_per_day(trend, baseline):
    month_count = 0
    random_items_by_day_list = []
    total_month = len(trend)
    for single_date in month_range(start_date, end_date):
        assert month_count < total_month
        total_in_month = int(
            (trend[month_count] * baseline))
        max_per_day_sold = int(total_in_month / 15) + 1
        min_per_day_sold = int(total_in_month / 60) + 1
        x = np.random.randint(min_per_day_sold, max_per_day_sold, size=(30,))
        while sum(x) > total_in_month*1.2 or sum(x) < total_in_month*0.8:
            x = np.random.randint(min_per_day_sold, max_per_day_sold, size=(30,))
        # Sample total_in_month in a random order
        # x.sort()
        random_items_by_day_list.extend(x)
        month_count += 1
    result = {}
    day_count = 0
    max_perday_sold = len(random_items_by_day_list)
    for single_date in date_range(start_date, end_date):
        ds = single_date.strftime("%Y-%m-%d")
        if day_count >= max_perday_sold:
            result[ds] = random_items_by_day_list[max_perday_sold - 1]
            continue
        result[ds] = random_items_by_day_list[day_count]
        day_count += 1
    return result


def test_generate_sales_table():
    data, header = generate_data_for_product_sales()
    file_name = 'raw_fct_sales.csv'
    create_file(data, file_name, header)


def test_generate_case_table():
    data, header = generate_data_for_product_cases()
    file_name = 'raw_customer_support_cases.csv'
    create_file(data, file_name, header)


def test_generate_marketing_campaign_table():
    data = generate_data_for_marketing_campaign(get_campaign_distribution, get_row=set_campaign_specific_rows)
    file_name = 'raw_fct_campaign.csv'
    header = ["id_campaign", "dim_campaign_type", "dim_region", "dim_product", "ds"]
    create_file(data, file_name, header)


def test_generate_competing_table():
    data = generate_data_for_competing_product()
    file_name = 'raw_fct_competing_product.csv'
    header = ["dim_product", "m_price", "m_competing_price", "dim_region", "ds"]
    create_file(data, file_name, header)


def get_campaign_distribution(product_properties):
    return product_properties.marketing_campaign_distribution


def set_campaign_specific_rows(ds, id, product):
    campaign_type = random.choice(campaign_types)
    region = random.choice(regions)
    row = [id, campaign_type, region, product, ds]
    return row


def generate_data_for_competing_product():
    data = []
    for product in product_properties_map.keys():
        product_properties = product_properties_map.get(product)
        price = product_properties.price
        competing_price = price
        competing_price_rate_of_change = product_properties.competing_price_drop_rate
        region = random.choice(regions)
        # TODO: Randomly change sales per day. Need to start and end date to product properties.
        for single_date in date_range(start_date, end_date):
            competing_price = competing_price*competing_price_rate_of_change
            ds = single_date.strftime("%Y-%m-%d")
            row = [product, price, competing_price, region, ds]
            data.append(row)
    return data


def generate_data_for_marketing_campaign(distribution, get_row):
    data = []
    id = 1
    for product in product_properties_map.keys():
        product_properties = product_properties_map.get(product)
        # TODO: Randomly change sales per day. Need to start and end date to product properties.
        items_per_day = calculate_randomized_items_per_day(distribution(product_properties), 2)
        for single_date in date_range(start_date, end_date):
            ds = single_date.strftime("%Y-%m-%d")
            number_of_sales_per_day = items_per_day.get(ds)
            for _ in range(1, number_of_sales_per_day):
                row = get_row(ds, id, product)
                id += 1
                data.append(row)
    return data


def generate_data_for_product_cases():
    header = ["id_case", "id_agent", "id_customer", "dim_issue_type", "dim_product", "dim_region", "ds"]
    data = []
    case_id = 1
    for product in product_properties_map.keys():
        product_properties = product_properties_map.get(product)
        # TODO: Randomly change sales per day. Need to start and end date to product properties.
        items_per_day = calculate_randomized_items_per_day(product_properties.case_distribution, 100)
        for single_date in date_range(start_date, end_date):
            ds = single_date.strftime("%Y-%m-%d")
            number_of_sales_per_day = items_per_day.get(ds)
            for _ in range(1, number_of_sales_per_day):
                customer_id = random.randint(1, 10000)
                customer_care_agent = random.choice(sales_reps)
                region = random.choice(regions)
                issue_type = random.choice(issue_types)
                row = [case_id, customer_care_agent, customer_id, issue_type, product, region, ds]
                case_id += 1
                data.append(row)
    return data, header


def generate_data_for_product_sales():
    header = ["id_sales", "m_amount", "id_customer", "id_sales_rep", "dim_product", "dim_region", "ds"]
    data = []
    sales_id = 1
    for product in product_properties_map.keys():
        product_properties = product_properties_map.get(product)
        # TODO: Randomly change sales per day. Need to start and end date to product properties.
        sales_per_day = calculate_randomized_items_per_day(product_properties.sales_drop_trend,
                                                           product_properties.base_sale_number)
        for single_date in date_range(start_date, end_date):
            ds = single_date.strftime("%Y-%m-%d")
            number_of_sales_per_day = sales_per_day.get(ds)
            for _ in range(1, number_of_sales_per_day):
                customer_id = random.randint(1, 10000)
                sales_rep = random.choice(sales_reps)
                region = random.choice(regions)
                amount = product_properties.price
                row = [sales_id, amount, customer_id, sales_rep, product, region, ds]
                sales_id += 1
                data.append(row)
    return data, header


def create_file(data, file_name, header):
    with open(file_name, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(data)


def date_range(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def month_range(start_date, end_date):
    for n in range(int((end_date - start_date).days / 30)):
        yield start_date + timedelta(n)

# var = random.sample(range(1, 10000), 20)
# var.sort()
