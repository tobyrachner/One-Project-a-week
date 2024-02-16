function filterBy(tag) {
    const container = document.getElementById('container');
    const projects = container.getElementsByTagName('*');

    for (let i = 0; i < projects.length; i++) {
        var tags = projects[i].data-tags;
        console.log(typeof tags)
        if (tags.includes(tag)) {
            projects[i].style.display = 'initial';
        } else {
        projects[i].style.display = 'none';
        }
    }
}