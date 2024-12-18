"use client";

import React, { useEffect, useState } from "react";
import Image from "next/image";
import { BlogCategory } from "@/types/blog-category";

export default function BlogsCategories() {
    const [blogCategories, setBlogCategories] = useState<BlogCategory[]>([]);

    useEffect(() => {
        const fetchBlogCategories = async () => {
            try {
                const response = await fetch('http://localhost:8000/blogs/categories/');
                const data = await response.json();
                setBlogCategories(data);
            } catch (error) {
                console.error(error);
            }
        };
        fetchBlogCategories();
    }, []);
    
    return (
        <section className="flex flex-col p-8 justify-around max-sm:p-2 my-12">
            <div className="flex justify-between flex-col p-4 m-6">
                <h4 className="text-3xl text-primary font-bold p-2 text-center">دسته بندی بلاگ ها</h4>
                <p className="text-2xl text-secondary font-bold text-center">با انتخاب دسته بندی مورد نظر به بلاگ های مربوط به آن دسته بندی دسترسی داشته باشید.</p>
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4 p-5 m-3">
                {blogCategories.map((category) => (
                    <div key={category.id} className="bg-white border rounded-xl p-4 shadow-custom-dark transition-transform transform hover:scale-105 hover:shadow-lg hover:brightness-110 hover:text-secondary">
                        <Image src={category.image_url} width={50} height={50} alt={category.category} className="mx-auto mb-2" />
                        <h6 className="text-center text-xl font-bold">{category.category}</h6>
                    </div>
                ))}
            </div>
        </section>
    );
}