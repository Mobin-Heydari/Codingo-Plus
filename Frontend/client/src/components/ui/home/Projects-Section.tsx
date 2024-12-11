"use client";

import React, { useState } from 'react';
import Image from 'next/image'; // Assuming you're using Next.js for Image component
import logo from '../../../assets/imgs/logo/logo.png'; // Make sure to import your logo image

const projectsData = [
  { id: 1, category: 'Web Development', title: 'Project 1', description: 'Description 1', demoLink: '#', detailsLink: '#' },
  { id: 2, category: 'Mobile Development', title: 'Project 2', description: 'Description 2', demoLink: '#', detailsLink: '#' },
  { id: 3, category: 'Web Development', title: 'Project 3', description: 'Description 3', demoLink: '#', detailsLink: '#' },
  // Add more projects as needed
];

const ProjectsSection = () => {
  const [selectedCategory, setSelectedCategory] = useState<string>('All');

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
        <button onClick={() => handleCategoryChange('All')} className="mx-2 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">همه</button>
        <button onClick={() => handleCategoryChange('Web Development')} className="mx-2 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">توسعه وب</button>
        <button onClick={() => handleCategoryChange('Mobile Development')} className="mx-2 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">توسعه موبایل</button>
      </div>
      {/* Card Container */}
      <div className="flex flex-wrap justify-center">
        {filteredProjects.map(project => (
          <div key={project.id} className="bg-white border border-gray-300 rounded-lg shadow-md m-2 p-4 w-80 hover:shadow-lg transition-shadow duration-200">
            <div className="mb-2">
              <span className="text-sm text-gray-500">دسته بندی: {project.category}</span>
            </div>
            <div className="mb-4">
              <Image src="" alt="" width={300} height={200} className="rounded" /> {/* Add a valid image source for each project */}
            </div>
            <div>
              <h6 className="text-lg font-semibold text-gray-800">{project.title}</h6>
              <p className="text-gray-600">{project.description}</p>
              <div className="mt-4">
                <a href={project.demoLink} className="text-blue-500 hover:underline mr-2">مشاهده دمو</a>
                <a href={project.detailsLink} className="text-blue-500 hover:underline">توضیحات</a>
              </div>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
};

export default ProjectsSection;