from pathlib import Path
import overheads, profit_loss


def main():
    """
    - This function will be the one that combines all modular programs
    - This function will import cash_on_hand.py, overheads.py, and profit_loss.py
    - This function does not require any parameters
    """
    
    overheads.overheads_function()
    profit_loss.profitloss_function()


