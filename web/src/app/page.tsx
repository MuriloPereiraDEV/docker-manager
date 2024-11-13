'use client';

import Link from "next/link";


export default function Home() {
  return (
    <div>
      <h1>Home</h1>
      <p>Welcome to the Docker Manager!</p>
      <br />
      <Link href="/auth/login">Acessar</Link>
    </div>
  );
}
