import webbrowser
import os

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Bland Mist Anime</title>
  <style>
    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: 'Segoe UI', sans-serif;
      background-color: black;
      color: red;
      display: flex;
      flex-direction: column;
      min-height: 100vh;
    }
    header {
      background-color: red;
      color: black;
      padding: 20px;
      text-align: center;
      font-size: 2em;
      font-weight: bold;
    }
    nav {
      background-color: #1a1a1a;
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      gap: 10px;
      padding: 10px;
    }
    nav a {
      color: red;
      text-decoration: none;
      font-weight: bold;
      padding: 8px 16px;
      border-radius: 4px;
      transition: 0.3s;
    }
    nav a:hover {
      background-color: red;
      color: black;
    }
    .main-container {
      display: flex;
      flex: 1;
      padding: 20px;
    }
    .content {
      flex: 3;
    }
    .search-bar {
      margin: 0 auto 20px;
      max-width: 400px;
    }
    .search-bar input {
      width: 100%;
      padding: 10px;
      border: 2px solid red;
      border-radius: 6px;
      background: #1a1a1a;
      color: red;
      font-size: 1em;
    }
    .anime-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
      gap: 20px;
    }
    .anime-card {
      background-color: #111;
      border: 1px solid red;
      border-radius: 8px;
      padding: 10px;
      text-align: center;
      transition: 0.3s;
      text-decoration: none;
      color: red;
    }
    .anime-card:hover {
      transform: scale(1.05);
      background-color: #220000;
      box-shadow: 0 0 10px red;
      color: white;
    }
    .anime-card img {
      width: 100%;
      border-radius: 5px;
      margin-bottom: 10px;
    }
    .anime-card h3 {
      margin: 0;
      font-size: 1rem;
      text-transform: capitalize;
    }
    .sidebar {
      flex: 1;
      margin-left: 20px;
      border-left: 1px solid red;
      padding-left: 20px;
      max-height: 600px;
      overflow-y: auto;
    }
    .sidebar h3 {
      color: white;
      margin-bottom: 10px;
      text-align: center;
    }
    .top-anime {
      list-style: none;
      padding: 0;
      color: red;
    }
    .top-anime li {
      background-color: #111;
      border: 1px solid red;
      border-radius: 5px;
      padding: 8px;
      margin-bottom: 10px;
      transition: 0.3s;
      cursor: pointer;
    }
    .top-anime li:hover {
      background-color: red;
      color: black;
    }
    footer {
      background-color: red;
      color: black;
      text-align: center;
      padding: 12px;
      font-size: 0.9rem;
    }
  </style>
</head>
<body>

<header>Bland Mist Anime</header>

<nav>
  <a href="#">Home</a>
  <a href="#">Anime List</a>
  <a href="#">Watched</a>
</nav>

<div class="main-container">
  <div class="content">
    <div class="search-bar">
      <input type="text" id="searchInput" placeholder="Search anime..." onkeyup="searchAnime()">
    </div>

    <div class="anime-grid" id="animeGrid">
      <a href="attack-on-titan.html" class="anime-card">
        <img src="https://cdn.myanimelist.net/images/anime/10/47347.jpg" alt="Attack on Titan">
        <h3>Attack on Titan</h3>
      </a>
      <a href="demon-slayer.html" class="anime-card">
        <img src="https://cdn.myanimelist.net/images/anime/1208/94745.jpg" alt="Demon Slayer">
        <h3>Demon Slayer</h3>
      </a>
      <a href="jujutsu-kaisen.html" class="anime-card">
        <img src="https://cdn.myanimelist.net/images/anime/1160/109947.jpg" alt="Jujutsu Kaisen">
        <h3>Jujutsu Kaisen</h3>
      </a>
      <a href="jujutsu-kaisen-s2.html" class="anime-card">
        <img src="https://cdn.myanimelist.net/images/anime/1513/117355.jpg" alt="Jujutsu Kaisen 2nd Season">
        <h3>Jujutsu Kaisen 2nd Season</h3>
      </a>
      <a href="my-hero-academia.html" class="anime-card">
        <img src="https://cdn.myanimelist.net/images/anime/1575/105763.jpg" alt="My Hero Academia">
        <h3>My Hero Academia</h3>
      </a>
      <a href="chainsaw-man.html" class="anime-card">
        <img src="https://cdn.myanimelist.net/images/anime/1987/117512.jpg" alt="Chainsaw Man">
        <h3>Chainsaw Man</h3>
      </a>
      <a href="tokyo-revengers.html" class="anime-card">
        <img src="https://cdn.myanimelist.net/images/anime/1223/126488.jpg" alt="Tokyo Revengers">
        <h3>Tokyo Revengers</h3>
      </a>
      <a href="spy-x-family.html" class="anime-card">
        <img src="https://cdn.myanimelist.net/images/anime/1517/109840.jpg" alt="Spy x Family">
        <h3>Spy x Family</h3>
      </a>
      <a href="solo-leveling.html" class="anime-card">
        <img src="https://static.wikia.nocookie.net/solo-leveling/images/7/72/Solo_Leveling_Logo.png" alt="Solo Leveling">
        <h3>Solo Leveling</h3>
      </a>
    </div>
  </div>

  <aside class="sidebar">
    <h3>🔥 Top Anime</h3>
    <ul class="top-anime">
      <li onclick="location.href='attack-on-titan.html'">Attack on Titan</li>
      <li onclick="location.href='jujutsu-kaisen.html'">Jujutsu Kaisen</li>
      <li onclick="location.href='solo-leveling.html'">Solo Leveling</li>
      <li onclick="location.href='my-hero-academia.html'">My Hero Academia</li>
      <li onclick="location.href='chainsaw-man.html'">Chainsaw Man</li>
      <li onclick="location.href='spy-x-family.html'">Spy x Family</li>
    </ul>
  </aside>
</div>

<footer>
  &copy; 2025 Bland Mist Anime. Powered by Rifat Souls 😎😎😎
</footer>

<script>
function searchAnime() {
  const input = document.getElementById('searchInput').value.toLowerCase();
  const cards = document.querySelectorAll('.anime-card');
  cards.forEach(card => {
    const title = card.querySelector('h3').textContent.toLowerCase();
    card.style.display = title.includes(input) ? 'block' : 'none';
  });
}
</script>

</body>
</html>
"""

file_name = "bland_mist_anime.html"
with open(file_name, "w", encoding="utf-8") as f:
    f.write(html)

webbrowser.open(f"file://{os.path.abspath(file_name)}")
print("✅ Homepage with Top Anime List created and opened!")