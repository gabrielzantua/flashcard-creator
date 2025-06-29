# Flashcard Creator for Obsidian

A time-efficient desktop application for creating Anki-style flashcards that are compatible with the [Space Repetition](https://github.com/st3v3nmw/obsidian-spaced-repetition) plugin in Obsidian.

## 🎯 Purpose

This application streamlines the process of creating flashcards for use with Obsidian's Space Repetition plugin. Instead of manually formatting each flashcard in markdown, you can quickly create multiple cards using this GUI application and export them as a properly formatted markdown file.

## ✨ Features

- **Intuitive GUI**: Clean, dark-themed interface built with CustomTkinter
- **Flexible Card Order**: Choose between "Question First" or "Answer First" formats
- **Text & Image Support**: Add text, images, or both as questions and/or answers
- **Image Preview**: See a thumbnail preview of selected images before adding the card
- **Batch Creation**: Add multiple cards quickly without switching between files
- **Obsidian Compatible**: Exports in the exact format required by the Space Repetition plugin, with images referenced in markdown and copied to an `images/` folder
- **Modern, Non-Resizable UI**: Window is centered, non-resizable, and visually consistent

## 🚀 Installation

### Option 1: Download Pre-built Executable (Windows)

1. Download the latest release from the [Releases](https://github.com/gabrielzantua/flashcard-creator/releases) page
2. Extract the ZIP file
3. Run `templater.exe`

### Option 2: Build from Source

#### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

#### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/gabrielzantua/flashcard-creator.git
   cd flashcard-creator
   ```

2. Install dependencies:
   ```bash
   pip install customtkinter pyinstaller pillow
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
   - Enter the question/definition in the "Question/Definition" field (text and/or image)
   - Enter the answer in the "Answer" field (text and/or image)
   - Use the 🖼️ button to add an image to either field (a file dialog will open)
   - A thumbnail preview will appear next to the field when an image is selected
   - Click **Add Card** to add it to your collection
   - Repeat for all your flashcards
4. **Preview**: The preview box shows how your cards will look in the final format (including markdown image links)
5. **Save**: Click **Save and Exit** to export your cards as a markdown file. All images used will be copied to an `images/` folder next to your markdown file.

### Importing to Obsidian

1. **Save the Markdown File**: Choose a location in your Obsidian vault
2. **Add Tags**: Add the appropriate tags for the Space Repetition plugin (e.g., `#flashcards`)
3. **Enable in Space Repetition**: The plugin will automatically detect and import the cards

### Card Format

The application creates cards in this format:
```
Question text
![](images/image1.png)
?
Answer text
![](images/image2.png)
```
Or with "Answer First" selected:
```
Answer text
![](images/image2.png)
?
Question text
![](images/image1.png)
```
You can mix text and images in either field.

## 🎨 Interface Overview

- **Card Order Menu**: Select whether questions or answers appear first
- **Question/Definition Field**: Enter the front of the card (text and/or image)
- **Answer Field**: Enter the back of the card (text and/or image)
- **🖼️ Image Button**: Add an image to the respective field (with tooltip and preview)
- **Add Card Button**: Add the current card to your collection
- **Preview Box**: Real-time preview of all cards
- **Save Button**: Export all cards as a markdown file (with images)
- **Close Button**: Exit the application

## 🔧 Technical Details

- **Framework**: CustomTkinter (modern Tkinter-based GUI)
- **Language**: Python 3.7+
- **Dependencies**: 
  - `customtkinter` - Modern GUI framework
  - `tkinter` - Standard Python GUI library (included with Python)
  - `pillow` - For image preview support

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) for the modern GUI framework
- [Obsidian Space Repetition Plugin](https://github.com/st3v3nmw/obsidian-spaced-repetition) for the flashcard format specification
- The Obsidian community for inspiration and feedback

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/gabrielzantua/flashcard-creator/issues) page
2. Create a new issue with detailed information about your problem
3. Include your operating system and Python version if applicable

---

**Happy studying! 📚✨** 
