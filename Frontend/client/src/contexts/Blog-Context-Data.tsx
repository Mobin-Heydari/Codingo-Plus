// context/BlogContext.tsx
"use client"; // Ensure this is a client component

import React, { createContext, useContext, useEffect, useState } from 'react';
import { Blogs } from '@/types/blog';

// Define the structure of the BlogContext
interface BlogContextType {
    blogs: Blogs[]; // Array of blog posts
    getNewBlogs: () => Blogs[]; // Function to get the newest blogs
}

// Create the BlogContext
const BlogContext = createContext<BlogContextType | undefined>(undefined);

// BlogProvider component to provide context to children
export const BlogProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
    const [blogs, setBlogs] = useState<Blogs[]>([]); // State to hold blog posts

    // Fetch blogs from the API when the component mounts
    useEffect(() => {
        const fetchBlogs = async () => {
            try {
                const response = await fetch('http://localhost:8000/blogs/blog/');
                const data = await response.json();
                setBlogs(data); // Set the fetched blogs to state
            } catch (error) {
                console.error(error); // Log any errors
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

    // Provide the context values to children
    return (
        <BlogContext.Provider value={{ blogs, getNewBlogs }}>
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