"use client";

import { useState } from "react";
import Image from "next/image";

import logo from '../../assets/imgs/logo/text-logo.png';


export default function Header() {
    const [isOpen, setIsOpen] = useState(false);

    const toggleSidebar = () => {
        setIsOpen(!isOpen);
    };

    return (
        <nav className="flex items-center justify-between p-5 bg-white shadow-custom-dark m-5 rounded-3xl">
            <div className="logo">
            <Image src={logo} width={120} height={50} alt="codingo plus" />
            </div>
                <ul className="hidden lg:flex justify-between lg:w-3/5"> {/* This adds space between the list items */}
                    <li><a href="#" className="text-lg hover:text-primary primary-transitsion">طراحی سایت</a></li>
                    <li><a href="#" className="text-lg hover:text-primary primary-transitsion">طراحی ابلیکیشن</a></li>
                    <li><a href="#" className="text-lg hover:text-primary primary-transitsion">نمونه کار ها</a></li>
                    <li><a href="#" className="text-lg hover:text-primary primary-transitsion">وبلاگ</a></li>
                    <li><a href="#" className="text-lg hover:text-primary primary-transitsion">درباره ما</a></li>
                    <li><a href="#" className="text-lg hover:text-primary primary-transitsion">تماس با ما</a></li>
                </ul>
            <div className="hidden lg:inline-block">
                <button className="ml-4 px-4 py-2 text-lg text-text bg-primary rounded-2xl hover:bg-secondary hover:text-white primary-transitsion">
                    دریافت مشاوره <span className="">رایگان</span>
                </button>
            </div>
            <div className="lg:hidden">
                <button onClick={toggleSidebar} className="p-2 text-text hover:text-primary primary-transitsion">
                    <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M4 6h16M4 12h16m-7 6h7" />
                    </svg>
                </button>
            </div>
            {/* Sidebar for mobile */}
            <div className={`fixed inset-0 bg-gray-800 bg-opacity-50 transition-opacity ${isOpen ? 'opacity-100' : 'opacity-0 pointer-events-none'}`} onClick={toggleSidebar}></div>

            <div className={`fixed top-0 left-0 w-64 bg-white h-full shadow-lg transform transition-transform primary-transitsion rounded-r-2xl ${isOpen ? 'translate-x-0' : '-translate-x-full'}`}>
                
                    <div className="flex justify-end p-4">
                        <button onClick={toggleSidebar} className="text-text hover:text-primary primary-transitsion">
                            <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M6 18L18 6M6 6l12 12" />
                            </svg>
                        </button>
                    </div>

                    <ul className="flex flex-col p-4 space-y-4 justify-between mt-2">
                        <li><a href="#" className="hover:text-primary primary-transitsion">طراحی ابلیکیشن</a></li>
                        <li><a href="#" className="hover:text-primary primary-transitsion">طراحی سایت</a></li>
                        <li><a href="#" className="hover:text-primary primary-transitsion">نمونه کار ها</a></li>
                        <li><a href="#" className="hover:text-primary primary-transitsion">تماس با ما</a></li>
                        <li><a href="#" className="hover:text-primary primary-transitsion">درباره ما</a></li>
                        <li><a href="#" className="hover:text-primary primary-transitsion">وبلاگ</a></li>
                    </ul>

                    <div className="justify-self-center mt-10">
                        <button className="ml-4 px-4 py-2 text-lg text-text bg-primary rounded-2xl hover:bg-secondary hover:text-white primary-transitsion">
                            دریافت مشاوره <span>رایگان</span>
                        </button>
                    </div>
            </div>
        </nav>
    );
}