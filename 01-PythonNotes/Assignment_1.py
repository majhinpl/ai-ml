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
output = input.strip(" ").replace("maintained...", "Maint...").title()
print(output)

# 10. Data Import from Banks
# Clean CSV headers from banking partners
input = [" Transaction_ID_", "_Amount__ "]
output = [c.strip(" _").replace("_", " ") for c in input]
print(output)

# Hard Level (Advanced Financial Systems)
# 1. Multi-Source Ticker Matching
input = ["NTC@NEPSE", "*SCB*", "HIDCL-"]
output = [k.strip("*-").replace("@NEPSE", "") for k in input]
print(output)

# 2. Real-Time Data Feed Sanitization
# Process websocket streams with numeric prefixes.
input = "12345|NTC|1520.25"
output = input.lstrip("12345|")
print(output)

# 3. Forum Sentiment Corpus
# Clean/analyze community discussions.
# Output: {"Buy", "Ntc", "Scb", "Overvalued"}

input = [" Buy NTC!! ", "SCB overvalued"]
output = {word for sentence in input for word in sentence.strip(" ").replace("!!", "").title().split()}
print(output) # need methods to get in ordered.

# 4. Historical Data Reconciliation
# Clean 20-year NEPSE records with inconsistent formatting.
# output : {"year": 2005, "symbol": "NTC", "price": 1250.50}
input = "2005;__NTC;1250.50_"
clean_input = input.strip("_").replace(";__", " ").replace(";", " ").split()
output = {
    "year": int(clean_input[0]),
    "symbol": clean_input[1],
    "price" : float(clean_input[2])
}
print(output)

# 5. Regulatory Document Processing
# Extract cleaned company names from SEC filings.
input = "Report for %%Nepal Investment Bank ltd.%%"
output = input.strip("%").replace(" %%", " ").title()
print(output)

# 6. Automated News Summarization
# Preprocess RSS feeds for AI models.
# output : "Market Alert: Nepse Index Hits All Time High"
input = "!!!MARKET ALRET: NEPSE_index_hits_all-time_high!!!"
output = input.strip("!").replace("_", " ").replace("-", " ").title()
print(output)

# 7. Multi-Language Support
# Clean Nepali/English mixed data
# output = {"en": "Nepal Bank (NBL) +2.5%", "ne": "नेपाल बैंक (NBL) +2.5%"}
input = "नेपाल बैंक (NBL) +2.5%"
output = {
    "en": "Nepal Bank (NBL) +2.5%",
    "ne": input
}
print(output)

# 8. Fraud Detection Logs
# Sanitize suspicious activity reports.
input = "USER123__; Multiple_orders; NTC; "
clean_input = input.strip(" ").replace("__; ", " ").replace(";", "").split()
output = {
    "user" : clean_input[0],
    "activity": clean_input[1].replace("_", " "),
    "symbol": "NTC"

}
print(output)

# 9. Portfolio Performance Reports
# Clean PDF text extraction outputs.
input = "Q4_2024: Return=12.5%___"
output = input.strip("_").replace("_", " ").replace("=", " ")
print(output)

# 10. API Integration Pipeline
# Process third-party financial data with inconsistent formats.
# Output: {"stock": "NTC", "price": 1500.00}
input = {"Stock": " NTC ", "Price": "Rs 1500.00 "}
output = {
    key.lower(): value.strip().replace("Rs ", "")
    for key, value in input.items()
}
print(output)