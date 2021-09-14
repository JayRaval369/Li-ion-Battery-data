import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('C:/Users/jayra/Desktop/Batteryarchieve/HNEI_18650/HNEI_18650_NMC_LCO_25C_0-100_0.5-1.5C_a_timeseries (1).csv')
df1=df[df["Cycle_Index"] <= 10]

# plt.figure(figsize=(15,15))
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
# fig.savefig('test2png.png', dpi=100)

plt.plot(df1['Test_Time (s)'],df1['Voltage (V)'])

plt.title('Voltage vs Time',fontsize=18)
plt.xlabel('time (s)',fontsize=18)
plt.ylabel('voltage (V)',fontsize=18)
plt.grid()
fig.savefig("Voltage_vs_Time.png")
plt.show()
