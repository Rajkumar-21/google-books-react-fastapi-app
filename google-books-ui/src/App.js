import React, { useState } from 'react';
import axios from 'axios';
import BooksTable from './BooksTable';
import './App.css';

const App = () => {
  const [query, setQuery] = useState('');
  const [responseJson, setResponseJson] = useState(null);
  const [searchType, setSearchType] = useState('all'); // 'all', 'title', 'author', or 'category'
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSearch = async (e) => {
    e.preventDefault();
    if (!query.trim()) {
      setError('Please enter a search item');
      return;
    }
    
    setIsLoading(true);
    setError(null);
    
    try {
      let url;
      let params = {};
      
      switch (searchType) {
        case 'title':
          url = `http://localhost:8000/books/title/${encodeURIComponent(query)}`;
          break;
        case 'author':
          url = `http://localhost:8000/books/author/${encodeURIComponent(query)}`;
          break;
        case 'category':
          url = `http://localhost:8000/books/category/${encodeURIComponent(query)}`;
          break;
        default:
          url = `http://localhost:8000/books`;
          params = { q: query };
          break;
      }

      console.log('Sending request to:', url);
      
      const response = await axios.get(url, {
        params,
        headers: {
          'Accept': 'application/json',
        },
      });
      
      console.log('Response status:', response.status);
      console.log('Response data:', response.data);
      
      setResponseJson(response.data);
    } catch (error) {
      console.error('Error details:', error);
      setError(`Error: ${error.message}`);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="App">
      <h1>Google Books Search</h1>
      <form onSubmit={handleSearch} className="search-form">
        <div className="search-container">
          <div className="search-options">
            <select 
              value={searchType} 
              onChange={(e) => setSearchType(e.target.value)}
              className="search-type"
            >
              <option value="all">All Books</option>
              <option value="title">Search by Title</option>
              <option value="author">Search by Author</option>
              <option value="category">Search by Category</option>
            </select>
            <input
              type="text"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Enter search term..."
              className="search-input"
            />
          </div>
          <button type="submit" disabled={isLoading} className="search-button">
            {isLoading ? 'Searching...' : 'Search'}
          </button>
        </div>
      </form>
      
      {error && <div className="error-message">{error}</div>}
      {isLoading && <div className="loading-message">Loading results...</div>}
      
      {responseJson && responseJson.items && responseJson.items.length > 0 ? (
        <div>
          <div className="total-items">
            {responseJson.totalItems !== undefined && 
              `Total books found: ${responseJson.totalItems}`
            }
          </div>
          <BooksTable books={responseJson.items} />
        </div>
      ) : responseJson && (
        <p>No books found matching your search criteria.</p>
      )}
    </div>
  );
};

export default App;
