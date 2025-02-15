#!/usr/bin/env python3

import re

# Defining the DataExtractor class to extract different data types
class DataExtractor:
    def __init__(self, text):
        self.text = text
        self.patterns = {
            "emails": r"(?:(?!\.)[a-zA-Z0-9._%+-]+(?<!\.)@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})",
            "urls": r"https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?",
            "phone_numbers": r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}",
            "credit_cards": r"\b(?:\d{4}[-\s]?){3}\d{4}\b",
            "time_formats": r"\b(?:0?[1-9]|1[0-2]):[0-5]\d\s?(?:AM|PM|am|pm)?|\b(?:[01]?\d|2[0-3]):[0-5]\d\b",
            "currency_amounts": r"(?:(?:\$|€|₦|RWF)\s?\d{1,3}(?:,\d{3})*(?:\.\d{2})?)"
        }

# Defining the extract method to extract specific data types
    def extract(self, data_type):
        """Extracts specific data type while handling edge cases."""
        pattern = self.patterns.get(data_type)
        if pattern:
            results = re.findall(pattern, self.text)
            if data_type == "emails":
                results = [email for email in results if ".." not in email]  # This removes invalid emails
            return results
        return []

    def extract_all(self):
        """Extracts all defined patterns while handling edge cases."""
        return {key: self.extract(key) for key in self.patterns}

# Display the extracted results in a formatted style
    def display_results(self):
        """Prints the extracted results."""
        extracted_data = self.extract_all()
        for key, values in extracted_data.items():
            print(f"\n{key.capitalize()} Found:")
            if values:
                for value in values:
                    print(value)
            else:
                print("No valid matches found.")

# Test text with different data types and some edge cases, you can edit this
test_text = """
Hello Hii!, my name is HonourGod Levison with email address: h.levison@alustudent.com or hlevi@@gmail.com.
This is a test text written at 13:54 and I have a phone number of +25079357358 or 08168493523.
My credit card number is 9452-5452-5532-5452 with $100,000.00 balance.
You are free to use it on any site like https://www.amazon.com and https://www aliexpress.com.
Don't worry about thanking me, what are friends for?.

"""

# Create an instance and runs the extraction
extractor = DataExtractor(test_text)
extractor.display_results()
