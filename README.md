# Fdx-pro-ai
# FDX Pro AI

**Convert screenplay treatments to Final Draft (FDX) format with AI**

FDX Pro AI is a web application that uses artificial intelligence to transform screenplay treatments into professionally formatted Final Draft (FDX) files. This tool bridges the gap between your creative narrative and industry-standard screenplay format.

## 🌟 Features

- **AI-Powered Conversion**: Analyzes your treatment and intelligently structures it into proper screenplay format
- **FDX Output**: Generate industry-standard Final Draft files compatible with professional screenwriting software
- **Multiple Input Methods**: Paste text directly or upload various file formats (.txt, .docx, .pdf, .rtf)
- **Simple Interface**: Easy-to-use web interface with clear instructions
- **Fast Processing**: Quick conversions with immediate download links

## 🚀 Live Demo

Check out the live demo at [https://fdx-pro-ai.onrender.com/](https://fdx-pro-ai.onrender.com/)

## 🔧 Technology Stack

- **Backend**: Node.js with Express
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **AI**: OpenAI GPT-4 API for intelligent text processing
- **XML**: XML generation using xmlbuilder2 for FDX file creation
- **Deployment**: Render.com

## 📋 How It Works

1. **Input**: Enter your screenplay treatment or upload a treatment file
2. **Processing**: Our AI analyzes your treatment and formats it as a proper screenplay with:
   - Scene Headings (INT/EXT)
   - Action descriptions
   - Character names
   - Dialogue
   - Parentheticals
   - Transitions
3. **Output**: Download your treatment as a .fdx file ready to open in Final Draft

## 🛠️ Installation and Setup

### Prerequisites

- Node.js (v18 or higher)
- NPM
- OpenAI API key

### Local Development

1. Clone the repository:
   ```
   git clone https://github.com/your-username/fdx-pro-ai.git
   cd fdx-pro-ai
   ```

2. Install dependencies:
   ```
   npm install
   ```

3. Create a `.env` file in the root directory with:
   ```
   PORT=3000
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. Start the development server:
   ```
   npm run dev
   ```

5. Visit `http://localhost:3000` in your browser

### Deployment to Render

1. Create a new Web Service on Render
2. Connect to this GitHub repository
3. Set the build command to `npm install`
4. Set the start command to `node app.js`
5. Add the environment variable `OPENAI_API_KEY`
6. Deploy!

## 📄 License

MIT License - See LICENSE file for details.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/your-username/fdx-pro-ai/issues).

## 📝 Notes for Screenwriters

- The AI provides a good first draft but you should always review and refine the output
- Standard screenplay format guidelines are followed, but creative decisions are ultimately yours
- For best results, provide clear and well-structured treatments with distinct scenes and character interactions

---

*Not affiliated with Final Draft, Inc.*