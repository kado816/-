# tkinterをインポート
import tkinter as tk
# ランダムモジュールをインポート
import random
# クイズデータを辞書で定義
quiz_data = {
    "日本で一番狭い都道府県は？": ["大阪府", "東京都", "香川県", "沖縄県", 2],
    "日本で一番広い県は？": ["長野県", "神奈川県", "岩手県", "福島県", 2],
    "日本で一番多い苗字は？": ["田中", "高橋", "鈴木", "佐藤", 3],
    "みかん生産量が一番多い都道府県は？": ["和歌山県", "熊本県", "愛媛県", "静岡県", 0]
}
# クイズのキー（問題文）をリストに変換
quiz_keys = list(quiz_data.keys())
# クイズの数を取得
quiz_num = len(quiz_keys)
# 現在のクイズのインデックスを初期化
quiz_index = 0
# 正解数を初期化
correct_count = 0

# ルートウィンドウを作成
root = tk.Tk()
# ウィンドウのタイトルを設定
root.title("tkinter quiz")
# ウィンドウのサイズを設定
root.geometry("400x300")

# 問題文ラベルを作成
question_label = tk.Label(root, text="問題文")
# 問題文ラベルを配置
question_label.pack(pady=10)

# 選択肢ラジオボタンの値を保持する変数を作成
choice_var = tk.IntVar()
# 選択肢ラジオボタンのリストを作成
choice_buttons = []
# 選択肢の数だけ繰り返す
for i in range(4):
    # 選択肢ラジオボタンを作成
    choice_button = tk.Radiobutton(root, text="選択肢" + str(i), variable=choice_var, value=i)
    # 選択肢ラジオボタンを配置
    choice_button.pack(anchor=tk.W)
    # 選択肢ラジオボタンをリストに追加
    choice_buttons.append(choice_button)

# 結果ラベルを作成
result_label = tk.Label(root, text="結果")
# 結果ラベルを配置（初期状態では非表示）
result_label.pack(pady=10)
result_label.pack_forget()

# OKボタンが押されたときの処理
def ok_click():
    # グローバル変数を参照する宣言
    global quiz_index, correct_count
    # 結果ラベルを非表示にする
    result_label.pack_forget()
    # 選択肢が選ばれているかどうか判定
    if choice_var.get() == -1:
        # 選ばれていない場合はメッセージボックスを表示して処理終了
        tk.messagebox.showinfo("エラー", "選択肢を選んでください")
        return
    # 選ばれている場合は正解かどうか判定
    if choice_var.get() == quiz_data[quiz_keys[quiz_index]][4]:
        # 正解の場合は正解数を増やす
        correct_count += 1
        # 結果ラベルに正解と表示
        result_label["text"] = "正解！"
    else:
        # 不正解の場合は結果ラベルに不正解と表示
        result_label["text"] = "不正解…"
    # 結果ラベルを表示
    result_label.pack()
    # クイズのインデックスを増やす
    quiz_index += 1
    # クイズのインデックスがクイズの数以上になったかどうか判定
    if quiz_index >= quiz_num:
        # なった場合は全問終了とメッセージボックスを表示してウィンドウを閉じる
        tk.messagebox.showinfo("終了", "全問終了です\n正解数：" + str(correct_count))
        root.destroy()
        return
    # ならない場合は次の問題を表示する関数を呼ぶ
    show_quiz()

# 次の問題を表示する関数
def show_quiz():
    # グローバル変数を参照する宣言
    global quiz_index, quiz_keys, quiz_data
    # 問題文ラベルに問題文を表示
    question_label["text"] = quiz_keys[quiz_index]
    # 選択肢ラジオボタンに選択肢を表示
    for i in range(4):
        choice_buttons[i]["text"] = quiz_data[quiz_keys[quiz_index]][i]
    # 選択肢ラジオボタンの値をリセット
    choice_var.set(-1)

# 最初の問題を表示する関数を呼ぶ
show_quiz()

# OKボタンを作成
ok_button = tk.Button(root, text="OK", command=ok_click)
# OKボタンを配置
ok_button.pack(pady=10)

# メインループを開始
root.mainloop()
