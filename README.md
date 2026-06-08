# Label Generator for Google Slides

A simple Google Apps Script web application that generates printable labels in a Google Slides presentation from a CSV file.

The application uses the first slide in a Google Slides deck as a template and automatically creates duplicate slides populated with names from a CSV file.

---

## Table of Contents

* [Features](#features)
* [Web App URL](#web-app-url)
* [How It Works](#how-it-works)
* [Template Requirements](#template-requirements)
* [CSV Format](#csv-format)
* [Project Structure](#project-structure)
* [Server-Side Functions](#server-side-functions)
* [Deployment](#deployment)
* [Usage](#usage)
* [Example Workflow](#example-workflow)
* [Error Handling](#error-handling)
* [Technologies Used](#technologies-used)
* [Notes](#notes)
* [Roadmap](#roadmap)

---

## Features

* Upload a CSV file containing names.
* Generate labels directly in Google Slides.
* Uses the first slide as a template.
* Creates two labels per slide.
* Automatically removes previously generated slides before creating new ones.
* Returns a direct link to the updated presentation.

---

## Web App URL

### Current Deployment

Access the application here:
[Label Generator Web App](https://script.google.com/a/macros/onebyone.io/s/AKfycbzyvK15XRWi-9nN058qgUHFuw5q_tylMqkNsDve62HHknDkAAP-IP8CHqZYdoVR-7nwnw/exec)


After deploying the Apps Script as a Web App, your application will be available at:

```text
https://script.google.com/macros/s/DEPLOYMENT_ID/exec
```

Example:

```text
https://script.google.com/macros/s/AKfycbxxxxxxxxxxxxxxxxxxxxxxxxxxxx/exec
```

You can obtain this URL from:

**Deploy → Manage Deployments → Web App URL**

---

## How It Works

1. Enter a Google Slides presentation URL.
2. Upload a CSV file.
3. Click **Generate Labels**.
4. The application:

   * Opens the specified Google Slides presentation.
   * Uses the first slide as the template.
   * Reads names from the CSV file.
   * Creates duplicate slides as needed.
   * Replaces placeholders with names.
   * Returns a link to the updated presentation.

---

## Template Requirements

The first slide in your presentation must contain the following placeholders:

```text
{{NAME_1}}
{{NAME_2}}
```

Example:

```text
+------------------+
| {{NAME_1}}       |
|                  |
| {{NAME_2}}       |
+------------------+
```

Each generated slide will populate these placeholders with names from the CSV file.

---

## CSV Format

The CSV file must contain a header row.

Example:

```csv
Contact
John Doe
Jane Smith
Michael Tan
Sarah Lee
```

### Mapping

| CSV Row     | Placeholder             |
| ----------- | ----------------------- |
| John Doe    | {{NAME_1}}              |
| Jane Smith  | {{NAME_2}}              |
| Michael Tan | {{NAME_1}} (next slide) |
| Sarah Lee   | {{NAME_2}} (next slide) |

---

## Project Structure

```text
.
├── Code.gs
├── index.html
└── README.md
```

| File       | Description                    |
| ---------- | ------------------------------ |
| Code.gs    | Server-side Apps Script logic  |
| index.html | Web application user interface |
| README.md  | Documentation                  |

---

## Server-Side Functions

### doGet()

Serves the web application.

```javascript
function doGet()
```

### extractSlideId(slideUrl)

Extracts the Google Slides ID from a presentation URL.

```javascript
function extractSlideId(slideUrl)
```

### generateLabels(slideUrl, csvText)

Main label generation workflow.

```javascript
function generateLabels(slideUrl, csvText)
```

Responsibilities:

* Parse CSV data.
* Open the Google Slides deck.
* Remove previously generated slides.
* Duplicate the template slide.
* Replace placeholders with names.
* Return the presentation URL.

---

## Deployment

### 1. Create Apps Script Project

Create a new Apps Script project and add:

* `Code.gs`
* `index.html`

### 2. Save the Project

Give the project a name such as:

```text
Label Generator
```

### 3. Deploy as a Web App

1. Click **Deploy → New Deployment**
2. Select **Web App**
3. Configure:

| Setting        | Value                                           |
| -------------- | ----------------------------------------------- |
| Execute As     | Me                                              |
| Who Has Access | Anyone with the link (or your preferred option) |

4. Click **Deploy**
5. Authorize the application
6. Copy the generated Web App URL

---

## Usage

1. Create a Google Slides presentation.
2. Design the label layout on the first slide.
3. Add placeholders:

   * `{{NAME_1}}`
   * `{{NAME_2}}`
4. Copy the Google Slides URL.
5. Open the deployed Web App URL.
6. Paste the Google Slides URL.
7. Upload a CSV file.
8. Click **Generate Labels**.
9. Open the generated presentation from the success message.

---

## Example Workflow

### Template Slide

```text
{{NAME_1}}

{{NAME_2}}
```

### CSV

```csv
Contact
Alice Johnson
Bob Smith
Charlie Brown
Diana Lee
```

### Generated Output

**Slide 1**

```text
Alice Johnson
Bob Smith
```

**Slide 2**

```text
Charlie Brown
Diana Lee
```

---

## Error Handling

The application handles:

* Invalid Google Slides URLs
* Missing CSV uploads
* Empty presentation URLs
* Presentation access permission errors
* CSV parsing issues
* Unexpected Apps Script exceptions

Errors are displayed directly within the web application.

---

## Technologies Used

* Google Apps Script
* Google Slides Service (`SlidesApp`)
* HTML5
* JavaScript
* Tailwind CSS

---

## Notes

* The first slide is always treated as the template slide.
* All slides except the template are removed before generation.
* Names are processed in pairs.
* If an odd number of names exists, the final label is left blank.
* The Google account running the script must have edit access to the target presentation.
* Generated labels are written directly into the existing Google Slides deck.

## Roadmap

| Feature | Status |
|----------|---------|
| Dynamic Field Mapping | 🚧 Planned |
| Flexible Label Layouts | 🚧 Planned |
| Drag-and-Drop Upload | 🚧 Planned |
| Enhanced UI/UX | 🚧 Planned |
| Excel (.xlsx) Support | 💡 Future |