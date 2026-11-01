import os
import json

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
  <meta name="keywords" content="makeup, cosmetic chemistry, skincare scanner, comedogenic checker, toxic ingredients makeup, acne safe makeup, remake app, {product} comedogenic, {product} acne safe">
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
      <a href="/" class="hover:text-[#2A2421] transition-colors">Home</a>
      <span>/</span>
      <span class="text-[#2A2421]">{brand}</span>
    </div>

    <div class="grid md:grid-cols-2 gap-12 lg:gap-20">
      
      <!-- Left Column: Score & Hero -->
      <div class="relative">
        <div class="card-luxury p-8 flex flex-col items-center justify-center text-center aspect-square relative overflow-hidden">
          
          <!-- Score Ring -->
          <div class="relative w-48 h-48 mb-6">
            <svg class="w-full h-full transform -rotate-90" viewBox="0 0 100 100">
              <circle cx="50" cy="50" r="45" fill="none" stroke="#F5DDE3" stroke-width="2" />
              <circle cx="50" cy="50" r="45" fill="none" stroke="#D98A96" stroke-width="4" stroke-dasharray="283" stroke-dashoffset="{score_offset}" class="transition-all duration-1000 ease-out" />
            </svg>
            <div class="absolute inset-0 flex flex-col items-center justify-center">
              <span class="font-numbers text-5xl text-[#2A2421] tracking-tighter">{score}</span>
              <span class="text-[9px] uppercase tracking-[0.2em] text-[#7C726E] mt-1 font-bold">Safety Score</span>
            </div>
          </div>

          <h1 class="font-luxury text-4xl leading-tight text-[#2A2421] mb-2">{product}</h1>
          <p class="text-xs uppercase tracking-widest text-[#7C726E] mb-6">{brand}</p>
          
          <div class="inline-flex items-center justify-center px-4 py-1.5 rounded-full {badge_color} border text-[10px] font-bold uppercase tracking-widest mb-6">
            {badge}
          </div>

        </div>
      </div>

      <!-- Right Column: Details & Verdict -->
      <div class="flex flex-col justify-center">
        <h2 class="text-xs font-bold uppercase tracking-widest text-[#7C726E] mb-3">AI Cosmetic Chemist Verdict</h2>
        <p class="text-sm md:text-base leading-relaxed text-[#2A2421] font-light mb-8">
          {verdict}
        </p>

        <h3 class="text-xs font-bold uppercase tracking-[0.15em] text-[#2A2421] mb-4 border-b border-[#F5DDE3]/50 pb-2">Flagged Ingredients</h3>
        
        <div class="space-y-4 mb-10">
          {ingredients_html}
        </div>

        <h3 class="text-xs font-bold uppercase tracking-[0.15em] text-[#2A2421] mb-4 border-b border-[#F5DDE3]/50 pb-2">Chemical Profile</h3>
        <div class="space-y-2 mb-10 text-sm">
          {specs_html}
        </div>
        
        <!-- CTA -->
        <a href="https://apps.apple.com/us/app/remake-beauty/id6785347578" class="group relative w-full flex justify-center py-4 px-4 border-none text-sm font-bold uppercase tracking-[0.2em] text-white bg-[#2A2421] hover:bg-black transition-all duration-300 shadow-[0_8px_30px_rgb(42,36,33,0.2)] hover:shadow-[0_8px_30px_rgb(42,36,33,0.4)]">
          Scan With Remake App
          <span class="absolute right-6 group-hover:translate-x-2 transition-transform duration-300">→</span>
        </a>
        <p class="text-center text-[10px] text-[#7C726E] mt-3 uppercase tracking-wider">Available on iOS</p>
      </div>

    </div>
  </main>

  <footer class="mt-20 border-t border-[#F5DDE3]/50 py-12 text-center bg-white/30 backdrop-blur-sm">
    <p class="font-luxury text-xl text-[#2A2421] mb-2 tracking-widest uppercase">REMAKE</p>
    <p class="text-[10px] uppercase tracking-widest text-[#7C726E] mb-6">Exposing the beauty industry.</p>
    <div class="flex justify-center gap-6 text-[10px] uppercase tracking-widest font-semibold text-[#2A2421]">
      <a href="/privacy.html" class="hover:text-[#D98A96] transition-colors">Privacy</a>
      <a href="/terms.html" class="hover:text-[#D98A96] transition-colors">Terms</a>
      <a href="mailto:theremakeapp@gmail.com" class="hover:text-[#D98A96] transition-colors">Contact</a>
    </div>
  </footer>  

</body>  
</html>"""

def generate_pages():
    os.makedirs("/tmp/remake-waitlist-app-seo/products", exist_ok=True)
    
    p = {
        "slug": "is-carrageenan-comedogenic-acne",
        "brand": "Skincare Ingredient Audit",
        "product": "Carrageenan",
        "rating": "5.0/5",
        "badge": "SEVERE PORE-CLOGGING RISK",
        "badge_color": "bg-red-100 text-red-700 border-red-200",
        "score": "15",
        "score_offset": "240",
        "verdict": "Carrageenan is an emulsifier derived from seaweed that is notoriously one of the most comedogenic ingredients in skincare. It is given a 5 out of 5 on the comedogenicity scale. Found in many 'natural' or 'marine' skincare lines, it is highly likely to cause severe acne breakouts, closed comedones, and skin irritation for those with acne-prone skin.",
        "meta_desc": "Is Carrageenan acne safe? Remake app exposes Carrageenan as a highly comedogenic (5/5) ingredient that will clog your pores and destroy your skin barrier.",
        "ingredients": [
            {
                "name": "Comedogenic Rating: 5/5",
                "risk": "Severe Pore-Clogging Risk",
                "desc": "Carrageenan has a devastating comedogenic rating of 5, meaning it will almost certainly clog pores and cause acne breakouts for anyone with oily or acne-prone skin."
            },
            {
                "name": "Skin Barrier Disruption",
                "risk": "Irritation Risk",
                "desc": "Aside from causing breakouts, carrageenan can trigger skin sensitivities and inflammation, leading to redness and further compromising a damaged skin barrier."
            },
            {
                "name": "Hidden in 'Natural' Skincare",
                "risk": "Deceptive Marketing",
                "desc": "Because it is derived from red seaweed, brands often use carrageenan in 'clean' or 'natural' products, giving consumers a false sense of safety."
            }
        ],
        "metrics": {
            "Comedogenicity Rating": "5/5 (Severe)",
            "Irritation Rating": "2/5 (Low to Moderate)",
            "Acne Safe": "NO",
            "Fungal Acne Safe": "NO"
        }
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
        border_col = "border-[#D98A96]" if "Remake Only" in ing["risk"] else "border-gray-400"
        bg_badge = "bg-pink-50 text-pink-700 border-pink-200" if "Remake Only" in ing["risk"] else "bg-gray-100 text-gray-700 border-gray-200"
        
        ing_html = f'''<div class="border-l-2 {border_col} pl-4 py-1">
            <div class="flex justify-between items-start">
              <span class="font-semibold text-sm text-[#2A2421]">{ing["name"]}</span>
              <span class="text-[10px] {bg_badge} border px-2 py-0.5 rounded-full font-bold uppercase tracking-wider">{ing["risk"]}</span>
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

if __name__ == "__main__":
    generate_pages()
