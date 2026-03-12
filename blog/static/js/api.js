async function loadPosts() {
    const token = localStorage.getItem("access");
    const response = await fetch("/api/posts", {
       method: "GET",
       headers: {
        "Authorization": "Bearer"+accessToken
       }
    });

    const data = await response.json();
}