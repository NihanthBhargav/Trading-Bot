"""Binance Futures REST API Client with HMAC-SHA256 authentication"""
import hmac
import hashlib
import time
import json
import os
from typing import Dict, Any, Optional
import httpx

from .logging_config import logger


class BinanceFuturesClient:
    """Client for Binance Futures Testnet API"""
    
    BASE_URL = "https://testnet.binancefuture.com"
    
    def __init__(self, api_key: str, api_secret: str):
        """
        Initialize the Binance Futures client
        
        Args:
            api_key: Binance API Key
            api_secret: Binance API Secret
        """
        self.api_key = api_key
        self.api_secret = api_secret
        
        # Check if mock mode is enabled
        self.mock_mode = os.getenv("MOCK_MODE", "false").lower() == "true"
        
        if self.mock_mode:
            self.client = None
            logger.info("Binance Futures Client initialized in MOCK MODE")
        else:
            if not api_key or not api_secret:
                raise ValueError("API key and secret must not be empty")
            
            self.client = httpx.Client(base_url=self.BASE_URL, timeout=30.0)
            logger.info("Binance Futures Client initialized")
    
    def _generate_signature(self, query_string: str) -> str:
        """Generate HMAC-SHA256 signature"""
        return hmac.new(
            self.api_secret.encode(),
            query_string.encode(),
            hashlib.sha256
        ).hexdigest()
    
    def _get_mock_response(self, endpoint: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Generate mock response for testing without real API"""
        import random
        
        if "/fapi/v1/order" in endpoint:
            order_id = random.randint(100000000, 999999999)
            price = float(params.get("price", 50000))
            quantity = float(params.get("quantity", 0.01))
            
            return {
                "orderId": order_id,
                "symbol": params.get("symbol", "BTCUSDT"),
                "status": "FILLED" if params.get("type") == "MARKET" else "NEW",
                "side": params.get("side", "BUY"),
                "type": params.get("type", "MARKET"),
                "origQty": quantity,
                "executedQty": quantity if params.get("type") == "MARKET" else 0,
                "avgPrice": str(price),
                "cumQuote": str(quantity * price) if params.get("type") == "MARKET" else "0",
                "price": str(price),
                "timeInForce": params.get("timeInForce", "GTC"),
                "updateTime": int(time.time() * 1000),
                "msg": "Order placed successfully (MOCK)"
            }
        elif "/fapi/v2/account" in endpoint:
            return {
                "totalWalletBalance": "10000.00",
                "totalUnrealizedProfit": "0.00",
                "msg": "Account info (MOCK)"
            }
        else:
            return {"msg": "Mock response"}
    
    
    def _make_request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        signed: bool = True
    ) -> Dict[str, Any]:
        """
        Make HTTP request to Binance API
        
        Args:
            method: HTTP method (GET, POST, DELETE, etc.)
            endpoint: API endpoint path
            params: Query/body parameters
            signed: Whether request needs HMAC signature
        
        Returns:
            Response JSON as dict
        
        Raises:
            Exception: On API errors
        """
        if params is None:
            params = {}
        
        # If mock mode is enabled, return mock response
        if self.mock_mode:
            logger.info(f"[MOCK MODE] Making {method} request to {endpoint}")
            logger.debug(f"[MOCK MODE] Parameters: {params}")
            mock_response = self._get_mock_response(endpoint, params)
            logger.debug(f"[MOCK MODE] Response: {json.dumps(mock_response, indent=2)}")
            return mock_response
        
        # Add timestamp for signed requests
        if params is None:
            params = {}
        
        if signed:
            params['timestamp'] = int(time.time() * 1000)
        
        # Build query string
        query_string = "&".join(
            [f"{key}={value}" for key, value in sorted(params.items())]
        )
        
        # Add signature for signed requests
        headers = {"X-MBX-APIKEY": self.api_key}
        if signed:
            signature = self._generate_signature(query_string)
            query_string += f"&signature={signature}"
        
        # Make request
        url = f"{endpoint}?{query_string}"
        logger.debug(f"Making {method} request to {endpoint}")
        logger.debug(f"Parameters: {params}")
        
        try:
            if method.upper() == "GET":
                response = self.client.get(url, headers=headers)
            elif method.upper() == "POST":
                response = self.client.post(url, headers=headers)
            elif method.upper() == "DELETE":
                response = self.client.delete(url, headers=headers)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
            
            logger.debug(f"Response status code: {response.status_code}")
            
            # Handle errors
            if response.status_code >= 400:
                error_msg = f"API Error: {response.status_code}"
                try:
                    error_data = response.json()
                    if 'msg' in error_data:
                        error_msg += f" - {error_data['msg']}"
                    if 'code' in error_data:
                        error_msg += f" (Code: {error_data['code']})"
                except:
                    error_msg += f" - {response.text}"
                
                logger.error(error_msg)
                raise Exception(error_msg)
            
            # Parse response
            result = response.json()
            logger.debug(f"Response: {json.dumps(result, indent=2)}")
            
            return result
        
        except httpx.RequestError as e:
            logger.error(f"HTTP Request failed: {str(e)}")
            raise
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse JSON response: {str(e)}")
            raise
    
    def place_order(
        self,
        symbol: str,
        side: str,
        order_type: str,
        quantity: float,
        price: Optional[float] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Place an order on Binance Futures
        
        Args:
            symbol: Trading symbol (e.g., BTCUSDT)
            side: BUY or SELL
            order_type: MARKET or LIMIT
            quantity: Order quantity
            price: Order price (required for LIMIT orders)
            **kwargs: Additional parameters
        
        Returns:
            Order response dict with orderId, status, executedQty, avgPrice
        
        Raises:
            Exception: On API errors or validation errors
        """
        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
        }
        
        if order_type == "LIMIT":
            if price is None:
                raise ValueError("Price is required for LIMIT orders")
            params["price"] = price
            params["timeInForce"] = kwargs.get("timeInForce", "GTC")
        
        # Add any additional parameters
        for key, value in kwargs.items():
            if key not in params:
                params[key] = value
        
        logger.info(f"Placing {order_type} {side} order: {symbol} qty={quantity}")
        
        return self._make_request("POST", "/fapi/v1/order", params, signed=True)
    
    def get_account_info(self) -> Dict[str, Any]:
        """Get account information"""
        logger.info("Fetching account information")
        return self._make_request("GET", "/fapi/v2/account", {}, signed=True)
    
    def get_order(self, symbol: str, order_id: str) -> Dict[str, Any]:
        """Get order details"""
        params = {"symbol": symbol, "orderId": order_id}
        logger.info(f"Fetching order {order_id} for {symbol}")
        return self._make_request("GET", "/fapi/v1/order", params, signed=True)
    
    def cancel_order(self, symbol: str, order_id: str) -> Dict[str, Any]:
        """Cancel an order"""
        params = {"symbol": symbol, "orderId": order_id}
        logger.info(f"Cancelling order {order_id} for {symbol}")
        return self._make_request("DELETE", "/fapi/v1/order", params, signed=True)
    
    def close(self):
        """Close the HTTP client"""
        if self.client:
            self.client.close()
        logger.info("Binance Futures Client closed")
