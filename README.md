# Flashcard Creator for Obsidian

A time-efficient desktop application for creating Anki-style flashcards that are compatible with the [Space Repetition](https://github.com/st3v3nmw/obsidian-spaced-repetition) plugin in Obsidian.

## 🎯 Purpose

This application streamlines the process of creating flashcards for use with Obsidian's Space Repetition plugin. Instead of manually formatting each flashcard in markdown, you can quickly create multiple cards using this GUI application and export them as a properly formatted markdown file.

## ✨ Features

- **Intuitive GUI**: Clean, dark-themed interface built with CustomTkinter
- **Flexible Card Order**: Choose between "Question First" or "Answer First" formats
- **Real-time Preview**: See how your cards will look as you type
- **Batch Creation**: Add multiple cards quickly without switching between files
- **Obsidian Compatible**: Exports in the exact format required by the Space Repetition plugin
- **Cross-platform**: Works on Windows, macOS, and Linux

## 🚀 Installation

### Option 1: Download Pre-built Executable (Windows)

1. Download the latest release from the [Releases](https://github.com/yourusername/flashcard-creator/releases) page
2. Extract the ZIP file
3. Run `templater.exe`

### Option 2: Build from Source

#### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

#### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/flashcard-creator.git
   cd flashcard-creator
   ```

2. Install dependencies:
   ```bash
   pip install customtkinter pyinstaller
   ```

3. Run the application:
   ```bash
   python templater.py
   ```

#### Building Executable
To create a standalone executable:
```bash
pyinstaller --onefile --windowed templater.py
```

The executable will be created in the `dist/` folder.

## 📖 Usage

### Creating Flashcards

1. **Launch the Application**: Run `templater.exe` or `python templater.py`

2. **Set Card Order**: Choose whether questions or answers should appear first on the cards

3. **Add Cards**:
   - Enter the question/definition in the "Question/Definition" field
   - Enter the answer in the "Answer" field
   - Click "➕ Add Card" to add it to your collection
   - Repeat for all your flashcards

4. **Preview**: The preview box shows how your cards will look in the final format

5. **Save**: Click "💾 Save and Exit" to export your cards as a markdown file

### Importing to Obsidian

1. **Save the Markdown File**: Choose a location in your Obsidian vault
2. **Add Tags**: Add the appropriate tags for the Space Repetition plugin (e.g., `#flashcards`)
3. **Enable in Space Repetition**: The plugin will automatically detect and import the cards

### Card Format

The application creates cards in this format:
```
Question
?
Answer
```

Or with "Answer First" selected:
```
Answer
?
Question
```

## 🎨 Interface Overview

- **Card Order Menu**: Select whether questions or answers appear first
- **Question/Definition Field**: Enter the front of the card
- **Answer Field**: Enter the back of the card
- **Add Card Button**: Add the current card to your collection
- **Preview Box**: Real-time preview of all cards
- **Save Button**: Export all cards as a markdown file
- **Close Button**: Exit the application

## 🔧 Technical Details

- **Framework**: CustomTkinter (modern Tkinter-based GUI)
- **Language**: Python 3.7+
- **Dependencies**: 
  - `customtkinter` - Modern GUI framework
  - `tkinter` - Standard Python GUI library (included with Python)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) for the modern GUI framework
- [Obsidian Space Repetition Plugin](https://github.com/st3v3nmw/obsidian-spaced-repetition) for the flashcard format specification
- The Obsidian community for inspiration and feedback

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/yourusername/flashcard-creator/issues) page
2. Create a new issue with detailed information about your problem
3. Include your operating system and Python version if applicable

---

**Happy studying! 📚✨** 