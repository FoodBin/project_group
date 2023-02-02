from pathlib import Path
import cash_on_hand, overheads, profit_loss


def main():
    """
    - This function will be the one that combines all modular programs
    - This function will import cash_on_hand.py, overheads.py, and profit_loss.py
    - This function does not require any parameters
    """
     
    overheads.overheads_function()
    cash_on_hand.coh_function()
    profit_loss.profitloss_function()


#Executing the final function
main()