import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import json

def tirets(titre):
    return titre.replace("-", " ").lower()

def create_html_page():
    title = title_text.get("1.0", "end-1c").strip()
    image_name = title.upper()
    anime_link = link_text.get("1.0", "end-1c").strip()
    genres = genres_text.get("1.0", "end-1c").strip()
    review_date = review_date_text.get("1.0", "end-1c").strip()
    critique = critique_text.get("1.0", "end-1c").strip()
    synopsis = synopsis_text.get("1.0", "end-1c").strip()
    selected_page_type = page_type_var.get()
    if selected_page_type == "Anime":
        num_episodes = episodes_text.get("1.0", "end-1c").strip()
        num_seasons = seasons_text.get("1.0", "end-1c").strip()
        status = status_text.get("1.0", "end-1c").strip()
        air_date = date_text.get("1.0", "end-1c").strip()
        opening_rating = opening_text.get("1.0", "end-1c").strip()
        ending_rating = ending_text.get("1.0", "end-1c").strip()
        note_finale = final_text_anime.get("1.0", "end-1c").strip()

        html_content = generate_anime_html_page(title, image_name, note_finale, anime_link, genres, num_episodes, num_seasons, status, air_date, opening_rating, ending_rating, review_date, critique, synopsis)
    elif selected_page_type == "Film":
        ost_rating = OST_text.get("1.0", "end-1c").strip()
        air_date = air_date_text.get("1.0", "end-1c").strip()
        note_finale = final_text_film.get("1.0", "end-1c").strip()

        html_content = generate_film_html_page(title, image_name, critique, synopsis, review_date, genres, ost_rating, air_date, anime_link, note_finale)

    new_anime = {
        "name": title,
        "image": image_name + ".jpg",
        "rating": note_finale,
        "genre": ", ".join(genres.split(", ")[:3])
    }

    update_json_file(new_anime)

    with open(f"{tirets(title)}.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    messagebox.showinfo("Success", "Page HTML créée avec succès!")

def update_json_file(new_anime):
    with open("animes.json", "r+", encoding="utf-8") as file:
        anime_list = json.load(file)
        anime_list.append(new_anime)
        file.seek(0)
        json.dump(anime_list, file, indent=4)

def generate_anime_html_page(title, image_name, note_finale, anime_link, genres, num_episodes, num_seasons, status, air_date, opening_rating, ending_rating, review_date, critique, synopsis):
    template = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" type="image/png" href="logo.png">
    <link rel="stylesheet" href="anime.css">
    <title>{title}</title>
</head>
<body>
    <div class="container">
        <h2>{title}</h2>
        <img src="images_Animes/{title.upper()}.JPG" alt="Image de l'anime">
        <div class="info-box">
            <div class="rating">
                {note_finale}/10
            </div>
            <p>Lien de l'anime : <a href="https://anime-sama.fr/catalogue/{anime_link}/">{title}</a></p>
            <p>Genres : <span class="genre-info">{genres}</span></p>
            <p>Nombre d'épisodes : <span class="episode-info">{num_episodes}</span> <br> Nombre de saisons : <span class="episode-info">{num_seasons}</span></p>
            <p>Statut : <span class="status-info">{status}</span> <br> Date de diffusion : <span class="date-info">{air_date}</span></p>
            <p>Opening : <span class="opening-info">{opening_rating}/10</span> <br> Ending : <span class="ending-info">{ending_rating}/10</span></p>
            <p>Date de la critique : <span class="date-info">{review_date}</span></p>
        </div>
        <div class="review-box">
            <p class="title">Critique de l'anime</p>
            <p>{critique}</p>
            <p class="title">Synopsis</p>
            <p>{synopsis}</p>
        </div>
        <p><a href="index.html">Revenir à la page d'accueil</a></p>

    </div>
</body>
</html>"""
    return template

def generate_film_html_page(title, image_name, critique, synopsis, review_date, genres, ost_rating, air_date, anime_link, note_finale):
    template = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="anime.css">
    <link rel="icon" type="image/png" href="logo.png">
    <title>{title}</title>
</head>
<body>
    <div class="container">
        <h2>{title}</h2>
        <img src="images_Animes/{image_name.upper()}.jpg" alt="Image du film">
        <div class="info-box">
            <div class="rating">
                {note_finale}/10
            </div>
            <p>Lien de l'anime : <a href="https://anime-sama.fr/catalogue/{anime_link}/">{title}</a></p>
            <p>Genres : <span class="genre-info">{genres}</span></p>
            <p>OST : <span class="opening-info">{ost_rating}/10</span></p>
            <p>Date de diffusion : <span class="date-info">{air_date}</span></p>
            <p>Date de la critique : <span class="date-info">{review_date}</span></p>
        </div>
        <div class="review-box">
            <p class="title">Critique du film</p>
            <p>{critique}</p>
            <p class="title">Synopsis</p>
            <p>{synopsis}</p>
        </div>
        <p><a href="index.html">Revenir à la page d'accueil</a></p>

    </div>
</body>
</html>"""
    return template

root = tk.Tk()
root.title("Créateur de page HTML pour le site de critiques")
root.configure(bg="#000")
style = ttk.Style()
style.configure('Custom.TButton', foreground='#ffa500', background='#000', font=('Arial', 16))

page_type_var = tk.StringVar(root, "Anime")

page_type_label = ttk.Label(root, text="Type de page:", foreground='#ffa500', background='#000', font=('Arial', 16))
page_type_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)

