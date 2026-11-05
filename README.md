# Horror Movie Roulette

A modern horror movie discovery website that takes the indecision out of choosing what to watch.

Explore thousands of horror films, narrow your search with custom filters, or let the roulette choose your next nightmare.

**[Launch Horror Movie Roulette](https://drdavidreed.github.io/horror-movie-roulette/)**

---

## Preview

![Horror Movie Roulette website preview](screenshot.png)

---

## Features

- **Movie Roulette** — Get a random horror movie recommendation based on your selected filters.
- **Extensive Catalogue** — Explore over 7,000 horror films, from popular releases to hidden gems.
- **Subgenre Discovery** — Browse paranormal, slasher, psychological, found footage and other horror categories.
- **Custom Filters** — Refine recommendations by release period and minimum TMDB rating.
- **Movie Details** — View posters, descriptions, release years and community ratings.
- **Watched Tracking** — Mark films as watched and exclude them from future recommendations.
- **Responsive Interface** — Designed for desktop, tablet and mobile devices.
- **Local Storage** — Keep your watched history saved in your browser without an account.

## Technology

| Technology | Purpose |
| --- | --- |
| HTML5 | Website structure |
| CSS3 | Responsive layout and styling |
| JavaScript | Roulette, filtering and watched tracking |
| Python | Movie catalogue generation |
| TMDB API | Movie metadata and posters |
| GitHub Pages | Website hosting |
| GitHub Actions | Optional automated catalogue updates |

The frontend is built without a JavaScript framework or backend database.

## Getting Started

### Use the live website

Visit **[Horror Movie Roulette](https://drdavidreed.github.io/horror-movie-roulette/)** to start discovering movies.

### Run locally

Clone the repository:

```bash
git clone https://github.com/DrDavidReed/horror-movie-roulette.git
cd horror-movie-roulette
```

Start a local development server:

```bash
python3 -m http.server 8000
```

Open `http://localhost:8000` in your browser.

The website loads its movie catalogue from `data/movies.json`.

## Movie Catalogue

Movie information is sourced from [The Movie Database (TMDB)](https://www.themoviedb.org/).

The catalogue is stored locally as JSON, allowing visitors to browse movies without supplying an API key. A Python script can regenerate the catalogue, and GitHub Actions can be configured to automate updates.

API credentials should be stored in GitHub repository secrets rather than committed to the repository.

## Watched History

Watched movies are stored in your browser using local storage. Your selections persist between visits on the same browser, but they are not automatically synchronised between devices. Clearing browser data may remove your history.

## Attribution

This product uses the TMDB API but is not endorsed or certified by TMDB.

Movie artwork and metadata are provided by TMDB and their respective rights holders.

## Author

Created by **[DrDavidReed](https://github.com/DrDavidReed)**.

[Live Website](https://drdavidreed.github.io/horror-movie-roulette/) | [GitHub Repository](https://github.com/DrDavidReed/horror-movie-roulette/)
