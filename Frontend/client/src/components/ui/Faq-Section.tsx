"use client";

import { useState, useEffect } from "react";
import Image from "next/image";

import { Faq } from "@/types/FAQ";


const FaqSection = () => {
    const [faqData, setFaqData] = useState<Faq[]>([]);

    useEffect(() =>{
        const fetchFaq = async () => {
            const response = await fetch('http://127.0.0.1:8000/faqs/');
            const data = await response.json();
            setFaqData(data);
        };
        fetchFaq();
    }, []);

    return (
        <section className="flex flex-col p-8 justify-around max-sm:p-2 mb-12 gap-4">
            <div className="flex justify-center p-4 mt-6">
                <h6 className="text-3xl text-secondary font-bold p-2 hover:text-primary primary-transitsion">سوالات متداول</h6>
            </div>
            <div className="flex flex-col">
                {faqData.map(faq => (
                    <details key={faq.id} className="p-4 m-4 rounded-2xl shadow-custom-light border-r-4 border-primary font-bold primary-transitsion">
                        <summary key={faq.id} className="text-secondary hover:text-primary primary-transitsion p-4 flex justify-between cursor-pointer">
                            <span className="text-xl">{faq.question}</span>
                        </summary>
                        <p className="text-lg text-text p-3 mt-2 border-t-2 border-t-secondary">{faq.answer}</p>
                    </details>
                ))}            
            </div>
        </section>
    )
}

export default FaqSection;