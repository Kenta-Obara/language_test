import tkinter as tk
from tkinter import ttk
import numpy as np
import pandas as pd
import random

# ---------------データの読み込み--------------------------------
df = pd.read_csv("english.csv")
df_dic = df.to_dict(orient="records")

# --------------文章を更新---------------

# root メインウィンドウの設定
root = tk.Tk()
root.title("New English Test")
root.configure(bg="green")
root.geometry("500x500")

# メインフレームの作成と設置
frame = tk.Frame(root)
frame.pack(padx=20,pady=10)

# ウィジェットの作成
# button = tk.Button(frame, text="tkinter")
# button_ttk = ttk.Button(frame, text="ttk")
year_list = list(df.columns)
combobox = ttk.Combobox(master=frame, values=year_list)

# 各種ウィジェットの設置
# button.grid(row=0, column=0, padx=5)
# button_ttk.grid(row=0, column=1)
combobox.grid(row=0, column=0)

root.mainloop()
