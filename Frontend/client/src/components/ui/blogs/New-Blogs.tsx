// components/NewestBlogs.tsx
"use client"; // Ensure this is a client component

import React from 'react';
import { useBlogContext } from '@/contexts/Blog-Context-Data';
import Image from 'next/image';

const NewestBlogs: React.FC = () => {
    const { getNewBlogs } = useBlogContext(); // Get the function to retrieve the newest blogs from context
    const newBlogs = getNewBlogs(); // Call the function to get the newest blogs

    return (
        <div className="">
            <h4 className="text-3xl text-primary font-bold p-2 text-center">جدید ترین بلاگ</h4> {/* Title for the section */}
            <div className="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 p-5 m-3">
                {/* Map through the new blogs and display each one */}
                {newBlogs.map(blog => (
                    <div key={blog.id} className="shadow-custom-dark rounded-3xl flex flex-col justify-evenly p- w-full sm:w-full gap-4 text-wrap">
                        <div className="py-2 mt-4">
                            <span className="text-white shadow-custom-light text-xl font-bold pl-2 rounded-l-full bg-primary">
                                {blog.category}
                            </span>
                        </div>
                        <a href="#">
                            <Image
                                loader={({ src, width, quality }) =>
                                    `${src}?w=${width}&q=${quality}`
                                }
                                src={blog.image_url}
                                alt={blog.title}
                                width={700}
                                height={200}
                                className="rounded-xl p-2"
                            />
                        </a>
                        <div className="flex flex-col justify-evenly items-center text-center gap-4">
                            <a href="" className="rounded-md p-2">
                                <h6 className="text-xl text-secondary hover:text-primary primary-transitsion font-bold">
                                    {blog.title}
                                </h6>
                            </a>
                            <p className="text-text p-3">{blog.content}</p>
                            <div className="flex justify-normal gap-5 font-bold p-2 my-2">
                                <a
                                    href=""
                                    className="text-xl text-secondary font-bold p-2 px-2 hover:text-primary primary-transitsion"
                                >
                                    ادامه
                                </a>
                            </div>
                        </div>
                        <div className="flex justify-normal p-2 m-2 border-t-2 border-t-primary">
                            <p className="text-text text-lg font-bold">{blog.created}</p>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default NewestBlogs; // Export the component for use in other parts of the application