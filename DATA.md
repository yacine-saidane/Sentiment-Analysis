# Data card

## Datasets
| Dataset | Reviews | Positive / negative | Role |
|---|---|---|---|
| IMDB 50k (Maas et al., 2011) | 49,582 after deduplication | 24,884 / 24,698 | Train, validation, test |
| Pang & Lee polarity v2.0 (2004) | 2,000 | 1,000 / 1,000 | External test |
| Own reviews (TMDB) | 300 | 150 / 150 | Real-world test only |

## Own reviews
- Source: TMDB API, retrieved on <date>. This product uses the TMDB API but is not endorsed or certified by TMDB.
- Label: reviewer's rating on a 10-point scale, >= 7 positive, <= 4 negative, others discarded.
- 215 films (2016-2026), 8 genres, at most 6 reviews per film, 20-300 words.
- Hard cases: VADER polarity contradicts the rating (95 of 300).
- Agreement: second annotator on 50 reviews, kappa = 0.96.
- Files kept local, not published (see .gitignore).