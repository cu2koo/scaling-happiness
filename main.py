import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Create non-existing paths
def createPath(path):
    if not os.path.exists(path):
        os.makedirs(path)


def createBarChart(dest, csv, yLabel, title, name):
    df = pd.read_csv("data/" + csv, index_col="Company")
    x = np.arange(len(df.axes[1]))
    width = 0.1
    _, ax = plt.subplots()
    ax.bar(
        x - 1.5 * width,
        df.values[0],
        width,
        label="Unternehmen 1",
    )
    ax.bar(
        x - 0.5 * width,
        df.values[1],
        width,
        label="Unternehmen 2",
    )
    ax.bar(
        x + 0.5 * width,
        df.values[2],
        width,
        label="Unternehmen 3",
    )
    ax.bar(
        x + 1.5 * width,
        df.values[3],
        width,
        label="Unternehmen 4",
    )
    ax.set_ylabel(yLabel, labelpad=10.0)
    ax.set_title(title)
    ax.set_ylim(ymin=0)
    ax.set_xticks(x, df.axes[1])
    ax.legend()
    plt.savefig(dest + "/" + name)


def createLineChart(dest, csv, yLabel, title, name):
    df = pd.read_csv("data/" + csv, index_col="Costs per Product")
    _, ax = plt.subplots()
    i = 0
    for c in df.axes[0]:
        ax.plot(df.axes[1], df.values[i], label=c)
        i += 1
    ax.set_ylabel(yLabel, labelpad=10.0)
    ax.set_title(title)
    ax.set_ylim(ymin=0)
    ax.legend()
    plt.savefig(dest + "/" + name)


def createSalesGraph(dest):
    createBarChart(
        dest,
        "sales.csv",
        "Umsatzerlös (MEUR)",
        "Umsatzerlöse nach Unternehmen",
        "sales",
    )


def createOperatingIncomeGraph(dest):
    createBarChart(
        dest,
        "operating_income.csv",
        "Betriebsergebnis (MEUR)",
        "Betriebsergebnisse nach Unternehmen",
        "operating_income",
    )


def createStockPriceGraph(dest):
    df = pd.read_csv("data/" + "stock_price.csv", index_col="Company")
    _, ax = plt.subplots()
    i = 0
    for c in df.axes[0]:
        thickness = 1.0
        if c == "U2":
            thickness = 2.0
        ax.plot(df.axes[1], df.values[i], label=c, linewidth=thickness)
        i += 1
    ax.set_ylabel("Aktienkurs (EUR / Aktie)", labelpad=10.0)
    ax.set_title("Aktienkurse nach Unternehmen")
    ax.set_ylim(ymin=0)
    ax.legend()
    plt.savefig(dest + "/" + "stock_price")


def createSalesCategorizedGraph(dest):
    df = pd.read_csv("data/" + "sales_categorized.csv", index_col="Product")
    _, ax = plt.subplots()
    x = np.arange(len(df.axes[1]))
    width = 0.5
    bottom = np.zeros(len(df.axes[1]))
    i = 0
    for c in df.axes[0]:
        ax.bar(x, df.values[i], width, label=c, bottom=bottom)
        bottom += df.values[i]
        i += 1
    ax.set_ylabel("Umsatzerlös (MEUR)", labelpad=10.0)
    ax.set_title("Umsatzerlöse von Unternehmen 2 nach Produkten")
    ax.set_ylim(ymin=0)
    ax.set_xticks(x, df.axes[1])
    ax.legend()
    plt.savefig(dest + "/" + "sales_categorized")


def createCostPerProductGraph(dest):
    createLineChart(
        dest,
        "cost_per_product_copy_i.csv",
        "Kosten (EUR / Stück)",
        "Herstell- und Selbstkosten von Unternehmen 2 für COPY I",
        "cost_per_product_copy_i",
    )
    createLineChart(
        dest,
        "cost_per_product_copy_ii.csv",
        "Kosten (EUR / Stück)",
        "Selbstkosten von Unternehmen 2 für COPY II",
        "cost_per_product_copy_ii",
    )


# Run script
def main():
    dest = "result"
    createPath(dest)
    createSalesGraph(dest)
    createOperatingIncomeGraph(dest)
    createStockPriceGraph(dest)
    createSalesCategorizedGraph(dest)
    createCostPerProductGraph(dest)


if __name__ == "__main__":
    main()
