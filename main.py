from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


@app.get('/blog') # '/' is base path, .get is operation on the path, @app is path operation decorator
def index(limit=10, published:bool = True, sort: Optional[str] = None): # this is the path operation function
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}

@app.get('/blog/{id}') # dynamic routes
def show(id: int): # you have to accept variable inside the function
    return {'data': id}

# @app.get('/blog/unpublished') #this can't work here because of dynamic routing. Move above dynamic routes.
# def unpublished(id)

@app.get('blog/{id}/comments')
def comments(id):
    return {'data': 'comments'}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]
    

@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f"Blog is created with a title as {blog.title}"}

# if __name__ == '__main__':
#     uvicorn.run(app,host='localhost',port=9000)

