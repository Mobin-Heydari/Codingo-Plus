"use client";

import React, { useState, useEffect } from 'react';
import Image from 'next/image';
import logo from '../../../assets/imgs/logo/logo.png';
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
    <section className="p-6 bg-gray-100">
      <div className="text-center mb-6">
        <Image src={logo} alt="codingo" width={100} height={100} />
        <h4 className="text-2xl font-bold text-gray-800">نمونه کارهای برتر مجموعه کدینگو</h4>
      </div>
      <div className="text-center mb-4">
        <p className="text-gray-600">
          برای برسی کامل و دقیق نمونه کار های اخیر مجموعه کدینگو <span><a href="" className="text-blue-500 hover:underline">کلیک کنید</a></span>
        </p>
      </div>
      {/* Category Buttons */}
      <div className="flex justify-center mb-6">
        {categoriesData.map(category => (
          <button key={category.id} onClick={() => handleCategoryChange(category.category)} className="mx-2 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">
            {category.category}
          </button>
        ))}
      </div>
      {/* Card Container */}
      <div className="flex flex-wrap justify-center">
        {filteredProjects.map(project => (
          <div key={project.id} className="bg-white border border-gray-300 rounded-lg shadow-md m-2 p-4 w-80 hover:shadow-lg transition-shadow duration-200">
            <div className="mb-2">
              <span className="text-sm text-gray-500">دسته بندی: {project.category}</span>
            </div>
            <div className="mb-4">
            <Image
              loader={({ src, width, quality }) => `${src}?w=${width}&q=${quality}`}
              src={project.image_url}
              alt={project.title}
              width={300}
              height={200}
              className="rounded"
            />
            </div>
            <div>
              <h6 className="text-lg font-semibold text-gray-800">{project.title}</h6>
              <p className="text-gray-600">{project.description}</p>
              <div className="mt-4">
                <a href={project.url} className="text-blue-500 hover:underline mr-2">مشاهده دمو</a>
                <a href="" className="text-blue-500 hover:underline">توضیحات</a>
              </div>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
};

export default ProjectsSection;