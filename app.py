from flask import Flask, render_template, request, jsonify
from openpyxl import load_workbook
from io import BytesIO
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_excel', methods=['POST'])
def process_excel():
    try:
        # クライアントから送信されたURLを取得
        data = request.json
        excel_url = data.get('url')
        if not excel_url:
            return jsonify({"error": "URLが指定されていません。"}), 400

        # ネット上のエクセルファイルを取得
        response = requests.get(excel_url)
        if response.status_code != 200:
            return jsonify({"error": "エクセルファイルの取得に失敗しました。"}), 500

        # エクセルデータの読み込み
        excel_data = BytesIO(response.content)
        workbook = load_workbook(excel_data)
        sheet = workbook.active

        # 指定したセルの値を取得 (例: B2)
        cell_value = sheet["B2"].value

        # 数式に基づく値の計算
        if isinstance(cell_value, (int, float)):
            calculated_value = cell_value * 1.2  # 値を1.2倍
            result = {
                "original": cell_value,
                "calculated": calculated_value
            }
        else:
            return jsonify({"error": "セルの値が数値ではありません。"}), 400

        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
