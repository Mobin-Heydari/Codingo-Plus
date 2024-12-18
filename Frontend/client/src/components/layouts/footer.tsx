"use client";


export default function Footer() {
    return (
        <footer className="shadow-custom-light bg-white text-text py-10">
            <div className="container mx-auto grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-10">
                
                {/* Description Section */}
                <div className="text-center shadow-custom-dark p-4 rounded-3xl flex flex-col justify-evenly">
                    <h2 className="text-xl font-bold mb-4 text-primary">مجموعه کدینگو <span>:)</span></h2>
                    <div className="text-lg text-text mb-4">
                        <p className="text-text">ما متعهد به ارائه بهترین خدمات ممکن هستیم. تیم ما اینجاست تا در تمام نیازهای شما به شما کمک کند.</p>
                    </div>
                </div>


                {/* Addresses and Contact Details Section */}
                <div className="flex justify-evenly flex-col rounded-3xl p-4 text-center shadow-custom-dark">
                    <h2 className="text-secondary text-lg font-bold mb-4 mt8">اطلاعات تماس</h2>
                    <div className="flex flex-col justify-normal gap-10">
                        <div className="flex justify-normal gap-7 shadow-sm rounded-xl p-3 hover:text-primary primary-transitsion cursor-pointer font-bold">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="size-6">
                                <path strokeLinecap="round" strokeLinejoin="round" d="M2.25 6.75c0 8.284 6.716 15 15 15h2.25a2.25 2.25 0 0 0 2.25-2.25v-1.372c0-.516-.351-.966-.852-1.091l-4.423-1.106c-.44-.11-.902.055-1.173.417l-.97 1.293c-.282.376-.769.542-1.21.38a12.035 12.035 0 0 1-7.143-7.143c-.162-.441.004-.928.38-1.21l1.293-.97c.363-.271.527-.734.417-1.173L6.963 3.102a1.125 1.125 0 0 0-1.091-.852H4.5A2.25 2.25 0 0 0 2.25 4.5v2.25Z" />
                            </svg>
                            <p>0910-207-2859</p>
                        </div>
                        <div className="flex justify-normal gap-7 shadow-sm rounded-xl p-3 hover:text-primary primary-transitsion cursor-pointer font-bold">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="size-6">
                                <path strokeLinecap="round" strokeLinejoin="round" d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                                <path strokeLinecap="round" strokeLinejoin="round" d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z" />
                            </svg>
                            <p>تهران زعفرانیه مجموعه بزرگ کدینگو</p>
                        </div>
                        <div className="flex justify-normal gap-3 shadow-sm rounded-xl p-3 hover:text-primary primary-transitsion cursor-pointer font-bold">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="size-6">
                                <path strokeLinecap="round" strokeLinejoin="round" d="M21.75 6.75v10.5a2.25 2.25 0 0 1-2.25 2.25h-15a2.25 2.25 0 0 1-2.25-2.25V6.75m19.5 0A2.25 2.25 0 0 0 19.5 4.5h-15a2.25 2.25 0 0 0-2.25 2.25m19.5 0v.243a2.25 2.25 0 0 1-1.07 1.916l-7.5 4.615a2.25 2.25 0 0 1-2.36 0L3.32 8.91a2.25 2.25 0 0 1-1.07-1.916V6.75" />
                            </svg>
                            <p>codingo.plus.company@gmail.com</p>
                        </div>
                        
                    </div>
                </div>

                {/* Popular Links Section */}
                <div className="flex flex-col justify-evenly p-4 text-center shadow-custom-dark rounded-3xl">
                    <h2 className="text-secondary text-lg font-bold mb-4 mt8">صفحات محبوب</h2>
                    <ul className="flex justify-between flex-col gap-4 text-text">
                        <li className="shadow-sm rounded-xl p-2 hover:text-primary primary-transitsion cursor-pointer font-bold flex justify-normal gap-x-28">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="size-6">
                            <path strokeLinecap="round" strokeLinejoin="round" d="m2.25 12 8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
                        </svg>

                            <a href="#" className="hover:underline">خانه</a>
                        </li>
                        <li className="shadow-sm rounded-xl p-2 hover:text-primary primary-transitsion cursor-pointer font-bold flex justify-normal gap-x-28">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="size-6">
                            <path strokeLinecap="round" strokeLinejoin="round" d="M11.42 15.17 17.25 21A2.652 2.652 0 0 0 21 17.25l-5.877-5.877M11.42 15.17l2.496-3.03c.317-.384.74-.626 1.208-.766M11.42 15.17l-4.655 5.653a2.548 2.548 0 1 1-3.586-3.586l6.837-5.63m5.108-.233c.55-.164 1.163-.188 1.743-.14a4.5 4.5 0 0 0 4.486-6.336l-3.276 3.277a3.004 3.004 0 0 1-2.25-2.25l3.276-3.276a4.5 4.5 0 0 0-6.336 4.486c.091 1.076-.071 2.264-.904 2.95l-.102.085m-1.745 1.437L5.909 7.5H4.5L2.25 3.75l1.5-1.5L7.5 4.5v1.409l4.26 4.26m-1.745 1.437 1.745-1.437m6.615 8.206L15.75 15.75M4.867 19.125h.008v.008h-.008v-.008Z" />
                        </svg>

                            <a href="#" className="hover:underline">خدمات</a>
                        </li>
                        <li className="shadow-sm rounded-xl p-2 hover:text-primary primary-transitsion cursor-pointer font-bold flex justify-normal gap-x-28">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="size-6">
                                <path strokeLinecap="round" strokeLinejoin="round" d="M20.25 3.75v4.5m0-4.5h-4.5m4.5 0-6 6m3 12c-8.284 0-15-6.716-15-15V4.5A2.25 2.25 0 0 1 4.5 2.25h1.372c.516 0 .966.351 1.091.852l1.106 4.423c.11.44-.054.902-.417 1.173l-1.293.97a1.062 1.062 0 0 0-.38 1.21 12.035 12.035 0 0 0 7.143 7.143c.441.162.928-.004 1.21-.38l.97-1.293a1.125 1.125 0 0 1 1.173-.417l4.423 1.106c.5.125.852.575.852 1.091V19.5a2.25 2.25 0 0 1-2.25 2.25h-2.25Z" />
                            </svg>

                            <a href="#" className="hover:underline">تماس با ما</a>
                        </li>
                        <li className="shadow-sm rounded-xl p-2 hover:text-primary primary-transitsion cursor-pointer font-bold flex justify-normal gap-x-28">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="size-6">
                                <path strokeLinecap="round" strokeLinejoin="round" d="M12 6.042A8.967 8.967 0 0 0 6 3.75c-1.052 0-2.062.18-3 .512v14.25A8.987 8.987 0 0 1 6 18c2.305 0 4.408.867 6 2.292m0-14.25a8.966 8.966 0 0 1 6-2.292c1.052 0 2.062.18 3 .512v14.25A8.987 8.987 0 0 0 18 18a8.967 8.967 0 0 0-6 2.292m0-14.25v14.25" />
                            </svg>
                            <a href="#" className="hover:underline">بلاگ</a>
                        </li>
                    </ul>
                </div>
                {/* Contact Form Section */}
                <div className="flex flex-col justify-evenly p-4 text-center shadow-custom-dark rounded-3xl bg-primary">
                    <h2 className="text-secondary text-lg font-bold mb-4 mt8">Contact Us</h2>
                    <form>
                        <input type="text" placeholder="نام و نام خانوادگی" className="w-full p-2 mb-2 rounded-2xl bg-white focus:outline-0" required/>
                        <input type="email" placeholder="ایمیل" className="w-full p-2 mb-2 rounded-2xl bg-white focus:outline-0" required/>
                        <input type="email" placeholder="شماره تماس" className="w-full p-2 mb-2 rounded-2xl bg-white focus:outline-0" required/>
                        <textarea placeholder="بیام" className="w-full p-2 mb-2 rounded-2xl bg-white focus:outline-0" rows={4} required/>
                        <button type="submit" className="bg-secondary hover:bg-hover text-white font-bold py-2 px-4 rounded primary-transitsion">ارسال</button>
                    </form>
                </div>
            </div>
        </footer>
    )
}