# 🥗 NutriLens - Meal Nutrition Analyzer

## 📝 Overview

NutriLens is an intelligent nutrition analysis application that leverages Google's Gemini API to provide instant, detailed nutritional insights from your meal images. Simply upload a picture of your food, and get a comprehensive breakdown of calories, food items, and nutritional information.

## ✨ Features

- 📸 Image-based Nutrition Analysis
- 🔢 Calorie Counting
- 📋 Detailed Food Item Breakdown
- 💡 Nutritional Insights
- 🌈 Modern, User-Friendly Interface

## 🛠 Technology Stack

- Python
- Streamlit
- Google Generative AI (Gemini)
- PIL (Python Imaging Library)

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Google Cloud Account
- Gemini API Key

### Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/nutrilens.git
cd nutrilens
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables
Create a `.env` file in the project root and add:
```
GOOGLE_API_KEY=your_google_api_key_here
```

### Running the App

```bash
streamlit run app.py
```

## 🔧 Configuration

- Modify `input_prompt` in the code to customize nutritional analysis
- Adjust CSS in `local_css()` function to change UI styling

## 📦 Requirements File

Create a `requirements.txt` with:
```
streamlit
google-generativeai
python-dotenv
Pillow
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🔒 Security

- Never commit your `.env` file or API keys to version control
- Use environment variables for sensitive information

## 📊 How It Works

1. Upload a meal image
2. (Optional) Add context about your dietary goals
3. Click "Analyze Meal Nutrition"
4. Receive instant nutritional breakdown

## 📈 Future Roadmap

- [ ] Multiple language support
- [ ] Dietary goal tracking
- [ ] Export nutrition reports
- [ ] Recipe suggestions based on nutrition

## 🏷️ Versioning

Current Version: 1.0.0

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 🌐 Deployed Application

### 🔗 Live 
- **Render**: https://nutrilens-b8iq.onrender.com

## 📞 Contact

Your Name - [vivekyad5223@gmail.com](mailto:vivekyad5223@gmail.com)

Project Link: [https://github.com/taskmaster-1/nutrilens](https://github.com/taskmaster-1/nutrilens)

## 🙏 Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Google Generative AI](https://cloud.google.com/ai)
- [Python](https://www.python.org/)

---

**Disclaimer**: NutriLens provides estimated nutritional information. Always consult a professional nutritionist for precise dietary advice.
