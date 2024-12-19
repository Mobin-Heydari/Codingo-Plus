"use client";

import React, { useState, useEffect } from 'react';
import { useBlogContext } from '@/contexts/Blog-Context-Data';


const BlogsPaginatorControls = () => {
  const { blogs, totalBlogs, blogsPerPage } = useBlogContext();
  const [currentPage, setCurrentPage] = useState(1);

  const totalPages = Math.ceil(totalBlogs / blogsPerPage);

  const handlePageChange = (page: number) => {
      setCurrentPage(page);
      // Fetch new blogs based on the current page
  };
  useEffect(() => {
      // Fetch blogs for the current page when it changes
  }, [currentPage]);

  return (
      <div>
          <ul>
              {blogs.map(blog => (
              <li key={blog.id}>{blog.title}</li>
              ))}
          </ul>
          <div>
              <button onClick={() => handlePageChange(currentPage - 1)} disabled={currentPage === 1}>
              Previous
              </button>
              {Array.from({ length: totalPages }, (_, index) => (
              <button key={index} onClick={() => handlePageChange(index + 1)}>
                  {index + 1}
              </button>
              ))}
              <button onClick={() => handlePageChange(currentPage + 1)} disabled={currentPage === totalPages}>
              Next
              </button>
          </div>
      </div>
  );
};

export default BlogsPaginatorControls;