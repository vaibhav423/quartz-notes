# DOM Manipulation Cheatsheet

## 1. Selecting Elements
| Method | Usage | Returns |
| :--- | :--- | :--- |
| `getElementById()` | `document.getElementById('id')` | Single Element |
| `querySelector()` | `document.querySelector('.class')` | First Match |
| `querySelectorAll()` | `document.querySelectorAll('li')` | NodeList (All) |



---

## 2. Content & Attributes
| Property | Usage | Description |
| :--- | :--- | :--- |
| `.textContent` | `el.textContent = 'Hi'` | Plain text inside tag |
| `.value` | `input.value` | Content of input/form |
| `.innerHTML` | `el.innerHTML = '<b>Hi</b>'` | HTML content inside tag |
| `.disabled` | `btn.disabled = true` | Disables buttons/inputs |
| `.type` | `input.type = 'password'` | Changes attribute type |

---

## 3. Class & Style Management
| Tool | Usage | Description |
| :--- | :--- | :--- |
| `.classList.add()` | `el.classList.add('active')` | Adds class |
| `.classList.remove()` | `el.classList.remove('active')` | Removes class |
| `.classList.toggle()` | `el.classList.toggle('done')` | Flips class ON/OFF |
| `.style.property` | `el.style.color = 'red'` | Changes inline CSS |

---

## 4. Event Listening
| Event | Trigger |
| :--- | :--- |
| `'click'` | User clicks element |
| `'input'` | Value changes (live) |
| `'dblclick'` | User double-clicks |



---

## 5. Creating & Removing Elements
| Method | Usage | Description |
| :--- | :--- | :--- |
| `createElement()` | `document.createElement('li')` | Creates new tag |
| `appendChild()` | `parent.appendChild(child)` | Adds to end of parent |
| `remove()` | `el.remove()` | Deletes element |
| `cloneNode(true)` | `el.cloneNode(true)` | Duplicates element |

---

## 6. Common Logic
* **`e.target`**: The specific element that triggered an event.
* **`tagName`**: Returns element type in caps (e.g., `'LI'`, `'BUTTON'`).
* **`trim()`**: Removes empty spaces from strings.
* **`Math.random()`**: Generates a random number between 0 and 1.
