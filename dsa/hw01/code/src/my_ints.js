const fs = require('fs');
const path = require('path');

// Define the paths
const inputFilePath = path.join(__dirname, '..', 'sample_inputs', 'sample_01.txt');
const outputDirPath = path.join(__dirname, '..', 'sample_results');
const outputFilePath = path.join(outputDirPath, 'results_01.txt');

// Max and min values
const maxInt = 1023;
const minInt = -1013;

// Create a set to hold unique numbers
const numbers = new Set();

// Read the input file
fs.readFile(inputFilePath, 'utf8', (err, data) => {
    if (err) {
        console.error(`Error reading file: ${err}`);
        return;
    }

    const lines = data.split('\n');

    lines.forEach(line => {
        const strippedLine = line.trim();  // Remove whitespace
        if (strippedLine) {  // Check if the line is not empty
            const number = parseFloat(strippedLine);  // Convert to float
            if (!isNaN(number) && number >= minInt && number <= maxInt) {
                numbers.add(number);  // Add to the set if valid
            }
        }
    });

    // Convert the set to an array and sort it
    const sortedNumbers = Array.from(numbers).sort((a, b) => a - b);

    // Ensure the output directory exists
    fs.mkdir(outputDirPath, { recursive: true }, (err) => {
        if (err) {
            console.error(`Error creating directory: ${err}`);
            return;
        }

        // Write the results to the output file
        fs.writeFile(outputFilePath, sortedNumbers.join('\n'), (err) => {
            if (err) {
                console.error(`Error writing file: ${err}`);
                return;
            }
            console.log('Results saved successfully!');
        });
    });
});
