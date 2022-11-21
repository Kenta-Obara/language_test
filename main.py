import tkinter as tk
from tkinter import ttk
import numpy as np
import pandas as pd
import random

# ---------------データの読み込み--------------------------------
df = pd.read_csv("english.csv")
df_dic = df.to_dict(orient="records")

# --------------文章を更新---------------

def change_sentence():
  text_widget.delete('1.0','end')
  topic = combobox.get().capitalize()
  try:
    current_word = random.choice(df_dic)
    df_dic.remove(current_word)
  except IndexError:
    tk.messagebox.showinfo(title="DONE", message="全て終了です！")
  except KeyError:
    tk.messagebox.showinfo(title="DONE", message="そのトピックはありません")
  finally:
    current_sentence = current_word[topic]
    if current_sentence is np.nan:
      change_sentence()
    else:
      text_widget.insert('1.0', current_sentence)

# --------------ウィンドウを閉じるfunction

def close_window():
  root.destroy()

# root メインウィンドウの設定
root = tk.Tk()
root.title("New English Test")
root.configure(bg="skyblue")
root.geometry("700x500")

# メインフレームの作成と設置
frame = ttk.Frame(root)
frame.pack(padx=20,pady=50)


# combobox用の内容作成
year_list = list(df.columns)

# ウィジェットの作成
guide_label = tk.Label(master=frame, text="期間を選択してください",fg="black")
combobox = ttk.Combobox(master=frame, values=year_list, width=8, justify="center",state="readonly")
text_widget = tk.Text(master=frame, height=7, bg="white", fg="black")
text_widget.config(wrap="word")
quit_button = tk.Button(master=frame, text = "終了",command = close_window, bg='#F0F8FF', fg='#FF4500')
change_button = tk.Button(master=frame, text="NEXT", fg="black",justify="center", command=change_sentence)

# 各種ウィジェットの設置
guide_label.grid(row=0, column=0)
combobox.grid(row=1, column=0)
text_widget.grid(row=2, column=0)
change_button.grid(row=3,column=0)
quit_button.grid(row=4, column=0)

# def callbackFunc(event):
#   print("New Element Selected")
#   print(combobox.current())
#   print(combobox.get())

# combobox.current(1)
# combobox.bind("<<ComboboxSelected>>", callbackFunc)

root.mainloop()

# def callbackFunc(event):
#   print("New Element Selected")
#   print(combobox.current())
#   print(combobox.get())
