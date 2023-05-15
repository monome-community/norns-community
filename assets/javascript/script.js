"use strict";
(function () {
    let activeTags = [];
    const refresh = () => {
        console.log(activeTags);
        // if there are no activeTags, show everything
        if (activeTags.length === 0) {
            const projects = document.querySelectorAll('.project');
            projects.forEach(project => {
                if (project instanceof HTMLElement) {
                    project.classList.add('show');
                }
            });
            return;
        }
        // show all projects which a classname in activeTags
        const projects = document.querySelectorAll('.project');
        projects.forEach(project => {
            if (project instanceof HTMLElement) {
                // protect against undefined tags
                if (project.dataset.tags === undefined) {
                    return;
                }
                const projectTags = project.dataset.tags.split(' ');
                if (activeTags.some(tag => projectTags.includes(tag))) {
                    project.classList.add('show');
                }
                else {
                    project.classList.remove('show');
                }
            }
        });
    };
    const tagClick = (button) => {
        const activeClass = 'tag-active';
        let tag = button.dataset.tag;
        // protect against undefined tags
        if (tag === undefined) {
            return;
        }
        button.dataset.toggle = (button.dataset.toggle === 'off') ? 'on' : 'off';
        // add or remove the tag from activeTags
        if (button.dataset.toggle === 'on') {
            activeTags.push(tag);
            button.classList.add(activeClass);
        }
        else {
            activeTags = activeTags.filter(activeTag => activeTag !== tag);
            button.classList.remove(activeClass);
        }
        refresh();
    };
    // add event listeners to all tag buttons
    const buttons = document.querySelectorAll('button');
    buttons.forEach(button => {
        button.addEventListener('click', event => {
            if (event.target instanceof HTMLElement) {
                tagClick(event.target);
            }
        });
    });
    refresh();
})();
