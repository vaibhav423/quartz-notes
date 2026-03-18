import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
// @ts-ignore
import foldableScript from "./scripts/foldable.inline"

export default (() => {
  const FoldableHeadings: QuartzComponent = ({}: QuartzComponentProps) => {
    return null // This component only injects scripts and styles
  }

  FoldableHeadings.css = `
  article.popover-hint h1,
  article.popover-hint h2,
  article.popover-hint h3,
  article.popover-hint h4,
  article.popover-hint h5,
  article.popover-hint h6 {
    position: relative;
    display: flex;
    align-items: center;
  }

  .foldable-arrow {
    background: transparent;
    border: none;
    cursor: pointer;
    padding: 0;
    margin: 0;
    margin-right: 0.5rem;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--gray);
    transition: transform 0.2s ease, color 0.2s ease;
    width: 1.2em;
    height: 1.2em;
  }

  .foldable-arrow:hover {
    color: var(--secondary);
  }

  .foldable-arrow svg {
    width: 100%;
    height: 100%;
    transition: transform 0.2s ease;
  }

  /* When collapsed, rotate the arrow to point right */
  h1.collapsed .foldable-arrow svg,
  h2.collapsed .foldable-arrow svg,
  h3.collapsed .foldable-arrow svg,
  h4.collapsed .foldable-arrow svg,
  h5.collapsed .foldable-arrow svg,
  h6.collapsed .foldable-arrow svg {
    transform: rotate(-90deg);
  }
  `

  FoldableHeadings.afterDOMLoaded = foldableScript

  return FoldableHeadings
}) satisfies QuartzComponentConstructor
