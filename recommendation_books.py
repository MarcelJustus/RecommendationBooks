import goodreads
from goodreads import client
import pandas as pd

def prepare_data():
    """gets the data from files "books_dataset%d.csv", d in range (1,6)
    cleans it to keep only useful data
    """

    books_df = pd.concat([pd.read_csv("/Users/carlamartin/Desktop/books_datasets/books_dataset_%d.csv" %id) for id in range(1,6)], ignore_index=True)
    books_df.set_index('id')

    #drop useless columns
    del books_df['asin']
    del books_df['buy_links']
    del books_df['format']
    del books_df['isbn13']
    del books_df['kindle_asin']
    del books_df['marketplace_id']
    del books_df['public_document']
    del books_df['reviews_widget']
    del books_df['small_image_url']

    #prepare column author
    authors = books_df['authors']
    authors_name = []
    for a in authors:
        try:
            start = str(a).find('name')+8
            i = start
            name = ''
            while(a[i]!='\''):
                name = name+a[i]
                i+=1
            authors_name.append(name)
        except:
            authors_name.append(a)
    books_df['authors']=authors_name

    #popular_shelves extract main genre
    
    return books_df

books_df = prepare_data()

print(books_df.info())

