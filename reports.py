from ORM import MongoDB


db = MongoDB(
    database_name='quake',
    collection_name='games'
)
db.collection.find()
