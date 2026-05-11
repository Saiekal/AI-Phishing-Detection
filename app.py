
# AI-BASED REAL-TIME PHISHING URL DETECTOR

import streamlit as st
import re

# PAGE SETTINGS

st.set_page_config(
    page_title="Phishing URL Detector",
    layout="centered"
)


# TITLE

st.title("🔒 AI-Based Phishing URL Detector")

st.write(
    "Enter a website URL to check whether "
    "it is Safe or Phishing."
)


# URL SAFETY CHECK FUNCTION

def check_url_safety(url):

    score = 0

    
    # HTTPS CHECK
    
    if "https://" in url:
        score += 3
    else:
        score -= 3

    
    # URL LENGTH CHECK
   

    if len(url) > 75:
        score -= 2

    
    # @ SYMBOL CHECK
   
    if "@" in url:
        score -= 4

    
    # TOO MANY HYPHENS
    

    if url.count('-') > 3:
        score -= 2

    
    # TOO MANY DOTS
    

    if url.count('.') > 4:
        score -= 1

    
    # DIGIT COUNT
    

    digit_count = sum(c.isdigit() for c in url)

    if digit_count > 6:
        score -= 2

        # SUSPICIOUS WORDS
    

    suspicious_words = [
        "login",
        "verify",
        "secure",
        "update",
        "banking",
        "free",
        "bonus",
        "password",
        "signin",
        "account",
        "wallet",
        "paypal"
    ]

    for word in suspicious_words:

        if word in url.lower():
            score -= 2

    # ======================================
    # IP ADDRESS CHECK
    # ======================================

    ip_pattern = re.compile(
        r'(([01]?\d\d?|2[0-4]\d|25[0-5])\.){3}'
        r'([01]?\d\d?|2[0-4]\d|25[0-5])'
    )

    if re.search(ip_pattern, url):
        score -= 5

    # ======================================
    # SHORTENED URL CHECK
    # ======================================

    shorteners = [
        "bit.ly",
        "tinyurl",
        "goo.gl",
        "t.co",
        "ow.ly"
    ]

    for shortener in shorteners:

        if shortener in url:
            score -= 3

    # ======================================
    # FINAL RESULT
    # ======================================

    if score >= 0:
        return "safe", score
    else:
        return "phishing", score

# ==========================================
# USER INPUT
# ==========================================

url = st.text_input(
    "Enter Website URL",
    placeholder="https://example.com"
)

# ==========================================
# BUTTON
# ==========================================

if st.button("Check Website"):

    if url == "":

        st.warning("Please enter a website URL.")

    else:

        result, score = check_url_safety(url)

        # ==================================
        # RESULT DISPLAY
        # ==================================

        st.subheader("Prediction Result")

        if result == "safe":

            st.success("✅ Safe Website")

        else:

            st.error("⚠ Phishing Website Detected")

        # ==================================
        # RISK LEVEL
        # ==================================

        st.subheader("Risk Score")

        if score >= 3:

            st.success("🟢 Low Risk")

        elif score >= 0:

            st.warning("🟡 Medium Risk")

        else:

            st.error("🔴 High Risk")

        # ==================================
        # SCORE DISPLAY
        # ==================================

        st.write(f"Security Score: {score}")
