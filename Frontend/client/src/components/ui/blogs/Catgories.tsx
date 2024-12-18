"use client";

import React, {useEffect, useState} from "react";
import Image from "next/image";
import { BlogCategory } from "@/types/blog-category";


export default function BlogsCategories() {
    const [blogCategories, setBlogCategories] = useState<BlogCategory[]>([]);

    useEffect(() => {
        const fetchBlogCategories = async () => {
            try {
                const response = await fetch('http://localhost:8000/blogs/categories/')
                const data = await response.json()
                setBlogCategories(data)
            }catch (error) {
                console.error(error)
            }
        }
        fetchBlogCategories();
    }, []);
    
    return (
        <section className="">
            <div className="">
                <h4 className="">دسته بندی بلاگ ها</h4>
                <p className="">با انتخاب دسته بندی مورد نظر به بلاکگ های مربوط به آن دسته بندی دسترسی داشته باشید.</p>
            </div>
            <div className="">
                {blogCategories.map((category) => (
                    <div key={category.id}  className="">
                        <Image src={category.image_url} width={50} height={50} alt={category.category}/>
                        <h6 className="">{category.category}</h6>
                    </div>
                ))}
            </div>
        </section>
    )
}