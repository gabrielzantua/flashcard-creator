# Contributing to Flashcard Creator

Thank you for your interest in contributing to Flashcard Creator! This document provides guidelines and information for contributors.

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- Git
- pip (Python package installer)

### Setting Up Development Environment

1. **Fork the Repository**
   ```bash
   git clone https://github.com/yourusername/flashcard-creator.git
   cd flashcard-creator
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   python templater.py
   ```

## 🛠️ Development Guidelines

### Code Style
- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions focused and single-purpose

### Testing
- Test your changes thoroughly before submitting
- Ensure the application works on different operating systems if possible
- Test the exported markdown format with Obsidian's Space Repetition plugin

### Commit Messages
Use clear, descriptive commit messages:
- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests after the first line

Example:
```
Add dark mode toggle functionality

- Implement theme switching between light and dark modes
- Add system theme detection
- Update UI elements to support both themes

Fixes #123
```

## 📝 Types of Contributions

### Bug Reports
When reporting bugs, please include:
- Operating system and version
- Python version
- Steps to reproduce the issue
- Expected vs actual behavior
- Screenshots if applicable

### Feature Requests
When requesting features, please:
- Describe the feature clearly
- Explain why it would be useful
- Provide examples of how it would work
- Consider the impact on existing functionality

### Code Contributions
1. Create a new branch for your feature/fix
2. Make your changes
3. Test thoroughly
4. Update documentation if needed
5. Submit a pull request

## 🔧 Building and Testing

### Building Executable
```bash
pyinstaller --onefile --windowed templater.py
```

### Running Tests
Currently, manual testing is required. Please test:
- Adding cards with various content
- Different card order settings
- Saving to different locations
- Importing the generated markdown into Obsidian

## 📋 Pull Request Process

1. **Update Documentation**: If you're adding a new feature, update the README.md
2. **Test Your Changes**: Ensure everything works as expected
3. **Submit PR**: Create a pull request with a clear description
4. **Review**: Address any feedback from maintainers

## 🎯 Areas for Contribution

- **UI/UX Improvements**: Better layouts, themes, accessibility
- **Export Formats**: Support for other flashcard formats
- **Import Features**: Import from existing markdown files
- **Performance**: Optimize for large flashcard sets
- **Testing**: Add automated tests
- **Documentation**: Improve guides and examples

## 📞 Getting Help

- Open an issue for bugs or feature requests
- Join discussions in existing issues
- Check the README for common questions

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

Thank you for contributing to Flashcard Creator! 🎉 