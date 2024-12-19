"use client";

import React, { useState, useEffect } from "react";
import Image from "next/image";
import { Blogs } from "@/types/blog";

const BlogSection = () => {
  const [blogsData, setBlogsData] = useState<Blogs[]>([]);

  useEffect(() => {
    const fetchProjects = async () => {
      try {
        const response = await fetch("http://localhost:8000/blogs/blog/"); // Adjust the URL as needed
        const data: Blogs[] = await response.json();
        setBlogsData(data);
      } catch (error) {
        console.error("Error fetching blogs:", error);
      }
    };

    fetchProjects();
  }, []);

  return (
    <section className="flex flex-col p-8 justify-around max-sm:p-2 my-12 gap-5">
      <div className="flex justify-center p-4 m-6">
        <h4 className="text-3xl text-secondary font-bold p-2 border-r-4 border-r-primary">
          وبلاگ تخصصی <span className="text-primary">مجموعه کدینگو</span>
        </h4>
      </div>

      <div className="flex justify-center p-2 max-md:flex-col max-md:gap-2">
        <p className="text-xl font-bold p-2 border-r-4 border-r-secondary">
          برای آگاهی بیشتر از دنیای فناوری و تکنولوژی از وبلاگ جامع مجموعه
          کدینگو{" "}
          <a
            href=""
            className="text-xl text-secondary font-bold p-2 px-2 hover:text-primary primary-transitsion"
          >
            بازدید کنید
          </a>
        </p>
      </div>

      <div className="flex justify-evenly flex-wrap gap-x-2 gap-y-7 p-2">
        {blogsData.map((blog) => (
          <div
            key={blog.id}
            className="shadow-custom-dark rounded-3xl flex flex-col justify-evenly p- w-full sm:w-full md:w-1/2 lg:w-1/3 gap-4"
          >
            <div className="py-2 mt-4">
              <span className="text-white shadow-custom-light text-xl font-bold pl-2 rounded-l-full bg-primary">
                {blog.category}
              </span>
            </div>
            <div className="">
              <Image
                loader={({ src, width, quality }) =>
                  `${src}?w=${width}&q=${quality}`
                }
                src={blog.image_url}
                alt={blog.title}
                width={700}
                height={200}
                className="rounded-xl"
              />
            </div>
            <div className="flex flex-col justify-evenly items-center text-center gap-4">
              <a href="" className="rounded-md p-2">
                <h6 className="text-xl text-secondary hover:text-primary primary-transitsion font-bold">
                  {blog.title}
                </h6>
              </a>
              <p className="text-text">{blog.content}</p>
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
      <div className="flex justify-center p-4">
        <a
          href=""
          className="shadow-custom-light text-text rounded-full p-4 hover:bg-primary hover:shadow-custom-dark text-2xl font-bold hover:text-white primary-transitsion"
        >
          مطالب بیشتر
        </a>
      </div>
    </section>
  );
};

export default BlogSection;
