function filterBy(tag) {
    const container = document.getElementById('container');
    const projects = container.children

    for (let i = 0; i < projects.length; i++) {
        if (tag == 'All') {
            projects[i].style.display = 'initial';
        } else {
            let tags = projects[i].dataset.tags;
            if (tags.includes(tag)) {
                projects[i].style.display = 'initial';
            } else {
            projects[i].style.display = 'none';
            }
        }
    }
}

function toggleFilters(div) {
    const children = div.children;
    let tags = ['All', ...div.dataset.tags.split(', ')];
    let isToggled = children[0].dataset.toggled;

    if (isToggled == 't') {
        children[0].dataset.toggled = 'f';
        for (let i = 1; i < children.length; i++) {
            children[i].style.display = 'none';
        }
    } else {
        children[0].dataset.toggled = 't';
        for (let i = 0; i < tags.length; i++) {
            let button = document.createElement('button');
            button.classList.add('filter-tag');
            button.innerText = tags[i];
            button.setAttribute('onclick', "filterBy('" + tags[i] + "')");
            div.append(button);
        }
    }
}