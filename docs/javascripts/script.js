"use strict";
(function () {
    // detect the theme on page load
    const detectColorScheme = () => {
        let theme = 'dark'; // default to dark
        // local storage is used to override OS theme settings
        if (localStorage.getItem('theme')) {
            if (localStorage.getItem('theme') === 'light') {
                theme = 'light';
            }
        }
        else if (!window.matchMedia) {
            // matchMedia method not supported
            return;
        }
        else if (window.matchMedia('(prefers-color-scheme: light)').matches) {
            theme = 'light';
        }
        if (theme === 'light') {
            document.documentElement.setAttribute('data-theme', 'light');
        }
    };
    detectColorScheme();
    // enable toggling the theme
    const toggleSwitch = document.querySelector('.theme-switch input[type="checkbox"]');
    // sets a localStorage variable to track the theme between page loads
    function switchTheme(e) {
        if (e.target.checked) {
            localStorage.setItem('theme', 'light');
            document.documentElement.setAttribute('data-theme', 'light');
            if (toggleSwitch != null) {
                toggleSwitch.checked = true;
            }
        }
        else {
            localStorage.setItem('theme', 'dark');
            document.documentElement.setAttribute('data-theme', 'dark');
            if (toggleSwitch != null) {
                toggleSwitch.checked = false;
            }
        }
    }
    // event listener
    if (toggleSwitch != null) {
        toggleSwitch.addEventListener('change', switchTheme, false);
    }
    // keep checkbox in sync
    if (document.documentElement.getAttribute('data-theme') === 'light' && toggleSwitch != null) {
        toggleSwitch.checked = true;
    }
    // index page table sorting
    const indexTable = document.getElementById('index-table');
    if (indexTable) {
        const tbody = indexTable.querySelector('tbody');
        const headers = indexTable.querySelectorAll('th.sortable');
        const sortTable = (colIndex) => {
            if (!tbody)
                return;
            const rows = Array.from(tbody.querySelectorAll('tr'));
            rows.sort((a, b) => {
                const aText = (a.cells[colIndex].textContent || '').toLowerCase();
                const bText = (b.cells[colIndex].textContent || '').toLowerCase();
                return aText.localeCompare(bText);
            });
            rows.forEach(row => {
                // clear old author anchors
                row.removeAttribute('id');
                tbody.appendChild(row);
            });
            // set anchors on first occurrence of each author when sorted by author
            if (colIndex === 1) {
                const seen = {};
                rows.forEach(row => {
                    const authorLinks = row.cells[1].querySelectorAll('a');
                    authorLinks.forEach(link => {
                        const name = link.textContent || '';
                        if (!seen[name]) {
                            seen[name] = true;
                            row.id = name;
                        }
                    });
                });
            }
        };
        const setActiveHeader = (target) => {
            headers.forEach(h => h.classList.remove('active'));
            target.classList.add('active');
        };
        headers.forEach((header, _idx) => {
            header.addEventListener('click', () => {
                const sort = header.dataset.sort;
                const colIndex = sort === 'author' ? 1 : 0;
                setActiveHeader(header);
                sortTable(colIndex);
            });
        });
        // handle hash navigation: sort by author and scroll to anchor
        const hash = window.location.hash.substring(1);
        if (hash) {
            sortTable(1);
            setActiveHeader(indexTable.querySelector('th[data-sort="author"]'));
            // scroll to the author anchor after sort
            requestAnimationFrame(() => {
                const target = document.getElementById(hash);
                if (target) {
                    target.scrollIntoView();
                }
            });
        }
    }
    // explore page tags
    let activeTags = [];
    const countVisibleProjects = () => {
        const projectElements = document.getElementsByClassName('project');
        let count = 0;
        for (let i = 0; i < projectElements.length; i++) {
            const element = projectElements[i];
            if (element.classList.contains('show')) {
                count++;
            }
        }
        return count;
    };
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
                if (activeTags.every(tag => projectTags.includes(tag))) {
                    project.classList.add('show');
                }
                else {
                    project.classList.remove('show');
                }
            }
        });
        // display a "no results" message
        const noResults = document.getElementById('no-results');
        if (noResults != undefined) {
            if (countVisibleProjects() == 0) {
                noResults.classList.add('show');
            }
            else {
                noResults.classList.remove('show');
            }
        }
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
