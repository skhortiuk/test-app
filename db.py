import os

import pymongo

host, port = os.getenv("mongodb_host", "127.0.0.1"), os.getenv("mongodb_port", 27017)
connect = pymongo.MongoClient(host, port)
collection = connect["Users"]["Views"]


def get_view_stats():
    pattern = "IP address: {ipAddress}, views: {views}."
    views = collection.find(projection=["ipAddress", "views"])
    return "\n".join(pattern.format(**view) for view in views)


def increase_views_count(request):
    collection.update(
        {
            "ipAddress": request.remote_addr
        },
        {
            "$inc": {"views": 1}
        },
        upsert=True
    )
