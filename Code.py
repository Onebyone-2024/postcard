function createLabels() {
  var deck = SlidesApp.openById('1bfXZNts1hzFTAo5Znnc90hO9TX2NL-746kS8GKCdQ0I');
  var slides = deck.getSlides();
  var templateSlide = slides[0];
  
  // Cleanup: Remove all slides except the first one (template)
  for (var i = slides.length - 1; i > 0; i--) {
    slides[i].remove();
  }
  
  var namePairs = [["Matt", "Matt"], ["Liam", "Sam"], ["Graham", "Glen"], ["John", "Thomas"], ["Chris", "Joe"], ["Nicholas", "Belinda"], ["John", "Kirsten"], ["Adrian", "John"], ["Kelvin", "Danny"], ["Brad", "Alex"], ["Gilbert", "Bobby"], ["Evan", "Cheslie"], ["Colin", "Rod"], ["Andrew", "Justin"], ["Stephen", "Gary"], ["Nigel", "Sachintha"], ["Maryanne", "Adam"], ["Zack", "Nicola"], ["Mark", "John"], ["Samir", "Peter"], ["Michael", "Jacqueline"], ["Vesna", "Angela"], ["Kylie", "Louise"], ["Cheryl", "Sebastian"], ["Ian", "Nathan"], ["James", "Scott"], ["Kimberly", "Michael"], ["Timothy", "Paul"], ["Sara", "John"], ["Richard", "Chris"], ["Jordan", "John"], ["Brett", "Carl"], ["Brayden", "Ali"], ["Darren", "Kelvin"], ["Max", "John"], ["Travis", "Kathy"], ["Tim", "Henri"], ["John", "Rowan"], ["Marius", "Paul"], ["Ian", "Ashley"], ["Steven", "Julie"], ["Mark", "Samuel"], ["Jordan", "Chris"], ["Michael", "Travan"], ["Stuart", "Nikki"], ["Brian", "Sandra"], ["Chris", "Kareen"], ["Sarah", "Josh"], ["Harry", "Dino"], ["Lloyd", "Gavin"], ["Gurinder", "Mark"], ["David", "Caitlin"], ["Fiona", "Lesley"], ["Rod", "Matt"], ["Andrew", "Daniel"], ["Jordan", "Shane"], ["Paul", "Miloy"], ["Deon", "Rob"], ["James", "Jeff"], ["Rick", "Nicki"], ["Darren", "Alessandra"], ["Adem", "Aaron"], ["Anasua", "Carlo"], ["Tania", "Nick"], ["David", "Heath"], ["Mathew", "Veronica"], ["Akihiko", "Shinji"], ["Bill", "Nigel"], ["Steve", "Alison"], ["Rohan", "Danny"], ["Robert", "Roman"], ["Matt", "Riyaz"], ["Michael", "Fleur"], ["Adam", "Cameron"], ["Sarah", "Vince"], ["Dan", "Katharina"], ["Jay", "Michael"], ["Anthony", "Jane"], ["Brodie", "Jessica"], ["Heath", "Elizabeth"], ["Peter", "Tim"], ["Michael", "Deborah"], ["Kurt", "Alison"], ["Ben", "Michael"], ["Tracey", "Sene-Li"], ["Stuart", "Gordon"], ["Brian", "Robert"], ["Seiya", "Brett"], ["Miles", "Louise"], ["Matthew", "Adrian"], ["Alison", "Bree"], ["James", "Brad"], ["Carmelo", "Yolanda"], ["Leigh", "Mark"], ["JEMAL", "Dean"], ["Holly", "Mathew"], ["Anthony", "Genevieve"], ["Renee", "Scott"], ["Tabarak", "Alan"], ["Belinda", "Samantha"], ["Trevor", "Ingrid"], ["Fernando", "Donna"], ["Carlos", "Nigel"], ["Patrick", "Manuel"], ["Alan", "Tim"], ["Ekrem", "Mark"], ["Tim", "Giovanni"], ["Neil", "Kate"], ["Simon", "Gerard"], ["Adrian", "Randall"], ["Sam", "Steven"], ["Shayne", "Paul"], ["Tien", "Debbie"], ["Stephen", "Ben"], ["David", "Colin"], ["Dean", "Brenton"], ["Sudhir", "Amit"], ["Justin", "Simon"], ["Joe", "Gavin"], ["Sony", "Tony"], ["Glenn", "Nigel"], ["Emilie", "Mark"], ["Amanda", "Phillip"], ["Kate", "Aaron"], ["Andrew", "Arsalan"], ["Daniel", "Thomai"], ["Caitlyn", "Ruben"], ["Igor", "Trish"], ["Sally", "Lachlan"], ["Luda", "Hayley"], ["Imran", "Bill"], ["Christian", "Volker"], ["Scott", "Eric"]];
  
  // Recursively find shapes with specific text
  function findShapesWithText(shapes, textToFind) {
    var found = [];
    for (var i = 0; i < shapes.length; i++) {
      var shape = shapes[i];
      if (shape.getShapeType() == SlidesApp.ShapeType.GROUP) {
        found = found.concat(findShapesWithText(shape.getGroup().getChildren(), textToFind));
      } else if (shape.getShapeType() == SlidesApp.ShapeType.TEXT_BOX || shape.getShapeType() == SlidesApp.ShapeType.AUTO_SHAPE) {
        var textRange = shape.getText();
        if (textRange && textRange.asString().indexOf(textToFind) !== -1) {
          found.push(shape);
        }
      }
    }
    return found;
  }

  for (var i = 0; i < namePairs.length; i++) {
    var pair = namePairs[i];
    var name1 = pair[0];
    var name2 = pair[1];
    
    var newSlide = templateSlide.duplicate();
    var allShapes = newSlide.getShapes();
    
    // Find all "Robert" placeholders on the slide
    var targets = findShapesWithText(allShapes, "Robert");
    
    if (targets.length >= 2) {
       // Sort targets by position to deterministically assign name1 and name2
       targets.sort(function(a, b) {
           if (Math.abs(a.getLeft() - b.getLeft()) > 50) {
               return a.getLeft() - b.getLeft();
           }
           return a.getTop() - b.getTop();
       });
       
       // Replace first placeholder with name1
       targets[0].getText().replaceAllText("Robert", name1);
       
       // Replace second placeholder with name2
       if (name2) {
           targets[1].getText().replaceAllText("Robert", name2);
       } else {
           targets[1].getText().replaceAllText("Robert", "");
       }
       
    } else if (targets.length == 1) {
       targets[0].getText().replaceAllText("Robert", name1);
       console.log("WARNING: Only 1 placeholder found on slide " + i + ". Name2 (" + name2 + ") skipped.");
    } else {
       console.log("WARNING: No 'Robert' placeholders found on slide " + i);
    }
  }
}
