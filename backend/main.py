from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
import httpx
from typing import List, Optional
from pydantic import BaseModel, Field

app = FastAPI()
# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React app's URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

GOOGLE_BOOKS_API_URL = "https://www.googleapis.com/books/v1/volumes"

# Define response models for better documentation
class PaginationMetadata(BaseModel):
    total_items: int
    current_page: int
    total_pages: int
    results_per_page: int
    has_next_page: bool
    has_previous_page: bool

class BookSearchResponse(BaseModel):
    items: List[dict] = Field(default_factory=list)
    pagination: PaginationMetadata

@app.get("/")
async def health_check():
    return {"status": "ok"}

@app.get("/books")
async def get_all_books(
    q: str, 
    page: int = Query(1, ge=1, description="Page number, starting from 1"), 
    results_per_page: int = Query(10, ge=1, le=40, description="Number of results per page (max 40)")
):
    # Calculate start index for pagination
    start_index = (page - 1) * results_per_page
    
    params = {
        "q": q,
        "startIndex": start_index,
        "maxResults": results_per_page
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.get(GOOGLE_BOOKS_API_URL, params=params)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error fetching data from Google Books API")
        
        data = response.json()
        total_items = data.get("totalItems", 0)
        total_pages = (total_items + results_per_page - 1) // results_per_page  # Ceiling division
        
        # Create pagination metadata
        pagination = {
            "total_items": total_items,
            "current_page": page,
            "total_pages": total_pages,
            "results_per_page": results_per_page,
            "has_next_page": page < total_pages,
            "has_previous_page": page > 1
        }
        
        # Restructure the response to include pagination metadata
        result = {
            "items": data.get("items", []),
            "pagination": pagination
        }
        
        return result

@app.get("/books/title/{title}")
async def get_books_by_title(
    title: str, 
    page: int = Query(1, ge=1, description="Page number, starting from 1"), 
    results_per_page: int = Query(10, ge=1, le=40, description="Number of results per page (max 40)")
):
    # Calculate start index for pagination
    start_index = (page - 1) * results_per_page
    
    params = {
        "q": f"intitle:{title}",
        "startIndex": start_index,
        "maxResults": results_per_page
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.get(GOOGLE_BOOKS_API_URL, params=params)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error fetching data from Google Books API")
        
        data = response.json()
        total_items = data.get("totalItems", 0)
        total_pages = (total_items + results_per_page - 1) // results_per_page  # Ceiling division
        
        # Create pagination metadata
        pagination = {
            "total_items": total_items,
            "current_page": page,
            "total_pages": total_pages,
            "results_per_page": results_per_page,
            "has_next_page": page < total_pages,
            "has_previous_page": page > 1
        }
        
        # Restructure the response to include pagination metadata
        result = {
            "items": data.get("items", []),
            "pagination": pagination
        }
        
        return result

@app.get("/books/author/{author}")
async def get_books_by_author(
    author: str, 
    page: int = Query(1, ge=1, description="Page number, starting from 1"), 
    results_per_page: int = Query(10, ge=1, le=40, description="Number of results per page (max 40)")
):
    # Calculate start index for pagination
    start_index = (page - 1) * results_per_page
    
    params = {
        "q": f"inauthor:{author}",
        "startIndex": start_index,
        "maxResults": results_per_page
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.get(GOOGLE_BOOKS_API_URL, params=params)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error fetching data from Google Books API")
        
        data = response.json()
        total_items = data.get("totalItems", 0)
        total_pages = (total_items + results_per_page - 1) // results_per_page  # Ceiling division
        
        # Create pagination metadata
        pagination = {
            "total_items": total_items,
            "current_page": page,
            "total_pages": total_pages,
            "results_per_page": results_per_page,
            "has_next_page": page < total_pages,
            "has_previous_page": page > 1
        }
        
        # Restructure the response to include pagination metadata
        result = {
            "items": data.get("items", []),
            "pagination": pagination
        }
        
        return result

@app.get("/books/category/{category}")
async def get_books_by_category(
    category: str, 
    page: int = Query(1, ge=1, description="Page number, starting from 1"), 
    results_per_page: int = Query(10, ge=1, le=40, description="Number of results per page (max 40)")
):
    # Calculate start index for pagination
    start_index = (page - 1) * results_per_page
    
    params = {
        "q": f"subject:{category}",
        "startIndex": start_index,
        "maxResults": results_per_page
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.get(GOOGLE_BOOKS_API_URL, params=params)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error fetching data from Google Books API")
        
        data = response.json()
        total_items = data.get("totalItems", 0)