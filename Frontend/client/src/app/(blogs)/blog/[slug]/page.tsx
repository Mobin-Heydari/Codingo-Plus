import { FC } from 'react';

interface BlogDetailPageProps {
    params: {
        slug: string; // Adjust the type based on your parameter
    };
}

const BlogDetailPage: FC<BlogDetailPageProps> = async ({ params }) => {
    const { slug } = params; // Access the dynamic route parameter
    const url = `http://127.0.0.1:8000/blogs/blog/${slug}`;
    console.log(`Fetching data from: ${url}`);

    const response = await fetch(url);
    
    // Validate the status code
    if (response.status === 404) {
        return <div>Blog not found</div>;
    }
    const data = await response.json(); // Await the json parsing

    return (
        <main>
            <h1>{data.title}</h1> {/* Assuming the data has a title property */}
            <p>{data.content}</p> {/* Assuming the data has a content property */}
        </main>
    );
};

export default BlogDetailPage;