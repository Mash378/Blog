async function refreshToken() {
    const refresh = localStorage.getItem("refresh");

    const res = await fetch("/api/token/refresh/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ refresh })
    });

    const data = await res.json();
    localStorage.setItem("access", data.access);
}