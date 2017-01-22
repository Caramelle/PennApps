import giphypop
from analysis import get_phrases
from findText import find_text

def fetch_gifs(url) :
	g = giphypop.Giphy()

	# scrape slides for text.
	# results are written into "slideTexts.txt".
	find_text(url)

	gifs = []
	slide_keywords = get_phrases("slideTexts.txt")

	for slide in slide_keywords:
		gifs.append([])
		list_size = len(slide)
		if (list_size == 0):
			continue

		# select 9 gifs for every slide
		for i in range (0,9):
			gif_phrase = slide[i % list_size]
			image = giphypop.translate(gif_phrase)
			if (image is None):
				i -= 1
				continue
			gifs[-1].append(image.fixed_height.downsampled.url)
			del image
	return gifs

fetch_gifs('https://docs.google.com/presentation/d/12yAQx0zVYam0Dlyg4C2P-eWLPFFvRd4U6AcWc2W-NIU/edit')
