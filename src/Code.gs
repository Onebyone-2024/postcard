function doGet() {
  return HtmlService.createHtmlOutputFromFile('index')
    .setTitle('Label Generator');
}

function extractSlideId(slideUrl) {
  const match = slideUrl.match(/\/presentation\/d\/([a-zA-Z0-9_-]+)/);

  if (!match) {
    throw new Error('Invalid Google Slides URL');
  }

  return match[1];
}

function generateLabels(slideUrl, csvText) {
  try {
    const slideId = extractSlideId(slideUrl);

    const rows = Utilities.parseCsv(csvText);
    const names = rows.slice(1).map(row => row[0] || '');

    const deck = SlidesApp.openById(slideId);
    const slides = deck.getSlides();
    const templateSlide = slides[0];

    for (let i = slides.length - 1; i > 0; i--) {
      slides[i].remove();
    }

    for (let i = 0; i < names.length; i += 2) {
      const name1 = names[i] || '';
      const name2 = names[i + 1] || '';

      const newSlide = templateSlide.duplicate();
      newSlide.move(deck.getSlides().length - 1);

      newSlide.replaceAllText('{{NAME_1}}', name1);
      newSlide.replaceAllText('{{NAME_2}}', name2);
    }

    return {
      success: true,
      slideUrl:
        'https://docs.google.com/presentation/d/' +
        slideId +
        '/edit'
    };

  } catch (err) {
    return {
      success: false,
      error: err.toString()
    };
  }
}