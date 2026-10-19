import os
import re

with open("run_new_seo.py", "r") as f:
    content = f.read()

html_template = content.split("p = {")[0]

p = {
    "slug": "stearic-acid-comedogenic-acne",
    "brand": "Skincare Ingredient Audit",
    "product": "Stearic Acid",
    "rating": "2.5/5",
    "rating_num": "2.5",
    "badge": "MODERATE COMEDOGENIC RISK",
    "badge_color": "bg-orange-100 text-orange-700 border-orange-200",
    "score": "45",
    "score_offset": "138.16",
    "meta_desc": "Is Stearic Acid comedogenic? Find out if this common fatty acid causes acne and closed comedones in our cosmetic chemistry teardown.",
    "verdict": "Stearic acid is a fatty acid found naturally in the skin barrier and used widely as an emulsifier and thickener in moisturizers. While it gives creams a rich, luxurious texture, it has a comedogenic rating of 3 out of 5. For acne-prone individuals, high concentrations of stearic acid can cause congestion and closed comedones, though it is less severe than its derivatives like Isopropyl Myristate.",
    "ingredients": [
        {
            "name": "Stearic Acid",
            "risk": "Moderate Comedogenic",
            "desc": "A saturated fatty acid with a comedogenic rating of 3. Can cause congestion and closed comedones when used in high concentrations on acne-prone skin."
        },
        {
            "name": "Glyceryl Stearate SE",
            "risk": "Fungal Acne Trigger",
            "desc": "A self-emulsifying form of stearic acid. Not only can it clog pores (rating 3), but it is a known trigger for Malassezia folliculitis (fungal acne)."
        },
        {
            "name": "Potassium Stearate",
            "risk": "High Risk",
            "desc": "Often used in shaving creams and soaps alongside stearic acid. Highly alkaline and can disrupt the acid mantle, leading to barrier damage and breakouts."
        }
    ],
    "metrics": {
        "Acne Safety": "Not Acne Safe",
        "Comedogenic Rating": "3/5 (Moderate-High)",
        "Malassezia Safe": "No (Triggers Fungal Acne)",
        "Barrier Safe": "Yes (When formulated correctly)",
        "Primary Function": "Emollient / Thickener"
    }
}

slug = p["slug"]
brand = p["brand"]
product = p["product"]
rating = p["rating"]
rating_num = p["rating"].split("/")[0]
badge = p["badge"]
badge_color = p["badge_color"]
score = p["score"]
score_offset = p["score_offset"]
verdict = p["verdict"]
meta_desc = p.get("meta_desc", f"Is {product} safe for acne? Read the full REMAKE chemical audit.")

ing_items = []
for ing in p["ingredients"]:
    border_color = "border-red-300" if "red" in badge_color else "border-orange-300"
    badge_bg = "bg-red-50 text-red-600 border-red-200" if "red" in badge_color else "bg-orange-50 text-orange-600 border-orange-200"
    
    ing_html = f'''<div class="border-l-2 {border_color} pl-4 py-1">
        <div class="flex justify-between items-start">
          <span class="font-semibold text-sm text-[#2A2421]">{ing["name"]}</span>
          <span class="text-[10px] {badge_bg} border px-2 py-0.5 rounded-full font-bold uppercase tracking-wider">{ing["risk"]}</span>
        </div>
        <p class="text-xs text-[#7C726E] font-light mt-1 leading-relaxed">{ing["desc"]}</p>
      </div>'''
    ing_items.append(ing_html)
ingredients_html = "\n              ".join(ing_items)

spec_items = []
for label, val in p["metrics"].items():
    spec_html = f'''<div class="flex justify-between items-center py-2 border-b border-[#F5DDE3]/50">
        <span class="text-[#7C726E]">{label}:</span>
        <span class="font-medium text-[#2A2421] text-right">{val}</span>
      </div>'''
    spec_items.append(spec_html)
specs_html = "\n              ".join(spec_items)

# Need to replace {rating_num} which was missing in original run_new_seo.py possibly
final_html = html_template.replace("p = ", "").format(
    slug=slug,
    brand=brand,
    product=product,
    rating=rating,
    rating_num=rating_num,
    badge=badge,
    badge_color=badge_color,
    score=score,
    score_offset=score_offset,
    verdict=verdict,
    meta_desc=meta_desc,
    ingredients_html=ingredients_html,
    specs_html=specs_html
)

path = f"/tmp/remake-waitlist-app-seo/products/{slug}.html"
with open(path, "w") as f:
    f.write(final_html)
print(f"Generated: {path}")

# --- UPDATE SITEMAP ---
with open("sitemap.xml", "r") as f:
    sitemap = f.read()

sitemap_entry = f"""  <url>
    <loc>https://remake.beauty/products/{slug}.html</loc>
    <priority>0.8</priority>
  </url>
</urlset>"""

sitemap = sitemap.replace("</urlset>", sitemap_entry)
with open("sitemap.xml", "w") as f:
    f.write(sitemap)
print("Updated sitemap.xml")

# --- UPDATE INDEX.HTML ---
with open("index.html", "r") as f:
    index = f.read()

footer_link = f"""<li><a href="/products/{slug}.html" class="hover:underline hover:text-[#2A2421] transition decoration-[#E8A0AA]">Stearic Acid Audit</a></li>
          <li><a href="/products/isopropyl-myristate-acne-safe.html\""""

index = index.replace('<li><a href="/products/isopropyl-myristate-acne-safe.html"', footer_link)
with open("index.html", "w") as f:
    f.write(index)
print("Updated index.html")
