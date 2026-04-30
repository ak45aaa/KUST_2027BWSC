import pandas as pd
import matplotlib.pyplot as plt

title_dic = {"Current1":"Output Current",
             "Current2":"Generate Current",
             "Speed":"Speed",
             "Voltage":"Voltage",
             "SOC":"SOC(Sate Of Charge)"}

def show_racing_data(df, cols=["Current1", "Speed", "Current2", "Voltage", "SOC"]):
    len_ = len(cols)
    
    fig, axes = plt.subplots(1, len_, figsize=(6*len_, 6))
    
    for i in range(len_):
        col = cols[i]
        axes[i].plot(df.index, df[col])
        axes[i].set_title(title_dic[col])
        
    plt.show()
        