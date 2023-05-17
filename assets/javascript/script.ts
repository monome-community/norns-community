(function() {

  // detect the theme on page load
  const detectColorScheme = () => {
    let theme = "dark"; // default to light
    // local storage is used to override OS theme settings
    if (localStorage.getItem("theme")) {
      if (localStorage.getItem("theme") === "light") {
        theme = "light";
      }
    } else if (!window.matchMedia) {
      // matchMedia method not supported
      return;
    } else if (window.matchMedia("(prefers-color-scheme: light)").matches) {
      // OS theme setting detected as dark
      theme = "light";
    }
    // light theme preferred
    if (theme === "light") {
      document.documentElement.setAttribute("data-theme", "light");
    }
  }
  detectColorScheme()

  // enable toggling the theme
  const toggleSwitch = document.querySelector<HTMLInputElement>('.theme-switch input[type="checkbox"]');

  // Function that changes the theme, and sets a localStorage variable to track the theme between page loads
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

  // Listener for changing themes
  if (toggleSwitch != null) {
    toggleSwitch.addEventListener('change', switchTheme, false);
  }

  // Pre-check the light-theme checkbox if light-theme is set
  if (document.documentElement.getAttribute('data-theme') === 'light' && toggleSwitch != null) {
    toggleSwitch.checked = true;
  }

  // explore page tags
  let activeTags : string[] = []

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
        if (activeTags.some(tag => projectTags.includes(tag))) {
          project.classList.add('show')
        } else {
          project.classList.remove('show')
        }
      }
    })
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