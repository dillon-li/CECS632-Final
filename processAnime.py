import csv

f = open('anime_formatted.csv','w')
writer = csv.writer(f)

genres = [
        'Action',
        'Adventure',
        'Cars',
        'Comedy',
        'Dementia',
        'Demons',
        'Drama',
        'Ecchi',
        'Fantasy',
        'Game',
        'Harem',
        'Hentai',
        'Historical',
        'Horror',
        'Josei',
        'Kids',
        'Magic',
        'Martial Arts',
        'Mecha',
        'Military',
        'Music',
        'Mystery',
        'Parody',
        'Police',
        'Psychological',
        'Romance',
        'Samurai',
        'School',
        'Sci-Fi',
        'Seinen',
        'Shoujo',
        'Shoujo Ai',
        'Shounen',
        'Shounen Ai',
        'Slice of Life',
        'Space',
        'Sports',
        'Super Power',
        'Supernatural',
        'Thriller',
        'Vampire',
        'Yaoi',
        'Yuri'
        ]

nos = []
for item in genres:
    nos.append(0)

with open('anime.csv','rb') as csvfile:
    reader = csv.reader(csvfile)
    firstrow = reader.next()
    firstrow.pop(2)
    fullHeader = firstrow + genres
    writer.writerow(fullHeader)
    #print(fullHeader)
    for row in reader:
        badData = False
        rowList = [
                row[0],
                row[1],
                row[3],
                row[4],
                row[5],
                row[6]
                ]
        rowList = rowList + nos
        print(rowList)
        g = row[2]
        genre_split = g.split(',')
        for genre in genre_split:
            genre = genre.strip()
            try:
                place = fullHeader.index(genre)
                rowList[place] = 1
            except:
                badData = True
                print("Bad Entry")
        if not badData:
            writer.writerow(rowList)
