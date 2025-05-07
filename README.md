# 📊 Stock Sentinel

**Stock Sentinel** is a lightweight stock market analysis tool built with Python and Streamlit. It provides users with real-time stock data, technical indicators, and the latest news headlines related to a given stock.

---

## 🚀 Features

* **Real-Time Stock Data** using Yahoo Finance
* **Technical Analysis Tools:**

  * RSI (Relative Strength Index)
  * MA20 (20-day Moving Average)
* **Interactive Charts** with Plotly
* **News Scraper**: Fetches latest headlines from Google News

---

## 🛠️ Tech Stack

| Layer         | Tools Used               |
| ------------- | ------------------------ |
| Frontend      | Streamlit                |
| Backend       | Python, yfinance, ta-lib |
| Visualization | Plotly                   |
| Web Scraping  | BeautifulSoup, requests  |
| Data Handling | Pandas                   |

---

## 📁 Project Structure

```
stock_sentinel/
├── app.py                # Main application file
├── README.md             # Project overview
├── requirements.txt      # Python dependencies
```

---

## ⚙️ Installation & Running

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/stock-sentinel.git
   cd stock-sentinel
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:

   ```bash
   pip install streamlit yfinance plotly ta pandas requests beautifulsoup4
   ```

3. Run the app:

   ```bash
   streamlit run app.py
   ```

-

## 🧠 Future Improvements

* Add candlestick chart
* Integrate sentiment analysis on news headlines
* Add predictive models (e.g. Prophet, LSTM)
* Deploy online via Streamlit Cloud / Heroku

---

## 📄 License

MIT License. Feel free to fork, modify, and contribute.

