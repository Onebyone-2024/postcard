function doGet() {
  return HtmlService
    .createHtmlOutputFromFile('index')
    .setTitle('Label Generator');
}

function generateLabels(
  slideUrl,
  csvText,
  mappings,
  recordsPerSlide
) {
  try {

    // ==========================
    // Validate input
    // ==========================

    if (!slideUrl) {
      throw new Error('Google Slides URL is required.');
    }

    if (!csvText) {
      throw new Error('CSV file is empty.');
    }

    if (!mappings || mappings.length === 0) {
      throw new Error('No mappings provided.');
    }

    // ==========================
    // Extract Presentation ID
    // ==========================

    const match =
      slideUrl.match(
        /\/d\/([a-zA-Z0-9-_]+)/
      );

    if (!match) {
      throw new Error(
        'Invalid Google Slides URL.'
      );
    }

    const presentationId =
      match[1];

    const presentation =
      SlidesApp.openById(
        presentationId
      );

    // ==========================
    // Get Template Slide
    // First slide is template
    // ==========================

    const slides =
      presentation.getSlides();

    if (slides.length === 0) {
      throw new Error(
        'Presentation has no slides.'
      );
    }

    const templateSlide =
      slides[0];

    // ==========================
    // Remove old generated slides
    // Keep template only
    // ==========================

    const existingSlides =
      presentation.getSlides();

    for (
      let i = existingSlides.length - 1;
      i >= 1;
      i--
    ) {
      existingSlides[i].remove();
    }

    // ==========================
    // Parse CSV
    // ==========================

    const parsed =
      Utilities.parseCsv(csvText);

    if (parsed.length < 2) {
      throw new Error(
        'CSV must contain a header row and at least one data row.'
      );
    }

    const headers =
      parsed.shift();

    const rows =
      parsed.map(row => {

        const record = {};

        headers.forEach(
          (header, index) => {

            record[
              String(header).trim()
            ] =
              row[index] || '';

          }
        );

        return record;

      });

    // ==========================
    // Generate Slides
    // ==========================

    for (
      let startRow = 0;
      startRow < rows.length;
      startRow += recordsPerSlide
    ) {

      const slide =
        templateSlide.duplicate();

      mappings.forEach(mapping => {

        const placeholder =
          mapping.placeholder;

        const column =
          mapping.column;

        // Example:
        // {NAME_1}
        // {EMAIL_2}
        // {COMPANY_3}

        const indexMatch =
          placeholder.match(
            /_(\d+)\}/i
          );

        const recordOffset =
          indexMatch
            ? Number(
              indexMatch[1]
            ) - 1
            : 0;

        const row =
          rows[
          startRow +
          recordOffset
          ];

        const value =
          row
            ? (
              row[column] || ''
            )
            : '';

        slide.replaceAllText(
          placeholder,
          String(value)
        );

      });

    }

    presentation.saveAndClose();

    return {
      success: true,
      slideUrl:
        presentation.getUrl()
    };

  } catch (error) {

    Logger.log(error);

    return {
      success: false,
      error:
        error.message ||
        'Unexpected error.'
    };
  }
}