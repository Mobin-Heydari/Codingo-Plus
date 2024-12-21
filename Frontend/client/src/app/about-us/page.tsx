import Image from "next/image";

export default function AboutUs() {
    return (
        <main className="flex flex-col justify-evenly">
            <section className="flex flex-row max-lg:flex-col p-8 justify-around max-sm:p-2 my-12">
                <div className="basis-2/5 flex justify-between flex-col">
                    <h1 className="text-3xl text-center text-primary p-3 font-bold">ماموریت ما</h1>
                    <p className="text-lg text-text p-6 my-5">
                        تیم کدینگو پلاس متعهد به ارائه راه‌حل‌های نوآورانه و کارآمد است که نیازهای مشتریان را به بهترین نحو برآورده می‌کند. ما با تلفیق خلاقیت و فناوری‌های پیشرفته، تجربیاتی را خلق می‌کنیم که نه تنها جذاب و کاربردی هستند، بلکه تأثیری ماندگار بر روی کسب‌وکار شما می‌گذارند. هدف ما این است که با همکاری نزدیک با شما، راه‌حل‌های منحصر به فردی طراحی کنیم که به رشد و توسعه کسب‌وکارتان کمک کند. ما به اهمیت هر پروژه به عنوان یک فرصت برای ارائه ارزش پایدار باور داریم و تمام تلاشمان را می‌کنیم تا بهترین نتیجه ممکن را ارائه دهیم.
                    </p>
                </div>
                <div className="flex justify-center mt-4 md:mt-0">
                    <Image src="" alt="ماموریت ما" width={450} height={200} />
                </div>
            </section>

            <section className="flex flex-row max-lg:flex-col p-8 justify-around max-sm:p-2 my-12">
                <div className="basis-2/5 flex justify-between flex-col">
                    <h2 className="text-3xl text-center text-primary p-3 font-bold">داستان ما</h2>
                    <p className="text-lg text-text p-6 my-5">
                        تیم کدینگو پلاس در سال ۲۰۱۵ با اشتیاق به فناوری و طراحی خلاقانه تأسیس شد. از آن زمان تاکنون، ما با تحقق رویاهای دیجیتالی مشتریانمان، مسیری پر از موفقیت را پیموده‌ایم. هر پروژه برای ما فرصتی است تا نشان دهیم چگونه می‌توان با هم‌افزایی تجربه و نوآوری، نتایجی فراتر از انتظارات را ارائه داد. ما باور داریم که داستان‌های موفقیت ما، گواهی بر تعهد و توانمندی‌های بی‌نظیر تیم ما هستند. از اولین پروژه‌هایی که با اشتیاق و انگیزه بالا انجام دادیم تا به امروز که به یکی از برترین تیم‌های حوزه طراحی و توسعه وب و اپلیکیشن تبدیل شده‌ایم، همیشه تلاش کرده‌ایم تا بهترین‌ها را برای مشتریانمان به ارمغان بیاوریم. ما به آینده‌ای روشن و پر از فرصت‌های جدید نگاه می‌کنیم و آماده‌ایم تا با شما در این مسیر همراه باشیم.
                    </p>
                </div>
                <div className="flex justify-center mt-4 md:mt-0">
                    <Image src="" alt="داستان ما" width={450} height={200} />
                </div>
            </section>

            <section className="flex flex-row max-lg:flex-col p-8 justify-around max-sm:p-2 my-12">
                <div className="basis-2/5 flex justify-between flex-col">
                    <h2 className="text-3xl text-center text-primary p-3 font-bold">ارزش‌های ما</h2>
                    <p className="text-lg text-text p-6 my-5">
                        ما در کدینگو پلاس به مجموعه‌ای از ارزش‌های بنیادین پایبند هستیم که در تمام فعالیت‌های ما نمود پیدا می‌کنند:
                        <ul className="grid gap-3 mt-3">
                            <li><strong className="font-bold text-secondary">صداقت و شفافیت:</strong> ارتباطات صادقانه و شفاف با مشتریان و همکاران، کلید موفقیت ما است. ما به اهمیت اعتماد و شفافیت در تمام تعاملاتمان باور داریم و تلاش می‌کنیم تا با ایجاد محیطی صادقانه و باز، پایه‌های یک همکاری موفق را بنا کنیم.</li>
                            <li><strong className="font-bold text-secondary">خلاقیت و نوآوری:</strong> ما به دنبال راه‌حل‌های خلاقانه و نوآورانه هستیم که به ما امکان می‌دهد تا بهترین نتایج را ارائه دهیم. خلاقیت در مرکز تمامی فعالیت‌های ما قرار دارد و ما به طور مداوم به دنبال راه‌های جدید و خلاقانه برای بهبود خدمات و محصولاتمان هستیم.</li>
                            <li><strong className="font-bold text-secondary">مشتری‌مداری:</strong> رضایت مشتریان و تحقق نیازهای آنها در اولویت نخست ما قرار دارد. ما به اهمیت گوش دادن به مشتریان و درک دقیق نیازها و انتظارات آنها باور داریم و تمام تلاشمان را می‌کنیم تا با ارائه خدماتی ممتاز، مشتریانمان را راضی و خوشنود نگه داریم.</li>
                            <li><strong className="font-bold text-secondary">کیفیت و تعهد:</strong> ما متعهد به ارائه خدمات با بالاترین کیفیت ممکن و حفظ استانداردهای برتر هستیم. کیفیت در تمامی مراحل کار ما نقش حیاتی دارد و ما به اهمیت ارائه خدماتی که استانداردهای بالای صنعت را رعایت می‌کنند، اعتقاد داریم.</li>
                        </ul>
                    </p>
                </div>
                <div className="flex justify-center mt-4 md:mt-0">
                    <Image src="" alt="ارزش‌های ما" width={450} height={200} />
                </div>
            </section>

            <section className="flex flex-row max-lg:flex-col p-8 justify-around max-sm:p-2 my-12">
                <div className="basis-2/5 flex justify-between flex-col">
                    <h2 className="text-3xl text-center text-primary p-3 font-bold">چرا ما را انتخاب کنید</h2>
                    <p className="text-lg text-text p-6 my-5">
                        تیم کدینگو پلاس به دلیل تخصص، تعهد و نوآوری، انتخاب برتر شما برای همکاری در پروژه‌های دیجیتالی است.
                    </p>
                    <h2 className="text-2xl text-secondary p-3 font-bold">تجربه و تخصص</h2>
                    <p className="text-lg text-text p-6 my-5">
                        ما با ترکیب تجربه‌های موفق و تخصص‌های متنوع، راه‌حل‌هایی کارآمد و موثر ارائه می‌دهیم. تجربه‌های ما در پروژه‌های مختلف نشان‌دهنده توانایی ما در ارائه راه‌حل‌های پیچیده و سفارشی برای نیازهای منحصر به فرد هر مشتری است.
                    </p>
                    <h2 className="text-2xl text-primary p-3 font-bold">تعهد به کیفیت</h2>
                    <p className="text-lg text-text p-6 my-5">
                        ما همواره تلاش می‌کنیم تا با حفظ بالاترین استانداردهای کیفیت، نتایجی فراتر از انتظارات شما ارائه دهیم. کیفیت در مرکز تمامی فعالیت‌های ما قرار دارد و ما به اهمیت ارائه خدماتی که استانداردهای بالای صنعت را رعایت می‌کنند، اعتقاد داریم.
                    </p>
                    <h2 className="text-2xl text-secondary p-3 font-bold">ارتباط و همکاری</h2>
                    <p className="text-lg text-text p-6 my-5">
                        ما معتقدیم که ارتباط موثر و همکاری نزدیک با مشتریان، کلید اصلی تحقق اهداف مشترک و موفقیت پروژه‌ها است. ما به اهمیت گوش دادن به نیازها و نظرات مشتریانمان باور داریم و تلاش می‌کنیم تا با ایجاد یک محیط همکاری باز و شفاف، بهترین نتایج را به دست آوریم.
                    </p>
                    <h2 className="text-2xl text-primary p-3 font-bold">نوآوری و خلاقیت</h2>
                    <p className="text-lg text-text p-6 my-5">
                        با تکیه بر خلاقیت و نوآوری، ما راه‌حل‌های منحصر به فردی ارائه می‌دهیم که کسب‌وکار شما را متمایز می‌کند. خلاقیت در مرکز تمامی فعالیت‌های ما قرار دارد و ما به طور مداوم به دنبال راه‌های جدید و خلاقانه برای بهبود خدمات و محصولاتمان هستیم.
                    </p>
                </div>
                <div className="flex justify-center mt-4 md:mt-0">
                    <Image src="" alt="چرا ما را انتخاب کنید" width={450} height={200} />
                </div>
            </section>
        </main>
    )
}