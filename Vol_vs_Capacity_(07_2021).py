import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def print_graph_of_cycl3(num1, num2):
    for i in range(num1, num2):
        df=pd.read_csv('C:/Users/jayra/Desktop/split/a.csv')
        #df1=df[df["Cycle_Index"] <= 10]
        df1 = df[df["Cycle_Index"] == i]
        df2 = df1.loc[(df1["Current (A)"] != 0) & (df1["Charge_Capacity (Ah)"] != 0)]
        df3 = df1.loc[(df1["Current (A)"] != 0) & (df1["Discharge_Capacity (Ah)"] != 0)]

        fig = plt.gcf()
        fig.set_size_inches(18.5, 10.5)
    # fig.savefig('V_vs_Ahpng.png', dpi=100)

        plt.plot(df2['Charge_Capacity (Ah)'], df2['Voltage (V)'], label= f'Ch{i}')
        plt.plot(df3['Discharge_Capacity (Ah)'], df3['Voltage (V)'], label =f'Dis{i}')


        plt.title('Voltage vs Capacity',fontsize=18)
        plt.xlabel('capacity (Ah)',fontsize=18)
        plt.ylabel('voltage (V)',fontsize=18)
#         plt.legend(['Ch1 ' , 'Dis1','Ch2 ' , 'Dis2','Ch3 ' , 'Dis3','Ch4 ' , 'Dis4','Ch5 ' , 'Dis5'])
        #plt.legend([i])

        # mplcursors.cursor()
        plt.grid()
        fig.savefig("1_V vs Ah.png")
        plt.legend()
    plt.show()
print_graph_of_cycl3(1, 11)

