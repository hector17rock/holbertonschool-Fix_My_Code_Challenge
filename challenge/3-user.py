#!/usr/bin/env python3
"""
User class implementation with password validation
"""
import hashlib

class User:
    def __init__(self, name, password):
        """Initialize a new User"""
        self.name = name
        # BUG: Store hashed password but don't hash input during validation
        self.password = hashlib.md5(password.encode()).hexdigest()
    
    def is_valid_password(self, password):
        """Check if provided password is valid"""
        # FIXED: Hash the input password and compare with stored hash
        hashed_input = hashlib.md5(password.encode()).hexdigest()
        return self.password == hashed_input

# Test the User class
if __name__ == "__main__":
    # Create a user with a password
    user = User("Test User", "secret123")
    print(user.name)
    
    # Test password validation - this should return True but doesn't
    if not user.is_valid_password("secret123"):
        print("is_valid_password should return True if it's the right password")
    else:
        print("Password validation works correctly")
    
    # Test with wrong password
    if user.is_valid_password("wrong_password"):
        print("is_valid_password should return False if it's the wrong password")
    else:
        print("Correctly rejects wrong password")