page_type_dropdown = ttk.Combobox(root, textvariable=page_type_var, values=["Anime", "Film"], state="readonly")
page_type_dropdown.grid(row=0, column=1, padx=10, pady=10)

title_label = ttk.Label(root, text="Titre:", foreground='#ffa500', background='#000', font=('Arial', 16))
title_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)
title_text = tk.Text(root, height=1, width=40, font=('Arial', 14), background='#111', foreground='#ffa500')
title_text.grid(row=1, column=1, padx=10, pady=10)

link_label = ttk.Label(root, text="Lien de l'anime:", foreground='#ffa500', background='#000', font=('Arial', 16))
link_label.grid(row=2, column=0, sticky="w", padx=10, pady=10)
link_text = tk.Text(root, height=1, width=40, font=('Arial', 14), background='#111', foreground='#ffa500')
link_text.grid(row=2, column=1, padx=10, pady=10)

genres_label = ttk.Label(root, text="Genres:", foreground='#ffa500', background='#000', font=('Arial', 16))
genres_label.grid(row=3, column=0, sticky="w", padx=10, pady=10)
genres_text = tk.Text(root, height=1, width=40, font=('Arial', 14), background='#111', foreground='#ffa500')
genres_text.grid(row=3, column=1, padx=10, pady=10)

def toggle_input_fields(event):
    selected_page_type = page_type_var.get()
    if selected_page_type == "Anime":
        episodes_label.grid()
        episodes_text.grid()
        seasons_label.grid()
        seasons_text.grid()
        status_label.grid()
        status_text.grid()
        date_label.grid()
        date_text.grid()
        opening_label.grid()
        opening_text.grid()
        ending_label.grid()
        ending_text.grid()
        final_label_anime.grid()
        final_text_anime.grid()
        final_label_film.grid_remove()
        final_text_film.grid_remove()
        OST_label.grid_remove()
        OST_text.grid_remove()
        air_date_label.grid_remove()
        air_date_text.grid_remove()
    elif selected_page_type == "Film":
        episodes_label.grid_remove()
        episodes_text.grid_remove()
        seasons_label.grid_remove()
        seasons_text.grid_remove()
        status_label.grid_remove()
        status_text.grid_remove()
        date_label.grid_remove()
        date_text.grid_remove()
        opening_label.grid_remove()
        opening_text.grid_remove()
        ending_label.grid_remove()
        ending_text.grid_remove()
        final_label_anime.grid_remove()
        final_text_anime.grid_remove()
        final_label_film.grid()
        final_text_film.grid()
        OST_label.grid()
        OST_text.grid()
        air_date_label.grid()
        air_date_text.grid()

page_type_dropdown.bind("<<ComboboxSelected>>", toggle_input_fields)

episodes_label = ttk.Label(root, text="Nombre d'épisodes:", foreground='#ffa500', background='#000', font=('Arial', 16))
episodes_label.grid(row=4, column=0, sticky="w", padx=10, pady=10)
episodes_text = tk.Text(root, height=1, width=40, font=('Arial', 14), background='#111', foreground='#ffa500')
episodes_text.grid(row=4, column=1, padx=10, pady=10)

seasons_label = ttk.Label(root, text="Nombre de saisons:", foreground='#ffa500', background='#000', font=('Arial', 16))
seasons_label.grid(row=5, column=0, sticky="w", padx=10, pady=10)
seasons_text = tk.Text(root, height=1, width=40, font=('Arial', 14), background='#111', foreground='#ffa500')
seasons_text.grid(row=5, column=1, padx=10, pady=10)

