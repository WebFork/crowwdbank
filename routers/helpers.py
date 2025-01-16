def calculate_investment_details(invested_amount, total_raised_amount):

    total_profit = total_raised_amount - invested_amount
    
    profit_percentage = (invested_amount / total_raised_amount) * 100
    
    user_profit = (profit_percentage / 100) * total_profit
    
    return total_profit, profit_percentage, user_profit
