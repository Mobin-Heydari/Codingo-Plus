import Image from "next/image";
import codingo_poster from '../assets/imgs/home/codingo-poster.png';
import web_card from '../assets/imgs/home/web.jpg';
import testing from '../assets/imgs/home/testing.png';
import server from '../assets/imgs/home/server.png'
import coding from '../assets/imgs/home/coding.png'
import ui_ux from '../assets/imgs/home/Ui-Ux.png'
import support from '../assets/imgs/home/support.png'

export default function Home() {
  return (
    <main className="flex flex-col justify-evenly">

      <section className="flex flex-row max-lg:flex-col p-8 justify-around max-sm:p-2 my-12">

        <div className="basis-2/5 flex justify-between flex-col">

          <h2 className="text-3xl text-secondary p-5 my-4 rounded border-r-4 border-r-primary max-sm:text-2xl font-bold">تحقق رویاهای <span className="text-primary">دیجیتال</span> شما</h2>
          <p className="text-lg text-text p-6 my-4 rounded border-r-4 border-r-primary">
            در <strong className="font-bold text-secondary">مجموعه کدینگ و پلاس</strong>، ما با ترکیب خلاقیت و فناوری پیشرفته، راه‌حل‌هایی نوآورانه برای وب‌سایت‌ها و اپلیکیشن‌های شما ارائه می‌دهیم. ما به تحقق رؤیاهای دیجیتالی شما ایمان داریم و تلاش می‌کنیم تا هر پروژه را به یک داستان موفقیت‌آمیز تبدیل کنیم.
          </p>
          <p className="text-lg text-text p-6 my-4 rounded border-r-4 border-r-secondary">
            <strong className="font-bold">مأموریت ما:</strong> خلق تجربه‌های دیجیتالی که نه تنها جذاب و کارآمد هستند بلکه تأثیری ماندگار بر روی کسب‌وکار شما می‌گذارند.
          </p>
          <p className="text-lg text-text p-6 my-4 rounded border-r-4 border-r-primary">
            کدنیگو پلاس مجموعه ای از طراحان و توسعه دهندگانی با تجربه و مدرن است که در زمینه ی طراحی و توسعه وب اپلیکیشن و اپلیکیشن سال ها تجربه و تخصص جمع آوری کرده اند.
          </p>

          <div className="flex justify-evenly max-sm:flex-col text-center my-5 flex-wrap gap-4">
            <p className="cursor-pointer p-4 text-sm text-text rounded-xl shadow-custom-light border-r-4 border-primary max-sm:my-3 font-bold">بشتیبانی رایگان</p>
            <p className="cursor-pointer p-4 text-sm text-text rounded-xl shadow-custom-light border-r-4 border-primary max-sm:my-3 font-bold">طراحی اختصاصی</p>
            <p className="cursor-pointer p-4 text-sm text-text rounded-xl shadow-custom-light border-r-4 border-secondary max-sm:my-3 font-bold">کدنویسی بهینه</p>
            <p className="cursor-pointer p-4 text-sm text-text rounded-xl shadow-custom-light border-r-4 border-primary max-sm:my-3 font-bold">تکنولوژی های روز</p>
          </div>

          <div className="flex justify-evenly text-center my-5 max-sm:flex-col gap-4">
            <a className="p-4 bg-secondary rounded-2xl w-2/4 text-white text-center shadow-custom-light hover:bg-primary hover:text-text primary-transitsion max-sm:w-full font-bold" href="">
              دریافت مشاوره
            </a>
            <a className="p-4 bg-primary rounded-2xl w-2/4 text-text text-center shadow-custom-light hover:bg-hover hover:text-white primary-transitsion max-sm:w-full font-bold" href="">
              نمونه کار ها
            </a>
          </div>
        </div>

        <div className="flex justify-center mt-4 md:mt-0">
          <Image src={codingo_poster} alt="Codingo Plus" width={450} height={200} className="rounded-3xl max-w-full h-auto"/>
        </div>
        
      </section>

      {/* Services part */}
      <section className="flex justify-evenly flex-col gap-4 p-8 max-sm:p-0 shadow-custom-light my-12">

        <div className="text-center text-text flex flex-col justify-between gap-3">
          <div>
            <h3 className="text-3xl text-secondary p-3 m-3 rounded border-r-4 border-r-secondary inline-block font-bold"><span className="text-primary">مجموعه کدینگو پلاس</span> چه خدماتی به شما ارايه می دهد؟</h3>
          </div>
          <div className="">
            <h4 className="text-2xl p-3 m-2 font-bold rounded border-r-4 border-r-primary inline-block">طراحی و توسعه انواع بلتفرم ها و کسب و کار های آنلاین و راه اندازی آن ها در بستر وب و مبایل از تخصص متخصاصن کدینگو است</h4>
          </div>
        </div>

        {/* card container */}
        <div className="flex justify-evenly flex-wrap gap-x-2 gap-y-7 p-2">

          {/* cards */}
          <div className="flex justify-evenly flex-col gap-8 w-full sm:w-1/3 md:w-1/4 lg:w-1/5 shadow-custom-dark rounded-3xl p-2">
            <div>
              <Image src={web_card} alt="codingo" className="rounded-3xl max-w-full h-auto"/>
            </div>
            <div className="flex flex-col justify-evenly items-center text-center gap-4">
              <a href="" className="rounded-md border-r-primary border-r-4 p-2">
                <h5 className="text-xl text-secondary hover:text-primary primary-transitsion font-bold">طراحی و توسعه وب</h5>
              </a>
              <p className="text-sm text-justify p-2">texts here</p>
            </div>
          </div>

          {/* Repeat the card div for additional cards */}
          <div className="flex justify-evenly flex-col gap-8 w-full sm:w-1/3 md:w-1/4 lg:w-1/5 shadow-custom-dark rounded-3xl p-2">
            <div>
              <Image src={web_card} alt="codingo" className="rounded-3xl max-w-full h-auto"/>
            </div>
            <div className="flex flex-col justify-evenly items-center text-center gap-4">
              <a href="" className="rounded-md border-r-primary border-r-4 p-2">
                <h5 className="text-xl text-secondary hover:text-primary primary-transitsion font-bold">طراحی و توسعه وب</h5>
              </a>
              <p className="text-sm text-justify p-2">texts here</p>
            </div>
          </div>
          {/* Repeat the card div for additional cards */}
          <div className="flex justify-evenly flex-col gap-8 w-full sm:w-1/3 md:w-1/4 lg:w-1/5 shadow-custom-dark rounded-3xl p-2">
            <div>
              <Image src={web_card} alt="codingo" className="rounded-3xl max-w-full h-auto"/>
            </div>
            <div className="flex flex-col justify-evenly items-center text-center gap-4">
              <a href="" className="rounded-md border-r-primary border-r-4 p-2">
                <h5 className="text-xl text-secondary hover:text-primary primary-transitsion font-bold">طراحی و توسعه وب</h5>
              </a>
              <p className="text-sm text-justify p-2">texts here</p>
            </div>
          </div>
          {/* Repeat the card div for additional cards */}
          <div className="flex justify-evenly flex-col gap-8 w-full sm:w-1/3 md:w-1/4 lg:w-1/5 shadow-custom-dark rounded-3xl p-2">
            <div>
              <Image src={web_card} alt="codingo" className="rounded-3xl max-w-full h-auto"/>
            </div>
            <div className="flex flex-col justify-evenly items-center text-center gap-4">
              <a href="" className="rounded-md border-r-primary border-r-4 p-2">
                <h5 className="text-xl text-secondary hover:text-primary primary-transitsion font-bold">طراحی و توسعه وب</h5>
              </a>
              <p className="text-sm text-justify p-2">texts here</p>
            </div>
          </div>
        {/* Add more cards as needed */}
        </div>
      </section>
      {/* Platform Development Process Section */}
      <section>

        <div>
          <h3>فرآیند طراحی و توسعه پلتفرم</h3> 
          <p>مراحل سفارش, طراحی, توسعه و تست پلتفرم دیجتال شما در مجموعه کدینگو به صورت کامل و اطلاعات دقیق</p>
        </div>

        <div>
          <div>
            <div>
              <Image src={support} alt=""/>
            </div>
            <h5>دریافت مشاوره رایگان</h5>
            <p>شناسایی نیاز کسب وکار شما</p>
            <p>آنالیز رقابای شما</p>
            <p>پردازش ایده های نوین و خلاقانه</p>
            <p>تایید و تصویب طرح کلی</p>
          </div>

          <div>
            <div>
              <Image src={ui_ux} alt=""/>
            </div>
            <h5>طراحی UiوUx</h5>
            <p>انتخاب تم رنگی و طرح بصری با توجه به کسب وکار شما</p>
            <p>طراحی طرح UiوUx</p>
            <p>ادیت و اصلاح طرح UiوUx</p>
            <p>تایید و تصویب طرح UiوUx</p>
          </div>

          <div>
            <div>
              <Image src={coding} alt=""/>
            </div>
            <h5>توسعه و پیاده سازی</h5>
            <p>پیاده سازی الگریتم ها</p>
            <p>توسعه ‌Back-end و API</p>
            <p>توسعه Front-end</p>
            <p>تست و اطمینان از کیفیت و سرعت پلتفرم</p>
          </div>

          <div>
            <div>
              <Image src={testing} alt=""/>
            </div>
            <h5>تست و تضمین کیفیت</h5>
            <p>تست های خودکار</p>
            <p>تست سرعت وبارگزاری</p>
            <p>تست نفوز و امنیت</p>
            <p>برطرف کردن مشکلات احتمالی</p>
          </div>
          
          <div>
            <div>
              <Image src={server} alt=""/>
            </div>
            <h5>راه اندازی و پشتیبانی رایگان یکساله</h5> 
            <p>تهیه ی سرور و راه اندازی آن</p>
            <p>بهینه سازی سرور</p>
            <p>بالا بردن امنیت سرور</p>
            <p>پشتیبانی بیت و چهار ساعته رایگان به مدت یک سال</p>
          </div>

        </div>
      </section>
    </main>
  );
}