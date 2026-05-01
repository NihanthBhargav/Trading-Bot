@echo off
REM Setup script for Trading Bot

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║   BINANCE FUTURES TRADING BOT - SETUP GUIDE                    ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

REM Create .env from template
if not exist ".env" (
    echo [*] Creating .env file from template...
    copy .env.example .env
    echo [✓] .env file created. Update it with your API credentials.
) else (
    echo [✓] .env file already exists
)

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║   NEXT STEPS:                                                   ║
echo ╠════════════════════════════════════════════════════════════════╣
echo ║                                                                ║
echo ║  1. GET API CREDENTIALS:                                       ║
echo ║     - Go to https://testnet.binancefuture.com                  ║
echo ║     - Login or create a new account                            ║
echo ║     - Navigate to Account > API Management                     ║
echo ║     - Create a new API key                                     ║
echo ║     - Copy the API Key and API Secret                          ║
echo ║                                                                ║
echo ║  2. CONFIGURE .env FILE:                                       ║
echo ║     - Open .env file in an editor                              ║
echo ║     - Replace 'your_api_key_here' with your API Key            ║
echo ║     - Replace 'your_api_secret_here' with your API Secret      ║
echo ║     - Save the file (don't commit to git!)                     ║
echo ║                                                                ║
echo ║  3. TEST THE BOT:                                              ║
echo ║     - Run: python test.py                                      ║
echo ║     - This will test your connection and optionally place      ║
echo ║       test orders on the testnet                               ║
echo ║                                                                ║
echo ║  4. USE THE BOT:                                               ║
echo ║     - Market order:                                            ║
echo ║       python cli.py --symbol BTCUSDT --side BUY ^              ║
echo ║         --type MARKET --quantity 0.01                          ║
echo ║                                                                ║
echo ║     - Limit order:                                             ║
echo ║       python cli.py --symbol BTCUSDT --side SELL ^             ║
echo ║         --type LIMIT --quantity 0.01 --price 45000             ║
echo ║                                                                ║
echo ║  5. CHECK LOGS:                                                ║
echo ║     - All activity logged to trading_bot.log                   ║
echo ║                                                                ║
echo ║  6. SUBMIT PROJECT:                                            ║
echo ║     - Push to GitHub (public repo)                             ║
echo ║     - Include trading_bot.log in submission                    ║
echo ║     - Submit via: Google Form (link in task)                   ║
echo ║                                                                ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.
pause
