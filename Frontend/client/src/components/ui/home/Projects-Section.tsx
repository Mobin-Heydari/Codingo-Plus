"use client";

import React, { useState, useEffect } from 'react';
import Image from 'next/image';
import { Project } from '@/types/project';
import { Category } from '@/types/category';

const ProjectsSection = () => {
  const [projectsData, setProjectsData] = useState<Project[]>([]);
  const [categoriesData, setCategoriesData] = useState<Category[]>([]);
  const [selectedCategory, setSelectedCategory] = useState<string>('All');

  useEffect(() => {
    const fetchProjects = async () => {
      try {
        const response = await fetch('http://localhost:8000/projects/'); // Adjust the URL as needed
        const data: Project[] = await response.json();
        setProjectsData(data);
      } catch (error) {
        console.error('Error fetching projects:', error);
      }
    };

    const fetchCategories = async () => {
      try {
        const response = await fetch('http://localhost:8000/categories/'); // Adjust the URL as needed
        const data: Category[] = await response.json();
        setCategoriesData(data);
      } catch (error) {
        console.error('Error fetching categories:', error);
      }
    };
    
    fetchProjects();
    fetchCategories();
  }, []);

  const handleCategoryChange = (category: string) => {
    setSelectedCategory(category);
  };

  const filteredProjects = selectedCategory === 'All' 
    ? projectsData 
    : projectsData.filter(project => project.category === selectedCategory);

  return (
    <section className="flex flex-col p-8 justify-around max-sm:p-2 my-12">
      <div className="flex justify-center p-4 m-6">
        <h4 className="text-3xl text-secondary font-bold p-2 border-r-4 border-r-primary">نمونه کارهای برتر مجموعه <span className="text-primary">کدینگو</span></h4>
      </div>
      <div className="flex justify-center p-2">
        <p className="text-xl font-bold p-2 border-r-4 border-r-secondary">برای برسی کامل و دقیق نمونه کار های اخیر مجموعه کدینگو <a href="" className="text-xl text-secondary font-bold p-2 px-2 hover:text-primary primary-transitsion">کلیک کنید</a></p>
        
      </div>
      {/* Category Buttons */}
      <div className="flex justify-center mb-6">
        {categoriesData.map(category => (
          <button
            key={category.id}
            onClick={() => handleCategoryChange(category.category)}
            className={`p-2 my-10 text-3xl font-bold border-primary hover:text-primary primary-transition ${
              selectedCategory === category.category ? 'text-primary' : 'text-secondary'
            }`}
          >
          {category.category}
        </button>
        ))}
      </div>
      {/* Card Container */}
      <div className="flex justify-evenly flex-wrap gap-x-2 gap-y-7 p-2">
        {filteredProjects.map(project => (
          <div key={project.id} className="shadow-custom-dark rounded-3xl flex flex-col justify-evenly p- w-full sm:w-full md:w-1/2 lg:w-1/3 gap-4">
            <div className="py-2 mt-4">
              <span className="text-white shadow-custom-light text-xl font-bold pl-2 rounded-l-full bg-primary">{project.category}</span>
            </div>
            <div className="">
              <Image
                loader={({ src, width, quality }) => `${src}?w=${width}&q=${quality}`}
                src={project.image_url}
                alt={project.title}
                width={700}
                height={200}
                className="rounded-xl"
              />
            </div>
            <div className='flex flex-col justify-evenly items-center text-center gap-4'>
              <a href="" className="rounded-md p-2">
                <h6 className="text-xl text-secondary hover:text-primary primary-transitsion font-bold">{project.title}</h6>
              </a>
              <p className="text-text text-justify">{project.description}</p>
              <div className="flex justify-evenly gap-5 font-bold p-2 my-2">
                <a href={project.url} className="p-2 text-primary shadow-custom-dark rounded-2xl hover:bg-white primary-transitsion">مشاهده دمو</a>
                <a href="" className="p-2 text-text shadow-custom-dark rounded-2xl hover:bg-white hover:text-secondary primary-transitsion">مطالب بیشتر</a>
              </div>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
};

export default ProjectsSection;