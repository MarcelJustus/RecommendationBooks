import goodreads
from goodreads import client
import pandas as pd

gc = client.GoodreadsClient('CDUrvt2ZhSNCO4kD8CrZeg', '4ylsiMWVlCmjz34kLt4fEOROOhMd1kj6pv3ioAbj0')
books_data=[]

for k in range(1,50001):
    if(k%10000==0): 
        books_df = pd.DataFrame(books_data)
        id = k/10000
        books_df.to_csv('books_dataset_%d.csv' %id)
        books_data=[]
    try:
        books_data.append(dict(gc.book(k).__dict__['_book_dict']))
    except:
        continue
