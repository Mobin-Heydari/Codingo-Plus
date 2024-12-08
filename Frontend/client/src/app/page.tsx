import Image from "next/image";
import poster from '../assets/imgs/codingo-poster.png';

export default function Home() {
  return (
    <main className="flex flex-col justify-evenly">
      <div className="flex flex-col md:flex-row p-12 justify-around">

        <div className="basis-2/5 flex justify-between flex-col">
          <h2 className="text-3xl text-secondary p-5 my-4 rounded border-r-4 border-r-primary max-sm:text-justify ">تحقق رویاهای <span className="text-primary">دیجیتال</span> شما</h2>
          <p className="text-lg text-text p-6 my-4 rounded border-r-4 border-r-primary">
            در <strong className="font-bold text-secondary">مجموعه کدینگ و پلاس</strong>، ما با ترکیب خلاقیت و فناوری پیشرفته، راه‌حل‌هایی نوآورانه برای وب‌سایت‌ها و اپلیکیشن‌های شما ارائه می‌دهیم. ما به تحقق رؤیاهای دیجیتالی شما ایمان داریم و تلاش می‌کنیم تا هر پروژه را به یک داستان موفقیت‌آمیز تبدیل کنیم.
          </p>
          <p className="text-lg text-text p-6 my-4 rounded border-r-4 border-r-secondary">
            <strong>مأموریت ما:</strong> خلق تجربه‌های دیجیتالی که نه تنها جذاب و کارآمد هستند بلکه تأثیری ماندگار بر روی کسب‌وکار شما می‌گذارند.
          </p>
          <p className="text-lg text-text p-6 my-4 rounded border-r-4 border-r-primary">
            کدنیگو پلاس مجموعه ای از طراحان و توسعه دهندگانی با تجربه و مدرن است که در زمینه ی طراحی و توسعه وب اپلیکیشن و اپلیکیشن سال ها تجربه و تخصص جمع آوری کرده اند.
          </p>

          <div className="flex justify-evenly max-sm:flex-col text-center my-5 flex-wrap">
            <p className="cursor-pointer p-4 text-sm text-text rounded-xl shadow-custom-light border-r-4 border-primary max-sm:my-3">بشتیبانی رایگان</p>
            <p className="cursor-pointer p-4 text-sm text-text rounded-xl shadow-custom-light border-r-4 border-primary max-sm:my-3">طراحی اختصاصی</p>
            <p className="cursor-pointer p-4 text-sm text-text rounded-xl shadow-custom-light border-r-4 border-secondary max-sm:my-3">کدنویسی بهینه</p>
            <p className="cursor-pointer p-4 text-sm text-text rounded-xl shadow-custom-light border-r-4 border-primary max-sm:my-3">تکنولوژی های روز</p>
          </div>

          <div className="flex justify-evenly p-2 mx-0 mt-3 max-sm:flex-col">
            <a className="p-4 m-4 bg-secondary rounded-2xl w-2/4 text-white text-center shadow-custom-light hover:bg-primary hover:text-text primary-transitsion max-sm:w-full" href="">
              دریافت مشاوره
            </a>
            <a className="p-4 m-4 bg-primary rounded-2xl w-2/4 text-text text-center shadow-custom-light hover:bg-hover hover:text-white primary-transitsion max-sm:w-full" href="">
              نمونه کار ها
            </a>
          </div>
        </div>

        <div className="flex justify-center mt-4 md:mt-0">
          <Image src={poster} alt="Codingo Plus" width={450} height={200} className="rounded-3xl max-w-full h-auto"/>
        </div>

      </div>
    </main>
  );
}