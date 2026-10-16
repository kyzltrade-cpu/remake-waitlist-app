import os

html_template = """<!DOCTYPE html>  
<html lang="en">  
<head>  
  <meta charset="UTF-8" />  
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />  
  <meta name="theme-color" content="#2A2421" />  
  <meta name="apple-mobile-web-app-capable" content="yes" />
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
  <meta name="apple-mobile-web-app-title" content="REMAKE" />
  <link rel="canonical" href="https://remake.beauty/products/{slug}.html" />
  <meta name="description" content="{meta_desc}">  
  <title>{product} - Comedogenic Risk & Acne Safety | REMAKE Chemical Audit</title>
  <meta name="keywords" content="makeup, cosmetic chemistry, skincare scanner, comedogenic checker, toxic ingredients makeup, acne safe makeup, remake app, {product} comedogenic, {product} acne safe, Aquaphor for acne">
  <meta name="author" content="REMAKE Beauty">
  
  <script src="https://cdn.tailwindcss.com"></script>  
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400&family=Montserrat:wght@300;400;500;600&display=swap" rel="stylesheet">  
  <style>  
    :root {{ --primary-pink: #FFD1E3; --bg-pink: #FDF7F9; --luxury-dark: #2A2421; }}  
    body {{ background-color: var(--bg-pink); font-family: 'Montserrat', sans-serif; -webkit-font-smoothing: antialiased; }}  
    .font-luxury {{ font-family: 'Cormorant Garamond', serif; }}  
    .font-numbers {{ font-family: 'Playfair Display', serif; }}  
    .card-luxury {{ background: rgba(255, 255, 255, 0.6); backdrop-filter: blur(12px); border: 1px solid rgba(255, 209, 227, 0.4); box-shadow: 0 8px 32px rgba(42, 36, 33, 0.04); border-radius: 20px; }}
  </style>  
</head>  
<body class="min-h-screen text-[#2A2421] selection:bg-[#FFD1E3] selection:text-[#2A2421]">  

  <nav class="fixed top-0 w-full z-50 bg-white/70 backdrop-blur-xl border-b border-[#F5DDE3]/50">  
    <div class="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">  
      <a href="/" class="font-luxury text-2xl tracking-widest text-[#2A2421] uppercase">REMAKE</a>  
      <a href="https://apps.apple.com/us/app/remake-beauty/id6785347578" class="text-[10px] font-bold uppercase tracking-widest bg-[#2A2421] text-white px-5 py-2.5 rounded-full hover:bg-black transition-colors shadow-sm">Get App</a>  
    </div>  
  </nav>  

  <main class="pt-28 pb-16 px-4 md:px-8 max-w-5xl mx-auto">  
    
    <div class="mb-8 flex items-center gap-2 text-xs font-medium text-[#7C726E] uppercase tracking-wider">
      <a href="/" class="hover:text-[#2A2421] transition">Home</a>
      <span>/</span>
      <span>Product Audit</span>
      <span>/</span>
      <span class="text-[#2A2421]">{product}</span>
    </div>

    <div class="grid md:grid-cols-12 gap-8 md:gap-12">  
      
      <div class="md:col-span-5 space-y-6">  
        <div class="card-luxury p-8 flex flex-col items-center justify-center text-center">  
          <div class="text-[10px] font-bold uppercase tracking-widest text-[#7C726E] mb-3">{brand}</div>
          <h1 class="font-luxury text-4xl md:text-5xl leading-tight mb-6">{product}</h1>
          <div class="{badge_color} text-[10px] font-bold uppercase tracking-widest px-4 py-1.5 rounded-full mb-8">
            {badge}
          </div>
          
          <div class="relative w-40 h-40 flex items-center justify-center mb-6">  
            <svg class="absolute inset-0 w-full h-full transform -rotate-90" viewBox="0 0 100 100">  
              <circle cx="50" cy="50" r="40" stroke="#F5DDE3" stroke-width="4" fill="none" />  
              <circle cx="50" cy="50" r="40" stroke="#2A2421" stroke-width="4" fill="none" stroke-dasharray="251.2" stroke-dashoffset="{score_offset}" stroke-linecap="round" class="transition-all duration-1000 ease-out" />  
            </svg>  
            <div class="text-center flex flex-col items-center justify-center relative z-10 pt-2">  
              <span class="font-numbers text-5xl font-light leading-none text-[#2A2421] tracking-tight">{score}</span>  
              <span class="text-[9px] uppercase tracking-widest text-[#7C726E] mt-1 font-semibold">Safety Score</span>  
            </div>  
          </div>  

          <div class="text-3xl text-pink-300 font-luxury tracking-widest mb-2">{rating_num}<span class="text-xl text-[#7C726E]/40">/5</span></div>
          <div class="flex gap-1 text-pink-300 text-sm">
            ★★☆☆☆
          </div>
        </div>  

        <div class="card-luxury p-6 bg-[#2A2421] text-white">
          <h3 class="font-luxury text-xl mb-3 text-pink-100">The AI Verdict</h3>
          <p class="text-sm text-white/80 leading-relaxed font-light">{verdict}</p>
        </div>
      </div>  

      <div class="md:col-span-7 space-y-8">  
        <div class="space-y-6 mt-8 md:mt-0">  
          
          <div class="card-luxury p-6 bg-white/70">  
            <h3 class="font-luxury text-2xl text-[#2A2421] mb-6">Chemical Profile & Risk Factors</h3>  
            <div class="space-y-6">  
              {ingredients_html}  
            </div>  
          </div>  

          <div class="card-luxury p-6 bg-white/70">  
            <h3 class="font-luxury text-xl text-[#2A2421] mb-5">Detailed Specifications</h3>  
            <div class="space-y-4 text-sm">  
              {specs_html}  
            </div>  
          </div>  
        </div>  
      </div>  
    </div>  
  </main>  

  <footer class="bg-[#2A2421] text-white py-12 px-6 border-t border-[#F5DDE3]/10 mt-16">  
    <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-6">  
      <div class="flex flex-col items-center md:items-start text-center md:text-left">  
        <span class="font-luxury text-2xl tracking-widest text-pink-100 uppercase">REMAKE</span>  
        <p class="text-[10px] text-white/60 uppercase tracking-widest mt-2">© 2026 REMAKE LABS. All rights reserved.</p>  
      </div>  
      <div class="flex gap-6 text-xs text-white/80 font-light">  
        <a href="https://remake.beauty/privacy.html" class="hover:text-pink-100 transition">Privacy Policy</a>  
        <a href="https://remake.beauty/terms.html" class="hover:text-pink-100 transition">Terms of Service</a>  
      </div>  
    </div>  
  </footer>  

</body>  
</html>"""

