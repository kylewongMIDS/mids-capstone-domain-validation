import streamlit as st
import json

st.title("Step 3: 🐟 Phish Fence API Setup")
st.markdown("Use this API to submit certificate requests and receive predictions on potential malicious domains.")
st.markdown("Please contact [clifton.harris@berkeley.edu](clifton.harris@berkeley.edu) to setup your organization's API url.")
st.markdown('---')
selected_ca = st.session_state.get('selected_ca', 'Unknown CA')
# --- Endpoint ---
st.subheader("📍 Endpoint")
st.code("https://your-api-url.amazonaws.com/default/FeatureExtractorContainer", language="bash")

# --- Request Format ---
st.subheader("📦 Expected JSON Payload")
st.markdown("Each object in the array represents one certificate request. `san_identities` should be a stringified list of domains.")

example_payload = [
    {
        "san_identities": json.dumps(["secure-login-paypal.net", "secure-login-venmo.net"]),
        "not_before": "2024-06-01T00:00:00Z",
        "not_after": "2024-09-01T00:00:00Z",
        "ca_name": selected_ca
    },
    {
        "san_identities": json.dumps(["go0gle.com", "facebo0k.com"]),
        "not_before": "2024-06-01T00:00:00Z",
        "not_after": "2024-09-01T00:00:00Z",
        "ca_name": selected_ca
    }
]

st.code(json.dumps(example_payload, indent=2), language="json")

# --- PowerShell Example ---
st.subheader("🖥️ Example Request (Windows PowerShell)")

st.code(r'''
& "C:\Windows\System32\curl.exe" -X POST "https://your-api-url.amazonaws.com/default/FeatureExtractorContainer" `
-H "Content-Type: application/json" `
--data "@cert_requests.json"
''', language="powershell")

# --- macOS/Linux Example ---
st.subheader("💻 Example Request (macOS / Linux)")

st.code("""
curl -X POST "https://your-api-url.amazonaws.com/default/FeatureExtractorContainer" \\
-H "Content-Type: application/json" \\
--data @cert_requests.json
""", language="bash")

# --- Sample Response ---
st.subheader("📥 Example API Response")

st.code("""
{
  "features": [
    {"parsed_domainname": "secure-login-paypal.net", "prediction": 0.714},
    {"parsed_domainname": "secure-login-venmo.net", "prediction": 0.814},
    {"parsed_domainname": "go0gle.com", "prediction": 0.343},
    {"parsed_domainname": "facebo0k.com", "prediction": 0.400}
  ]
}
""", language="json")

# --- Notes ---
st.subheader("📝 Notes")
st.markdown("""
- The API supports multiple certificate requests in a single call.
- `san_identities` **must be a JSON-encoded string** of domain names (e.g. `"[\"example.com\"]"`).
- All timestamps should be in ISO 8601 format with timezone (`Z`).
- The response contains a flat list of domains and their maliciousness score (0 to 1).
""")
