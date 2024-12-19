import type { Metadata } from "next";
import "../assets/css/globals.css";
import Image from 'next/image';
import Header from "@/components/layouts/Header";
import Footer from "@/components/layouts/footer";

export const metadata: Metadata = {
  title: "کدینگو",
  description: "Dev Compony",
  icons: {
    icon: '/imgs/logo/logo.png',
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="fa" dir="rtl">
      <head>
        <link rel="icon" href="/imgs/logo/logo.png" />
      </head>
      <body className="bg-background">
        <Header></Header>
        {children}
        <Footer></Footer>
      </body>
    </html>
  );
}