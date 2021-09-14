import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('C:/Users/jayra/Desktop/split/a.csv')

df.rename(columns={'Open Circuit Voltage': 'Open_Circuit_Voltage'}, inplace=True)
clean_df = df[df['Open_Circuit_Voltage'].apply(str).str.startswith(('DCC', 'CCC'))]
test = clean_df.reset_index(drop=True)
test.drop('Unnamed: 0',inplace=True,axis=1)

test.to_csv('testtt.csv')
data=pd.read_csv('testtt.csv')
data.drop('Unnamed: 0',inplace=True,axis=1)


# Dataframe to list of list
CL =data.values.tolist()

# List of Voltage
vls=[]
for i in range(0,len(CL)):
    vls.append(CL[i][4])  

# List of charging capacity  
chls=[]
for i in range(0,len(CL)):
    chls.append(CL[i][5])

# List of discharging capacity 
dchls=[]
for i in range(0,len(CL)):
    dchls.append(CL[i][6])

# Diffrence for voltage ----For Numerator of dv/dc or dv/dd
diff_vls=[]
for i in range(0,len(vls)-1):
    res = vls[i] - vls[i+1]
    diff_vls.append(res)

# Diffrence for charging capacity--- For Denominator of dv/dc
diff_chls=[]
for i in range(0,len(chls)-1):
    res = chls[i] - chls[i+1]
    diff_chls.append(res)

# Diffrence for discharging capacity--- For Denominator of dv/dd 
diff_dchls=[]
for i in range(0,len(dchls)-1):
    res = dchls[i] - dchls[i+1]
    diff_dchls.append(res)

# For dv/dc
dv_by_dcc=[]
for i in range (0,len(diff_vls)):
    if diff_chls[i] == 0:
        dv_by_dcc.append(None)
    else:
        dv_by_dcc.append(diff_vls[i]/diff_chls[i])

# For dv/dd        
dv_by_ddcc=[]
for i in range (0,len(diff_vls)):
    if diff_dchls[i] == 0:
        dv_by_ddcc.append(None)
    else:
        dv_by_ddcc.append(diff_vls[i]/diff_dchls[i])

for i in range(0,len(dv_by_dcc)):
    if dv_by_dcc[i]  == None:
        pass
    elif dv_by_dcc[i]  < 0:
        dv_by_dcc.pop(i)
        dv_by_dcc.insert(i,None)

for j in range(0,len(dv_by_ddcc)):
    if dv_by_ddcc[j]  == None:
        pass
    elif dv_by_ddcc[j]  < -10:
        dv_by_ddcc.pop(j)
        dv_by_ddcc.insert(j,None)

# For matching a length of the dataframe
dv_by_dcc.append(None)
dv_by_ddcc.append(None)

# Inserstion of a column in dataframe
data.insert(11,"dv/dc",dv_by_dcc,True)
data.insert(12,"dv/dd",dv_by_ddcc,True)

data.to_csv('dv_dc.csv')

def print_graph_of_cycl3(num1, num2,gap):
    for i in range(num1, num2,gap):
        df4 = pd.read_csv('dv_dc.csv')
        df5 = df4[df4["Cycle_Index"] == i]
       

        fig = plt.gcf()
        fig.set_size_inches(18.5, 10.5)
    # fig.savefig('V_vs_Ahpng.png', dpi=100)
    
        plt.plot(df5['Voltage (V)'],df5['dv/dc'],label= f'Ch{i}')
        plt.plot(df5['Voltage (V)'],df5['dv/dd'],label =f'Dis{i}')

        scale_factor = 1.3
        #xmin, xmax = plt.xlim()
        ymin, ymax = plt.ylim()
        #plt.xlim(xmin * scale_factor, xmax * scale_factor)
        plt.ylim(ymin * scale_factor, ymax * scale_factor)
        

        plt.title('Voltage vs dv/dq',fontsize=18)
        plt.xlabel('voltage (V)',fontsize=18)
        plt.ylabel('dv/dq',fontsize=18)
#         plt.legend(['Ch1 ' , 'Dis1','Ch2 ' , 'Dis2','Ch3 ' , 'Dis3','Ch4 ' , 'Dis4','Ch5 ' , 'Dis5'])
        #plt.legend([i])

        # mplcursors.cursor()
        plt.grid()
        fig.savefig(f"{num1}_dv_{num2}_dq.png")
        plt.legend()
    plt.show()
print_graph_of_cycl3(1, 6,1)



