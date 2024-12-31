import os
import json
from flask import Flask, render_template, request
import matplotlib.pyplot as plt

app = Flask(__name__)

# JSONファイル（対応表）を読み込む
MAPPINGS_FILE = os.path.join(os.path.dirname(__file__), 'lib', 'mappings.json')
with open(MAPPINGS_FILE, 'r', encoding='utf-8') as f:
    mappings = json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    selected_option = request.form.get("selectedOption")
    
    if selected_option not in mappings:
        return render_template("result.html", message="無効な選択です。")

    # 仮データ：Excelから取得するデータの代わり
    g_list = [5, 15, 10, 20, 25]  # 実際にはExcelからデータを取得してください

    # グラフを作成
    img_path = os.path.join("static", "graph.png")
    create_radar_chart(g_list, img_path)

    return render_template("result.html", graph_url=img_path, g_list=g_list)

def create_radar_chart(data, output_path):
    labels = ["A", "B", "C", "D", "E"]
    num_vars = len(labels)

    # レーダーチャートの角度
    angles = [n / float(num_vars) * 2 * 3.14159 for n in range(num_vars)]
    angles += angles[:1]

    # データの準備
    data += data[:1]

    # プロット
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, data, color='blue', alpha=0.25)
    ax.plot(angles, data, color='blue', linewidth=2)
    ax.set_yticks([])  # Y軸の値を非表示
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)

    # 保存
    plt.savefig(output_path)
    plt.close()

if __name__ == "__main__":
    app.run(debug=True)
