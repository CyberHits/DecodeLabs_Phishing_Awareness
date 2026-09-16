import re


SUSPICIOUS_KEYWORDS = [
    "urgent",
    "verify",
    "password",
    "account suspended",
    "click now",
    "winner",
    "bank",
    "login",
    "security alert",
    "limited time",
    "act now"
]


def analyze_message(message):
    message_lower = message.lower()

    found_keywords = []

    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword in message_lower:
            found_keywords.append(keyword)

    links = re.findall(r'https?://[^\s]+', message)

    red_flags = []

    if any(word in message_lower for word in [
        "urgent",
        "act now",
        "click now",
        "limited time"
    ]):
        red_flags.append("Urgent or pressure-based language")

    if any(word in message_lower for word in [
        "password",
        "login"
    ]):
        red_flags.append("Request for account or login information")

    if any(phrase in message_lower for phrase in [
        "verify your account",
        "verify your identity",
        "confirm your account",
        "confirm your identity"
    ]):
        red_flags.append("Request for account verification")

    if links:
        red_flags.append(
            "Contains a link that should be verified before clicking"
        )

    if any(phrase in message_lower for phrase in [
        "bank",
        "account suspended",
        "security alert"
    ]):
        red_flags.append(
            "Claims to involve an important account or security issue"
        )

    if not red_flags:
        risk_level = "LOW RISK"
    elif len(red_flags) <= 2:
        risk_level = "MEDIUM RISK"
    else:
        risk_level = "HIGH RISK"

    print("\n=== PHISHING AWARENESS ANALYZER ===")

    print("\nSuspicious Keywords:")
    if found_keywords:
        for keyword in found_keywords:
            print(f"- {keyword}")
    else:
        print("- None detected")

    print("\nLinks Found:")
    if links:
        for link in links:
            print(f"- {link}")
    else:
        print("- No links detected")

    print("\nRed Flags Found:")
    if red_flags:
        for number, flag in enumerate(red_flags, 1):
            print(f"[{number}] {flag}")
    else:
        print("- No obvious red flags detected")

    print(f"\nRisk Assessment: {risk_level}")

    print("\nWhy should you be cautious?")

    if risk_level == "HIGH RISK":
        print(
            "The message contains several indicators commonly associated "
            "with phishing, including urgency, requests for sensitive "
            "information, or suspicious links."
        )
    elif risk_level == "MEDIUM RISK":
        print(
            "The message contains some suspicious characteristics. "
            "Verify the sender and message through a trusted channel."
        )
    else:
        print(
            "No obvious phishing indicators were detected, but this does "
            "not guarantee that the message is completely safe."
        )

    print("\nRecommendation:")
    print(
        "Do not click suspicious links or provide passwords or sensitive "
        "information. Verify unexpected messages through an official "
        "website or trusted communication channel."
    )


print("=== DecodeLab Project 3 ===")
print("Phishing Awareness Analyzer")
print("\nPaste a sample email or message below.")
print("Press ENTER twice when finished.\n")

lines = []

while True:
    line = input()

    if line == "":
        break

    lines.append(line)

message = "\n".join(lines)

if not message.strip():
    print("\nNo message was entered. Please try again.")
else:
    analyze_message(message)
