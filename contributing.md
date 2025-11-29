# 🤝 Contributing to Resume Screening AI

First off, thank you for considering contributing to Resume Screening AI! It's people like you that make this project better for everyone.

## 🌟 How Can I Contribute?

### 📝 Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples**
- **Describe the behavior you observed and what you expected**
- **Include screenshots if relevant**
- **Include your environment details** (OS, Python version, etc.)

### 💡 Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Use a clear and descriptive title**
- **Provide a detailed description of the suggested enhancement**
- **Explain why this enhancement would be useful**
- **List some examples of how it would be used**

### 🔧 Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** following our coding standards
3. **Test your changes** thoroughly
4. **Update documentation** if needed
5. **Write clear commit messages**
6. **Submit your pull request**

## 📋 Coding Standards

### Python Style Guide

- Follow **PEP 8** style guide
- Use **meaningful variable names**
- Add **docstrings** to functions and classes
- Keep functions **small and focused**
- Add **comments** for complex logic
- Maximum line length: **88 characters** (Black formatter)

### Code Example

```python
def process_resume(resume_text: str) -> dict:
    """
    Process and clean resume text.
    
    Args:
        resume_text: Raw resume text string
        
    Returns:
        Dictionary containing processed resume data
    """
    # Clean the text
    cleaned_text = clean_text(resume_text)
    
    # Extract features
    features = extract_features(cleaned_text)
    
    return {
        'cleaned_text': cleaned_text,
        'features': features
    }
```

## 🧪 Testing

- Write unit tests for new features
- Ensure all tests pass before submitting PR
- Aim for at least 80% code coverage
- Test with different Python versions (3.8, 3.9, 3.10, 3.11)

## 📚 Documentation

- Update README.md if you change functionality
- Add docstrings to new functions
- Update requirements.txt if you add dependencies
- Include examples for new features

## 🎯 Project Priorities

We're especially interested in contributions that:

1. **Improve model accuracy** - Better algorithms or feature engineering
2. **Add new features** - Resume parsing, skill extraction, etc.
3. **Enhance visualizations** - More insightful charts and graphs
4. **Improve performance** - Faster processing, better scaling
5. **Add datasets** - More diverse resume examples
6. **Fix bugs** - Any bug fixes are welcome!

## 🔄 Development Workflow

1. **Clone the repository**
   ```bash
   git clone https://github.com/alam025/resume-screening-ai.git
   cd resume-screening-ai
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a new branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

5. **Make your changes and commit**
   ```bash
   git add .
   git commit -m "Add: Brief description of your changes"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request** on GitHub

## 📝 Commit Message Guidelines

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit first line to 72 characters
- Reference issues and pull requests after the first line

**Examples:**
```
Add: Support for PDF resume parsing
Fix: Memory leak in text preprocessing
Update: Improve model accuracy to 95%
Docs: Add installation instructions
```

## 🎨 Areas Needing Contribution

- [ ] Add support for PDF and DOCX resume parsing
- [ ] Implement deep learning models (BERT, transformers)
- [ ] Create web interface using Streamlit or Flask
- [ ] Add more visualization options
- [ ] Implement skill extraction and matching
- [ ] Add multilingual support
- [ ] Create API endpoints
- [ ] Add database integration
- [ ] Improve test coverage
- [ ] Add CI/CD pipeline

## 🤔 Questions?

Feel free to ask questions by:
- Opening an issue with the `question` label
- Reaching out to the maintainers
- Joining our community discussions

## 📜 Code of Conduct

### Our Pledge

We pledge to make participation in our project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

### Our Standards

**Positive behavior includes:**
- Being respectful and inclusive
- Gracefully accepting constructive criticism
- Focusing on what's best for the community
- Showing empathy towards others

**Unacceptable behavior includes:**
- Trolling, insulting comments, or personal attacks
- Public or private harassment
- Publishing others' private information
- Other conduct inappropriate in a professional setting

## 🙏 Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes for significant contributions
- Special mentions in project updates

Thank you for contributing to Resume Screening AI! 🚀

---

**Happy Coding!** 💻✨