'use client';

import { signOut } from "next-auth/react";

export default function SignOutComponents() {
    return (
        <button onClick={() => signOut({ callbackUrl: "/" })}>Sair</button>
    )
}