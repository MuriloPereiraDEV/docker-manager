'use client';

import { signIn } from "next-auth/react";
import { useRouter } from "next/navigation";
import { useState } from "react";

export default function FormLogin() {
    const router = useRouter();

    const [email, setEmail] = useState<string>('');
    const [password, setPassword] = useState<string>('');
    const [error, setError] = useState<string | null>(null);

    const handleSubmit = async (event: React.FormEvent) => {
        event.preventDefault();

        if (!email || !password) {
            setError('Preencha todos os campos');
            return;
        }

        try {
            const response = await signIn('credentials', {
                redirect: false,
                email,
                password
            })
            console.log('[LOGIN_RESPONSE]: ', response);

            if (!response?.error) {
                router.refresh()
                router.push('/manager')
            } else {
                setError('Email ou senha invalidos!')
            }
        } catch (error) {
            console.error("[LOGIN_ERROR]: ", error);
            setError('Erro ao fazer login');
        }
    }

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <h1>Login</h1>
                <p>Faça login para continuar</p>
                <div>
                    <div>
                        <label htmlFor="email">E-mail</label>
                        <input
                            type="text"
                            name="email"
                            onChange={(e) => setEmail(e.target.value)}
                            className="border rounded w-fit p-3"
                        />
                    </div>
                    <div>
                        <label htmlFor="password">Senha</label>
                        <input
                            type="text"
                            name="password"
                            onChange={(e) => setPassword(e.target.value)}
                            className="border rounded w-fit p-3"
                        />
                    </div>
                    {error && <span className="text-red-400 text-sm block mt-2">{error}</span>}
                    <button
                        type="submit"
                        className="mt -10 bg-rose-950 text-slate-50 rounded"
                    >Entrar</button>
                </div>
            </form>
        </div>
    );
}