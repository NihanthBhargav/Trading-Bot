"""Input validators for trading bot"""
from typing import Tuple


class ValidationError(ValueError):
    """Custom validation error"""
    pass


def validate_symbol(symbol: str) -> str:
    """Validate trading symbol"""
    if not symbol or not isinstance(symbol, str):
        raise ValidationError("Symbol must be a non-empty string")
    
    symbol = symbol.upper()
    
    if len(symbol) < 6:
        raise ValidationError(f"Invalid symbol format: {symbol}")
    
    return symbol


def validate_side(side: str) -> str:
    """Validate order side (BUY or SELL)"""
    if not side or not isinstance(side, str):
        raise ValidationError("Side must be a non-empty string")
    
    side = side.upper()
    
    if side not in ["BUY", "SELL"]:
        raise ValidationError(f"Side must be BUY or SELL, got: {side}")
    
    return side


def validate_order_type(order_type: str) -> str:
    """Validate order type (MARKET or LIMIT)"""
    if not order_type or not isinstance(order_type, str):
        raise ValidationError("Order type must be a non-empty string")
    
    order_type = order_type.upper()
    
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValidationError(f"Order type must be MARKET or LIMIT, got: {order_type}")
    
    return order_type


def validate_quantity(quantity: float) -> float:
    """Validate order quantity"""
    try:
        qty = float(quantity)
    except (ValueError, TypeError):
        raise ValidationError(f"Quantity must be a valid number, got: {quantity}")
    
    if qty <= 0:
        raise ValidationError(f"Quantity must be positive, got: {qty}")
    
    return qty


def validate_price(price: float) -> float:
    """Validate order price"""
    try:
        p = float(price)
    except (ValueError, TypeError):
        raise ValidationError(f"Price must be a valid number, got: {price}")
    
    if p <= 0:
        raise ValidationError(f"Price must be positive, got: {p}")
    
    return p


def validate_limit_order_params(symbol: str, side: str, quantity: float, price: float) -> Tuple[str, str, float, float]:
    """Validate all parameters for a limit order"""
    symbol = validate_symbol(symbol)
    side = validate_side(side)
    quantity = validate_quantity(quantity)
    price = validate_price(price)
    
    return symbol, side, quantity, price


def validate_market_order_params(symbol: str, side: str, quantity: float) -> Tuple[str, str, float]:
    """Validate all parameters for a market order"""
    symbol = validate_symbol(symbol)
    side = validate_side(side)
    quantity = validate_quantity(quantity)
    
    return symbol, side, quantity
