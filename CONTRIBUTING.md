# 🤝 Contributing to Data Quality & Anomaly Detection Project

Thank you for your interest in contributing to our research project! This document provides guidelines for contributing to the Data Quality & Anomaly Detection in Mobility Systems project.

## 🎯 Project Overview

This project focuses on:
- Data quality assessment in mobility systems
- Advanced anomaly detection techniques
- Machine learning implementation
- Hyperparameter optimization
- Practical applications in transportation

## 📋 How to Contribute

### 1. Fork the Repository
1. Go to the main repository page
2. Click the "Fork" button in the top right
3. Clone your forked repository to your local machine

### 2. Create a Feature Branch
```bash
git checkout -b feature/your-feature-name
```

### 3. Make Your Changes
- Follow the existing code style
- Add appropriate comments and documentation
- Include tests for new functionality
- Update relevant documentation

### 4. Commit Your Changes
```bash
git add .
git commit -m "Add: brief description of your changes"
```

### 5. Push and Create Pull Request
```bash
git push origin feature/your-feature-name
```
Then create a Pull Request from your fork to the main repository.

## 🛠️ Development Setup

### Prerequisites
- Python 3.8+
- pip package manager
- Git

### Local Development Environment
```bash
# Clone your fork
git clone https://github.com/yourusername/data-quality-anomaly-detection.git
cd data-quality-anomaly-detection

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -r requirements-dev.txt  # if available
```

## 📝 Code Style Guidelines

### Python Code
- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings for all functions and classes
- Keep functions focused and concise

### Example:
```python
def detect_anomalies(data: pd.DataFrame, method: str = 'isolation_forest') -> np.ndarray:
    """
    Detect anomalies in the given dataset using specified method.
    
    Args:
        data: Input DataFrame containing numerical data
        method: Anomaly detection method ('isolation_forest', 'dbscan', 'pca')
    
    Returns:
        Array of boolean values indicating anomalies
    """
    # Implementation here
    pass
```

### Jupyter Notebooks
- Keep cells focused and well-documented
- Include markdown explanations
- Use consistent formatting
- Add clear section headers

## 🧪 Testing

### Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=.

# Run specific test file
pytest tests/test_anomaly_detection.py
```

### Writing Tests
- Test all new functionality
- Include edge cases
- Use descriptive test names
- Follow AAA pattern (Arrange, Act, Assert)

## 📚 Documentation

### Code Documentation
- Update README.md for new features
- Add inline comments for complex logic
- Document API changes
- Update requirements.txt if adding new packages

### Research Documentation
- Document methodology changes
- Update analysis procedures
- Include references to relevant papers
- Maintain reproducibility

## 🔍 Review Process

### Pull Request Guidelines
1. **Clear Description**: Explain what your PR does and why
2. **Related Issues**: Link to any related issues
3. **Testing**: Ensure all tests pass
4. **Documentation**: Update relevant documentation
5. **Code Review**: Address reviewer comments

### Review Checklist
- [ ] Code follows style guidelines
- [ ] Tests are included and passing
- [ ] Documentation is updated
- [ ] No sensitive data is included
- [ ] Changes are well-documented

## 🚫 What Not to Include

### Excluded from Repository
- Large data files (>100MB)
- Personal presentation materials
- Sensitive information
- Generated files (can be recreated)
- Virtual environment files

### Specifically Excluded
- PowerPoint slides (`slide*.png`)
- Presentation guides (`POWERPOINT_*.md`)
- Prezi materials (`PREZI_*.md`)
- Virtual environment (`venv/`)

## 🎓 Research Contributions

### Academic Contributions
- Novel anomaly detection methods
- Performance improvements
- New evaluation metrics
- Case studies and applications
- Literature reviews

### Implementation Contributions
- Code optimizations
- Bug fixes
- New visualization methods
- Performance improvements
- Documentation enhancements

## 📞 Getting Help

### Questions and Discussions
- Create an issue for questions
- Use GitHub Discussions if enabled
- Contact the maintainers directly

### Communication Channels
- GitHub Issues
- GitHub Discussions
- Email: [your.email@univ-eiffel.fr]

## 🏆 Recognition

Contributors will be:
- Listed in the README.md file
- Acknowledged in research publications
- Mentioned in project presentations
- Given appropriate credit for their work

## 📄 License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

---

## 🙏 Thank You!

Your contributions help advance research in data quality and anomaly detection for mobility systems. Every contribution, no matter how small, makes a difference!

---

*This contributing guide is part of the Data Quality & Anomaly Detection in Mobility Systems project at COSYS/GRETTIA, Université Gustave Eiffel.*
