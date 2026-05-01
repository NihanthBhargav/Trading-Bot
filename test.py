"""
Test script for the trading bot
This script helps you test the bot with your Binance Futures Testnet credentials
"""

import os
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from bot.client import BinanceFuturesClient
from bot.orders import OrderManager
from bot.logging_config import logger
from dotenv import load_dotenv


def test_connection():
    """Test API connection"""
    print("\n" + "="*70)
    print("TESTING BINANCE FUTURES TESTNET CONNECTION")
    print("="*70)
    
    # Load environment variables
    load_dotenv()
    
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")
    
    if not api_key or not api_secret:
        print("\n✗ ERROR: API credentials not found!")
        print("Please create a .env file with the following content:")
        print("\nBINANCE_API_KEY=your_api_key_here")
        print("BINANCE_API_SECRET=your_api_secret_here")
        print("\nTo get credentials:")
        print("1. Go to https://testnet.binancefuture.com")
        print("2. Create an account or login")
        print("3. Go to Account > API Management")
        print("4. Create a new API key")
        return False
    
    print("\n✓ API credentials loaded from .env file")
    
    try:
        # Create client
        client = BinanceFuturesClient(api_key, api_secret)
        print("✓ Client initialized")
        
        # Test connection by getting account info
        print("\n📡 Testing connection to Binance Futures Testnet...")
        account_info = client.get_account_info()
        
        print("✓ Connection successful!")
        print(f"\nAccount Information:")
        print(f"  - Wallet Balance: ${account_info.get('totalWalletBalance', 'N/A')}")
        print(f"  - Total Unrealized PnL: {account_info.get('totalUnrealizedProfit', 'N/A')}")
        
        client.close()
        return True
    
    except Exception as e:
        print(f"\n✗ Connection failed: {str(e)}")
        return False


def test_market_order(symbol="BTCUSDT", quantity=0.001):
    """Test placing a market order"""
    print("\n" + "="*70)
    print("TESTING MARKET ORDER")
    print("="*70)
    
    load_dotenv()
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")
    
    if not api_key or not api_secret:
        print("✗ API credentials not configured")
        return False
    
    try:
        client = BinanceFuturesClient(api_key, api_secret)
        order_manager = OrderManager(client)
        
        print(f"\n📊 Placing MARKET BUY order:")
        print(f"   Symbol: {symbol}")
        print(f"   Quantity: {quantity}")
        
        order_info = order_manager.place_market_order(
            symbol=symbol,
            side="BUY",
            quantity=quantity
        )
        
        print(f"\n✓ Market order placed successfully!")
        print(f"   Order ID: {order_info.get('orderId')}")
        print(f"   Status: {order_info.get('status')}")
        print(f"   Executed Qty: {order_info.get('executedQty')}")
        print(f"   Avg Price: {order_info.get('avgPrice')}")
        
        client.close()
        return True
    
    except Exception as e:
        print(f"\n✗ Market order failed: {str(e)}")
        return False


def test_limit_order(symbol="BTCUSDT", quantity=0.001, price=30000):
    """Test placing a limit order"""
    print("\n" + "="*70)
    print("TESTING LIMIT ORDER")
    print("="*70)
    
    load_dotenv()
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")
    
    if not api_key or not api_secret:
        print("✗ API credentials not configured")
        return False
    
    try:
        client = BinanceFuturesClient(api_key, api_secret)
        order_manager = OrderManager(client)
        
        print(f"\n📊 Placing LIMIT SELL order:")
        print(f"   Symbol: {symbol}")
        print(f"   Quantity: {quantity}")
        print(f"   Price: {price}")
        
        order_info = order_manager.place_limit_order(
            symbol=symbol,
            side="SELL",
            quantity=quantity,
            price=price
        )
        
        print(f"\n✓ Limit order placed successfully!")
        print(f"   Order ID: {order_info.get('orderId')}")
        print(f"   Status: {order_info.get('status')}")
        print(f"   Original Qty: {order_info.get('origQty')}")
        print(f"   Price: {order_info.get('price')}")
        
        client.close()
        return True
    
    except Exception as e:
        print(f"\n✗ Limit order failed: {str(e)}")
        return False


def main():
    """Run tests"""
    print("\n")
    print("╔════════════════════════════════════════════════════════════════╗")
    print("║     BINANCE FUTURES TRADING BOT - TEST SUITE                   ║")
    print("╚════════════════════════════════════════════════════════════════╝")
    
    # Test connection
    if not test_connection():
        print("\n⚠ Setup .env file with API credentials and try again")
        sys.exit(1)
    
    # Ask user if they want to test orders
    response = input("\n\nDo you want to test placing orders? (yes/no): ").strip().lower()
    
    if response == "yes" or response == "y":
        # Test market order with small quantity
        test_market_order(symbol="BTCUSDT", quantity=0.001)
        
        # Test limit order with small quantity
        test_limit_order(symbol="BTCUSDT", quantity=0.001, price=30000)
        
        print("\n" + "="*70)
        print("✓ ALL TESTS COMPLETED!")
        print("="*70)
        print("\nCheck trading_bot.log for detailed logs")
    
    print("\n")


if __name__ == "__main__":
    main()
