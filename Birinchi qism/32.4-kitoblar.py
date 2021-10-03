my_books = ['sariq devni minib', 'dunyoning ishlari', 'shum bola', 'kichkina shahzoda']

book = input('Kitob nomi: ')

if book.lower() in my_books:
	print('Bu kitobni o\'qiganman!')
else:
	print('Bu kitobni o\'qimaganman')