import type { Metadata } from "next";
import "./assets/css/globals.css";



export const metadata: Metadata = {
  title: "Codingo Plus",
  description: "Dev Compony",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>
        {children}
      </body>
    </html>
  );
}
