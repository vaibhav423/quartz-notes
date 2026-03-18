function toggleHeading(this: HTMLElement) {
  const heading = this.parentElement!
  heading.classList.toggle("collapsed")
  const isCollapsed = heading.classList.contains("collapsed")

  // Find the heading level (e.g., 2 for H2)
  const level = parseInt(heading.tagName.substring(1))

  let currentElement = heading.nextElementSibling as HTMLElement | null

  while (currentElement) {
    // If we hit a heading of the same or higher level, stop hiding
    if (currentElement.tagName.match(/^H[1-6]$/)) {
      const currentLevel = parseInt(currentElement.tagName.substring(1))
      if (currentLevel <= level) {
        break
      }
    }

    // Toggle the display property
    if (isCollapsed) {
      currentElement.style.display = "none"
    } else {
      currentElement.style.display = ""
    }

    currentElement = currentElement.nextElementSibling as HTMLElement | null
  }
}

function setupFoldableHeadings() {
  const article = document.querySelector("article.popover-hint")
  if (!article) return

  const headings = article.querySelectorAll("h1, h2, h3, h4, h5, h6")

  for (const heading of headings) {
    // Prevent adding multiple arrows if re-navigated
    if (heading.querySelector(".foldable-arrow")) continue

    // Create the fold arrow button
    const arrowButton = document.createElement("button")
    arrowButton.className = "foldable-arrow"
    arrowButton.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-chevron-down"><path d="m6 9 6 6 6-6"/></svg>`

    // Add click listener
    arrowButton.addEventListener("click", toggleHeading)
    window.addCleanup(() => arrowButton.removeEventListener("click", toggleHeading))

    // Prepend the arrow to the heading
    heading.insertBefore(arrowButton, heading.firstChild)
  }
}

document.addEventListener("nav", setupFoldableHeadings)
