# Label Generator for Google Slides

A Google Apps Script web application that generates labels, postcards, address cards, and other printable layouts in Google Slides using data from a CSV file.

The application uses the first slide of a Google Slides presentation as a template and automatically creates populated slides by replacing placeholders with values from uploaded CSV records.

---

# Features

* Upload CSV files directly from the web interface
* Generate labels and printable layouts in Google Slides
* Use custom placeholders and CSV column mappings
* Support multiple records per slide
* Built-in presets for common layouts

  * Postcard
  * Address Label
* Automatically remove previously generated slides before regeneration
* Generate content directly inside an existing Google Slides presentation
* Return a direct link to the updated presentation

---

# Web App URL

### Current Deployment

https://script.google.com/a/macros/onebyone.io/s/AKfycbzyvK15XRWi-9nN058qgUHFuw5q_tylMqkNsDve62HHknDkAAP-IP8CHqZYdoVR-7nwnw/exec

After deploying the Apps Script project as a Web App, a unique deployment URL will be generated:

```text
https://script.google.com/macros/s/DEPLOYMENT_ID/exec
```

You can find the deployment URL under:

```text
Deploy → Manage Deployments
```

---

# How It Works

1. Enter a Google Slides presentation URL.
2. Upload a CSV file.
3. Configure the number of records per slide.
4. Map placeholders to CSV columns.
5. Optionally select a preset.
6. Generate labels.

The application will:

* Open the specified Google Slides presentation
* Use the first slide as the template
* Remove any previously generated slides
* Parse the uploaded CSV data
* Duplicate the template slide as needed
* Replace placeholders using the configured mappings
* Save the updated presentation
* Return a link to the finished deck

---

# Template Requirements

The first slide in the presentation is always treated as the template slide.

You may use any placeholders that follow your desired naming convention.

For example, if **Records Per Slide** is set to `2`, then:

```text
{NAME_1}
{EMAIL_1}
```

will use the first CSV row on that slide, while:

```text
{NAME_2}
{EMAIL_2}
```

will use the second CSV row.

---

# CSV Format

The CSV file must contain a header row.

Example:

```csv
COMPANY,CONTACT,ADDRESS,EMAIL
Acme Inc,John Doe,123 Main St,john@example.com
Globex Corp,Jane Smith,456 Oak Ave,jane@example.com
```

Headers become available as selectable columns when creating mappings.

Example mapping:

| Placeholder | CSV Column |
| ----------- | ---------- |
| {COMPANY_1} | COMPANY    |
| {CONTACT_1} | CONTACT    |
| {ADDRESS_1} | ADDRESS    |
| {EMAIL_1}   | EMAIL      |

Any placeholder can be mapped to any CSV column.

---

# Presets

The application includes preset configurations for common layouts.

### Postcard

Automatically configures:

```text
Records Per Slide: 2
```

Mappings:

```text
{NAME_1} → CONTACT
{NAME_2} → CONTACT
```

### Address

Automatically configures:

```text
Records Per Slide: 1
```

Mappings:

```text
{COMPANY} → COMPANY
{CONTACT} → CONTACT
{ADDRESS} → ADDRESS
```

Presets can be used as-is or modified after selection.

---

# Project Structure

```text
.
├── Code.gs
├── index.html
└── README.md
```

| File       | Description                   |
| ---------- | ----------------------------- |
| Code.gs    | Server-side Apps Script logic |
| index.html | User interface                |
| README.md  | Project documentation         |

---

# Server-Side Functions

## doGet()

Serves the web application.

```javascript
function doGet()
```

---

## generateLabels()

Main slide generation workflow.

```javascript
function generateLabels(
  slideUrl,
  csvText,
  mappings,
  recordsPerSlide
)
```

Responsibilities:

* Validate user input
* Extract the presentation ID
* Parse CSV data
* Open the Google Slides presentation
* Remove previously generated slides
* Duplicate the template slide
* Replace placeholders with mapped values
* Generate slides according to the configured record count
* Return the presentation URL

---

# Deployment

## 1. Create an Apps Script Project

Create a new Google Apps Script project and add:

```text
Code.gs
index.html
```

---

## 2. Save the Project

Example:

```text
Label Generator
```

---

## 3. Deploy as a Web App

1. Click **Deploy → New Deployment**
2. Select **Web App**
3. Configure:

| Setting        | Value                                       |
| -------------- | ------------------------------------------- |
| Execute As     | User accessing the web app                  |
| Who Has Access | Anyone within OneByOne                      |

4. Click **Deploy**
5. Authorize the application
6. Copy the generated deployment URL

---

# Usage

1. Create a Google Slides presentation.
2. Design the label layout on the first slide.
3. Add placeholders to the template.
4. Copy the Google Slides URL.
5. Open the deployed web application.
6. Paste the Google Slides URL.
7. Upload a CSV file.
8. Set the number of records per slide.
9. Configure placeholder mappings.
10. Optionally select a preset.
11. Click **Generate Labels**.
12. Open the generated presentation.

---

# Example Workflow

### Template Slide

```text
{COMPANY_1}
{CONTACT_1}

{COMPANY_2}
{CONTACT_2}
```

### CSV

```csv
COMPANY,CONTACT
Acme Inc,John Doe
Globex Corp,Jane Smith
TechWorks,Michael Tan
BlueSky,Sarah Lee
```

### Generated Slide 1

```text
Acme Inc
John Doe

Globex Corp
Jane Smith
```

### Generated Slide 2

```text
TechWorks
Michael Tan

BlueSky
Sarah Lee
```

---

# Error Handling

The application validates and handles:

* Missing Google Slides URLs
* Invalid Google Slides URLs
* Missing CSV uploads
* Empty CSV files
* Missing placeholder mappings
* Missing template slides
* CSV parsing errors
* Google Slides access or permission issues
* Unexpected Apps Script exceptions

Errors are displayed directly within the web application interface.

---

# Technologies Used

* Google Apps Script
* Google Slides API (`SlidesApp`)
* HTML5
* JavaScript
* Tailwind CSS

---

# Notes

* The first slide is always treated as the template slide.
* All generated slides are removed before new slides are created.
* Placeholder names are fully customizable.
* Any CSV column can be mapped to any placeholder.
* Placeholder numbering determines which record is used.
* Presets provide quick configuration for common layouts.
* The executing Google account must have edit access to the target presentation.
* Generated content is written directly into the existing Google Slides presentation.

---

# Roadmap

| Feature                    | Status     |
| -------------------------- | ---------- |
| Dynamic Field Mapping      | ✅ Complete |
| Presets                    | ✅ Complete |
| Flexible Records Per Slide | ✅ Complete |
| Placeholder Auto-Detection | 🚧 Planned |
| Excel (.xlsx) Support      | 🚧 Planned |
| Save Mapping Templates     | 💡 Future  |
| Drag-and-Drop Upload       | 💡 Future  |
| Slide Preview              | 💡 Future  |
| Enhanced UI/UX             | 💡 Future  |
