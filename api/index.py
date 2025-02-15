from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

# HTML قالب
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Garena Card Checker</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-image: url('https://dl.dir.freefiremobile.com/common/web_event/official2.ff.garena.all/202210/ce405ad07404fecfb3196b77822aec8b.jpg');
            background-size: cover;
            background-attachment: fixed;
            color: white;
            text-align: center;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            padding: 30px;
            background-color: rgba(0, 0, 0, 0.8);
            border-radius: 15px;
            max-width: 400px;
            box-shadow: 0px 0px 15px rgba(255, 255, 255, 0.2);
        }
        input, button {
            padding: 12px;
            width: 100%;
            margin: 10px 0;
            border-radius: 5px;
            border: none;
            font-size: 16px;
        }
        button {
            background-color: #FF4500;
            color: white;
            cursor: pointer;
        }
        .result {
            padding: 15px;
            font-size: 18px;
            margin-top: 20px;
            border-radius: 5px;
            font-weight: bold;
        }
        .valid { background-color: green; }
        .invalid { background-color: red; }
        .telegram-link {
            margin-top: 20px;
            display: inline-block;
            text-decoration: none;
            color: white;
            background-color: #0088cc;
            padding: 10px 20px;
            border-radius: 5px;
            font-size: 16px;
            font-weight: bold;
        }
        .telegram-link:hover {
            background-color: #0077aa;
        }
        .footer {
            margin-top: 20px;
            font-size: 20px;
            font-weight: bold;
            color: #FFD700;
            text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.7);
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Garena Card Checker for MENA Server</h1>
        <form method="POST">
            <label for="card_number">Enter Garena Card Number:</label><br>
            <input type="text" id="card_number" name="card_number" placeholder="Enter card number" required><br>
            <button type="submit">Check Card</button>
        </form>
        {% if result %}
            <div class="result {{ result_class }}">
                {{ result_message }}
            </div>
        {% endif %}
        <a class="telegram-link" href="https://t.me/MROXTPCOM" target="_blank">Join Our Telegram Group</a>
    </div>
    <div class="footer">By : HP LVL BOOOT</div>
</body>
</html>
"""

@app.route("/FF", methods=["GET", "POST"])
def card_checker():
    result = None
    result_class = ""
    result_message = ""

    if request.method == "POST":
        card_number = request.form.get("card_number")

        # إعداد الطلب
        cookies = {
    'mspid2': '65e63cd84e27663fb0175abbe13eac42',
    'region': 'ME',
    'language': 'en',
    'source': 'mb',
    'session_key': 'lr2oehn7tu8v6tbg09d2bu3ijlmh274f',
    'datadome': '4cO0F0GXPrnQoZ154NMoA9F4G0BNKyhoFlYqcEWAZXuRme564f1V3G7zpxZdqqSSmMdqDrh1up53aWi~4beyyJhUKDldinK71gdga34VPrDjHvsnKIjlDJ10FqrTYZFb',
    '__csrf__': 'AOO6Z0G7gPe4Dx8wDdBWNp2eUeHiTSyN',
        }

        headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ar-AE,ar;q=0.9,en-IN;q=0.8,en;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'mspid2=65e63cd84e27663fb0175abbe13eac42; region=ME; language=en; source=mb; session_key=lr2oehn7tu8v6tbg09d2bu3ijlmh274f; datadome=4cO0F0GXPrnQoZ154NMoA9F4G0BNKyhoFlYqcEWAZXuRme564f1V3G7zpxZdqqSSmMdqDrh1up53aWi~4beyyJhUKDldinK71gdga34VPrDjHvsnKIjlDJ10FqrTYZFb; __csrf__=AOO6Z0G7gPe4Dx8wDdBWNp2eUeHiTSyN',
    'Origin': 'https://shop2game.com',
    'Referer': 'https://shop2game.com/?channel=299999',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'x-csrf-token': 'AOO6Z0G7gPe4Dx8wDdBWNp2eUeHiTSyN',
        }

        json_data = {
            'app_id': 100067,
            'packed_role_id': 0,
            'channel_id': 299999,
            'service': 'mb',
            'channel_data': {
                'card_password': card_number,
            },
            'revamp_experiment': {
                'session_id': '65e63cd84e27663fb0175abbe13eac42',
                'group': 'treatment2',
                'service_version': 'mshop_frontend_20250213',
                'source': 'mb',
                'domain': 'shop2game.com',
            },
        }

        # إرسال الطلب
        response = requests.post('https://shop2game.com/api/shop/pay/init', headers=headers, cookies=cookies, json=json_data)

        # معالجة الاستجابة
        if response.status_code == 200:
            data = response.json()
            display_id = data.get("display_id")
            result_code = data.get("result")
            error_code = data.get("error")

            # التحقق من صلاحية البطاقة
            if display_id == "0" or result_code == "error_invalid_card" or error_code == "error_require_login":
                result_message = "Invalid Garena Card"
                result_class = "invalid"
            else:
                result_message = "Valid Garena Card"
                result_class = "valid"
        else:
            result_message = "Error checking the card"
            result_class = "invalid"

        result = True

    return render_template_string(html_template, result=result, result_class=result_class, result_message=result_message)

if __name__ == "__main__":
    app.run(debug=True)
