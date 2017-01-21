import giphypop
import analysis

g = giphypop.Giphy()
gifs = []
keyword = 'coffee'
for i in range (0,9):
	image = giphypop.translate(keyword)
	gifs.append(image.fixed_height.downsampled.url)
	del image
print gifs
