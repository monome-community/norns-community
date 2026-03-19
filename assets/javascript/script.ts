(function() {

  // detect the theme on page load
  const detectColorScheme = () => {
    let theme = 'dark'; // default to dark
    // local storage is used to override OS theme settings
    if (localStorage.getItem('theme')) {
      if (localStorage.getItem('theme') === 'light') {
        theme = 'light';
      }
    } else if (!window.matchMedia) {
      // matchMedia method not supported
      return;
    } else if (window.matchMedia('(prefers-color-scheme: light)').matches) {
      theme = 'light';
    }
    if (theme === 'light') {
      document.documentElement.setAttribute('data-theme', 'light');
    }
  }
  detectColorScheme()

  // enable toggling the theme
  const toggleSwitch = document.querySelector<HTMLInputElement>('.theme-switch input[type="checkbox"]');

  // sets a localStorage variable to track the theme between page loads
  function switchTheme(e: Event): void {
    if ((e.target as HTMLInputElement).checked) {
      localStorage.setItem('theme', 'light');
      document.documentElement.setAttribute('data-theme', 'light');
      if (toggleSwitch != null) {
        toggleSwitch.checked = true;
      }
    } else {
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
  const indexTable = document.getElementById('index-table')
  if (indexTable) {
    const tbody = indexTable.querySelector('tbody')
    const headers = indexTable.querySelectorAll('th.sortable')

    const sortTable = (colIndex: number) => {
      if (!tbody) return
      const rows = Array.from(tbody.querySelectorAll('tr'))
      rows.sort((a, b) => {
        const aText = (a.cells[colIndex].textContent || '').toLowerCase()
        const bText = (b.cells[colIndex].textContent || '').toLowerCase()
        return aText.localeCompare(bText)
      })
      rows.forEach(row => {
        row.removeAttribute('id')
        tbody.appendChild(row)
      })
      // set anchors when sorted by author: composite slug of all authors joined with -
      if (colIndex === 1) {
        const seen: Record<string, boolean> = {}
        rows.forEach(row => {
          const link = row.cells[1].querySelector('a')
          if (!link) return
          const slug = link.getAttribute('href')?.replace('/#', '') || ''
          if (slug && !seen[slug]) {
            seen[slug] = true
            row.id = slug
          }
        })
      }
    }

    const setActiveHeader = (target: Element) => {
      headers.forEach(h => h.classList.remove('active'))
      target.classList.add('active')
    }

    headers.forEach((header, _idx) => {
      header.addEventListener('click', () => {
        const sort = (header as HTMLElement).dataset.sort
        const colIndex = sort === 'author' ? 1 : 0
        setActiveHeader(header)
        sortTable(colIndex)
      })
    })

    // handle hash navigation: sort by author and scroll to anchor
    const hash = window.location.hash.substring(1)
    if (hash) {
      sortTable(1)
      setActiveHeader(indexTable.querySelector('th[data-sort="author"]')!)
      // scroll to the author anchor after sort
      // supports both composite slugs (license-tyleretters) and individual author names
      requestAnimationFrame(() => {
        let target = document.getElementById(hash)
        if (!target && tbody) {
          // find first row whose composite anchor contains this author
          const rows = Array.from(tbody.querySelectorAll<HTMLElement>('tr[id]'))
          target = rows.find(row => row.id.split('-').includes(hash)) || null
        }
        if (target) {
          target.scrollIntoView()
        }
      })
    }
  }

  // explore page tags
  let activeTags : string[] = []

  const countVisibleProjects = (): number => {
    const projectElements = document.getElementsByClassName('project');
    let count = 0;
    for (let i = 0; i < projectElements.length; i++) {
      const element = projectElements[i];
      if (element.classList.contains('show')) {
        count++;
      }
    }
    return count;
  }

  const refresh = () => {
    console.log(activeTags)
    // if there are no activeTags, show everything
    if (activeTags.length === 0) {
      const projects = document.querySelectorAll('.project')
      projects.forEach(project => {
        if (project instanceof HTMLElement) {
          project.classList.add('show')
        }
      })
      return
    }
    // show all projects which a classname in activeTags
    const projects = document.querySelectorAll('.project')
    projects.forEach(project => {
      if (project instanceof HTMLElement) {
        // protect against undefined tags
        if (project.dataset.tags === undefined) {
          return
        }
        const projectTags = project.dataset.tags.split(' ')
        if (activeTags.every(tag => projectTags.includes(tag))) {
          project.classList.add('show')
        } else {
          project.classList.remove('show')
        }
      }
    })

    // display a "no results" message
    const noResults = document.getElementById('no-results')
    if (noResults != undefined) {
      if (countVisibleProjects() == 0) {
        noResults.classList.add('show')
      } else {
        noResults.classList.remove('show')
      }
    }
  }

  const tagClick = (button: HTMLElement) => {
    const activeClass = 'tag-active'
    let tag = button.dataset.tag
    // protect against undefined tags
    if (tag === undefined) {
      return
    }
    button.dataset.toggle = (button.dataset.toggle === 'off') ? 'on' : 'off'
    // add or remove the tag from activeTags
    if (button.dataset.toggle === 'on') {
      activeTags.push(tag)
      button.classList.add(activeClass)
    } else {
      activeTags = activeTags.filter(activeTag => activeTag !== tag)
      button.classList.remove(activeClass)
    }
    refresh()
  }

  // add event listeners to all tag buttons
  const buttons = document.querySelectorAll('button')
  buttons.forEach(button => {
    button.addEventListener('click', event => {
      if (event.target instanceof HTMLElement) {
        tagClick(event.target)
      }
    })
  })

  refresh()

})()