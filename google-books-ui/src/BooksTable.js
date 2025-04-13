import React from 'react';
import './App.css';

const BooksTable = ({ books }) => {
  return (
    <div className="table-container">
      <table className="books-table">
        <thead>
          <tr>
            <th>Title</th>
            <th>Subtitle</th>
            <th>Author(s)</th>
            <th>Publisher</th>
            <th>Published Date</th>
          </tr>
        </thead>
        <tbody>
          {books.map((book) => (
            <tr key={book.id}>
              <td>{book.volumeInfo.title || 'N/A'}</td>
              <td>{book.volumeInfo.subtitle || 'N/A'}</td>
              <td>{book.volumeInfo.authors ? book.volumeInfo.authors.join(', ') : 'N/A'}</td>
              <td>{book.volumeInfo.publisher || 'N/A'}</td>
              <td>{book.volumeInfo.publishedDate || 'N/A'}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default BooksTable;