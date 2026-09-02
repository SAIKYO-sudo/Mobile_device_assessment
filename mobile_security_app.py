import streamlit as st

st.set_page_config(
    page_title="Mobile Device Security Assessment",
    page_icon="📱",
    layout="centered"
)

st.title("📱 Mobile Device Security Assessment")
st.subheader("Android / iOS Dynamic Risk Assessment")
st.write(
    "Answer the following questions to receive a mobile device security "
    "risk assessment and personalized recommendations."
)

st.divider()

os_type = st.radio(
    "Select your mobile operating system:",
    ["Android", "iOS"]
)

st.markdown("## 🔐 Device Security")

screen_lock = st.radio(
    "Do you use a screen lock/passcode?",
    ["Yes", "No"]
)

update = st.radio(
    "How often do you update your operating system?",
    ["Immediately when available", "Within a few days", "Sometimes", "Rarely/Never"]
)

permission = st.radio(
    "Do you review application permissions?",
    ["Always", "Sometimes", "Rarely", "Never"]
)

if os_type == "Android":
    apk = st.radio(
        "Have you ever installed an APK from an unknown website?",
        ["No", "Yes", "Not Sure"]
    )
else:
    apk = "Not Applicable"

st.markdown("## 🛡️ Account and Data Security")

twofa = st.radio(
    "Do you use Two-Factor Authentication (2FA) for important accounts?",
    ["Yes", "No", "I don't know what 2FA is"]
)

passwords = st.radio(
    "Do you use different passwords for different important accounts?",
    ["Yes", "Sometimes", "No"]
)

backup = st.radio(
    "Do you regularly back up important mobile data?",
    ["Yes, regularly", "Sometimes", "No"]
)

st.markdown("## 🌐 Network and Phishing Security")

wifi = st.radio(
    "How often do you connect to public Wi-Fi?",
    ["Never", "Rarely", "Sometimes", "Frequently"]
)

links = st.radio(
    "Have you ever clicked on a suspicious or unknown link?",
    ["No", "Yes", "Not Sure"]
)

phishing = st.radio(
    "Do you know how to identify phishing messages?",
    ["Yes", "Not Sure", "No"]
)

if st.button("🔍 Assess My Security", use_container_width=True):
    score = 0
    risks = []
    recommendations = []

    if screen_lock == "No":
        score += 15
        risks.append("No screen lock/passcode")
        recommendations.append("Enable a strong screen lock, PIN, password, or biometric authentication.")

    if update == "Rarely/Never":
        score += 15
        risks.append("Operating system updates are rarely installed")
        recommendations.append("Install operating system and security updates regularly.")
    elif update == "Sometimes":
        score += 7
        risks.append("Operating system updates are inconsistent")
        recommendations.append("Enable automatic updates where possible.")

    if permission in ["Rarely", "Never"]:
        score += 10
        risks.append("Application permissions are rarely reviewed")
        recommendations.append("Review and remove unnecessary app permissions.")
    elif permission == "Sometimes":
        score += 5
        risks.append("Application permissions are reviewed inconsistently")
        recommendations.append("Check app permissions regularly.")

    if os_type == "Android":
        if apk == "Yes":
            score += 20
            risks.append("Unknown APK installation")
            recommendations.append("Avoid installing APK files from unknown or untrusted websites.")
        elif apk == "Not Sure":
            score += 8
            risks.append("Uncertainty about APK installation sources")
            recommendations.append("Install applications only from trusted sources such as Google Play.")

    if twofa == "No":
        score += 10
        risks.append("Two-Factor Authentication is not used")
        recommendations.append("Enable 2FA for important accounts.")
    elif "don't know" in twofa.lower():
        score += 10
        risks.append("Lack of awareness of Two-Factor Authentication")
        recommendations.append("Learn about and enable Two-Factor Authentication for important accounts.")

    if passwords == "No":
        score += 10
        risks.append("Different passwords are not used")
        recommendations.append("Use unique, strong passwords for important accounts.")
    elif passwords == "Sometimes":
        score += 5
        risks.append("Password practices are inconsistent")
        recommendations.append("Use unique passwords consistently for important accounts.")

    if backup == "No":
        score += 10
        risks.append("Important mobile data is not backed up")
        recommendations.append("Create regular backups of important data.")
    elif backup == "Sometimes":
        score += 5
        risks.append("Mobile data backup is inconsistent")
        recommendations.append("Schedule regular automatic backups.")

    if wifi == "Frequently":
        score += 8
        risks.append("Frequent use of public Wi-Fi")
        recommendations.append("Avoid sensitive transactions on public Wi-Fi and use trusted networks.")
    elif wifi == "Sometimes":
        score += 4
        risks.append("Occasional use of public Wi-Fi")
        recommendations.append("Use caution when connecting to public Wi-Fi.")

    if links == "Yes":
        score += 15
        risks.append("Suspicious or unknown links have been clicked")
        recommendations.append("Avoid clicking unknown links and verify senders before opening URLs.")
    elif links == "Not Sure":
        score += 5
        risks.append("Uncertainty about suspicious link exposure")
        recommendations.append("Be cautious with unexpected messages and links.")

    if phishing == "No":
        score += 10
        risks.append("Unable to identify phishing messages")
        recommendations.append("Learn common phishing warning signs such as urgent requests and suspicious URLs.")
    elif phishing == "Not Sure":
        score += 5
        risks.append("Uncertain about identifying phishing messages")
        recommendations.append("Improve awareness of phishing indicators.")

    if score <= 20:
        risk_level = "🟢 LOW RISK"
        message = "Your responses indicate generally good mobile security practices."
        recommendations.append("Continue maintaining good security habits and regularly review your settings.")
    elif score <= 45:
        risk_level = "🟡 MEDIUM RISK"
        message = "Some security weaknesses were identified and should be improved."
    else:
        risk_level = "🔴 HIGH RISK"
        message = "Multiple significant security weaknesses were identified and require attention."

    st.divider()
    st.markdown("## 📊 Assessment Result")
    st.metric("Risk Score", f"{score} points")
    st.markdown(f"### {risk_level}")
    st.write(message)

    if risks:
        st.markdown("### ⚠️ Identified Risk Factors")
        for item in risks:
            st.write(f"• {item}")

    st.markdown("### 💡 Security Recommendations")
    for item in dict.fromkeys(recommendations):
        st.write(f"• {item}")

    st.info(
        "Academic prototype: This assessment is designed for educational purposes "
        "and demonstrates dynamic mobile security risk scoring."
    )
