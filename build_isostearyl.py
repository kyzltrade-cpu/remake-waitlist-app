import os

template = """<!DOCTYPE html>  
<html lang="en">  
<head>  
  <meta charset="UTF-8" />  
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />  
  <meta name="theme-color" content="#2A2421" />  
  <meta name="apple-mobile-web-app-capable" content="yes" />
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
  <meta name="apple-mobile-web-app-title" content="REMAKE" />
  <link rel="canonical" href="https://remake.beauty/products/isostearyl-isostearate-comedogenic-acne.html" />
  <meta name="description" content="Is Isostearyl Isostearate comedogenic? Find out why this skincare ingredient has a high comedogenic rating of 4/5 and how it triggers deep acne breakouts.">  
  <title>Isostearyl Isostearate | REMAKE Beauty Scanner App</title>
  <meta name="keywords" content="makeup, cosmetic chemistry, skincare scanner, comedogenic checker, is Isostearyl Isostearate comedogenic, toxic ingredients makeup, acne safe makeup, remake app, Isostearyl Isostearate acne safe">
  <meta name="author" content="REMAKE Beauty">
  
  <script src="https://cdn.tailwindcss.com"></script>  
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400&family=Montserrat:wght@300;400;500;600&display=swap" rel="stylesheet">  
  <style>  
    :root { --primary-pink: #FFD1E3; --bg-pink: #FDF7F9; --luxury-dark: #2A2421; }  
    body { background-color: var(--bg-pink); font-family: 'Montserrat', sans-serif; -webkit-font-smoothing: antialiased; }  
    .font-luxury { font-family: 'Cormorant Garamond', serif; }  
    .font-numbers { font-family: 'Playfair Display', serif; }  
    .card-luxury { background: rgba(255, 255, 255, 0.6); backdrop-filter: blur(12px); border: 1px solid rgba(255, 209, 227, 0.4); box-shadow: 0 8px 32px rgba(42, 36, 33, 0.04); border-radius: 20px; }
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
      <span>Ingredient Teardown</span>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-12 gap-8 md:gap-12">  
      <div class="md:col-span-5 space-y-6">  
        
        <div class="card-luxury p-8 relative overflow-hidden group">
          <div class="absolute inset-0 bg-gradient-to-br from-red-100/50 to-transparent opacity-0 group-hover:opacity-100 transition duration-700"></div>
          <div class="relative z-10 flex flex-col items-center text-center">
            <div class="w-24 h-24 bg-red-100 rounded-full flex items-center justify-center mb-6 shadow-sm border border-red-200">
              <span class="font-numbers text-4xl text-red-600 font-bold">4/5</span>
            </div>
            <h1 class="font-luxury text-4xl text-[#2A2421] mb-2 leading-tight">Isostearyl Isostearate</h1>
            <p class="text-xs uppercase tracking-[0.2em] text-[#7C726E] font-semibold mb-4">Comedogenic Danger</p>
            <p class="text-sm font-light text-[#7C726E] leading-relaxed">A heavily occlusive skin-conditioning agent that is highly notorious for trapping bacteria and dead skin cells, causing severe closed comedones.</p>
          </div>
        </div>  

        <div class="card-luxury p-6 bg-[#2A2421] text-white">
          <h3 class="font-luxury text-xl mb-3 text-pink-100">The AI Verdict</h3>
          <p class="text-sm text-white/80 leading-relaxed font-light">Isostearyl Isostearate is an ester of isostearyl alcohol and isostearic acid, primarily used as a binder and emollient in thick creams and lipsticks. Earning a highly dangerous comedogenic rating of 4 out of 5, it is a significant threat to anyone with acne-prone or congested skin. We strongly advise scanning your cosmetics with the Remake app to ensure this pore-clogging ingredient is not in your daily routine.</p>
        </div>
      </div>  

      <div class="md:col-span-7 space-y-8">  
        <div class="space-y-6 mt-8 md:mt-0">  
          
          <div class="card-luxury p-6 bg-white/70">  
            <h3 class="font-luxury text-2xl text-[#2A2421] mb-6">Feature Breakdown & Safety Checking</h3>  
            <div class="space-y-6">  
              <div class="border-l-2 border-red-400 pl-4 py-1">
                <div class="flex justify-between items-start">
                  <span class="font-semibold text-sm text-[#2A2421]">Comedogenic Rating</span>
                  <span class="text-[10px] bg-red-50 text-red-700 border-red-200 border px-2 py-0.5 rounded-full font-bold uppercase tracking-wider">High Risk (4/5)</span>
                </div>
                <p class="text-xs text-[#7C726E] font-light mt-1 leading-relaxed">With a comedogenic rating of 4/5, Isostearyl Isostearate is considered highly pore-clogging. It creates an occlusive film over the skin that refuses to let pores breathe, leading to rapid congestion.</p>
              </div>
              <div class="border-l-2 border-yellow-400 pl-4 py-1">
                <div class="flex justify-between items-start">
                  <span class="font-semibold text-sm text-[#2A2421]">Barrier Disruption</span>
                  <span class="text-[10px] bg-yellow-50 text-yellow-700 border-yellow-200 border px-2 py-0.5 rounded-full font-bold uppercase tracking-wider">Low Risk</span>
                </div>
                <p class="text-xs text-[#7C726E] font-light mt-1 leading-relaxed">It conditions the surface layer but its thick, impenetrable consistency is completely unsuitable for skin prone to breakouts or excess sebum.</p>
              </div>
              <div class="border-l-2 border-red-400 pl-4 py-1">
                <div class="flex justify-between items-start">
                  <span class="font-semibold text-sm text-[#2A2421]">Acne Safe</span>
                  <span class="text-[10px] bg-red-50 text-red-700 border-red-200 border px-2 py-0.5 rounded-full font-bold uppercase tracking-wider">NOT ACNE SAFE</span>
                </div>
                <p class="text-xs text-[#7C726E] font-light mt-1 leading-relaxed">This ingredient is definitively not acne safe. If the Remake scanner detects Isostearyl Isostearate in your formula, it will trigger an immediate red flag.</p>
              </div>  
            </div>  
          </div>  

          <div class="card-luxury p-6 bg-white/70">  
            <h3 class="font-luxury text-xl text-[#2A2421] mb-5">Detailed Specifications</h3>  
            <div class="space-y-4 text-sm">  
              <div class="flex justify-between items-center py-2 border-b border-[#F5DDE3]/50">
                <span class="text-[#7C726E]">Comedogenic Rating:</span>
                <span class="font-medium text-[#2A2421] text-right">4/5 (Highly Pore Clogging)</span>
              </div>
              <div class="flex justify-between items-center py-2 border-b border-[#F5DDE3]/50">
                <span class="text-[#7C726E]">Irritation Score:</span>
                <span class="font-medium text-[#2A2421] text-right">Low</span>
              </div>
              <div class="flex justify-between items-center py-2 border-b border-[#F5DDE3]/50">
                <span class="text-[#7C726E]">Common Uses:</span>
                <span class="font-medium text-[#2A2421] text-right">Emollient, Binder, Skin-Conditioning</span>
              </div>
              <div class="flex justify-between items-center py-2 border-b border-[#F5DDE3]/50">
                <span class="text-[#7C726E]">Remake App Verdict:</span>
                <span class="font-medium text-[#2A2421] text-right">Avoid for Acne-Prone Skin</span>
              </div>  
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

with open('products/isostearyl-isostearate-comedogenic-acne.html', 'w') as f:
    f.write(template)

print("Created products/isostearyl-isostearate-comedogenic-acne.html")
