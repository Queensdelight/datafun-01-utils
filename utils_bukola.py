''' This module provides a reusable byline for the author's services. 
Company name: 'Analytics and More'
Analyst in charge: 'Bukola Adeniyan'
'''

import math
import statistics

def main():
    
    #define variables
    company_name: str = 'Queensdelight Inc'
    company_description: str= 'Giving life a meaning'
    company_founding_year: int = 2011
    company_city: str = 'Lincoln'
    company_state: str = 'Nebraska'
    company_number_employes: int = 1
    company_offers_benefits: bool = True
    products_offered:list = ['motivations', 'books', 'leadership conferences']
    product_prices: list = [500, 1000, 1500]
    count_active_projects: int = 5
    has_international_presence: bool = True
    average_client_satisfaction: float = 5.0
    satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]


#Multiline string with byline using f-string formatting
    byline: str =f"""
    Name: {company_name}
    Description: {company_description}
    Founding Year: {company_founding_year}
    City: {company_city}
    State: {company_state}
    Number of Employees: {company_number_employes}
    Benefits Availabilty: {company_offers_benefits}
    Products Offered: {products_offered}
    Product Prices: {product_prices}
    Active Projects: {count_active_projects}
    Internatinal Presence: {has_international_presence}
    Clients Satisfaction: {average_client_satisfaction}
    Satisfaction Score: {satisfaction_scores}
    """


    stats_string: str = f"""
    Smallest: {satisfaction_scores}
    Largest: {satisfaction_scores}
    Total: {satisfaction_scores}
    Count: {satisfaction_scores}
    Mean: {satisfaction_scores}
    Mode: {satisfaction_scores}
    Median: {satisfaction_scores}
    Standard Deviation: {satisfaction_scores}
    
    """

    byline: str = f"""
    """
   
    print(byline)






if __name__ == '__main__':
    main()


