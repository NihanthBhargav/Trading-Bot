# SUBMISSION GUIDE - Trading Bot Project

## Complete Checklist

Use this checklist to complete and submit your Trading Bot project by **May 1, 2026, 11:50 PM IST**.

---

## ✅ STEP 1: Get Binance Testnet API Credentials (5 minutes)

1. **Open Binance Futures Testnet**: https://testnet.binancefuture.com
2. **Create/Login to Account**:
   - Click "Register" if you don't have an account
   - Complete email verification
3. **Generate API Key**:
   - Click your account icon (top-right)
   - Select "API Management"
   - Click "Create API"
   - Label it "Trading Bot"
   - Complete the verification process
4. **Copy Your Credentials**:
   - Copy the **API Key**
   - Copy the **API Secret** (visible only once - copy it now!)
   - Store them safely

---

## ✅ STEP 2: Configure Your Project (2 minutes)

1. **Open `.env` file** in the project directory:
   ```
   BINANCE_API_KEY=paste_your_api_key_here
   BINANCE_API_SECRET=paste_your_api_secret_here
   ```

2. **Save the file** (Ctrl+S)

3. **IMPORTANT**: Never share or commit this file to GitHub!

---

## ✅ STEP 3: Test Your Bot (10 minutes)

### Option A: Using Test Script (Recommended)

1. **Open terminal** in the project directory
2. **Activate virtual environment**:
   ```bash
   venv\Scripts\activate
   ```
3. **Run test script**:
   ```bash
   python test.py
   ```
4. **Follow the prompts**:
   - Test will verify your API connection
   - You'll be asked if you want to test placing orders
   - Choose "yes" to place test orders

### Option B: Using CLI Commands Directly

1. **Activate virtual environment**:
   ```bash
   venv\Scripts\activate
   ```

2. **Place a MARKET order**:
   ```bash
   python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
   ```

3. **Place a LIMIT order**:
   ```bash
   python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 45000
   ```

### Expected Output:
- ✓ Order placed successfully message
- ✓ Order details displayed (Order ID, Status, Qty, Price)
- ✓ Entries added to `trading_bot.log`

---

## ✅ STEP 4: Verify Logs (2 minutes)

1. **Open `trading_bot.log`** file
2. **Verify it contains**:
   - Market order entry with response
   - Limit order entry with response
   - No sensitive credentials (if any seen, delete them!)

Example log entries you should see:
```
2026-05-01 10:30:45 - trading_bot - INFO - Placing MARKET BUY order: BTCUSDT qty=0.01
2026-05-01 10:30:46 - trading_bot - INFO - Market order placed successfully: {...}
2026-05-01 10:30:47 - trading_bot - INFO - Placing LIMIT SELL order: BTCUSDT qty=0.01 price=45000
2026-05-01 10:30:48 - trading_bot - INFO - Limit order placed successfully: {...}
```

---

## ✅ STEP 5: Push to GitHub (5 minutes)

### If you don't have a GitHub repo yet:

1. **Go to GitHub**: https://github.com/new
2. **Create New Repository**:
   - Name: `trading-bot` (or similar)
   - Description: "Binance Futures Testnet Trading Bot"
   - **Make it PUBLIC** (important for submission!)
   - Click "Create repository"

### Push your code:

1. **Copy the commands** GitHub shows (after creating repo)
2. **Open terminal** in your project directory
3. **Run the commands**:
   ```bash
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/trading-bot.git
   git push -u origin main
   ```

### Verify on GitHub:
- Visit your repository URL
- Confirm all files are there
- Confirm `.env` is NOT visible (it should be in `.gitignore`)

---

## ✅ STEP 6: Prepare Submission Files (2 minutes)

You need to submit:

1. **GitHub Repository URL**
   - Example: `https://github.com/username/trading-bot`

2. **Trading Bot Log File** (`trading_bot.log`)
   - Copy the file contents
   - Or attach the file if the form allows

3. **Screenshot (Optional but Recommended)**
   - Take a screenshot showing:
     - CLI order placement output
     - Log file with orders
   - This helps verify everything worked

---

## ✅ STEP 7: Submit via Google Form (2 minutes)

