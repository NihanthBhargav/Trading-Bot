"""Order management functions for the trading bot"""
from typing import Dict, Any, Optional

from .client import BinanceFuturesClient
from .validators import (
    validate_market_order_params,
    validate_limit_order_params,
    ValidationError
)
from .logging_config import logger


class OrderManager:
    """Manage trading orders"""
    
    def __init__(self, client: BinanceFuturesClient):
        """
        Initialize order manager
        
        Args:
            client: BinanceFuturesClient instance
        """
        self.client = client
    
    def _extract_order_info(self, order_response: Dict[str, Any]) -> Dict[str, Any]:
        """
        Extract key information from order response
        
        Args:
            order_response: Response from API
        
        Returns:
            Dict with orderId, status, executedQty, avgPrice
        """
        return {
            "orderId": order_response.get("orderId"),
            "status": order_response.get("status"),
            "executedQty": float(order_response.get("executedQty", 0)),
            "avgPrice": float(order_response.get("avgPrice", 0)),
            "cumQuote": float(order_response.get("cumQuote", 0)),
            "side": order_response.get("side"),
            "symbol": order_response.get("symbol"),
            "type": order_response.get("type"),
            "origQty": float(order_response.get("origQty", 0)),
            "price": float(order_response.get("price", 0)),
            "timeInForce": order_response.get("timeInForce"),
            "updateTime": order_response.get("updateTime"),
        }
    
    def place_market_order(
        self,
        symbol: str,
        side: str,
        quantity: float
    ) -> Dict[str, Any]:
        """
        Place a market order
        
        Args:
            symbol: Trading symbol (e.g., BTCUSDT)
            side: BUY or SELL
            quantity: Order quantity
        
        Returns:
            Dict with orderId, status, executedQty, avgPrice
        
        Raises:
            ValidationError: On invalid inputs
            Exception: On API errors
        """
        try:
            # Validate inputs
            symbol, side, quantity = validate_market_order_params(
                symbol, side, quantity
            )
            
            logger.info(f"Placing MARKET {side} order: {symbol} qty={quantity}")
            
            # Place order
            response = self.client.place_order(
                symbol=symbol,
                side=side,
                order_type="MARKET",
                quantity=quantity
            )
            
            # Extract and return key info
            order_info = self._extract_order_info(response)
            logger.info(f"Market order placed successfully: {order_info}")
            
            return order_info
        
        except ValidationError as e:
            logger.error(f"Validation error in market order: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Failed to place market order: {str(e)}")
            raise
    
    def place_limit_order(
        self,
        symbol: str,
        side: str,
        quantity: float,
        price: float
    ) -> Dict[str, Any]:
        """
        Place a limit order
        
        Args:
            symbol: Trading symbol (e.g., BTCUSDT)
            side: BUY or SELL
            quantity: Order quantity
            price: Order price
        
        Returns:
            Dict with orderId, status, executedQty, avgPrice
        
        Raises:
            ValidationError: On invalid inputs
            Exception: On API errors
        """
        try:
            # Validate inputs
            symbol, side, quantity, price = validate_limit_order_params(
                symbol, side, quantity, price
            )
            
            logger.info(f"Placing LIMIT {side} order: {symbol} qty={quantity} price={price}")
            
            # Place order
            response = self.client.place_order(
                symbol=symbol,
                side=side,
                order_type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )
            
            # Extract and return key info
            order_info = self._extract_order_info(response)
            logger.info(f"Limit order placed successfully: {order_info}")
            
            return order_info
        
        except ValidationError as e:
            logger.error(f"Validation error in limit order: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Failed to place limit order: {str(e)}")
            raise
