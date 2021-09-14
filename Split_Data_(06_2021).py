import pandas as pd
df =  pd.read_csv('C:/Users/jayra/Desktop/Batteryarchieve/HNEI_18650/HNEI_18650_NMC_LCO_25C_0-100_0.5-1.5C_a_timeseries (1).csv')
#df= df.iloc[:,:8]

#Started Splitting a data acoording to Parameters

for i in range(len(df['Cycle_Index'])):
   
    df.loc[(df['Current (A)'] == 0) & (df['Cycle_Index'] == i), 'Open Circuit Voltage'] = f'OCV_{i}' 
    df.loc[(df['Current (A)'] <= -0.106) & (df['Current (A)'] >= -4.205) & (df['Cycle_Index'] == i), 'Open Circuit Voltage'] = f'DCC_{i}'
    df.loc[(df['Current (A)'] <= 2.810) & (df['Current (A)'] >= 0.105) & (df['Cycle_Index'] == i), 'Open Circuit Voltage'] = f'CCC_{i}'
    df.loc[(df['Current (A)'] <= 1.302) & (df['Current (A)'] >= 0.049) & (df['Cycle_Index'] == i), 'Open Circuit Voltage'] = f'CCV_{i}'
    #print(i)

# Splitting DCV (For Discharge Constant Voltage) - Using reverse loop
for i in range(len(df)-1, -1, -1):
    #print(i)
    print(df.loc[i, 'Voltage (V)'])
    print(df.loc[i-1, 'Voltage (V)'])
    if df.loc[i, 'Voltage (V)'] != df.loc[i-1, 'Voltage (V)']:
        temp = i
        break
for i in range(temp, len(df)):
    df.loc[i, 'Open Circuit Voltage'] = f'DCV_{max(df["Cycle_Index"])}'

#Using Function and Counter for ex.- DCC_1_1 , DCC_1_2
def func(stri):
    max_cycle = max(df['Cycle_Index'])
    for j in range(1, max_cycle+1):
        counter = 1
        for i in range(len(df["Cycle_Index"])):
            #print(i)
            if df.loc[i, 'Open Circuit Voltage'] == f'{stri}_{j}':
                df.loc[i, 'Open Circuit Voltage'] = f'{stri}_{j}_{counter}'
                if i+1!=len(df["Cycle_Index"]):
                    if df.loc[i+1, 'Open Circuit Voltage'] != f'{stri}_{j}':
                        counter+=1
func('OCV')
func('DCC')
func('CCC')
func('CCV')

#save a data in CSV file
df.to_csv('a.csv')