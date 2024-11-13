import Link from "next/link";

export default function Denied() {
    return (
        <div>
            <h1>Access Denied</h1>
            <p>
                You do not have permission to access this page.
            </p>
            <Link href="/" className="p-4 bg-amber-950 text-slate-50">Voltar</Link>
        </div>
    );
}