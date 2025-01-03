# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 10:04:55 2025

@author: 流空
"""

import os
import json
from flask import Flask, render_template, request # type: ignore
import matplotlib.pyplot as plt # type: ignore
import numpy as np

app = Flask(__name__)

order = 0
count = 0
Getlist = []
Compare_list = []
Skills = ["20sec", "60sec", "2000m", "20min", "60min"]
selectedName = None
#サーバーから送られた選択肢
Selected = None
#サーバーから送られた選択肢
output_path = "radar_chart.png"
#返答

MAPPINGS_FILE = os.path.join(os.path.dirname(__file__), 'lib', 'mappings.json')
with open(MAPPINGS_FILE, 'r', encoding='utf-8') as f:
    mappings = json.load(f)
#mapping.jsonを取得

if selectedName in mappings and len(mappings[selectedName]) >= 5:
    while order < 5:
        Getlist.append(mappings[selectedName][order])
        order += 1
else:
    print(" '{}'のデータが見つかりませんでした")

if Selected in mappings and len(mappings[Selected]) >= 5:
    while count < 5:
        Compare_list.append(mappings[Selected][order])
        count += 1
else:
    print(" '{Selected}'のデータが見つかりませんでした")


@app.route("/", methods=["GET", "POST"])
def index():
    message = None
    if request.method == "POST":
        selected_name = request.form.get("selectedName")
        selected_type = request.form.get("selectedType")
        if selectedName not in mappings:
            return render_template("index.html", message="無効な選択です。")
        else:
            try:
                img_path = os.path.join("static", "graph.png")
                create_radar_chart(Getlist, img_path)
            except Exception as e:
                message = f"エラー: {e}"
        return render_template(
            "index.html",
            message=f"名前: {selected_name}, タイプ: {selected_type}",
        )
    return render_template("index.html")



def create_radar_chart(skills, Compare_list, Getlist, output_path):
    labels = np.array(skills)
    Compare_list = np.array(Compare_list)
    Getlist = np.array(Getlist)

    # データを閉じるために最初の値を最後に追加
    Compare_list = np.append(Compare_list,Compare_list[0])
    Getlist = np.append(Getlist, Getlist[0])
    labels = np.append(labels, labels[0])

    # 角度の計算
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=True)

    # レーダーチャートの描画
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    # 平均値グラフ
    ax.plot(angles, Compare_list, color='blue', linewidth=2, label='Average')
    ax.fill(angles, Compare_list, color='blue', alpha=0.25)

    # ユーザー値グラフ
    ax.plot(angles, Getlist, color='red', linewidth=2, label='Your score')
    ax.fill(angles, Getlist, color='red', alpha=0.25)

    # スキルラベルを設定
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(skills)

    # y軸の設定
    yticks = range(5, 105, 5)
    ax.set_yticks(yticks)
    ax.set_yticklabels([str(y) if (y - 5) % 10 == 09 else "" for y in yticks], color="gray")

    # タイトルと凡例
    ax.set_title("5items analysis", fontsize=20)
    ax.legend(loc=4, bbox_to_anchor=(1.1, 0))

    # 保存
    plt.savefig(output_path)
    plt.close()

if __name__ == "__main__":
    app.run(debug=True)
