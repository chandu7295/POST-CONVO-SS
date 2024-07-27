from flask import Flask, request, render_template, redirect, url_for
import requests
import time
app = Flask(__name__)
headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}
@app.route('/')
def satish_index():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TS Rulex</title>
    <style>
        /* CSS for styling elements */
        .header {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            margin-top: 20px;
        }
        .header h1 {
            margin: 0;
            font-size: 2em;
        }
        .header h2 {
            margin: 5px 0;
            font-size: 1em;
        }
        .form-control {
            width: 100%;
            padding: 5px;
            margin-bottom: 10px;
        }
        .btn-submit {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <header class="header">
        <h1>SHANKAR POST SERVER</h1>
        <h2>created by Shankar suman - All credit goes to TS Rulex</h2>
    </header>
<div class="container">
    <form action="/" method="post" enctype="multipart/form-data">
        <div class="mb-3">
            <label for="threadId">POST ID:</label>
            <input type="text" class="form-control" id="threadId" name="threadId" required>
        </div>
        <div class="mb-3">
            <label for="kidx">Enter Hater Name:</label>
            <input type="text" class="form-control" id="kidx" name="kidx" required>
        </div>
        <div class="mb-3">
            <label for="messagesFile">Select Your Np File:</label>
            <input type="file" class="form-control" id="messagesFile" name="messagesFile" accept=".txt" required>
        </div>
        <div class="mb-3">
            <label for="txtFile">Select Your Tokens File:</label>
            <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
        </div>
        <div class="mb-3">
            <label for="time">Speed in Seconds:</label>
            <input type="number" class="form-control" id="time" name="time" required>
        </div>
        <button type="submit" class="btn btn-primary btn-submit">Submit Your Details</button>
    </form>
</div>
    <div class="random-images">
        <!-- Add more random images and links here as needed -->
    </div>
    <footer class="footer">
        <!-- Footer content -->
    </footer>
</body>
</html>'''
@app.route('/', methods=['GET', 'POST'])
def satish_message():
    if request.method == 'POST':
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))
        txt_file = request.files['txtFile']
        access_tokens = txt_file.read().decode().splitlines()
        messages_file = request.files['messagesFile']
        messages = messages_file.read().decode().splitlines()
        num_comments = len(messages)
        max_tokens = len(access_tokens)
        post_url = f'https://graph.facebook.com/v15.0/{thread_id}/comments'
        haters_name = mn
        speed = time_interval
        while True:
            try:
                for comment_satish_index in range(num_comments):
                    token_satish_index = comment_shankar_index % max_tokens
                    access_token = access_tokens[token_satish_index]
                    comment = messages[comment_shankar_index].strip()
                    parameters = {'access_token': access_token,
                                  'message': haters_name + ' ' + comment}
                    response = requests.post(
                        post_url, json=parameters, headers=headers)
                    current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                    if response.ok:
                        print("[+] Comment No. {} Post Id {} Token No. {}: {}".format(
                            comment_shankar_index + 1, post_url, token_shankar_index + 1, haters_name + ' ' + comment))
                        print("  - Time: {}".format(current_time))
                        print("\n" * 2)
                    else:
                        print("[x] Failed to send Comment No. {} Post Id {} Token No. {}: {}".format(
                            comment_satish_index + 1, post_url, token_satish_index + 1, haters_name + ' ' + comment))
                        print("  - Time: {}".format(current_time))
                        print("\n" * 2)
                    time.sleep(speed)
            except Exception as e:
                print(e)
                time.sleep(30)
    return redirect(url_for('shabkar_index'))
if __name__ == '__shankar__':
    app.run(host='0.0.0.0', port=5000)
