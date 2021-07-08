import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

MyTx_1_Loop = pd.read_csv('MyTx-1-Loop.csv', delimiter=',')
MyTx_10_Loop = pd.read_csv('MyTx-10-Loop.csv', delimiter=',')
MyTx_50_Loop = pd.read_csv('MyTx-50-Loop.csv', delimiter=',')
MyTx_100_Loop = pd.read_csv('MyTx-100-Loop.csv', delimiter=',')
TCC_1_Loop = pd.read_csv('TCC-1-Loop.csv', delimiter=',')
TCC_10_Loop = pd.read_csv('TCC-10-Loop.csv', delimiter=',')
TCC_50_Loop = pd.read_csv('TCC-50-Loop.csv', delimiter=',')
TCC_100_Loop = pd.read_csv('TCC-100-Loop.csv', delimiter=',')


def show(loop):
    global TCC, MyTx
    if loop == 1:
        TCC = TCC_1_Loop
        MyTx = MyTx_1_Loop
    elif loop == 10:
        TCC = TCC_10_Loop
        MyTx = MyTx_10_Loop
    elif loop == 50:
        TCC = TCC_50_Loop
        MyTx = MyTx_50_Loop
    elif loop == 100:
        TCC = TCC_100_Loop
        MyTx = MyTx_100_Loop
    plotSingleModel(TCC, "TCC", loop)
    plotSingleModel(MyTx, "MyTx", loop)
    plotCmpModel(MyTx, TCC, loop)
    plotCmpModelThroughput(MyTx, TCC, loop)


def plotCmpModelThroughput(MyTx, TCC, loop):
    ymax = max(MyTx.get("throughput"))
    ymax = ymax + ymax * 0.1
    title = "Throughput Compare in " + str(loop) + " loops"
    plt.ylim(0, ymax)
    plt.xlim(-1, max(MyTx.get('thread_num')) + 5)
    # plt.suptitle("MyTx-TCC " + type + " latency compare")
    plt.grid(linestyle='-.')
    plt.xlabel('Client Thread Number')
    plt.ylabel("Throughput(TPS)")
    plt.xticks(MyTx.get('thread_num'), MyTx.get('thread_num'))
    plt.title(title)
    plt.bar(MyTx.get('thread_num') - 1, MyTx.get("throughput"), color='white', label="MyTx", align="center", width=1.5,
            edgecolor="black", linewidth=0.5)
    plt.bar(TCC.get('thread_num') + 1, TCC.get("throughput"), color='black', label="TCC", align="center", width=1.5,
            edgecolor="black", linewidth=0.5)
    plt.legend(loc='upper left')
    plt.savefig(title)
    plt.show()


def plotCmpModel(MyTx, TCC, loop):
    ymax = max(TCC.get("average"))
    ymax = ymax + ymax * 0.1
    title = "Average Latency Compare in " + str(loop) + " loops"
    plt.ylim(0, ymax)
    plt.xlim(-1, max(MyTx.get('thread_num')) + 5)
    # plt.suptitle("MyTx-TCC " + type + " latency compare")
    plt.grid(linestyle='-.')
    plt.xlabel('Client Thread Number')
    plt.ylabel("Latency(ms)")
    plt.xticks(MyTx.get('thread_num'), MyTx.get('thread_num'))
    plt.title(title)
    plt.bar(MyTx.get('thread_num') - 1, MyTx.get("average"), color='white', label="MyTx", align="center", width=1.5,
            edgecolor="black", linewidth=0.5)
    plt.bar(TCC.get('thread_num') + 1, TCC.get("average"), color='black', label="TCC", align="center", width=1.5,
            edgecolor="black", linewidth=0.5)
    plt.legend(loc='upper left')
    plt.savefig(title)
    plt.show()


def plotSingleModel(MyTx, title, loop):
    "average,median,90%line,95%line,99%line,min,max,"
    ymax = max(max(MyTx.get("average")), max(MyTx.get("median")), max(MyTx.get("90%line")), max(MyTx.get("95%line")),
               max(MyTx.get("99%line")), max(MyTx.get("min")), max(MyTx.get("max")))
    ymax = ymax + ymax * 0.1
    title = title + " Latency in " + str(loop) + " loops"
    plt.ylim(0, ymax)
    plt.xlim(0, max(MyTx.get('thread_num')) + 5)
    plt.grid()
    # plt.suptitle("MyTx-TCC " + type + " latency compare")
    plt.xlabel('Client Thread Number')
    plt.ylabel("Latency(ms)")
    plt.title(title)
    plt.plot(MyTx.get('thread_num'), MyTx.get("min"), color='black', label="min", marker='v', linestyle='-')
    plt.plot(MyTx.get('thread_num'), MyTx.get("average"), color='black', label="average", marker='o')
    plt.plot(MyTx.get('thread_num'), MyTx.get("median"), color='black', label="median", marker='x')
    plt.plot(MyTx.get('thread_num'), MyTx.get("90%line"), color='black', label="90%line", marker='^', linestyle='--')
    plt.plot(MyTx.get('thread_num'), MyTx.get("95%line"), color='black', label="95%line", marker='+')
    plt.plot(MyTx.get('thread_num'), MyTx.get("99%line"), color='black', label="99%line", marker='<', linestyle='-.')
    plt.plot(MyTx.get('thread_num'), MyTx.get("max"), color='black', label="max", marker='>', linestyle=':')
    plt.legend(loc='upper left')
    plt.savefig(title)
    plt.show()


if __name__ == '__main__':
    show(1)
    show(10)
    show(50)
    show(100)

