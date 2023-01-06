# DO NOT CHANGE THIS FILE
from distutils.command.config import config
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

from . import solutions

sns.set(rc={'figure.figsize':(12, 4)})
OUT_FILES = "results/"

def check_stats_solution_optional(gid, filename, corr_threshold, corr_level, stock, res):
    return_message = "Solution stats for stock " + stock + " with threshold: {} and corr_level : {} \n".format(corr_threshold, corr_level)
    
    if "small" in filename:
        sol = solutions.SMALL_FULL_SOLUTION[(corr_threshold)]
    elif "medium" in filename:
        sol = solutions.MEDIUM_FULL_SOLUTION[(corr_threshold)]
    elif "large" in filename:
        sol = solutions.LARGE_FULL_SOLUTION[(corr_threshold)]
    else:
        print("filename: {} not supported!".format(filename))
    

    error = False 
    if sol != res:    
        error = True
        return_message += "The number of connected components is not correct, expected {} but got {}.\n".format(sol, res)
    else:
        return_message += " IS CORRECT, Congratulations!"

    return error, return_message

def check_stats_solution(gid, filename, corr_threshold, corr_level, stock, res):
    return_message = "Solution stats for stock " + stock + " with threshold: {} and corr_level : {} \n".format(corr_threshold, corr_level)
    
    if "small" in filename:
        sol = solutions.SMALL_FULL_SOLUTION[(corr_threshold, stock, corr_level)]
    elif "medium" in filename:
        sol = solutions.MEDIUM_FULL_SOLUTION[(corr_threshold, stock, corr_level)]
    elif "large" in filename:
        sol = solutions.LARGE_FULL_SOLUTION[(corr_threshold, stock, corr_level)]
    else:
        print("filename: {} not supported!".format(filename))
         
    error = False 
    if sol != res:    
        error = True 
        if len(sol) != len(res):
            return_message += "The number of correlated stocks is not correct, expected {} but got {}.\n".format(len(sol), len(res))
        else:
            return_message += "The correlated stocks are not correct, expected {} but got {}.\n".format(sol, res)    
    else:
        return_message += " IS CORRECT, Congratulations!"

    return error, return_message



def check_timeseries_solution(group_id : int, stock: str, days: list, prices: list, plot: bool = True) -> str:
    """
    The method check the results of days, prices, and plot also the target/output

    :param group_id : the group id (unique) for each group
    :param stock: the name of the stock to print, it should be inside the dataset file
    :param days: a list of (ordered) days to validate/plot
    :param prices: a list of prices (ordered) to validate/plot
    :param plot: wheter plot or not the results
    :return: a string with the successfull or error message
    """
    return_message = "Solution time-series for stock " + stock + ":\n"
    soldays, solprices = solutions.TIME_SERIES_SOLUTION[stock]
    if len(days) != len(prices):
        return_message += "The two input lists have different len. Days has len {} while prices has len {} \n".format(str(len(days)),
                                                                                                   str(len(prices)))
    elif len(soldays) != len(days) or len(solprices) != len(prices):
        if len(soldays) != len(days):
            return_message += "Day lists have different len. Days should have len {} while got a list with {} elements \n".format(str(len(soldays)),
                                                                                                       str(len(days)))
        if len(solprices) != len(prices):
            return_message += "Price lists have different len. Prices should have len {} while got a list with {} elements \n".format(str(len(solprices)),
                                                                                                       str(len(prices)))
    elif soldays != days or solprices != [round(x, 2) for x in prices]:
        if soldays != days:
            return_message += "The list of days is not correct, expected {} \n - but got {} \n\n".format(str(soldays), str(days))
        if solprices != [round(x, 2) for x in prices]:
            return_message += "The list of prices is not correct, expected {} \n - but got {} \n\n".format(str(solprices), str(prices))
    else:
        return_message += " IS CORRECT, Congratulations!"

    print("Plotting results...")
    if plot:
        plot_stock_timeseries(stock, days, prices, OUT_FILES + "proj_v2_" + stock + "_result_gid_" + str(group_id) +".png")

    return return_message

def check_query_solution(dataset_file: str, group_id : int, k : int, target_price : float, res : list, plot=True):
    """

    :param group_id : the group id (unique) for each group
    :param k: the maximum number of stock to return
    :param target_price: the price we are looking for
    :param res: the results, a list of ordered tuple [(stock, first_day_with_target_price), ...]
    :return: a string with the successfull or error message
    """
    return_message = "Solution query for K:{} and Price-Target:{} \n".format(k, target_price)
    out_res = solutions.FULL_SOLUTION[(k, target_price)]
    if out_res != res:
        return_message += "The list of stocks is not correct, expected {} \n - but got {} \n\n".format(str(out_res), str(res))
    else:
        return_message += " IS CORRECT, Congratulations!"

    print("Plotting results...")
    if plot:
        stocks_to_plot = [s[0] for s in res]
        print(stocks_to_plot)
        stock_day_dict = {s[0] : s[1] for s in res}
        plot_solution(dataset_file, stocks_to_plot, stock_day_dict, OUT_FILES + "proj_v3_k" + str(k) + "_pr_" + str(target_price) + "_result_gid_" + str(group_id) +".png")

    return return_message


