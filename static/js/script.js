document.getElementById("crawling").addEventListener("submit", handleSubmit);

async function handleSubmit(e) {
    e.preventDefault();
    const hashtag = getHashtag();
    if (!hashtag)
        return;

    prepareUI();

    let videos = await fetchVideosWithFallback(hashtag);
    if (!Array.isArray(videos)) {
        showError("ERROR: Not an array");
        return;
    }

    renderResults(videos);
}

function getHashtag() {
    return document.getElementById("hashtag").value.trim();
}

function prepareUI() {
    document.getElementById("search-box").classList.add("expanded");
    document.getElementById("loading").classList.remove("hidden");
    document.getElementById("result").classList.add("hidden");
}

async function fetchVideosWithFallback(hashtag) {
    try {
        const res = await fetch(`/videos?hashtag=${encodeURIComponent(hashtag)}`);
        if (res.ok)
            return await res.json();

        if ([400, 404, 410].includes(res.status)) {
            return await crawlVideos(hashtag);
        }
    }
    catch (err) {
        showError("Error occurred");
        return null;
    }
}

async function crawlVideos(hashtag) {
    const formData = new FormData();
    formData.append("hashtag", hashtag);
    const res = await fetch("/crawl", { 
        method: "POST",
        body: formData
    });

    if (!res.ok) {
        showError("ERROR: Crawling Failed");
        return null;
    }
    
    return await res.json();
}

function showError(message) {
    document.getElementById("loading").classList.add("hidden");
    const resBox = document.getElementById("result");
    resBox.classList.remove("hidden");
    resBox.innerHTML = `<p style="color:red;">${message}</p>`;
}

function renderResults(videos) {
    document.getElementById("loading").classList.add("hidden");
    const resBox = document.getElementById("result");
    resBox.classList.remove("hidden");

    let result = `
        <p>The top 10 videos are selected based on this month's uploads and sorted by view count.</p>
        <table class="video-table">
        <thead>
            <tr>
                <th>Title</th>
                <th>Channel</th>
                <th>Link</th>
            </tr>
        </thead>
        <tbody>
    `;

    for (const video of videos) {
        result += `
        <tr>
            <td>${video.title}</td>
            <td>${video.channel}</td>
            <td><a href="${video.url}" target="_blank">Watch</a></td>
        </tr>`;
    }

    result += `
    </tbody>
    </table>`;
    resBox.innerHTML = result;
}
