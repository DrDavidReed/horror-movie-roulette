# 🎬 Horror Movie Roulette

**Can't decide what horror movie to watch? Let fate choose your next nightmare.**

Horror Movie Roulette is a free, responsive horror movie discovery website built with HTML, CSS and JavaScript.

Explore thousands of horror films, filter by your favourite subgenres, discover hidden gems, or spin the roulette to find something terrifying to watch.

Created by **[DrDavidReed](https://github.com/DrDavidReed)**.

### 🔴 [Launch Horror Movie Roulette](https://drdavidreed.github.io/horror-movie-roulette/)

---

## 📸 Screenshot

![Horror Movie Roulette Screenshot](screenshot.png)

---

## ✨ Features

- 🎲 **Movie Roulette** — Can't decide what to watch? Let the roulette choose a random horror film.
- 🎭 **Horror Subgenres** — Explore paranormal, slasher, psychological, found footage and other horror categories.
- 🔎 **Advanced Filtering** — Filter movies by release period and minimum TMDB rating.
- 🎞️ **7,000+ Horror Movies** — Browse a large catalogue of horror films, including popular releases and hidden gems.
- ⭐ **Movie Information** — View posters, descriptions, release years and community ratings.
- 👁️ **Watched Tracking** — Mark films you've watched and exclude them from future recommendations.
- 📱 **Responsive Design** — Designed for desktop, tablet and mobile.
- 🌑 **Minimal Black Theme** — A clean, dark interface with subtle red accents.
- 🔄 **Catalogue Updates** — Supports automated catalogue generation using GitHub Actions.

---

## 🛠️ Built With

- **HTML5** — Website structure
- **CSS3** — Styling and responsive layouts
- **JavaScript** — Roulette, filtering and watched tracking
- **TMDB API** — Movie information, posters and ratings
- **GitHub Pages** — Website hosting
- **GitHub Actions** — Optional automated catalogue updates

No frontend framework or database is required.

---

## 🚀 Getting Started

### View the website

Visit:

https://drdavidreed.github.io/horror-movie-roulette/

### Run locally

1. Clone the repository:

   `git clone https://github.com/DrDavidReed/horror-movie-roulette.git`

2. Enter the project directory:

   `cd horror-movie-roulette`

3. Start a local web server:

   `python3 -m http.server 8000`

4. Open your browser and visit:

   `http://localhost:8000`

The website loads movie information from `data/movies.json`.

---

## 🎲 How It Works

1. Choose your preferred horror subgenre.
2. Select a release period.
3. Adjust the minimum TMDB rating.
4. Click **Spin the Roulette**.
5. Discover your next horror movie!

Already watched the recommendation? Mark it as watched and spin again.

The catalogue combines popular horror movies with lesser-known titles, giving you a chance to discover something you might otherwise miss.

---

## 🔐 TMDB Integration

Movie information is sourced from **The Movie Database (TMDB)**.

The website uses a pre-generated JSON catalogue rather than requiring visitors to enter an API key.

The catalogue can be refreshed using a Python generator and GitHub Actions, with the TMDB API key stored securely as a repository secret named `TMDB_API_KEY`.

**This product uses the TMDB API but is not endorsed or certified by TMDB.**

Movie posters, descriptions and ratings belong to their respective owners and data providers.

TMDB: https://www.themoviedb.org/

---

## 💾 Watched Movies

Watched-film tracking uses your browser's local storage.

This means:

- Your watched movies remain saved between visits on the same browser.
- No account or login is required.
- Your watched list is not automatically synchronised between devices.
- Clearing browser storage may remove your watched history.

---

## 📱 Device Compatibility

Horror Movie Roulette uses responsive layouts to support:

- Desktop computers
- Laptops
- Tablets
- Mobile phones

The interface automatically adapts to different screen sizes.

---

## 🌐 Live Website

**[Horror Movie Roulette](https://drdavidreed.github.io/horror-movie-roulette/)**

---

## 👨‍💻 Author

Created by **DrDavidReed**.

GitHub: https://github.com/DrDavidReed

---

*Your next nightmare is only one spin away.*
