"use client";

import React, { useState, useEffect } from 'react';
import Image from 'next/image';
import { Blogs } from '@/types/blogs';


const BlogSection = () => {
    const [blogsData, setBlogsData] = useState<Blogs[]>([]);

    useEffect(() => {
    const fetchProjects = async () => {
        try {
        const response = await fetch('http://localhost:8000/blogs/'); // Adjust the URL as needed
        const data: Blogs[] = await response.json();
        setBlogsData(data);
        } catch (error) {
        console.error('Error fetching blogs:', error);
        }
    };

    fetchProjects();
    }, []);

    return (
        <section>
            <div>
                <h6>وبلاگ تخصصی <span>مجموعه کدینگو</span></h6>
                <p></p>
            </div>

            <div>
                {blogsData.map(blog => (
                    <div key={blog.id} className="">
                        <div className="">
                            <span className="">{blog.category}</span>
                        </div>
                        <div className="">
                            <Image
                            loader={({ src, width, quality }) => `${src}?w=${width}&q=${quality}`}
                            src={blog.image_url}
                            alt={blog.title}
                            width={700}
                            height={200}
                            className="rounded-xl"
                            />
                        </div>
                        <div className="">
                            <a href="" className="">
                                <h6 className="">{blog.title}</h6>
                            </a>
                            <p className="">{blog.description}</p>
                            <div className="">
                                <a href="" className="">مطالب بیشتر</a>
                            </div>
                        </div>
                        <div>
                            <p>{blog.created_at}</p>
                        </div>
                    </div>
                ))}
            </div>
        </section>
    )
}

export default BlogSection;