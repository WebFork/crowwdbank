def calculate_investment_details(invested_amount, total_profit):
    profit_percentage = (invested_amount / total_profit) * 100
    user_profit = (profit_percentage / 100) * total_profit
    return user_profit
