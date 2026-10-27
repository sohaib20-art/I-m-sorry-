<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>A Sincere Apology ♡</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 25px;
            font-family: Georgia, serif;
            color: #fff;
            background: linear-gradient(
                135deg,
                #120d19,
                #432239,
                #211327
            );
        }

        .card {
            width: 100%;
            max-width: 650px;
            padding: 40px 30px;
            text-align: center;
            border: 1px solid rgba(255,255,255,0.18);
            border-radius: 24px;
            background: rgba(255,255,255,0.07);
            backdrop-filter: blur(15px);
            box-shadow: 0 20px 60px rgba(0,0,0,0.35);
            animation: fadeIn 1.5s ease;
        }

        .heart {
            font-size: 48px;
            color: #ffd1e4;
            margin-bottom: 18px;
            animation: pulse 2s infinite;
        }

        h1 {
            font-size: 32px;
            color: #ffd1e4;
            margin-bottom: 25px;
        }

        .message {
            font-size: 17px;
            line-height: 1.9;
            color: #f8edf4;
            text-align: left;
            white-space: pre-line;
        }

        .signature {
            margin-top: 28px;
            font-size: 20px;
            font-style: italic;
            color: #ffd1e4;
        }

        button {
            margin-top: 30px;
            padding: 14px 25px;
            border: none;
            border-radius: 30px;
            background: #ffd1e4;
            color: #321629;
            font-size: 15px;
            cursor: pointer;
            transition: 0.3s;
        }

        button:hover {
            transform: scale(1.05);
            background: white;
        }

        #ending {
            display: none;
            margin-top: 25px;
            color: #ffd1e4;
            font-size: 17px;
            line-height: 1.8;
            animation: fadeIn 1s ease;
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes pulse {
            0%, 100% {
                transform: scale(1);
            }
            50% {
                transform: scale(1.12);
            }
        }

        @media (max-width: 480px) {
            .card {
                padding: 30px 22px;
            }

            h1 {
                font-size: 27px;
            }

            .message {
                font-size: 16px;
            }
        }
    </style>
</head>

<body>

    <main class="card">

        <div class="heart">♡</div>

        <h1>A Sincere Apology</h1>

        <div class="message">Sometimes words cannot fix everything, but a sincere apology is a place to start.

I've been thinking about what happened, and I want to sincerely apologize.

I know that my words or actions may have hurt you, and I'm truly sorry for that. I never wanted to make things difficult between us.

I understand that saying "I'm sorry" doesn't automatically make everything okay. I'm not asking you to forget what happened or to forgive me immediately.

I just want you to know that I recognize my mistake and that I want to learn from it.

You deserve honesty, respect, and understanding.

I hope that with time, my actions can show you how sincere these words really are.

Whatever you decide, I'll respect your feelings and your space.

Thank you for taking the time to read this.</div>

        <div class="signature">
            With sincere apologies ♡
        </div>

        <button onclick="showMessage()">
            One Last Thing ♡
        </button>

        <div id="ending">
            I can't change the past, but I can learn from it.
            <br><br>
            I'm truly sorry, and I wish you nothing but
            peace and happiness. 🤍
        </div>

    </main>

    <script>
        function showMessage() {
            const ending = document.getElementById("ending");
            const button = document.querySelector("button");

            if (ending.style.display === "block") {
                ending.style.display = "none";
                button.textContent = "One Last Thing ♡";
            } else {
                ending.style.display = "block";
                button.textContent = "Close Message ♡";
            }
        }
    </script>

</body>
</html>
