def create_love_page():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>For You ❤️</title>
        <style>
            body {
                background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 100%);
                font-family: 'Arial', sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                overflow: hidden;
            }
            .container {
                text-align: center;
                color: white;
            }
            h1 {
                font-size: 3rem;
                animation: fadeIn 2s ease-in-out;
            }
            p {
                font-size: 1.5rem;
                animation: fadeIn 3s ease-in-out;
            }
            .heart {
                font-size: 5rem;
                animation: beat 1s infinite;
            }
            @keyframes fadeIn {
                0% { opacity: 0; }
                100% { opacity: 1; }
            }
            @keyframes beat {
                0%, 100% { transform: scale(1); }
                50% { transform: scale(1.2); }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Dear [李艳香],</h1>
            <p>From the moment I saw you, my heart started beating in a new rhythm.</p>
            <p>You are the most amazing person I have ever met.</p>
            <p>I can't imagine my life without you.</p>
            <p>Will you be my 宝贝?</p>
            <div class="heart">❤️</div>
        </div>
        <audio autoplay loop>
            <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
            Your browser does not support the audio element.
        </audio>
    </body>
    </html>
    """

    with open("love_page.html", "w", encoding="utf-8") as file:
        file.write(html_content)

    print("表白页面已生成！请打开 'love_page.html' 查看。")

if __name__ == "__main__":
    create_love_page()