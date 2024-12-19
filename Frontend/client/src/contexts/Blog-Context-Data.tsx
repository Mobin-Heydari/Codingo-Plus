// context/BlogContext.tsx
"use client"; // Ensure this is a client component

import React, { createContext, useContext, useEffect, useState } from 'react';
import { Blogs } from '@/types/blog';

// Define the structure of the BlogContext
interface BlogContextType {
    blogs: Blogs[];
    totalBlogs: number; // Add totalBlogs to the type
    blogsPerPage: number;
    getNewBlogs: (currentPage: number) => Blogs[];
}


// Create the BlogContext
const BlogContext = createContext<BlogContextType | undefined>(undefined);

// BlogProvider component to provide context to children
const BlogProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
    const [blogs, setBlogs] = useState<Blogs[]>([]);
    const [totalBlogs, setTotalBlogs] = useState<number>(0); // New state for total blogs
    const blogsPerPage = 12; // Set the number of blogs per page

    useEffect(() => {
        const fetchBlogs = async () => {
            try {
                const response = await fetch('http://localhost:8000/blogs/blog/');
                const data = await response.json();
                setBlogs(data); // Set the fetched blogs to state
                setTotalBlogs(data.length); // Set total number of blogs
            } catch (error) {
                console.error(error);
            }
        };
        fetchBlogs();
    }, []);

    // Function to get the 6 newest blogs
    const getNewBlogs = () => {
        return blogs
            .sort((a, b) => new Date(b.created).getTime() - new Date(a.created).getTime())
            .slice(0, 6); // Get the 6 newest blogs
    };

    return (
        <BlogContext.Provider value={{ blogs, totalBlogs, blogsPerPage, getNewBlogs }}>
            {children}
        </BlogContext.Provider>
    );
};
// Custom hook to use the BlogContext
export const useBlogContext = () => {
    const context = useContext(BlogContext);
    if (!context) {
        throw new Error("useBlogContext must be used within a BlogProvider"); // Error if used outside of provider
    }
    return context; // Return the context
};

export default BlogProvider;