status_label = ttk.Label(root, text="Statut:", foreground='#ffa500', background='#000', font=('Arial', 16))
status_label.grid(row=6, column=0, sticky="w", padx=10, pady=10)
status_text = tk.Text(root, height=1, width=40, font=('Arial', 14), background='#111', foreground='#ffa500')
status_text.grid(row=6, column=1, padx=10, pady=10)

date_label = ttk.Label(root, text="Date de diffusion:", foreground='#ffa500', background='#000', font=('Arial', 16))
date_label.grid(row=7, column=0, sticky="w", padx=10, pady=10)
date_text = tk.Text(root, height=1, width=40, font=('Arial', 14), background='#111', foreground='#ffa500')
date_text.grid(row=7, column=1, padx=10, pady=10)

opening_label = ttk.Label(root, text="Note d'opening (sur 10):", foreground='#ffa500', background='#000', font=('Arial', 16))
opening_label.grid(row=8, column=0, sticky="w", padx=10, pady=10)
opening_text = tk.Text(root, height=1, width=40, font=('Arial', 14), background='#111', foreground='#ffa500')
opening_text.grid(row=8, column=1, padx=10, pady=10)

ending_label = ttk.Label(root, text="Note d'ending (sur 10):", foreground='#ffa500', background='#000', font=('Arial', 16))
ending_label.grid(row=9, column=0, sticky="w", padx=10, pady=10)
ending_text = tk.Text(root, height=1, width=40, font=('Arial', 14), background='#111', foreground='#ffa500')
ending_text.grid(row=9, column=1, padx=10, pady=10)

final_label_anime = ttk.Label(root, text="Note finale (sur 10):", foreground='#ffa500', background='#000', font=('Arial', 16))
final_label_anime.grid(row=10, column=0, sticky="w", padx=10, pady=10)
final_text_anime = tk.Text(root, height=1, width=40, font=('Arial', 14), background='#111', foreground='#ffa500')
final_text_anime.grid(row=10, column=1, padx=10, pady=10)

final_label_film = ttk.Label(root, text="Note finale (sur 10):", foreground='#ffa500', background='#000', font=('Arial', 16))
final_label_film.grid(row=11, column=0, sticky="w", padx=10, pady=10)
final_text_film = tk.Text(root, height=1, width=40, font=('Arial', 14), background='#111', foreground='#ffa500')
final_text_film.grid(row=11, column=1, padx=10, pady=10)

OST_label = ttk.Label(root, text="OST:", foreground='#ffa500', background='#000', font=('Arial', 16))
OST_label.grid(row=12, column=0, sticky="w", padx=10, pady=10)
OST_text = tk.Text(root, height=1, width=40, font=('Arial', 14), background='#111', foreground='#ffa500')
OST_text.grid(row=12, column=1, padx=10, pady=10)

air_date_label = ttk.Label(root, text="Date de diffusion:", foreground='#ffa500', background='#000', font=('Arial', 16))
air_date_label.grid(row=13, column=0, sticky="w", padx=10, pady=10)
air_date_text = tk.Text(root, height=1, width=40, font=('Arial', 14), background='#111', foreground='#ffa500')
air_date_text.grid(row=13, column=1, padx=10, pady=10)

review_date_label = ttk.Label(root, text="Date de la critique:", foreground='#ffa500', background='#000', font=('Arial', 16))
review_date_label.grid(row=14, column=0, sticky="w", padx=10, pady=10)
review_date_text = tk.Text(root, height=1, width=40, font=('Arial', 14), background='#111', foreground='#ffa500')
review_date_text.grid(row=14, column=1, padx=10, pady=10)

critique_label = ttk.Label(root, text="Critique:", foreground='#ffa500', background='#000', font=('Arial', 16))
critique_label.grid(row=15, column=0, sticky="w", padx=10, pady=10)
critique_text = tk.Text(root, height=5, width=30, foreground='#ffa500', background='#111', font=('Arial', 14))
critique_text.grid(row=15, column=1, padx=10, pady=10)

synopsis_label = ttk.Label(root, text="Synopsis:", foreground='#ffa500', background='#000', font=('Arial', 16))
synopsis_label.grid(row=16, column=0, sticky="w", padx=10, pady=10)
synopsis_text = tk.Text(root, height=5, width=30, foreground='#ffa500', background='#111', font=('Arial', 14))
synopsis_text.grid(row=16, column=1, padx=10, pady=10)

create_button = tk.Button(root, text="Créer la page HTML", bg="#000", fg="#ffa500", activebackground="#000", highlightbackground="#000", command=create_html_page)
create_button.grid(row=17, columnspan=2, pady=10)

root.mainloop()
