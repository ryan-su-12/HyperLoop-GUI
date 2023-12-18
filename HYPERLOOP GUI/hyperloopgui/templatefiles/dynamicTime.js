function getTime() {
    const now = new Date();
    const hours = now.getHours();
    const minutes = now.getMinutes();
    const seconds = now.getSeconds();
    const timeString = `${hours}:${minutes}:${seconds}`;
    return timeString;
    }
    
    function updateTime() {
        const timeElement = document.getElementById("time");
        const timeString = getTime();
        timeElement.innerHTML = timeString;
    }
    
    setInterval(updateTime, 1000);