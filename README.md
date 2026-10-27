# cdrischler.github.io

Source for **[cdrischler.github.io](https://cdrischler.github.io)**, the academic website of Christian Drischler, Assistant Professor of Physics at Ohio University's [Institute of Nuclear and Particle Physics](https://inpp.ohio.edu/~inpp/). Research: nuclear theory, neutron stars, the nuclear equation of state, and Bayesian uncertainty quantification.

Research, publications, talks, teaching, and the research group are all on the website. The complete publication list is on [INSPIRE-HEP](https://inspirehep.net/authors/1405840?ui-citation-summary=true).

## Where things live

| Page | File |
|---|---|
| Home (about, group, news) | `_pages/about.md` |
| Research | `_pages/research.md` |
| Publications | `_pages/publications.md` |
| CV | `_pages/cv.md` |
| Teaching | `_pages/teaching.md` |
| Talks | `_pages/talks.md` |
| Navigation menu | `_data/navigation.yml` |
| Sidebar profile and site settings | `_config.yml` |
| Profile photo | `images/profile.jpg` |

## Talk map

The map on the Talks page is `_talks/map.html`, which reads `_talks/org-locations.js`. To add a single city, append an entry like `["City, ST, USA", latitude, longitude]` to `_talks/org-locations.js`, and add the city to `talk_location_data.txt` so the list stays in sync.

To regenerate all coordinates, run `talkmap.ipynb` (it geocodes `talk_location_data.txt`), then copy only `talkmap/org-locations.js` into `_talks/`. Don't copy `talkmap/map.html`; it is the old template version.

## Preview locally

```bash
bundle install
bundle exec jekyll serve -l -H localhost   # http://localhost:4000
```

Or with Docker: `docker compose up`.

GitHub Pages rebuilds the site automatically on every push to `master`.

## Credits

Built with [Jekyll](https://jekyllrb.com) and [AcademicPages](https://github.com/academicpages/academicpages.github.io), a fork of [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) (MIT License; see `LICENSE`). The talk map uses [Leaflet](https://leafletjs.com) and [Leaflet.markercluster](https://github.com/Leaflet/Leaflet.markercluster).
