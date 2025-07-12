import webbrowser
import os

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Attack on Titan - Episode List</title>
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
      margin-bottom: 20px;
    }
    video {
      width: 100%;
      max-width: 480px;
      border: none;
      border-radius: 8px;
      margin: 20px auto 0;
      display: block;
      box-shadow: 0 0 10px red;
    }
    .episode-list {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 12px;
      margin-top: 30px;
    }
    .episode-button {
      background: #1a1a1a;
      color: red;
      padding: 10px 20px;
      border: 2px solid red;
      border-radius: 8px;
      cursor: pointer;
      text-decoration: none;
      font-size: 1rem;
      transition: 0.3s;
    }
    .episode-button:hover {
      background-color: red;
      color: black;
    }
    a.back {
      display: inline-block;
      margin-top: 40px;
      color: red;
      background: #1a1a1a;
      padding: 10px 20px;
      text-decoration: none;
      border-radius: 6px;
    }
    a.back:hover {
      background: red;
      color: black;
    }
  </style>
</head>
<body>
  <h1>Attack on Titan</h1>
  <img src="https://cdn.myanimelist.net/images/anime/10/47347.jpg" alt="Attack on Titan" />
  <p>Watch the epic story of humanity vs titans!</p>

  <video id="videoPlayer" controls>
    <source src="ep1.mp4" type="video/mp4" />
    Your browser does not support the video tag.
  </video>

  <div class="episode-list">
    <a class="episode-button" onclick="loadEpisode('ep1')">Episode 1: To You, in 2000 Years</a>
    <a class="episode-button" onclick="loadEpisode('ep2')">Episode 2: That Day</a>
    <a class="episode-button" onclick="loadEpisode('ep3')">Episode 3: A Dim Light Amid Despair</a>
  </div>

  <a class="back" href="bland_mist_anime.html">🔙 Back to Home</a>

  <script>
    function loadEpisode(epId) {
      const video = document.getElementById("videoPlayer");
      video.src = epId + ".mp4";
      video.load();
      video.play();
    }
  </script>
</body>
</html>
"""

file_name = "attack-on-titan.html"
with open(file_name, "w", encoding="utf-8") as f:
    f.write(html)

webbrowser.open(f"file://{os.path.abspath(file_name)}")
print("✅ Attack on Titan episode page created and opened!")
print("📁 Make sure ep1.mp4, ep2.mp4, ep3.mp4 are in the same folder.")
