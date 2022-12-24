# Movie Stats Data Analysis

**Data analysis on movie based on [Naver Movie](https://movie.naver.com/) to find whether the movie related comments 
influence the South Korean market compared to other global movie markets.**

![Python](https://img.shields.io/badge/Python-3.8-6db33f?logo=Python&style=flat)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](LICENSE)

## Websites Used
- <a href="https://www.worldometers.info/world-population/population-by-country/">worldometers</a>
- <a href="https://www.the-numbers.com/">The-Numbers</a>
- <a href="https://movie.naver.com/">Naver Movie</a>

## Motivation
Movie industry is huge. However, movies make a lot of profit from one country, while it does not in other countries.
There are many reasons to this such as culture, timing, population, etc. Out of these, I wanted to experiment to find
out if the movie review comments has any effects on the movie's profit in a specific country. As I wish to only figure
out a movie review platform's impact, I neglected other components that could affect my experiment such as population by
dividing the total profit of a movie by its population. I also compared South Korea with **G20** and **OECD** countries 
as I target on ignoring the data from developing countries.

## Conclusion

The Naive Bayes classifier accuracy was **68.59%**, meaning that Naver Movie review platform did not impact a movie's 
profit. This could mean other countries are same as well. However, there are many uncertainties in this experiment,
meaning that other experiments could go more deep into it and improve on this result.

## How it Works

### 0️⃣ Dependency Installation

```
pip install -r requirements.txt
```

### 1️⃣ Scrape Movie Statistics

```
python scrape_movie_stats.py
```

### 2️⃣ Preprocess Movie Statistics

#### Analysis Record
- Movie Name
- South Korea's Ratio
- Other Countries' Ratio
- Result (1 or 0)

#### South Korean Ratio Formula

![](https://latex.codecogs.com/svg.image?\frac{x}{y})

- x = South Korea's profit
- y = South Korea's population

#### Other Countries' Ratio Formula

![](https://latex.codecogs.com/svg.image?\frac{\sum^n_{i=0}&space;\frac{x_i}{y_i}}{n})

- x = Other countries' profit
- y = Other countries' population
- n = Total number of other countries

```
python preprocess_movie_stats.py
```

### 3️⃣ Scrape Movie Comments

```
python scrape_movie_comments.py
```

### 4️⃣ Train & Test

```
python train_test.py
```