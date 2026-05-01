"""Command-line interface for the trading bot"""
import argparse
import sys
import os
from dotenv import load_dotenv

from bot.client import BinanceFuturesClient
from bot.orders import OrderManager
from bot.logging_config import logger


def load_api_credentials():
    """Load API credentials from environment variables or .env file"""
    # Load from .env file if it exists
    load_dotenv()
    
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")
    
    if not api_key or not api_secret:
        logger.error("API credentials not found in environment variables")
        print("\nERROR: API credentials not found!")
        print("Please set BINANCE_API_KEY and BINANCE_API_SECRET environment variables")
        print("Or create a .env file with these values")
        sys.exit(1)
    
    return api_key, api_secret


def format_order_info(order_info):
    """Format order info for display"""
    return f"""
╔════════════════════════════════════════════════════════════════╗
║                    ORDER PLACED SUCCESSFULLY                   ║
╠════════════════════════════════════════════════════════════════╣
║ Order ID:           {order_info.get('orderId', 'N/A'):<44} ║
║ Status:             {order_info.get('status', 'N/A'):<44} ║
║ Symbol:             {order_info.get('symbol', 'N/A'):<44} ║
║ Side:               {order_info.get('side', 'N/A'):<44} ║
║ Type:               {order_info.get('type', 'N/A'):<44} ║
║ Original Qty:       {order_info.get('origQty', 0):<44} ║
║ Executed Qty:       {order_info.get('executedQty', 0):<44} ║
║ Average Price:      {order_info.get('avgPrice', 0):<44} ║
║ Cumulative Quote:   {order_info.get('cumQuote', 0):<44} ║
║ Price:              {order_info.get('price', 0):<44} ║
║ Time in Force:      {order_info.get('timeInForce', 'N/A'):<44} ║
║ Update Time:        {order_info.get('updateTime', 'N/A'):<44} ║
╚════════════════════════════════════════════════════════════════╝
"""


def format_request_summary(args):
    """Format request summary for display"""
    price_str = f"{args.price}" if args.price else "MARKET PRICE"
    return f"""
╔════════════════════════════════════════════════════════════════╗
║                      ORDER REQUEST SUMMARY                     ║
╠════════════════════════════════════════════════════════════════╣
║ Symbol:             {args.symbol:<44} ║
║ Side:               {args.side:<44} ║
║ Order Type:         {args.type:<44} ║
║ Quantity:           {args.quantity:<44} ║
║ Price:              {price_str:<44} ║
╚════════════════════════════════════════════════════════════════╝
"""


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Place a MARKET BUY order for 0.01 BTC
  python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
  
  # Place a LIMIT SELL order for 0.01 BTC at 45000 USDT
  python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 45000
        """
    )
    
    parser.add_argument(
        "--symbol",
        type=str,
        required=True,
        help="Trading symbol (e.g., BTCUSDT, ETHUSDT)"
    )
    
    parser.add_argument(
        "--side",
        type=str,
        required=True,
        choices=["BUY", "SELL"],
        help="Order side: BUY or SELL"
    )
    
    parser.add_argument(
        "--type",
        type=str,
        required=True,
        choices=["MARKET", "LIMIT"],
        help="Order type: MARKET or LIMIT"
    )
    
    parser.add_argument(
        "--quantity",
        type=float,
        required=True,
        help="Order quantity (must be positive)"
    )
    
    parser.add_argument(
        "--price",
        type=float,
        default=None,
        help="Order price (required for LIMIT orders)"
    )
    
    args = parser.parse_args()
    
    # Validate price for limit orders
    if args.type == "LIMIT" and not args.price:
        logger.error("Price is required for LIMIT orders")
        print("\nERROR: Price is required for LIMIT orders!")
        sys.exit(1)
    
    # Print request summary
    print(format_request_summary(args))
    
    try:
        # Load API credentials
        api_key, api_secret = load_api_credentials()
        
        # Create client and order manager
        client = BinanceFuturesClient(api_key, api_secret)
        order_manager = OrderManager(client)
        
        try:
            # Place order based on type
            if args.type == "MARKET":
                order_info = order_manager.place_market_order(
                    symbol=args.symbol,
                    side=args.side,
                    quantity=args.quantity
                )
            else:  # LIMIT
                order_info = order_manager.place_limit_order(
                    symbol=args.symbol,
                    side=args.side,
                    quantity=args.quantity,
                    price=args.price
                )
            
            # Print success message with order details
            print(format_order_info(order_info))
            print("✓ Order placed successfully!")
            
        finally:
            client.close()
    
    except Exception as e:
        logger.error(f"Failed to place order: {str(e)}")
        print(f"\n✗ ERROR: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
