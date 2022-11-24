import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import pandas as pd

# ---------------データの読み込み--------------------------------
df = pd.read_csv("english.csv")
df_dic = df.to_dict(orient="records")

# コンボボックス選択次に単語リスト作成

my_list = []

def callbackFunc(event):
  period = combobox.get().capitalize()
  word_list = list(df[period].dropna())
  for word in word_list:
    my_list.append(word)

# --------------文章を更新（新）---------------  
def change_sentence():
  text_widget.delete('1.0', 'end')
  try:
    current_sentence = my_list[0]
    text_widget.insert('1.0', current_sentence)
    my_list.pop(0)
  except IndexError:
    messagebox.showinfo(title="Done", message="全て終了です！")
    root.destroy()
  except KeyError:
    messagebox.showinfo(title="Done", message="そのトピックはありません")
    root.destroy()
  except:
    print("例外です")
    root.destroy()

# --------------ウィンドウを閉じるfunction

def close_window():
  root.destroy()

# root メインウィンドウの設定
root = tk.Tk()
root.title("New English Test")
root.configure(bg="skyblue")
root.geometry("1000x500")

# メインフレームの作成と設置
frame = ttk.Frame(root)
frame.pack(padx=20,pady=50)


# combobox用の内容作成
year_list = list(df.columns)

# ウィジェットの作成
guide_label = tk.Label(master=frame, text="期間を選択してください",fg="black")
combobox = ttk.Combobox(master=frame, values=year_list, width=8, justify="center",state="readonly")
text_widget = tk.Text(master=frame, height=3, bg="white", fg="black", font=("","17",""))
text_widget.config(wrap="word")
quit_button = tk.Button(master=frame, text = "終了",command = close_window, bg='#F0F8FF', fg='#FF4500', font=("","13","bold"))
change_button = tk.Button(master=frame, text="NEXT", fg="black",justify="center", command=change_sentence)

# 各種ウィジェットの設置
guide_label.grid(row=0, column=0)
combobox.grid(row=1, column=0)
text_widget.grid(row=2, column=0)
change_button.grid(row=3,column=0)
quit_button.grid(row=4, column=0)

combobox.bind("<<ComboboxSelected>>", callbackFunc)

root.mainloop()

