import webbrowser
import os


def create_anime_page(title, image_url, description, file_name):
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      <title>{title}</title>
      <style>
        body {{
          background-color: black;
          color: red;
          font-family: 'Segoe UI', sans-serif;
          text-align: center;
          padding: 20px;
        }}
        img {{
          width: 300px;
          border: 2px solid red;
          border-radius: 10px;
          margin-top: 20px;
        }}
        video {{
          width: 90%;
          max-width: 600px;
          border: 2px solid red;
          border-radius: 10px;
          margin-top: 20px;
        }}
        a {{
          display: inline-block;
          margin-top: 30px;
          color: red;
          background: #1a1a1a;
          padding: 10px 20px;
          text-decoration: none;
          border-radius: 6px;
        }}
        a:hover {{
          background: red;
          color: black;
        }}
      </style>
    </head>
    <body>
      <h1>{title}</h1>
      <img src="{image_url}" alt="{title}" />

      <p>{description}</p>

      <video controls>
        <source src="my-anime.mp4" type="video/mp4" />
        Your browser does not support the video tag.
      </video>

      <a href="bland_mist_anime.html">🔙 Back to Home</a>
    </body>
    </html>
    """

    with open(file_name, "w", encoding="utf-8") as f:
        f.write(html)
    file_path = os.path.abspath(file_name)
    webbrowser.open(f"file://{file_path}")
    print(f"✅ '{file_name}' page created and opened!")


# Create pages for each anime
create_anime_page(
    "Jujutsu Kaisen",
    "https://cdn.myanimelist.net/images/anime/1160/109947.jpg",
    "Follow Yuji Itadori as he joins the world of curses and sorcery to save humanity.",
    "jujutsu-kaisen.html"
)

create_anime_page(
    "My Hero Academia",
    "https://cdn.myanimelist.net/images/anime/1575/105763.jpg",
    "Join Izuku Midoriya and classmates at U.A. High as they train to become pro heroes.",
    "my-hero-academia.html"
)

create_anime_page(
    "Chainsaw Man",
    "https://cdn.myanimelist.net/images/anime/1987/117512.jpg",
    "Experience Denji's dark journey fighting devils with his chainsaw powers.",
    "chainsaw-man.html"
)

create_anime_page(
    "Tokyo Revengers",
    "https://cdn.myanimelist.net/images/anime/1223/126488.jpg",
    "Takemichi travels back in time to save his friends and change the future.",
    "tokyo-revengers.html"
)

create_anime_page(
    "Spy x Family",
    "https://cdn.myanimelist.net/images/anime/1517/109840.jpg",
    "Follow the spy Twilight and his unusual family as they undertake secret missions.",
    "spy-x-family.html"
)
