export default {
    install(app) {
      const themeStorageKey = "tablerTheme";
      const defaultTheme = "light";
      let theme = null;
  
      function initializeTheme() {
        const storedTheme = localStorage.getItem(themeStorageKey);
        theme = storedTheme ? storedTheme : defaultTheme;
        applyTheme();
      }
  
      function applyTheme() {
        if (theme === "dark") {
          document.body.setAttribute("data-bs-theme", theme);
        } else {
          document.body.removeAttribute("data-bs-theme");
        }
      }
  
      function toggleTheme() {
        theme = theme === "dark" ? "light" : "dark";
        localStorage.setItem(themeStorageKey, theme);
        applyTheme();
      }
  
      initializeTheme();
  
      app.config.globalProperties.$theme = {
        get: () => theme,
        toggle: toggleTheme,
      };
    },
  };
  