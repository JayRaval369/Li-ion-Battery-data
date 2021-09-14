import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('C:/Users/jayra/Desktop/split/a.csv')

df.rename(columns={'Open Circuit Voltage': 'Open_Circuit_Voltage'}, inplace=True)
clean_df = df[df['Open_Circuit_Voltage'].apply(str).str.startswith(('DCC', 'CCC'))]
test1 = clean_df.reset_index(drop=True)
test1.drop('Unnamed: 0',inplace=True,axis=1)

test1.to_csv('index_dv.csv')
data=pd.read_csv('index_dv.csv')
data.drop('Unnamed: 0',inplace=True,axis=1)

CL =data.values.tolist()


# List of Voltage
vls=[]
chls=[]
dchls=[]

for i in range(0,len(CL)):
    vls.append(CL[i][4])
    chls.append(CL[i][5])
    dchls.append(CL[i][6])

    
# Diffrence for voltage ----For Numerator of dv/dc or dv/dd
diff_vls=[]
diff_chls=[]
diff_dchls=[]

for i in range(0,len(vls)-1):
    r1 = vls[i] - vls[i+1]
    r2 = chls[i] - chls[i+1]
    r3 = dchls[i] - dchls[i+1]
    diff_vls.append(r1)
    diff_chls.append(r2)
    diff_dchls.append(r3)



# For dc/dv
dcc_by_dv=[]
for i in range (0,len(diff_vls)):
    if diff_vls[i] == 0:
        dcc_by_dv.append(None)
    else:
        dcc_by_dv.append(diff_chls[i]/diff_vls[i])

# For dd/dv        
ddcc_by_dv=[]
for i in range (0,len(diff_vls)):
    if diff_vls[i] == 0:
        ddcc_by_dv.append(None)
    else:
        ddcc_by_dv.append(diff_dchls[i]/diff_vls[i])

# For matching a length of the dataframe
dcc_by_dv.append(None)
ddcc_by_dv.append(None)


for i in range(len(CL)-1):
    if CL[i][2] !=  CL[i+1][2]:
        dcc_by_dv.pop(i)
        ddcc_by_dv.pop(i)
        dcc_by_dv.insert(i,None)
        ddcc_by_dv.insert(i,None)
        
for i in range(len(CL)):
    if dcc_by_dv[i] != 0 and ddcc_by_dv[i] != 0:
        dcc_by_dv.pop(i)
        ddcc_by_dv.pop(i)
        dcc_by_dv.insert(i,None)
        ddcc_by_dv.insert(i,None)

for i in range(len(dcc_by_dv)):
    if dcc_by_dv[i] == None or dcc_by_dv[i] == None:
        continue
        
    if dcc_by_dv[i] > 10:
        dcc_by_dv.pop(i)
        dcc_by_dv.insert(i,None)
    if ddcc_by_dv[i] > 10:
        ddcc_by_dv.pop(i)
        ddcc_by_dv.insert(i,None)
        

# Inserstion of a column in dataframe
data.insert(11,"dc/dv",dcc_by_dv,True)
data.insert(12,"dd/dv",ddcc_by_dv,True)

data.to_csv('ssdc_dv.csv')


def print_graph_of_cycl3(num1, num2,gap):
    for i in range(num1, num2,gap):
        df4 = pd.read_csv('ssdc_dv.csv')
        df5 = df4[df4["Cycle_Index"] == i]
       

        fig = plt.gcf()
        fig.set_size_inches(18.5, 10.5)
    # fig.savefig('V_vs_Ahpng.png', dpi=100)
    
        plt.plot(df5['Voltage (V)'],df5['dc/dv'],label= f'Ch{i}')
        plt.plot(df5['Voltage (V)'],df5['dd/dv'],label =f'Dis{i}')
        
#         scale_factor = 1.1

#         xmin, xmax = plt.xlim()
#         ymin, ymax = plt.ylim()

#         plt.xlim(xmin * scale_factor, xmax * scale_factor)
#         #plt.ylim(ymin * scale_factor, ymax * scale_factor)


        plt.title(' dq/dv vs Voltage ',fontsize=18)
        plt.xlabel('voltage (V)',fontsize=18)
        plt.ylabel('dq/dv',fontsize=18)
#         plt.legend(['Ch1 ' , 'Dis1','Ch2 ' , 'Dis2','Ch3 ' , 'Dis3','Ch4 ' , 'Dis4','Ch5 ' , 'Dis5'])
        #plt.legend([i])

        # mplcursors.cursor()
        plt.grid()
        fig.savefig(f"{num1}_dq_{num2}_dv.png")
        plt.legend()
    plt.show()
print_graph_of_cycl3(1, 6,1)




