# Data Cleaning Using String Functions for Variables and Data Structures
# Easy Level (Basic Cleaning for User-Generated Data)

# 1. User Registration Names
# Clean user signup names by removing extra spaces and capitalizing properly.

input = [" ram bahadur ", "SITA ", " kirshna-GURUNG"]
output = [n.strip(" ").replace("-", " ").capitalize() for n in input]
print(output)

# 2. Stock Symbol Formatting
# Standardize user-entered stock symbols by removing special characters.

input = "#NBL!*"
output = input.strip("#!*")
print(output)

# 3. Watchlist Entry Cleaning
# Remove trailing commas/spaces from watchlist items.

input = ["NTC, ", " SCB ", ", HDL"]
output = [n.strip(", ") for n in input]
print(output)

# 4. Educational Content Titles
# Capitalize tutorial titles correctly

input = "introduction to NEPSE"
output = input.title()
print(output)

# 5. Clean RSS feed titles by stripping leading/trailing junk characters.
input = "%%% Market Update: Nepal %%%"
output = input.strip("% ")
print(output)

# 6. User Profile Cities
# Standardize location entries for analytics.

input = ["ktm", "pokhara", "biratnagar"]
output = [s.capitalize() for s in input]
print(output)

# 7. Broker ID Formatting
# Remove trailing underscores from broker codes.

input = {"broker", "ABC_123_"}
output = {a.rstrip("_") for a in input}
print(output)

# 8. Dividend Announcements
# Clean excessive exclamations from notifications
input = "NMB dividend declared!!!!"
output = input.rstrip("!")
print(output)

# 9. Sector Tags
# Standardize industry tags in research reports.

input = [" Banking ", "Hydropower "]
output = [r.strip(" ") for r in input]
print(output)

# 10. API Endpoint Parameters
# Sanitize user-inputted stock codes for API calls.

input = " NTC ;"
output = input.strip(" ;")
print(output)

# Intermediate Level (Financial Data Tranformation)
# 1. Portfolio Holdings Cleanup
# Clean nested JSON from broker APIs with whitespace issues.

input = {"stocks" : [" NABIL ", " SCB "], "units" : ["100 ", "200"]}

output = {k: [v.strip(" ") for v in v] for k, v in input.items()}
print(output)

# 2. Transaction Note Standardization
# Remove leading transaction IDs and format notes.

input = "TX1234-Buy 10 NTC @1500"
output = input.strip("TX1234-").title()
print(output)

# 3. Email Notification Formatting
# Prepare user alerts with proper casing.

input = "ALERT: ntc REACHED TARGET PRICE"
output = input.title()
print(output)

# 4. Watchlist Deduplication
# Clean and deduplicate user-submitted stock list.

input = ["ntc", " NTC ", "scb", "SCB "]
output = list(set([d.strip(" ").capitalize() for d in input]))
print(output)

# 5. News Sentiment Analysis
# Preprocess headlines for NLP pipelines.

input = [" NEPSE index gains 2% ", "!Banking sector rallies!"]
output = [p.strip(" !").title() for p in input]
print(output)

# 6. Broker Report Metadata
# Clean PDF report tites with mixed casing.
input = "Q3_REPORT_naBIL.pdf"
output = input.replace("_", " ").title()
print(output)

# 7. user-Generated Tickers
# Conditionally remove hashtags from social feed stock mentions.

input = ["#NTC", "SCB", "#HDL"]
output = [t.lstrip("#") if t.startswith("#") else t for t in input]
print(output)

# 8. Sector Classification
# Group cleaned company names by sector.

input = [" Nabil Bank", "Chilime Hydropower"]
output = [p.lstrip(" ").title() for p in input]
grouped = {}
for p in output:
    key = p[0].upper() #Note: How to make custom key "B", "C"
    grouped.setdefault(key, []).append(p)

print(output)
print(grouped)

# 9. Mobile Notification Cleaning
# Trim push notifications to 40 characters.

input = " NTC +2.5%! Buy recommendation maintained..."
output