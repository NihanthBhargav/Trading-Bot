"""
Verification script to check if the project is ready for submission
"""

import os
import sys
from pathlib import Path


def check_file_exists(filepath, description):
    """Check if a file exists"""
    if os.path.exists(filepath):
        print(f"  ✓ {description}")
        return True
    else:
        print(f"  ✗ {description} - MISSING!")
        return False


def check_directory_exists(dirpath, description):
    """Check if a directory exists"""
    if os.path.isdir(dirpath):
        print(f"  ✓ {description}")
        return True
    else:
        print(f"  ✗ {description} - MISSING!")
        return False


def check_file_content(filepath, required_content, description):
    """Check if file contains required content"""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            if required_content.lower() in content.lower():
                print(f"  ✓ {description}")
                return True
            else:
                print(f"  ✗ {description}")
                return False
    except:
        print(f"  ✗ {description} - ERROR reading file")
        return False


def main():
    """Run verification checks"""
    print("\n")
    print("╔════════════════════════════════════════════════════════════════╗")
    print("║         TRADING BOT - PRE-SUBMISSION VERIFICATION             ║")
    print("╚════════════════════════════════════════════════════════════════╝\n")
    
    project_dir = Path(__file__).parent
    checks_passed = 0
    checks_total = 0
    
    # 1. Core files check
    print("1️⃣  CORE FILES CHECK:")
    core_files = [
        ("bot/__init__.py", "Bot package init"),
        ("bot/client.py", "Binance API client"),
        ("bot/orders.py", "Order management"),
        ("bot/validators.py", "Input validators"),
        ("bot/logging_config.py", "Logging configuration"),
        ("cli.py", "CLI entry point"),
        ("requirements.txt", "Dependencies"),
        ("README.md", "Documentation"),
        (".gitignore", "Git ignore rules"),
        ("SUBMISSION_GUIDE.md", "Submission guide"),
    ]
    
    for filepath, description in core_files:
        checks_total += 1
        full_path = project_dir / filepath
        if check_file_exists(full_path, description):
            checks_passed += 1
    
    # 2. Git repository check
    print("\n2️⃣  GIT REPOSITORY CHECK:")
    checks_total += 1
    if check_directory_exists(project_dir / ".git", "Git repository initialized"):
        checks_passed += 1
    
    # 3. Python dependencies check
    print("\n3️⃣  DEPENDENCIES CHECK:")
    dependencies = [
        ("requirements.txt", "httpx", "httpx library requirement"),
        ("requirements.txt", "python-dotenv", "python-dotenv library requirement"),
    ]
    
    for filepath, required, description in dependencies:
        checks_total += 1
        full_path = project_dir / filepath
        if check_file_content(full_path, required, description):
            checks_passed += 1
    
    # 4. Code quality check
    print("\n4️⃣  CODE QUALITY CHECK:")
    checks = [
        ("bot/client.py", "BinanceFuturesClient", "BinanceFuturesClient class"),
        ("bot/client.py", "_generate_signature", "HMAC-SHA256 signature method"),
        ("bot/orders.py", "OrderManager", "OrderManager class"),
        ("bot/orders.py", "place_market_order", "Market order method"),
        ("bot/orders.py", "place_limit_order", "Limit order method"),
        ("bot/validators.py", "validate_symbol", "Symbol validator"),
        ("bot/validators.py", "validate_side", "Side validator"),
        ("bot/logging_config.py", "setup_logging", "Logging setup function"),
        ("cli.py", "main", "CLI main function"),
    ]
    
    for filepath, required, description in checks:
        checks_total += 1
        full_path = project_dir / filepath
        if check_file_content(full_path, required, description):
            checks_passed += 1
    
    # 5. Environment setup check
    print("\n5️⃣  ENVIRONMENT SETUP CHECK:")
    checks_total += 1
    if check_file_exists(project_dir / ".env.example", ".env.example template"):
        checks_passed += 1
    
    checks_total += 1
    if check_file_exists(project_dir / "venv", "Python virtual environment"):
        checks_passed += 1
    else:
        print("  ⚠️  Virtual environment not found - run: python -m venv venv")
    
    # 6. Credentials check
    print("\n6️⃣  CREDENTIALS CHECK:")
    checks_total += 1
    env_file = project_dir / ".env"
    if os.path.exists(env_file):
        with open(env_file, 'r') as f:
            content = f.read()
            if "your_api_key_here" not in content.lower() and "BINANCE_API_KEY=" in content:
                print("  ✓ .env file configured with API credentials")
                checks_passed += 1
            else:
                print("  ⚠️  .env file found but not configured with real credentials")
                print("     - Update .env with your Binance Testnet API Key and Secret")
    else:
        print("  ⚠️  .env file not found")
        print("     - Copy .env.example to .env and add your credentials")
    
    # 7. Summary
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    print(f"\nChecks Passed: {checks_passed}/{checks_total}")
    percentage = (checks_passed / checks_total * 100) if checks_total > 0 else 0
    print(f"Completion: {percentage:.1f}%")
    
    if checks_passed == checks_total:
        print("\n✓ ALL CHECKS PASSED! Ready for submission!")
        print("\nNext steps:")
        print("  1. Configure .env with your Binance Testnet credentials")
        print("  2. Run: python test.py")
        print("  3. Place test orders (market and limit)")
        print("  4. Review trading_bot.log")
        print("  5. Push to GitHub")
        print("  6. Submit via Google Form")
        return 0
    else:
        print("\n⚠️  SOME CHECKS FAILED")
        print("\nPlease fix the issues above before submission")
        return 1


if __name__ == "__main__":
    sys.exit(main())