**Submission Form**: https://docs.google.com/forms/d/1326_9BfCgv1DdlO05vQM0olvtA5RhpAkQhLe58FJ6QU/preview

1. **Open the form**
2. **Fill in the fields**:
   - Name: Your full name
   - Email: Your email address
   - GitHub Repository URL: `https://github.com/username/trading-bot`
   - Log File: Paste contents of `trading_bot.log` or attach file
   - Any additional notes if needed

3. **Review all information**
4. **Click Submit**
5. **Take a screenshot** of the confirmation page

---

## 🎯 Project Summary

Your bot includes:

✓ **Authentication**: HMAC-SHA256 signed requests  
✓ **Market Orders**: Buy/Sell at market price  
✓ **Limit Orders**: Buy/Sell at specific price  
✓ **Input Validation**: All parameters validated  
✓ **Comprehensive Logging**: Console + file logging  
✓ **Clean CLI**: User-friendly command-line interface  
✓ **Error Handling**: Detailed error messages  
✓ **README**: Full documentation with examples  

---

## 📝 Files in Your Project

```
trading_bot/
├── bot/
│   ├── __init__.py           # Package init
│   ├── client.py             # API client with HMAC-SHA256
│   ├── orders.py             # Order management
│   ├── validators.py         # Input validation
│   └── logging_config.py     # Logging setup
├── cli.py                    # CLI interface
├── test.py                   # Test script
├── requirements.txt          # Dependencies
├── .env.example              # Template (DO NOT EDIT)
├── .env                      # Your credentials (DO NOT COMMIT!)
├── .gitignore                # Git ignore rules
├── README.md                 # Full documentation
├── setup.bat                 # Setup helper script
├── trading_bot.log          # Log file (auto-generated)
└── [others]
```

---

## ⚠️ Common Issues & Solutions

### "API credentials not found"
- **Solution**: Create `.env` file with your API credentials

### "Invalid signature" error
- **Solution**: 
  - Check that API credentials in `.env` are correct
  - Make sure no extra spaces around = sign
  - Verify system time is synchronized

### "Invalid symbol"
- **Solution**: Use symbols available on Testnet (BTCUSDT, ETHUSDT, etc.)

### "Orders appear pending"
- **Solution**: This is normal! They're waiting to be filled on testnet

### ".env file showing in GitHub"
- **Solution**: Add `.env` to `.gitignore` before first commit (already done for you)

---

## ✅ Final Checklist Before Submission

- [ ] API credentials obtained from Binance Testnet
- [ ] `.env` file configured with credentials
- [ ] Virtual environment activated
- [ ] Dependencies installed (pip list shows httpx, python-dotenv)
- [ ] Test script ran successfully
- [ ] At least 1 MARKET order placed
- [ ] At least 1 LIMIT order placed
- [ ] `trading_bot.log` contains order entries
- [ ] All code committed to Git
- [ ] Repository pushed to GitHub (PUBLIC)
- [ ] `.env` NOT visible in GitHub (in .gitignore)
- [ ] Submission form filled and submitted
- [ ] Confirmation screenshot taken

---

## 🚀 Next Steps After Submission

1. **Wait for confirmation** - Check email for submission confirmation
2. **Check for shortlist update** - Saturday morning update expected
3. **If shortlisted**:
   - Expect interview or assignment notification
   - Demonstrate understanding of the code
   - Be ready to explain HMAC-SHA256 authentication
   - Discuss API error handling and validation

---

## 📞 Need Help?

If you face blockers:
1. **Check logs**: `type trading_bot.log`
2. **Run test**: `python test.py` (provides detailed diagnostics)
3. **Review README.md**: Comprehensive documentation
4. **Reply with "BLOCKED"**: Include error screenshot if stuck

---

## 🎉 Good Luck!

You've built a fully functional trading bot with:
- Industry-standard authentication
- Robust error handling
- Clean architecture
- Comprehensive documentation

This demonstrates solid Python skills and understanding of:
- REST APIs
- Cryptographic signatures
- CLI development
- Logging and debugging
- Project structure

**Deadline: May 1, 2026, 11:50 PM IST**

**Time to complete: ~30-45 minutes**

Start now! ⏱️
