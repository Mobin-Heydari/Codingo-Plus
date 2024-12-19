import React from 'react';
import NewBlogs from '@/components/ui/blogs/New-Blogs';
import BlogProvider from '@/contexts/Blog-Context-Data';
import BlogsCategories from '@/components/ui/blogs/Catgories';
import BlogsPaginator from '@/components/ui/blogs/Blogs-Pagination';


const BlogPage: React.FC = () => {
  return (
      <section className="flex flex-col p-8 justify-around max-sm:p-2 my-12"> {/* Main section for the blog page */}
        <BlogsCategories />
        <BlogProvider>
          <NewBlogs /> {/* Render the NewestBlogs component to display the latest blog posts */}
          <BlogsPaginator />
        </BlogProvider>
      </section>
  );
};

export default BlogPage; // Export the BlogPage component for use in the application