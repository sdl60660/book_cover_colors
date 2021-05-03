# Book Cover Colors

Some pre-processing to extract the main color of each book cover in [this dataset](https://www.kaggle.com/lukaanicin/book-covers-dataset), before visualizing the data in [this Observable notebook](https://observablehq.com/@sdl60660/book-cover-colors).

The extracted colors are eventually rounded to a set of eleven distinct colors, using CIEDE2000 Color Distance and then grouped and visualized, by genre. Might expand this a little in the future, if I find some more interesting patterns, but pretty simple and straightforward as it is.

Some future areas of exploration would be:
* Scraping the release years or each book in the dataset and looking for patterns between decade of release and use of colors.
* Extracting title size data or other data about text on the cover (e.g. how many non-title words) and looking for correlations with genre/release year.
