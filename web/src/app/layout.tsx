import type { Metadata } from "next";
import localFont from "next/font/local";
import "./globals.css";
import SessionProv from "@/providers/SessionProv";

const geistSans = localFont({
  src: "./fonts/GeistVF.woff",
  variable: "--font-geist-sans",
  weight: "100 900",
});
const geistMono = localFont({
  src: "./fonts/GeistMonoVF.woff",
  variable: "--font-geist-mono",
  weight: "100 900",
});

export const metadata: Metadata = {
  title: "Docker Manager",
  description: "Docker manager that facilitates all configurations and handling.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <SessionProv>
      <html lang="pt-br">
        <body
        // className={`${geistSans.variable} ${geistMono.variable} antialiased`}
        >
          {children}
        </body>
      </html>
    </SessionProv>
  );
}
