const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

// Configuration
const CHANGELOG_PATH = 'changelog.md';

function getTimestamp() {
    const now = new Date();
    const offset = '+02:00'; // Hardcoded for this project's locale
    const date = now.toISOString().split('T')[0];
    const time = now.toTimeString().split(' ')[0].substring(0, 5);
    return `${date} ${time} (${offset})`;
}

function getGitUser() {
    try {
        return execSync('git config user.name').toString().trim();
    } catch (e) {
        return 'Maintainer';
    }
}

async function run() {
    console.log('\n--- Changelog Automator ---\n');

    const author = getGitUser();
    const timestamp = getTimestamp();

    // In a real CLI environment, we'd use a library like 'inquirer' or 'readline'.
    // Since I'm an agent, I'll provide a template and the user can pass arguments or I can prompt via ask_user.
    // However, to make it a standalone tool for the user, I'll use standard readline for their local use.

    const readline = require('readline').createInterface({
        input: process.stdin,
        output: process.stdout
    });

    const question = (query) => new Promise((resolve) => readline.question(query, resolve));

    try {
        console.log(`Date: ${timestamp}`);
        console.log(`Author: ${author}`);
        
        const teams = await question('Affected teams (comma separated): ');
        const files = await question('Modified files (comma separated): ');
        const change = await question('What changed? ');
        const reason = await question('Why was this needed? ');

        const entry = `
## ${timestamp}
- Auteur: ${author}
- Betrokken teams: ${teams || 'Geen'}
- Bestanden: ${files || 'Geen'}
- Wijziging: ${change}
- Reden: ${reason}
`;

        const currentContent = fs.readFileSync(CHANGELOG_PATH, 'utf8');
        const headerEndIndex = currentContent.indexOf('\n\n') + 2;
        
        const newContent = currentContent.slice(0, headerEndIndex) + entry + currentContent.slice(headerEndIndex);
        
        fs.writeFileSync(CHANGELOG_PATH, newContent);
        console.log('\n[SUCCESS] Changelog updated!');

    } catch (err) {
        console.error('\n[ERROR] Failed to update changelog:', err.message);
    } finally {
        readline.close();
    }
}

run();
