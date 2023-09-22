import random

# 問題と答えのリストを作成する
questions = [
    "日本の首都は？",
    "世界で最も高い山は？",
    "日本の国花は？"
]

answers = [
    ["東京", "大阪", "京都"],
    ["エベレスト", "富士山", "キリマンジャロ"],
    ["桜", "菊", "バラ"]
]

# 問題をランダムに選択する
question_index = random.randint(0, len(questions) - 1)

# 問題を表示する
print(questions[question_index])

# 選択肢を表示する
for i in range(len(answers[question_index])):
    print(str(i + 1) + ": " + answers[question_index][i])