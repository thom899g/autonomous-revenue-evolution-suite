"""
The Autonomous Revenue Evolution Suite (ARES) is an AI-powered monetization strategy 
evolution system designed to analyze market dynamics, customer insights, and business 
performance to drive sustainable growth. It consists of modular components that work 
together to continuously optimize revenue streams.
"""

from .market_analyzer import MarketAnalyzer
from .customer_insights import CustomerInsightsAgent
from .business_monitor import BusinessPerformanceMonitor
from .strategy_evolver import StrategyEvolver
from .revenue_optimizer import RevenueOptimizer

__all__ = [
    'MarketAnalyzer',
    'CustomerInsightsAgent', 
    'BusinessPerformanceMonitor',
    'StrategyEvolver',
    'RevenueOptimizer'
]