def plot_stock_stats(dataset_file: str, stock: str, min: float, max: float, mean: float, outfile : str = None) -> None:
    """
    The method plots the min, max, mean and prices of the input stock

    :param dataset_file: the dataset file to use
    :param stock: the name of the stock to print, it should be inside the dataset file
    :param min: the min price value observed
    :param max: the max price value
    :param mean: the mean price for the overall time-series
    :param outfile: the file query to save the result image, If None the code shows the results on video.
    :return: None
    """
    df = pd.read_csv(dataset_file)
    df.columns = ["Stock","Day","Price","Volume"]


    f, ax = plt.subplots()
    assert stock in df.Stock.unique(), "The input stock: {} is not in the dataset file".format(stock)
    stock_df = df[df["Stock"] == stock]
    stock_df = stock_df.sort_values(by=["Day"])
    stock_df = stock_df.set_index("Day")
    ax.plot(stock_df['Price'], label=stock, color="b")
    ax.axhline(y=min, color="g", label="Min")
    ax.axhline(y=max, color="r", label="Max")
    ax.axhline(y=mean, color="black", label="Mean")

    ax.legend()
    ax.set_ylabel('Price ($)')
    ax.set_xlabel('Days')

    plt.tight_layout()
    if outfile is not None:
        plt.savefig(outfile)
    else:
        plt.show()

    plt.clf()
    plt.close()


def plot_stock_timeseries(stock: str, days: list, prices : list, outfile : str = None) -> None:
    """
    The method plots the input time-series data

    :param stock: the name of the stock to print, it should be inside the dataset file
    :param days: the list of ordered days to plot
    :param prices: the list of orders price to plot
    :param outfile: the file query to save the result image, If None the code shows the results on video.
    :return: None
    """

    f, ax = plt.subplots()
    ax.plot(days, prices, label=stock, color="b")
    #ax.set_xticks(np.arange(len(days)))
    #ax.set_xticklabels(days)

    ax.legend()
    ax.set_ylabel('Price ($)')
    ax.set_xlabel('Days')

    plt.tight_layout()
    if outfile is not None:
        plt.savefig(outfile)
    else:
        plt.show()

    plt.clf()
    plt.close()


def plot_solution(dataset_file : str, stocks_to_plot : list, stock_day_dict : dict, outfile : str = None) -> None:
    """
    The function plots the results of your query

    :param dataset_file: the dataset file to use
    :param stocks_to_plot: the ordered list of stocks to print
    :param stock_day_dict: a dictionary with stock name as key and the day of the price change as value
    :param outfile: the file query to save the result image, If None the code shows the results on video.
    :return:
    """
    circle_rad = 15  # This is the radius, in points

    # we can't plot more than 5 symbols for visualization
    if len(stocks_to_plot) > 6:
        stocks_to_plot = stocks_to_plot[:5]

    f, (ax, ax2) = plt.subplots(1, 2, gridspec_kw={'width_ratios': [3, 1]})
    df = pd.read_csv(dataset_file)
    df.columns = ["Stock","Day","Price","Volume"]
    df = df.sort_values(by=["Stock", "Day"])
    vol_df = {}
    for stock in stocks_to_plot:
        stock_df = df[df["Stock"] == stock]
        stock_df = stock_df.set_index("Day")
        p = ax.plot(stock_df['Price'], label=stock)
        day_of_price_change = stock_day_dict[stock]
        ax.plot([day_of_price_change], [float(stock_df.loc[day_of_price_change, "Price"])], 'o',
                ms=circle_rad*2, mec=p[0].get_color(), mfc='none', mew=2)

        vol_df[stock] = (stock_df["Volume"].mean(), p[0].get_color())


    # plot volumnes
    names, values, colors = [], [], []
    for n in vol_df.keys():
        names += [n]
        values += [vol_df.get(n)[0]]
        colors += [vol_df.get(n)[1]]

    ax2.bar(np.arange(len(names)), values, color=colors)
    ax2.set_xticks(np.arange(len(names)))
    ax2.set_xticklabels(names)
    ax.legend()
    ax2.set_ylabel('Volume')
    ax.set_ylabel('Price ($)')
    ax.set_xlabel('Days')

    plt.tight_layout()
    if outfile is not None:
        plt.savefig(outfile)
    else:
        plt.show()

    plt.clf()
    plt.close()