p = {
    "slug": "aquaphor-healing-ointment-comedogenic-acne",
    "brand": "Product Teardown",
    "product": "Aquaphor Healing Ointment",
    "rating": "2.0/5",
    "badge": "HIGH COMEDOGENIC RISK",
    "badge_color": "bg-red-100 text-red-700 border-red-200",
    "score": "20",
    "score_offset": "200.96",
    "verdict": "Aquaphor is widely praised as a miracle cure for dry skin, but dermatologists often hide the brutal truth: it's a suffocating disaster for acne-prone skin. It relies on a heavy base of Petrolatum combined with Lanolin Alcohol—a highly comedogenic sheep sebum extract. This thick barrier traps sweat, dead skin, and bacteria directly against your pores, practically guaranteeing closed comedones and deep cystic breakouts.",
    "ingredients": [
        {
            "name": "Lanolin Alcohol",
            "risk": "Severe Comedogenic Risk (Rating 4)",
            "desc": "A wax derived from sheep's wool grease. While moisturizing, it is notorious for penetrating and clogging pores rapidly, leading directly to textured skin and acne."
        },
        {
            "name": "Petrolatum",
            "risk": "Total Occlusive (Pore-Suffocating)",
            "desc": "Forms an impermeable barrier over the skin. It does not let the skin breathe, trapping bacteria and dead skin cells in the pores."
        },
        {
            "name": "Mineral Oil",
            "risk": "Moderate Comedogenic Risk",
            "desc": "A cheap petroleum byproduct. Creates an oil slick on the skin that exacerbates sebum build-up and worsens oily, acne-prone skin types."
        }
    ],
    "metrics": {
        "Allergens": "High Risk (Wool Alcohols/Lanolin)",
        "Oily & Acne-Prone Match": "Strongly Avoid",
        "Barrier Health": "Occlusive (Traps Moisture & Bacteria)",
        "Ethics & Sourcing": "Contains Animal Byproducts (Lanolin)"
    },
    "meta_desc": "Is Aquaphor Healing Ointment safe for acne or will it clog your pores? Discover the truth about its comedogenic ingredients like Lanolin in our brutal teardown."
}

slug = p["slug"]
brand = p["brand"]
product = p["product"]
rating = p["rating"]
rating_num = rating.split("/")[0]
badge = p["badge"]
badge_color = p["badge_color"]
score = p["score"]
score_offset = p["score_offset"]
verdict = p["verdict"]
meta_desc = p["meta_desc"]

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

final_html = html_template.format(
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

