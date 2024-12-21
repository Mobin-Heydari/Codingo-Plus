import Image from "next/image";
import phoneIcon from "../../assets/imgs/icons/phone.png";
import emailIcon from "../../assets/imgs/icons/email.png";
import instagramIcon from "../../assets/imgs/icons/instagram.png";
import telegramIcon from "../../assets/imgs/icons/telegram.png";
import mapImage from "../../assets/imgs/contact/map.png";

import ContactsForm from "@/components/ui/contacts/Contacts-Form";




export default function ContactUs() {
    return (
        <main>
            <section className="flex flex-col justify-between gap-8 shadow-custom-light">
                <h1 className="text-2xl text-secondary text-center font-bold p-3">تماس با ما</h1>
                <div className="flex-1 flex flex-row p-2 m-3 gap-5 max-md:flex-col">
                    <div className="grid grid-cols-1 gap-2 p-2 m-3 w-2/5 max-md:w-full">
                        <div className="flex items-center p-3 m-2 shadow-custom-light rounded-2xl h-24 font-bold hover:shadow-custom-dark cursor-pointer primary-transitsion hover:brightness-110">
                            <a href="#" className="flex-shrink-0">
                                <Image src={phoneIcon} alt="phone icon" width={50} height={50} />
                            </a>
                            <a href="#" className="ml-4 text-xl flex-1 text-left overflow-hidden whitespace-nowrap text-ellipsis">910-207-2859</a>
                        </div>
                        <div className="flex items-center p-3 m-2 shadow-custom-light rounded-2xl h-24 font-bold hover:shadow-custom-dark cursor-pointer primary-transitsion hover:brightness-110">
                            <a href="#" className="flex-shrink-0">
                                <Image src={emailIcon} alt="email icon" width={50} height={50} />
                            </a>
                            <a href="#" className="ml-4 text-xl flex-1 text-left overflow-hidden whitespace-nowrap text-ellipsis">mail@codingo.com</a>
                        </div>
                        <div className="flex items-center p-3 m-2 shadow-custom-light rounded-2xl h-24 font-bold hover:shadow-custom-dark cursor-pointer primary-transitsion hover:brightness-110">
                            <a href="#" className="flex-shrink-0">
                                <Image src={instagramIcon} alt="instagram icon" width={50} height={50} />
                            </a>
                            <a href="#" className="ml-4 text-xl flex-1 text-left overflow-hidden whitespace-nowrap text-ellipsis">Codingo_Plus@</a>
                        </div>
                        <div className="flex items-center p-3 m-2 shadow-custom-light rounded-2xl h-24 font-bold hover:shadow-custom-dark cursor-pointer primary-transitsion hover:brightness-110">
                            <a href="#" className="flex-shrink-0">
                                <Image src={telegramIcon} alt="telegram icon" width={50} height={50} />
                            </a>
                            <a href="#" className="ml-4 text-xl flex-1 text-left overflow-hidden whitespace-nowrap text-ellipsis">Codingo_Plus@</a>
                        </div>
                    </div>
                    <div className="flex-1 flex justify-center w-3/5 max-md:w-full">
                        <Image src={mapImage} alt="نقشه زمین" className="max-w-full h-auto" />
                    </div>
                </div>
            </section>
            {/* Contacts form section */}
            <section className="flex flex-col justify-between gap-8 my-12">
                <h2 className="text-3xl text-secondary text-center font-bold p-3">فرم تماس با ما</h2>
                <p className="text-xl text-primary text-center font-bold p-3">نظرات وانتقادات خود را با ما به اشتراک بگذارید:)</p>
                <div className="">
                    <ContactsForm />
                </div>
                <p className="p-2 m-3 text-bold text-secondary text-center">
                    تمامی حقوق و اطلاعات شما نزد ما محفوظ می ماند.
                </p>
            </section>
        </main>
    );
}