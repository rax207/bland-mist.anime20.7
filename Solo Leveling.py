import webbrowser
import os

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Solo Leveling</title>
  <style>
    body {
      background-color: black;
      color: red;
      font-family: 'Segoe UI', sans-serif;
      text-align: center;
      padding: 20px;
    }
    img {
      width: 300px;
      border: 2px solid red;
      border-radius: 10px;
      margin-top: 20px;
    }
    video {
      width: 90%;
      max-width: 600px;
      border: 2px solid red;
      border-radius: 10px;
      margin-top: 20px;
    }
    a {
      display: inline-block;
      margin-top: 30px;
      color: red;
      background: #1a1a1a;
      padding: 10px 20px;
      text-decoration: none;
      border-radius: 6px;
    }
    a:hover {
      background: red;
      color: black;
    }
  </style>
</head>
<body>
  <h1>Solo Leveling</h1>
  <img src="https://cdn.myanimelist.net/images/anime/1616/112273.jpg" alt="Solo Leveling" />

  <p>Follow the thrilling journey of Sung Jin-Woo as he rises from the weakest hunter to the strongest.</p>

  <video controls>
    <source src="my-anime.mp4" type="video/mp4" />
    Your browser does not support the video tag.
  </video>

  <a href="bland_mist_anime.html">🔙 Back to Home</a>
</body>
</html>
"""

file_name = "solo-leveling.html"
with open(file_name, "w", encoding="utf-8") as f:
    f.write(html)

file_path = os.path.abspath(file_name)
print("Opening:", file_path)
webbrowser.open(f"file://{file_path}")

print(f"✅ '{file_name}' page created and opened in your browser!")
print("📁 Make sure your video file 'my-anime.mp4' is in the same folder.")
