import re

with open('/tmp/remake-waitlist-app-seo/generate_custom_seo.py', 'r') as f:
    content = f.read()

new_p = """p = {
    "slug": "is-oleth-3-comedogenic-acne-safe",
    "brand": "Skincare Ingredient Audit",
    "product": "Oleth-3",
    "rating": "0.0/5",
    "rating_num": 0.0,
    "badge": "SEVERE PORE-CLOGGING RISK",
    "badge_color": "bg-red-500",
    "score": "0/100",
    "score_offset": "440",
    "verdict": "Oleth-3 has a comedogenic rating of 5 out of 5. It is a highly comedogenic emulsifier that will almost certainly clog pores and trigger inflammatory breakouts for acne-prone skin types.",
    "meta_desc": "Is Oleth-3 comedogenic? Learn why this chemical has a 5/5 pore-clogging rating and how to scan your skincare for hidden acne triggers using the REMAKE app.",
    "ingredients": [
        {
            "name": "Oleth-3",
            "risk": "RATING: 5/5",
            "desc": "An oleyl alcohol derivative that acts as a surfactant and emulsifier. Recognized by dermatologists as a severe comedogenic ingredient that easily penetrates the follicular barrier, trapping sebum and bacteria."
        },
        {
            "name": "Barrier Risk",
            "risk": "HIGH",
            "desc": "Due to its high lipid solubility and low molecular weight, Oleth-3 disrupts the skin barrier, allowing other potential irritants deeper into the epidermis."
        }
    ],
    "metrics": {
        "Comedogenic Rating": "5/5 (Severe)",
        "Primary Function": "Emulsifier / Surfactant",
        "Acne Risk": "High (Cystic & Whiteheads)",
        "Safe for Acne-Prone Skin": "No"
    }
}"""

content = re.sub(r'p = \{.*?\n\}', new_p, content, flags=re.DOTALL)

with open('/tmp/remake-waitlist-app-seo/gen_oleth3_script.py', 'w') as f:
    f.write(content)
