import Image from "next/image";
import codingo_poster from '../assets/imgs/home/codingo-poster.png';
import web_card from '../assets/imgs/home/web.jpg';

export default function Home() {
  return (
    <main className="flex flex-col justify-evenly my-24">

      <section className="flex flex-row max-lg:flex-col p-12 justify-around max-sm:p-2">

        <div className="basis-2/5 flex justify-between flex-col">

          <h2 className="text-3xl text-secondary p-5 my-4 rounded border-r-4 border-r-primary max-sm:text-2xl">تحقق رویاهای <span className="text-primary">دیجیتال</span> شما</h2>
          <p className="text-lg text-text p-6 my-4 rounded border-r-4 border-r-primary">
            در <strong className="font-bold text-secondary">مجموعه کدینگ و پلاس</strong>، ما با ترکیب خلاقیت و فناوری پیشرفته، راه‌حل‌هایی نوآورانه برای وب‌سایت‌ها و اپلیکیشن‌های شما ارائه می‌دهیم. ما به تحقق رؤیاهای دیجیتالی شما ایمان داریم و تلاش می‌کنیم تا هر پروژه را به یک داستان موفقیت‌آمیز تبدیل کنیم.
          </p>
          <p className="text-lg text-text p-6 my-4 rounded border-r-4 border-r-secondary">
            <strong>مأموریت ما:</strong> خلق تجربه‌های دیجیتالی که نه تنها جذاب و کارآمد هستند بلکه تأثیری ماندگار بر روی کسب‌وکار شما می‌گذارند.
          </p>
          <p className="text-lg text-text p-6 my-4 rounded border-r-4 border-r-primary">
            کدنیگو پلاس مجموعه ای از طراحان و توسعه دهندگانی با تجربه و مدرن است که در زمینه ی طراحی و توسعه وب اپلیکیشن و اپلیکیشن سال ها تجربه و تخصص جمع آوری کرده اند.
          </p>

          <div className="flex justify-evenly max-sm:flex-col text-center my-5 flex-wrap gap-4">
            <p className="cursor-pointer p-4 text-sm text-text rounded-xl shadow-custom-light border-r-4 border-primary max-sm:my-3">بشتیبانی رایگان</p>
            <p className="cursor-pointer p-4 text-sm text-text rounded-xl shadow-custom-light border-r-4 border-primary max-sm:my-3">طراحی اختصاصی</p>
            <p className="cursor-pointer p-4 text-sm text-text rounded-xl shadow-custom-light border-r-4 border-secondary max-sm:my-3">کدنویسی بهینه</p>
            <p className="cursor-pointer p-4 text-sm text-text rounded-xl shadow-custom-light border-r-4 border-primary max-sm:my-3">تکنولوژی های روز</p>
          </div>

          <div className="flex justify-evenly text-center my-5 max-sm:flex-col gap-4">
            <a className="p-4 bg-secondary rounded-2xl w-2/4 text-white text-center shadow-custom-light hover:bg-primary hover:text-text primary-transitsion max-sm:w-full" href="">
              دریافت مشاوره
            </a>
            <a className="p-4 bg-primary rounded-2xl w-2/4 text-text text-center shadow-custom-light hover:bg-hover hover:text-white primary-transitsion max-sm:w-full" href="">
              نمونه کار ها
            </a>
          </div>
        </div>

        <div className="flex justify-center mt-4 md:mt-0">
          <Image src={codingo_poster} alt="Codingo Plus" width={450} height={200} className="rounded-3xl max-w-full h-auto"/>
        </div>
        
      </section>

      {/* Our services part */}
      <section className="flex justify-evenly flex-col gap-4">

        <div>
          <h3>کدینگو چه خدماتی به شما ارايه می دهد؟</h3>
          <h4>طراحی و توسعه انواع بلتفرم ها و کسب و کار های آنلاین و راه اندازی آن ها در بستر وب و مبایل از تخصص متخصاصن کدینگو است</h4>
        </div>

        <div className="flex justify-evenly flex-wrap gap-5">
        <div className="relative flex justify-evenly flex-col w-1/6 shadow-custom-dark rounded-3xl p-5 gap-5 hover:bg-orange-100 hover:w-1/5 primary-transitsion">
          <div className="relative">
            <Image src={web_card} alt="Codingo Plus" width={400} height={200} className="rounded-3xl max-w-full h-auto"/>
            <div className="absolute inset-0 bg-white opacity-50 transition-opacity duration-300 hover:opacity-100"></div>
            <div className="absolute inset-0 flex flex-col justify-center items-center text-center opacity-0 transition-opacity duration-300 hover:opacity-100">
              <h5 className="text-xl text-secondary hover:text-primary primary-transitsion">طراحی و توسعه وب</h5>
              <p className="text-sm text-justify p-2">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Impedit corporis ducimus expedita! Voluptatum praesentium minima adipisci aliquam fugit ut nemo similique debitis unde cumque. Expedita necessitatibus at unde maiores quo aperiam aspernatur repellendus aliquid nam? Commodi obcaecati, a voluptatem accusamus consequatur velit culpa rerum. Minus ipsa similique sequi facilis. Natus.</p>
            </div>
          </div>
        </div>
        </div>

      </section>
    </main>
  );
}