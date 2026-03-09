async function loadFiles(){
    try {
        let response = await fetch("/")
        let text = await response.text()
        // Simple parse for demo, ideally parse HTML list
        console.log("Files loaded");
    } catch(e) {
        console.error("Error loading files", e);
    }
}
window.onload = loadFiles;
