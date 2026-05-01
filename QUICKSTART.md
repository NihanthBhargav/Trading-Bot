# QUICK START GUIDE - Trading Bot

## ⚡ 5-Minute Setup

### 1️⃣ Get Binance Testnet API Credentials (2 min)
```
1. Go to: https://testnet.binancefuture.com
2. Login/Register
3. Account → API Management → Create API
4. Copy API Key and Secret
```

### 2️⃣ Configure Project (1 min)
```bash
# Edit the .env file and replace:
BINANCE_API_KEY=paste_your_key
BINANCE_API_SECRET=paste_your_secret
```

### 3️⃣ Verify Setup (1 min)
```bash
# Run from c:\Projects\Trading Bot\trading_bot
cd "c:\Projects\Trading Bot\trading_bot"
venv\Scripts\activate
python verify.py
```

### 4️⃣ Test the Bot (1 min)
```bash
# Test API connection and place sample orders
python test.py
```

---

## 🎯 Core Commands

### Place Market Order
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

### Place Limit Order
```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 45000
```

### View Help
```bash
python cli.py --help
```

---

## 📋 What's Included

✅ **Bot Package** (`bot/`)
- `client.py`: Binance API client with HMAC-SHA256 auth
- `orders.py`: Place market and limit orders
- `validators.py`: Input validation
- `logging_config.py`: Console and file logging

✅ **CLI Interface** (`cli.py`)
- User-friendly command-line tool
- Order summaries and confirmations
- Detailed error messages

✅ **Testing** (`test.py`)
- Connection verification
- Sample order placement
- Diagnostic output

✅ **Documentation**
- `README.md`: Full documentation
- `SUBMISSION_GUIDE.md`: Step-by-step submission guide
- This file: Quick reference

---

## 📁 File Structure

```
trading_bot/
├── bot/                     # Core trading bot package
├── cli.py                   # Main CLI entry point
├── test.py                  # Test script
├── verify.py                # Verification script
├── requirements.txt         # Python dependencies
├── .env                     # Your API credentials (don't commit!)
├── .env.example             # Credentials template
├── .gitignore               # Git ignore rules
├── README.md                # Full documentation
├── SUBMISSION_GUIDE.md      # How to submit
├── setup.bat                # Setup helper
└── trading_bot.log         # Generated logs
```

---

## ✅ Checklist

- [ ] Binance Testnet account created
- [ ] API credentials obtained
- [ ] `.env` file configured
- [ ] `python verify.py` passes all checks
- [ ] `python test.py` runs successfully
- [ ] At least 1 MARKET order placed
- [ ] At least 1 LIMIT order placed
- [ ] `trading_bot.log` contains order entries
- [ ] Code committed to Git
- [ ] Pushed to GitHub (public)
- [ ] Submitted via Google Form

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| "API credentials not found" | Update `.env` with your credentials |
| "Invalid signature" | Check API key/secret are copied correctly |
| "Symbol not found" | Use symbols available on testnet (BTCUSDT, ETHUSDT, etc.) |
| "Network error" | Check internet connection and firewall |
| Orders not filling | Normal on testnet - prices may not match |

---

## 🚀 Submission

1. Push to GitHub (public repo)
2. Go to: https://docs.google.com/forms/d/1326_9BfCgv1DdlO05vQM0olvtA5RhpAkQhLe58FJ6QU
3. Fill form with:
   - Your name and email
   - GitHub repo URL
   - Contents of `trading_bot.log`
4. Submit ✓

---

## 📞 Getting Help

- **Check logs**: `type trading_bot.log`
- **Run test**: `python test.py`
- **Read README**: Full documentation in `README.md`
- **Stuck?** Reply with "BLOCKED" + screenshot

---

**Deadline: May 1, 2026, 11:50 PM IST**

Good luck! 🎉
