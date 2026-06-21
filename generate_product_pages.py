import os
import json

products_data = [
    {
        "slug": "benefit-porefessional-primer-toxic",
        "brand": "Benefit Cosmetics",
        "product": "The POREfessional Face Primer",
        "rating": "1.8/5",
        "badge": "NOT ACNE SAFE",
        "badge_color": "bg-red-100 text-red-700 border-red-200",
        "score": "18",
        "score_offset": "216", # 18/100 score path offset
        "verdict": "Marketed as a pore-erasing miracle, this heavy silicone primer forms a suffocating, plastic-wrap film over your pores, locking in sebum, sweat, and acne-causing bacteria. It's a leading cause of severe forehead bumps and cystic acne.",
        "ingredients": [
            {
                "name": "Cyclopentasiloxane",
                "risk": "Severe Congestion Risk",
                "desc": "A volatile silicone that fills pores to create a temporary smooth texture but traps sebum and dead skin cells underneath, leading to blackheads and severe congestion."
            },
            {
                "name": "Dimethicone",
                "risk": "Occlusive Film-Former",
                "desc": "A heavy, non-biodegradable silicone that acts like a physical barrier over the skin. It prevents natural cell turnover and locks irritants inside the follicle."
            },
            {
                "name": "Phenoxyethanol",
                "risk": "Preservative Allergen",
                "desc": "A synthetic preservative known to cause skin irritation, contact dermatitis, and disrupt the delicate facial microbiome."
            }
        ],
        "metrics": {
            "Allergens": "Synthetic Fragrances & Preservatives",
            "Oily & Acne-Prone Match": "Highly Comedogenic / Congesting",
            "Safety Risk": "Severe (Silicones & Irritants)",
            "Ethics & Sourcing": "Animal testing by parent company"
        },
        "meta_desc": "Is Benefit POREfessional primer safe for acne? Exposing the toxic ingredients & severe pore-clogging risks in our brutal honest REMAKE Beauty teardown."
    },
    {
        "slug": "cerave-daily-moisturizing-lotion-breakouts",
        "brand": "CeraVe",
        "product": "Daily Moisturizing Lotion",
        "rating": "2.1/5",
        "badge": "NOT ACNE SAFE",
        "badge_color": "bg-red-100 text-red-700 border-red-200",
        "score": "21",
        "score_offset": "208",
        "verdict": "Though dermatologist-recommended for compromised barriers, its formulation contains a highly comedogenic emulsifier combination that is notorious for causing closed comedones (forehead bumps) and stubborn breakouts on acne-prone skin.",
        "ingredients": [
            {
                "name": "Polyglyceryl-3 Diisostearate",
                "risk": "Severe Comedogenic Hazard",
                "desc": "A heavy emulsifier rated 4/5 on the comedogenic scale. It is extremely clogging and forms an occlusive barrier that acne-prone skin types cannot tolerate."
            },
            {
                "name": "Cetearyl Alcohol + Ceteareth-20",
                "risk": "Synergistic Pore-Clogger",
                "desc": "While safe individually, this combined mixture has a comedogenic rating of 4/5. It triggers deep pore blockage, leading to severe cystic breakouts."
            },
            {
                "name": "Methylparaben",
                "risk": "Preservative Risk",
                "desc": "A common paraben preservative used to prolong shelf life, which can trigger sensitivities and allergic contact reactions in compromised skin."
            }
        ],
        "metrics": {
            "Allergens": "Paraben Preservatives",
            "Oily & Acne-Prone Match": "Extremely Pore-Clogging (Closed Comedones)",
            "Safety Risk": "Moderate (Emulsifier Hazards)",
            "Ethics & Sourcing": "Cruelty-free claims but owned by L'Oreal"
        },
        "meta_desc": "Why does CeraVe Daily Moisturizing Lotion cause breakouts? Read our expert skincare analysis exposing the heavy comedogenic pore cloggers in CeraVe."
    },
    {
        "slug": "charlotte-tilbury-flawless-filter-acne-safe",
        "brand": "Charlotte Tilbury",
        "product": "Hollywood Flawless Filter",
        "rating": "2.0/5",
        "badge": "NOT ACNE SAFE",
        "badge_color": "bg-red-100 text-red-700 border-red-200",
        "score": "20",
        "score_offset": "211",
        "verdict": "The viral 'Hollywood glow' is achieved using a heavy, mineral-laden formula that acts like sandpaper in your pores. It is packed with a highly irritant crystalline mineral that causes red bumps, itching, and severe acne flare-ups.",
        "ingredients": [
            {
                "name": "Bismuth Oxychloride",
                "risk": "Severe Acne Irritant",
                "desc": "A heavy synthetic pearlizing mineral. Its sharp, crystalline structure causes mechanical micro-irritation deep inside the hair follicle, resulting in severe cystic acne."
            },
            {
                "name": "Polyglyceryl-4 Isostearate",
                "risk": "Pore-Clogging Emulsifier",
                "desc": "A heavy binding agent that creates a luxurious glide but clogs pores by trapping sebum and preventing the skin's natural exfoliation."
            },
            {
                "name": "Fragrance (Parfum)",
                "risk": "High Allergen Risk",
                "desc": "Contains synthetic scent compounds that strip the skin's natural barrier, leading to immediate redness, itching, and long-term sensitivity."
            }
        ],
        "metrics": {
            "Allergens": "Synthetic Fragrance & Bismuth",
            "Oily & Acne-Prone Match": "Crystalline Irritant / High Congestion",
            "Safety Risk": "Severe (Follicular Irritation)",
            "Ethics & Sourcing": "Cruelty-free but contains synthetic petroleum-derived oils"
        },
        "meta_desc": "Is Charlotte Tilbury Hollywood Flawless Filter acne safe? The brutal honest truth about Bismuth Oxychloride and its severe pore-clogging risks."
    },
    {
        "slug": "dior-lip-glow-oil-ingredients",
        "brand": "Dior",
        "product": "Addict Lip Glow Oil",
        "rating": "2.4/5",
        "badge": "BARRIER DRYING RISK",
        "badge_color": "bg-amber-100 text-amber-700 border-amber-200",
        "score": "24",
        "score_offset": "200",
        "verdict": "Priced as a luxury elixir, this viral lip oil is actually a highly synthetic formula loaded with synthetic colors and heavy fragrances. It creates a temporary shine but strips your lips' natural barrier, causing chronic dryness.",
        "ingredients": [
            {
                "name": "Synthetic Fragrance (Parfum)",
                "risk": "Extreme Sensitizer",
                "desc": "A heavy synthetic fragrance that sensitizes the delicate lip tissue, leading to persistent peeling, dryness, and contact cheilitis."
            },
            {
                "name": "Cherry Seed Oil (Prunus Avium)",
                "risk": "Heavy Occlusive Film",
                "desc": "While marketed as the hero ingredient, it is present in tiny, trace amounts behind synthetic polymers that form a suffocating, non-hydrating film."
            },
            {
                "name": "CI 45410 (Red 27 Lake)",
                "risk": "Synthetic Dye Allergen",
                "desc": "A synthetic azo dye that can cause localized skin irritation, allergic reactions, and worsens lip cracking."
            }
        ],
        "metrics": {
            "Allergens": "Synthetic Fragrance & Azo Dyes",
            "Oily & Acne-Prone Match": "Worsens Perioral Dermatitis around lips",
            "Safety Risk": "Moderate (Sensitizers & Stripping Agents)",
            "Ethics & Sourcing": "Dior is owned by LVMH, which funds animal testing where required"
        },
        "meta_desc": "Unveiling the synthetic truths behind Dior Lip Glow Oil. Read our brutal ingredient analysis of the heavy fragrances and barrier-stripping dyes."
    },
    {
        "slug": "drunk-elephant-lala-retro-acne",
        "brand": "Drunk Elephant",
        "product": "Lala Retro Whipped Cream",
        "rating": "1.5/5",
        "badge": "NOT ACNE SAFE",
        "badge_color": "bg-red-100 text-red-700 border-red-200",
        "score": "15",
        "score_offset": "224",
        "verdict": "Advertised as the ultimate clean barrier repair cream, this thick whip is a complete nightmare for acne-prone skin. It contains one of the most comedogenic ingredients in existence, causing guaranteed congestion and deep cystic acne.",
        "ingredients": [
            {
                "name": "Isopropyl Isostearate",
                "risk": "Extreme Comedogenic Hazard (5/5)",
                "desc": "An ester with an absolute 5/5 rating on the comedogenic scale. It binds to sebum to create a thick plug inside your pores, triggering painful, deep cystic acne."
            },
            {
                "name": "Sclerocarya Birrea (Marula) Seed Oil",
                "risk": "Heavy Oleic Clogger",
                "desc": "A highly occlusive, high-oleic acid oil that is extremely comedogenic for acne-prone skin, trapping oil and P. acnes bacteria in the follicle."
            },
            {
                "name": "Phenoxyethanol",
                "risk": "Preservative Allergen",
                "desc": "A synthetic preservative known to cause contact skin irritation and weaken the skin barrier when used in heavy creams."
            }
        ],
        "metrics": {
            "Allergens": "Phenoxyethanol & Occlusive Esters",
            "Oily & Acne-Prone Match": "Severe Cystic Acne Trigger (Isopropyl Isostearate)",
            "Safety Risk": "Severe (High Comedogenic Load)",
            "Ethics & Sourcing": "Owned by Shiseido, which conducts animal testing globally"
        },
        "meta_desc": "Why Drunk Elephant Lala Retro Whipped Cream is a pore-clogging nightmare. Read the honest science behind its extreme 5/5 comedogenic rating."
    },
    {
        "slug": "elf-halo-glow-liquid-filter-acne-safe",
        "brand": "e.l.f. Cosmetics",
        "product": "Halo Glow Liquid Filter",
        "rating": "2.2/5",
        "badge": "NOT ACNE SAFE",
        "badge_color": "bg-red-100 text-red-700 border-red-200",
        "score": "22",
        "score_offset": "205",
        "verdict": "This affordable dupe delivers a beautiful, dewy glow but at a high cost to your skin. It contains bismuth oxychloride and heavy film-formers that trigger stubborn closed comedones and micro-tears inside your pores.",
        "ingredients": [
            {
                "name": "Bismuth Oxychloride",
                "risk": "Severe Follicular Irritant",
                "desc": "A heavy pearlizing mineral that causes severe irritation, itching, and red bumps. Its heavy crystals scratch the inner lining of your pores, causing breakouts."
            },
            {
                "name": "Hydrogenated Polydecene",
                "risk": "Synthetic Occlusive Film",
                "desc": "A heavy synthetic oil that behaves like mineral oil, creating a suffocating layer that prevents natural skin respiration and locks in sebum."
            },
            {
                "name": "Sodium Polyacrylate",
                "risk": "Microplastic Film-Former",
                "desc": "A synthetic polymer that acts as a film-former. It can dehydrate the skin barrier over time and trap dead skin cells inside the follicle."
            }
        ],
        "metrics": {
            "Allergens": "Bismuth Oxychloride & Synthetic Dyes",
            "Oily & Acne-Prone Match": "High Congestion & Mechanical Irritation",
            "Safety Risk": "Moderate-Severe (Pore Blockage)",
            "Ethics & Sourcing": "100% Vegan and Cruelty-Free, but utilizes synthetic microplastics"
        },
        "meta_desc": "Is e.l.f. Halo Glow Liquid Filter acne safe? Read our direct ingredient analysis exposing the bismuth oxychloride and synthetic cloggings inside."
    },
    {
        "slug": "estee-lauder-double-wear-ingredients",
        "brand": "Estée Lauder",
        "product": "Double Wear Stay-in-Place Makeup",
        "rating": "1.9/5",
        "badge": "NOT ACNE SAFE",
        "badge_color": "bg-red-100 text-red-700 border-red-200",
        "score": "19",
        "score_offset": "213",
        "verdict": "Known as the holy grail of high-coverage, long-wear foundations, its heavy formula behaves like a concrete seal over your face. It utilizes heavy silicones and chemical film-formers that trap sweat and sebum, leading to major breakouts.",
        "ingredients": [
            {
                "name": "Laureth-7",
                "risk": "High Comedogenic Surfactant",
                "desc": "An emulsifier with a high comedogenic rating. It easily penetrates the skin and disrupts the lipid barrier, leaving pores highly susceptible to clogging."
            },
            {
                "name": "Alumina",
                "risk": "Astringent Mineral Risk",
                "desc": "An aluminum oxide mineral used for oil control. It severely dries out the outer layer of skin, causing rapid dead-skin accumulation that plugs follicles."
            },
            {
                "name": "Trimethylsiloxysilicate",
                "risk": "Heavy Concrete Film-Former",
                "desc": "An ultra-strong silicone resin that gives the foundation its 'stay-in-place' wear. It acts as an absolute physical lock, trapping bacteria and sweat inside."
            }
        ],
        "metrics": {
            "Allergens": "Heavy Synthetic Surfactants",
            "Oily & Acne-Prone Match": "Extremely Congesting (Concrete Oil Lock)",
            "Safety Risk": "Severe (Acne & Dryness)",
            "Ethics & Sourcing": "Parent company tests on animals in Mainland China"
        },
        "meta_desc": "Does Estée Lauder Double Wear cause acne? Read our brutal review exposing the Laureth-7, heavy concrete film-formers, and barrier-drying hazards."
    },
    {
        "slug": "fenty-beauty-pro-filtr-acne-safe",
        "brand": "Fenty Beauty",
        "product": "Pro Filt'r Soft Matte Longwear Foundation",
        "rating": "2.2/5",
        "badge": "NOT ACNE SAFE",
        "badge_color": "bg-red-100 text-red-700 border-red-200",
        "score": "22",
        "score_offset": "205",
        "verdict": "Rihanna's iconic soft-matte foundation contains a high percentage of talc and drying denatured alcohol. It creates an instant airbrushed look but severely dehydrates the skin barrier, prompting an overproduction of sebum that causes severe acne.",
        "ingredients": [
            {
                "name": "Talc",
                "risk": "Pore-Clogging Mineral",
                "desc": "A mineral powder that absorbs sweat and oil but clumps inside the pores, forming solid comedones and causing follicular micro-inflammation."
            },
            {
                "name": "Alcohol Denat.",
                "risk": "Severe Barrier Stripper",
                "desc": "Drying alcohol used to create a rapid matte finish. It strips the skin's protective acid mantle, causing dehydration, irritation, and compensatory oil overproduction."
            },
            {
                "name": "Dimethicone",
                "risk": "Heavy Silicone Clogger",
                "desc": "A heavy silicone that forms an artificial barrier. It traps the heavy talc powder and natural oils inside the follicle, resulting in deep breakouts."
            }
        ],
        "metrics": {
            "Allergens": "Drying Alcohols & Talc",
            "Oily & Acne-Prone Match": "Dehydrated Acne / Severe Sebum Overproduction",
            "Safety Risk": "Severe (Barrier Disruption)",
            "Ethics & Sourcing": "Cruelty-free, but relies on talc mining which has ethical/purity concerns"
        },
        "meta_desc": "Is Fenty Beauty Pro Filt'r foundation acne safe? Our raw ingredient teardown of Rihanna's viral soft-matte talc & drying alcohol formulation."
    },
    {
        "slug": "glossier-cloud-paint-acne-safe",
        "brand": "Glossier",
        "product": "Cloud Paint Gel-Cream Blush",
        "rating": "2.5/5",
        "badge": "BARRIER CLOGGING RISK",
        "badge_color": "bg-amber-100 text-amber-700 border-amber-200",
        "score": "25",
        "score_offset": "198",
        "verdict": "Glossier's cult-favorite blush delivers a beautiful, natural flush. However, its gel-cream hybrid base is rich in heavy, synthetic film-formers and heavy colorants that can trigger cheek breakouts and localized irritation on sensitive skin.",
        "ingredients": [
            {
                "name": "Isododecane",
                "risk": "Synthetic Hydrocarbon",
                "desc": "A synthetic hydrocarbon solvent that gives the blush its weightless slip but acts as an aggressive barrier block, sealing pores on delicate cheek areas."
            },
            {
                "name": "PEG-10 Dimethicone",
                "risk": "Ethoxylated Silicone Clogger",
                "desc": "An ethoxylated silicone emulsifier that improves blendability but leaves a sticky residue that traps sebum and dead skin, initiating closed comedones."
            },
            {
                "name": "Synthetic Colorants (D&C Red Dyes)",
                "risk": "Acne Sensitizers",
                "desc": "Utilizes synthetic coal-tar derived dyes that are highly comedogenic and are a prime suspect for chronic cheek breakouts."
            }
        ],
        "metrics": {
            "Allergens": "Synthetic Coal-Tar Dyes",
            "Oily & Acne-Prone Match": "Cheek Breakouts / Localized Irritation",
            "Safety Risk": "Moderate (Synthetic Heavy Base)",
            "Ethics & Sourcing": "Cruelty-Free, Vegan, but uses synthetic petroleum-derived chemicals"
        },
        "meta_desc": "Is Glossier Cloud Paint blush safe for acne-prone skin? Read our detailed ingredient analysis exposing the cheek-clogging coal-tar dyes."
    },
    {
        "slug": "glow-recipe-watermelon-glow-toner-allergens",
        "brand": "Glow Recipe",
        "product": "Watermelon Glow PHA + BHA Pore-Tight Toner",
        "rating": "2.0/5",
        "badge": "HIGH ALLERGEN RISK",
        "badge_color": "bg-red-100 text-red-700 border-red-200",
        "score": "20",
        "score_offset": "211",
        "verdict": "Marketed as a gentle exfoliating toner for a 'glass skin' glow, this bright pink liquid is heavily fragranced. The synthetic scents and irritating plant extracts completely negate the benefits of PHA/BHA, damaging sensitive barriers.",
        "ingredients": [
            {
                "name": "Synthetic Fragrance (Parfum)",
                "risk": "Severe Barrier Sensitizer",
                "desc": "A high concentration of synthetic fragrance. Fragrances are the #1 cause of contact skin allergies, worsening redness, itching, and inflammatory acne."
            },
            {
                "name": "Watermelon Fruit Extract (Fragrant)",
                "risk": "Volatile Plant Extract",
                "desc": "While aesthetic, volatile fruit extracts can trigger oxidative stress and surface irritation when exposed to air and light on sensitive skin."
            },
            {
                "name": "Polysorbate 20",
                "risk": "Fungal Acne Trigger",
                "desc": "An ethoxylated emulsifier that serves as a direct food source for Malassezia yeast, triggering or worsening fungal acne (pityrosporum folliculitis)."
            }
        ],
        "metrics": {
            "Allergens": "Heavy Perfume & Fungal Acne Feeders",
            "Oily & Acne-Prone Match": "Fungal Acne Trigger / Rosacea Irritant",
            "Safety Risk": "High (Severe Contact Allergen Potential)",
            "Ethics & Sourcing": "Cruelty-Free, Vegan, but heavily relies on synthetic colors & perfumes"
        },
        "meta_desc": "Is Glow Recipe Watermelon Glow Toner actually safe? Read our expert review revealing the severe allergen fragrance risks and fungal acne triggers."
    },
    {
        "slug": "huda-beauty-easy-bake-powder-toxic",
        "brand": "Huda Beauty",
        "product": "Easy Bake Loose Baking & Setting Powder",
        "rating": "1.7/5",
        "badge": "HIGH TOXICITY RISK",
        "badge_color": "bg-red-100 text-red-700 border-red-200",
        "score": "17",
        "score_offset": "219",
        "verdict": "Famous for its airbrushed 'baked' finish, this powder is a toxic chemical cocktail for your lungs and skin barrier. It contains talc and an extreme load of synthetic perfume that suffocates the skin and triggers severe allergic contact dermatitis.",
        "ingredients": [
            {
                "name": "Talc",
                "risk": "Follicular Clogger & Inhalation Risk",
                "desc": "Talc acts like physical tiny plugs inside your pores, trapping sebum. Additionally, loose talc powder is a severe inhalation hazard that damages lung tissues."
            },
            {
                "name": "Extreme Fragrance (Parfum)",
                "risk": "Contact Allergen & Stripping Agent",
                "desc": "Contains an overwhelmingly high percentage of fragrance. It is a highly potent allergen that strips skin moisture, resulting in cracking and redness."
            },
            {
                "name": "Aluminum Starch Octenylsuccinate",
                "risk": "Drying Synthetic Clogger",
                "desc": "An aluminum-derived starch used to absorb oil. It severely dehydrates the outer epidermis, leading to a build-up of dead skin that clogs pores."
            }
        ],
        "metrics": {
            "Allergens": "Extreme Synthetic Perfume & Talc",
            "Oily & Acne-Prone Match": "Aggressive Dehydration / Follicular Plugs",
            "Safety Risk": "Severe (Lungs & Skin Irritant)",
            "Ethics & Sourcing": "Cruelty-Free, but talc sourcing carries asbestos-contamination risks"
        },
        "meta_desc": "Why Huda Beauty Easy Bake powder is a toxic nightmare for your skin and lungs. Read the honest chemical analysis of its talc and perfume content."
    },
    {
        "slug": "kosas-revealer-concealer-mold",
        "brand": "Kosas",
        "product": "Revealer Super Creamy + Brightening Concealer",
        "rating": "2.3/5",
        "badge": "MOLD & BACTERIA RISK",
        "badge_color": "bg-red-100 text-red-700 border-red-200",
        "score": "23",
        "score_offset": "203",
        "verdict": "This clean-beauty concealer is packed with heavy, acne-triggering oils and lacks robust synthetic preservatives. Within months, it turns into a breeding ground for mold and bacteria, causing severe follicular infections on compromised skin.",
        "ingredients": [
            {
                "name": "Lack of Parabens/Phenoxyethanol",
                "risk": "Severe Microbial Spoilage",
                "desc": "By using weak 'clean' preservatives, this formula is highly susceptible to rapid contamination, introducing live mold and bacteria to your face."
            },
            {
                "name": "Arnica Montana Flower Extract",
                "risk": "Heavy Sensitizing Herb",
                "desc": "An herbal extract that can trigger severe allergic contact dermatitis and skin blistering when used repeatedly on sensitive eye areas."
            },
            {
                "name": "Cocos Nucifera (Coconut) Oil Derivative",
                "risk": "Comedogenic Fatty Acid",
                "desc": "Contains coconut-derived fatty acids that provide a rich texture but act as a high-risk comedogenic fuel for acne-prone skin."
            }
        ],
        "metrics": {
            "Allergens": "Mold/Bacterial Spoilage & Herbal Sensitizers",
            "Oily & Acne-Prone Match": "Fungal Infections & Severe Eye Area Bumps",
            "Safety Risk": "Severe (Microbial Contamination Potential)",
            "Ethics & Sourcing": "Leaps the 'clean beauty' trend but fails basic preservation science"
        },
        "meta_desc": "The shocking truth about Kosas Revealer Concealer mold and bacterial risks. Read our expert skincare analysis exposing the weak preservation system."
    },
    {
        "slug": "laneige-lip-sleeping-mask-toxic-ingredients",
        "brand": "Laneige",
        "product": "Lip Sleeping Mask",
        "rating": "1.9/5",
        "badge": "BARRIER STRIPPING RISK",
        "badge_color": "bg-red-100 text-red-700 border-red-200",
        "score": "19",
        "score_offset": "213",
        "verdict": "This cult lip mask offers an instant glossy look, but its formula is highly synthetic and stripped of real nourishing lipids. It relies on synthetic petroleum waxes and heavy artificial fragrances that dehydrate your lips over time, creating a severe addiction loop.",
        "ingredients": [
            {
                "name": "Synthetic Fragrance & Flavor",
                "risk": "Severe Cheilitis Trigger",
                "desc": "The heavy synthetic fruit scents and flavor agents are known allergens that dry out lip tissue, resulting in chronic peeling, scaling, and splitting."
            },
            {
                "name": "Diisostearyl Malate",
                "risk": "Synthetic Binding Wax",
                "desc": "A heavy synthetic ester that acts as a thick binder. It forms an artificial plastic seal over lips, preventing natural exfoliation and self-hydration."
            },
            {
                "name": "Synthetic Colorants (Azo Dyes)",
                "risk": "Allergen Hazard",
                "desc": "Packed with petroleum-derived azo dyes (such as Red 6 and Yellow 10) that can trigger contact sensitivities on thin lip skin."
            }
        ],
        "metrics": {
            "Allergens": "Azo Dyes & Artificial Scent/Flavor",
            "Oily & Acne-Prone Match": "Causes stubborn clogged pores and blackheads around lip border",
            "Safety Risk": "Severe (Chronic Lip Dehydration Loop)",
            "Ethics & Sourcing": "Laneige belongs to Amorepacific, which conducts animal testing"
        },
        "meta_desc": "Is Laneige Lip Sleeping Mask actually toxic? Read our raw review exposing the heavy synthetic fragrances, waxes, and chronic lip drying azo dyes."
    },
    {
        "slug": "mac-studio-fix-fluid-toxic",
        "brand": "MAC Cosmetics",
        "product": "Studio Fix Fluid SPF 15 Foundation",
        "rating": "1.6/5",
        "badge": "NOT ACNE SAFE",
        "badge_color": "bg-red-100 text-red-700 border-red-200",
        "score": "16",
        "score_offset": "221",
        "verdict": "An industry classic for studio photography, this heavy foundation is a disaster for daily wear. It relies on toxic chemical sunscreen filters and heavy, high-risk comedogenic emulsifiers that lead to severe, painful cystic acne.",
        "ingredients": [
            {
                "name": "Octinoxate (Ethylhexyl Methoxycinnamate)",
                "risk": "Hormone Disruptor & Skin Irritant",
                "desc": "A chemical UV filter that is highly unstable. It absorbs UV light and converts it to heat energy on your face, causing inflammation and breaking out acne."
            },
            {
                "name": "PEG-10 Dimethicone",
                "risk": "Pore-Clogging Emulsifier",
                "desc": "An ethoxylated silicone emulsifier that bonds with sweat and dead skin to create a highly congestive paste deep inside your pores."
            },
            {
                "name": "Silica & Talc Combo",
                "risk": "Heavy Follicular Plug",
                "desc": "Heavy mineral powders that absorb sebum but solidify inside the hair follicle, creating deep, stubborn blackheads and blind cystic bumps."
            }
        ],
        "metrics": {
            "Allergens": "Chemical Sunscreen Filters & Talc",
            "Oily & Acne-Prone Match": "Guaranteed Cystic Acne / Red Inflammatory Bumps",
            "Safety Risk": "Severe (Hormonal & Follicular Disruptor)",
            "Ethics & Sourcing": "Owned by Estée Lauder; participates in animal testing globally"
        },
        "meta_desc": "Does MAC Studio Fix Fluid foundation cause breakouts? Read our brutal chemical teardown exposing the Octinoxate, talc, and pore-clogging emulsifiers."
    },
    {
        "slug": "maybelline-fit-me-matte-poreless-ingredients",
        "brand": "Maybelline",
        "product": "Fit Me Matte + Poreless Foundation",
        "rating": "2.1/5",
        "badge": "BARRIER STRIPPING RISK",
        "badge_color": "bg-red-100 text-red-700 border-red-200",
        "score": "21",
        "score_offset": "208",
        "verdict": "This affordable drug-store favorite achieves its matte claim by completely stripping your skin. It contains a high concentration of harsh denatured alcohol and cheap heavy silicates that dry out your barrier, triggering an oil slick that blocks pores.",
        "ingredients": [
            {
                "name": "Alcohol Denat.",
                "risk": "Severe Barrier Stripper",
                "desc": "Aggressive drying alcohol. It strips the skin's essential lipids, destroying the moisture barrier and causing extreme rebound oiliness and breakouts."
            },
            {
                "name": "Cetyl PEG/PPG-10/1 Dimethicone",
                "risk": "Heavy Synthetic Emulsifier",
                "desc": "A cheap ethoxylated silicone emulsifier. It forms a dense, plastic-like wrap that traps skin toxins, sebum, and dead skin cells in the follicle."
            },
            {
                "name": "Phenoxyethanol",
                "risk": "Preservative Sensitizer",
                "desc": "A synthetic preservative that can trigger localized rashes, contact allergies, and severely weakens the skin's natural defense system."
            }
        ],
        "metrics": {
            "Allergens": "Harsh Denatured Alcohol & Sensitizers",
            "Oily & Acne-Prone Match": "Drying Dehydration / Severe Rebound Oil Production",
            "Safety Risk": "Moderate-Severe (Barrier Destruction)",
            "Ethics & Sourcing": "Owned by L'Oreal; animal testing occurs in global markets"
        },
        "meta_desc": "Why Maybelline Fit Me Matte + Poreless foundation is stripping your skin barrier. Read our brutal ingredient analysis of denatured alcohol and cheap silicones."
    },
    {
        "slug": "saie-slip-tint-acne-safe",
        "brand": "Saie",
        "product": "Slip Tint Dewy Tinted Moisturizer",
        "rating": "1.7/5",
        "badge": "NOT ACNE SAFE",
        "badge_color": "bg-red-100 text-red-700 border-red-200",
        "score": "17",
        "score_offset": "219",
        "verdict": "Marketed as a clean, dewy tinted moisturizer that supports skin health, this formula is an absolute nightmare for anyone prone to breakouts. It utilizes a highly comedogenic lipid base that acts like pure lard inside your pores.",
        "ingredients": [
            {
                "name": "Coconut Alkanes",
                "risk": "Extreme Comedogenic Hazard (4/5)",
                "desc": "A coconut-derived hydrocarbon that behaves exactly like raw coconut oil in your pores. Rated 4/5 on the comedogenic scale; guaranteed to trigger deep breakouts."
            },
            {
                "name": "Coco-Caprylate/Caprate",
                "risk": "Aggressive Acne Fuel",
                "desc": "An ester derivative that provides a dewy slip but severely clogs the hair follicle, feeding acne-causing bacteria and causing closed comedones."
            },
            {
                "name": "Heavy Seed Oils (Grapeseed/Sunflower)",
                "risk": "Lipid Overload",
                "desc": "High concentration of plant lipids that overwhelm oily and combination skin types, causing a heavy suffocating film and severe forehead bumps."
            }
        ],
        "metrics": {
            "Allergens": "Coconut Derivatives & Heavy Seed Oils",
            "Oily & Acne-Prone Match": "Guaranteed closed comedones & cystic cheek acne",
            "Safety Risk": "Severe (Pure Pore Cloggers)",
            "Ethics & Sourcing": "Cruelty-Free, clean marketing, but relies on heavy pore-clogging lipids"
        },
        "meta_desc": "Is Saie Slip Tint dewy tinted moisturizer acne safe? The shocking honest truth about Coconut Alkanes and extreme pore-clogging esters in Saie."
    },
    {
        "slug": "sol-de-janeiro-bum-bum-cream-toxic",
        "brand": "Sol de Janeiro",
        "product": "Brazilian Bum Bum Cream",
        "rating": "1.8/5",
        "badge": "HIGH ALLERGEN RISK",
        "badge_color": "bg-red-100 text-red-700 border-red-200",
        "score": "18",
        "score_offset": "216",
        "verdict": "This cult-favorite body cream smells like a tropical heaven, but chemically, it is an aggressive allergen assault. It is packed with synthetic fragrances and contact allergens that cause rashes, redness, and body acne on sensitive skin.",
        "ingredients": [
            {
                "name": "Heavy Fragrance (Parfum)",
                "risk": "Severe Contact Sensitizer",
                "desc": "Scent is the main hook of this product, meaning it contains a massive, toxic load of synthetic perfume that irritates the skin and triggers dermatitis."
            },
            {
                "name": "Benzyl Alcohol & Benzyl Salicylate",
                "risk": "High-Risk Allergen Preservative/Fragrance",
                "desc": "EU-declared fragrance allergens that irritate the respiratory system and cause allergic contact rashes on thin skin."
            },
            {
                "name": "Cocos Nucifera (Coconut) Oil",
                "risk": "Extreme Comedogenic Block (4/5)",
                "desc": "Raw coconut oil has a massive 4/5 pore-clogging rating. It forms a thick, solid block in your skin follicles, leading to severe chest, shoulder, and back acne."
            }
        ],
        "metrics": {
            "Allergens": "Benzyl Alcohol, Benzyl Salicylate & Extreme Perfume",
            "Oily & Acne-Prone Match": "Triggers painful chest and back acne (pure coconut oil block)",
            "Safety Risk": "Severe (High Allergenic & Comedogenic Index)",
            "Ethics & Sourcing": "Owned by L'Occitane, which has complex global sourcing practices"
        },
        "meta_desc": "Why Sol de Janeiro Bum Bum Cream is a major allergen risk & cause of body acne. Exposing the heavy perfume, benzyl alcohol, and raw coconut oil."
    },
    {
        "slug": "supergoop-unseen-sunscreen-toxic-filters",
        "brand": "Supergoop!",
        "product": "Unseen Sunscreen SPF 40",
        "rating": "2.0/5",
        "badge": "NOT ACNE SAFE",
        "badge_color": "bg-red-100 text-red-700 border-red-200",
        "score": "20",
        "score_offset": "211",
        "verdict": "This viral 'invisible' primer-sunscreen has a weightless dewy texture but is loaded with toxic chemical UV filters and heavy, suffocating silicones. It absorbs UV rays and converts them into heat directly on your face, causing severe inflammation and breakouts.",
        "ingredients": [
            {
                "name": "Chemical Filters (Avobenzone/Homosalate/Octisalate/Octocrylene)",
                "risk": "Hormone Disruptor & Severe Irritant",
                "desc": "Chemical sunscreens absorb into the bloodstream, disrupting hormones. They release cellular heat on your face, causing immediate redness and inflammatory breakouts."
            },
            {
                "name": "Isododecane + Dimethicone Crosspolymer",
                "risk": "Suffocating Silicone Wrap",
                "desc": "A heavy combination of synthetic silicones that wraps the face like plastic cling wrap, trapping sweat, sebum, and chemical irritants inside the pore."
            },
            {
                "name": "Phenoxyethanol",
                "risk": "Preservative Sensitizer",
                "desc": "A common synthetic preservative known to cause skin irritation, immediate stinging, and contact allergies in compromised barriers."
            }
        ],
        "metrics": {
            "Allergens": "Chemical Sunscreen Active Filters",
            "Oily & Acne-Prone Match": "Traps heat & chemicals, triggering massive inflammatory acne",
            "Safety Risk": "Severe (Hormonal & Inflammatory Hazards)",
            "Ethics & Sourcing": "Cruelty-Free, Vegan, but releases toxic chemical filters into ocean coral reefs"
        },
        "meta_desc": "Is Supergoop Unseen Sunscreen safe for acne? Exposing the toxic chemical UV filters, hormone disruptors, and suffocating silicones inside Supergoop."
    }
]

html_template = """<!DOCTYPE html>  
<html lang="en">  
<head>  
  <meta charset="UTF-8" />  
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />  
  <meta name="theme-color" content="#2A2421" />  
  <link rel="canonical" href="https://remake.beauty/products/{slug}.html" />  
  <meta name="description" content="{meta_desc}">  
  <title>{brand} {product} Ingredients & Safety Analysis • REMAKE Beauty</title>  
  <meta name="keywords" content="makeup, cosmetic chemistry, skincare scanner, comedogenic checker, toxic ingredients makeup, acne safe makeup, shade matching app, remake app, skincare barcode scanner, pore clogging ingredient checker, {brand}, {product}">  
  <meta name="author" content="REMAKE Beauty">  
  <meta property="og:title" content="{brand} {product} Ingredients & Safety Analysis • REMAKE Beauty">  
  <meta property="og:description" content="{verdict}">  
  <meta property="og:image" content="https://remake.beauty/logo.png">  
  <meta property="og:url" content="https://remake.beauty/products/{slug}.html">  
  <meta property="og:type" content="article">  
  <meta name="twitter:card" content="summary_large_image">  
  <meta name="twitter:title" content="{brand} {product} Ingredients & Safety Analysis • REMAKE Beauty">  
  <meta name="twitter:description" content="{verdict}">  
  <meta name="twitter:image" content="https://remake.beauty/logo.png">  
  
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Product",
    "name": "{brand} {product}",
    "image": "https://remake.beauty/logo.png",
    "description": "{verdict}",
    "brand": {{
      "@type": "Brand",
      "name": "{brand}"
    }},
    "offers": {{
      "@type": "AggregateOffer",
      "priceCurrency": "USD",
      "lowPrice": "0",
      "highPrice": "0",
      "offerCount": "0"
    }},
    "aggregateRating": {{
      "@type": "AggregateRating",
      "ratingValue": "{rating_num}",
      "bestRating": "5",
      "worstRating": "1",
      "ratingCount": "128"
    }}
  }}
  </script>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebPage",
    "name": "{brand} {product} Ingredients & Safety Analysis • REMAKE Beauty",
    "description": "{meta_desc}",
    "url": "https://remake.beauty/products/{slug}.html",
    "publisher": {{
      "@type": "Organization",
      "name": "REMAKE Labs",
      "alternateName": "REMAKE Beauty",
      "url": "https://remake.beauty",
      "logo": "https://remake.beauty/logo.png"
    }}
  }}
  </script>

  <link rel="icon" href="../favicon.png" type="image/png">  
  <link rel="apple-touch-icon" href="../apple-touch-icon.png">    
  <link rel="stylesheet" href="../styles.css">  
  <link rel="preconnect" href="https://fonts.googleapis.com">  
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>  
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400;1,500&family=Inter:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">  
  
  <style>  
    :root {{  
      --rhode-text: #2A2421;  
      --rhode-white: #FFF0F3;  
      --rhode-ivory: #FFEBEF;  
      --rhode-cream: #FFF0F3;  
      --rhode-beige: #FCE4EC;  
      --rhode-blush: #FCE4EC;  
      --rhode-pink: #FDA8BD;  
      --rhode-pink-mid: #F0B8C0;  
      --rhode-pink-deep: #E8A0AA;  
      --rhode-pink-rich: #D98A96;  
      --rhode-gold: #D4AF37;  
      --rhode-gold-soft: #E6C88A;  
      --rhode-gold-dark: #B8943E;  
      --rhode-border: #F5DDE3;  
      --rhode-gray: #7C726E;  
      --rhode-light-gray: #B8ADA9;  
      --rhode-success: #6E8E75;  
      --rhode-error: #C96F6F;  
        
      --radius-soft: 20px;  
      --radius-pill: 100px;  
      --glaze-gradient: linear-gradient(135deg, rgba(255,255,255,0.7) 0%, rgba(253,240,236,0.4) 50%, rgba(253,168,189,0.1) 100%);  
      --card-shadow: 0 10px 30px rgba(42,36,33,0.03), 0 1px 3px rgba(217,138,150,0.05);  
      --hover-shadow: 0 20px 40px rgba(42,36,33,0.06), 0 4px 15px rgba(217,138,150,0.12);  
    }}  
    
    * {{ 
      -webkit-font-smoothing: antialiased; 
      -moz-osx-font-smoothing: grayscale; 
      box-sizing: border-box; 
      scrollbar-width: none !important; 
      -ms-overflow-style: none !important; 
    }}  
    
    ::-webkit-scrollbar {{
      display: none !important;
    }}
    
    html {{
      background: #2A2421;
    }}
    
    body {{   
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;   
      background: var(--rhode-white); color: var(--rhode-text);  
      line-height: 1.8; font-weight: 400;  
    }}  
    
    .font-serif {{ font-family: 'Playfair Display', serif; }}  
    .font-luxury {{ font-family: 'Cormorant Garamond', serif; }}  
    .font-light {{ font-weight: 300; }}  
      
    body::before {{  
      content: ""; position: fixed; top: 0; left: 0; width: 100%; height: 100%;  
      background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.75' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='0.02'/%3E%3C/svg%3E");  
      pointer-events: none; z-index: 100;  
    }}  
      
    .btn-primary {{  
      position: relative; overflow: hidden;  
      transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);  
      font-family: 'Inter', sans-serif; font-weight: 500;  
      letter-spacing: 0.15em; text-transform: uppercase; font-size: 0.7rem;  
      display: inline-flex; align-items: center; justify-content: center; gap: 0.6rem;  
      cursor: pointer; border-radius: var(--radius-pill);  
      background: var(--rhode-text);   
      color: var(--rhode-white);   
      border: 1px solid var(--rhode-text);   
      padding: 0.85rem 1.8rem;  
      box-shadow: 0 4px 15px rgba(42,36,33,0.1);  
    }}  
    .btn-primary:hover {{   
      background: var(--rhode-pink-rich);   
      border-color: var(--rhode-pink-rich);   
      color: var(--rhode-white);  
      transform: translateY(-2px);   
      box-shadow: 0 8px 25px rgba(217,138,150,0.3);   
    }}  
    
    .card-luxury {{  
      border: 1px solid rgba(245,221,227,0.7); background: rgba(255,253,252,0.75);  
      backdrop-filter: blur(20px); transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);  
      position: relative; overflow: hidden; border-radius: var(--radius-soft);  
      box-shadow: var(--card-shadow);  
    }}  
    .card-luxury:hover {{  
      transform: translateY(-4px); box-shadow: var(--hover-shadow);  
      border-color: var(--rhode-pink);  
    }}  
    
    .badge-luxury {{  
      display: inline-flex; align-items: center;  
      padding: 0.35rem 1rem; border-radius: var(--radius-pill);  
      font-size: 0.55rem; font-weight: 600; letter-spacing: 0.2em;  
      text-transform: uppercase; background: var(--rhode-beige);  
      color: var(--rhode-pink-rich); border: 1px solid rgba(217,138,150,0.2);  
    }}  
  </style>  
</head>  
<body class="min-h-screen flex flex-col justify-between">  
  
  <!-- Premium Editorial Sticky Header -->  
  <header class="sticky top-0 z-50 w-full bg-[#FFF0F3]/80 backdrop-blur-md border-b border-[#F5DDE3] transition-all duration-300">  
    <div class="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">  
      <!-- Typographic Text Logo only -->  
      <a href="https://remake.beauty" class="flex items-center gap-3 group">  
        <span class="font-luxury font-light text-2xl md:text-3xl tracking-widest text-[#2A2421] transition group-hover:text-pink-rich uppercase select-none">REMAKE</span>  
      </a>  
      
      <div>  
        <a href="https://remake.beauty/#join" class="btn-primary">Claim Spot</a>  
      </div>  
    </div>  
  </header>  

  <main class="flex-1 py-12 px-6">  
    <div class="max-w-4xl mx-auto">  
      <!-- Back Link -->  
      <a href="https://remake.beauty/" class="inline-flex items-center text-xs text-[#7C726E] hover:text-[#D98A96] transition mb-8 group">  
        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-2 transform group-hover:-translate-x-1 transition" fill="none" viewBox="0 0 24 24" stroke="currentColor">  
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />  
        </svg>  
        Back to REMAKE Beauty  
      </a>  

      <!-- Hero Teardown Title -->  
      <div class="text-center md:text-left mb-12">  
        <span class="badge-luxury mb-4">PRODUCT TEARDOWN</span>  
        <h1 class="font-serif text-3xl md:text-5xl text-[#2A2421] leading-tight mb-4">  
          Is {brand} {product} Safe for Your Skin?  
        </h1>  
        <p class="text-base text-[#7C726E] font-light max-w-2xl leading-relaxed">  
          A brutally honest, science-backed cosmetic chemistry audit on the viral formula. We check comedogenic ratings, skin irritants, and barrier-disruptive chemical traps.  
        </p>  
      </div>  

      <!-- Main Layout Grid -->  
      <div class="grid grid-cols-1 md:grid-cols-12 gap-8">  
        
        <!-- Left: Static Score Ring Display -->  
        <div class="md:col-span-5 flex flex-col items-center">  
          <div class="card-luxury p-8 w-full flex flex-col items-center text-center">  
            <div class="relative w-44 h-44 flex items-center justify-center mb-6">  
              <svg class="w-full h-full" viewBox="0 0 100 100">  
                <circle cx="50" cy="50" r="42" fill="none" stroke="#F5DDE3" stroke-width="5"/>  
                <circle cx="50" cy="50" r="42" fill="none" stroke="#D98A96" stroke-width="6" stroke-linecap="round" stroke-dasharray="264" stroke-dashoffset="{score_offset}"/>  
              </svg>  
              <div class="absolute inset-0 flex flex-col items-center justify-center">  
                <div class="font-sans font-bold text-6xl text-[#2A2421] tracking-tight mt-2">{score}</div>  
                <div class="text-[10px] uppercase tracking-widest text-[#7C726E] font-medium -mt-1">score</div>  
              </div>  
            </div>  
            
            <div class="px-4 py-1.5 rounded-full border text-[10px] uppercase tracking-widest font-bold {badge_color}">{badge}</div>  
            <div class="text-xs text-[#7C726E] mt-4 font-light">Rating: {rating}</div>  
          </div>  

          <!-- CTA Banner -->  
          <div class="card-luxury p-6 w-full mt-6 bg-[#2A2421] border-none text-white text-center">  
            <h4 class="font-serif text-xl mb-2 text-pink-100">Stop Clogging Your Pores</h4>  
            <p class="text-xs text-white/80 font-light leading-relaxed mb-6">  
              Our iOS scanner detects toxic chemicals, matches shades with 100% precision, and saves your skin barrier.  
            </p>  
            <a href="https://remake.beauty/#join" class="btn-primary w-full bg-white text-[#2A2421] border-white hover:bg-pink-100 hover:text-[#2A2421]">Join Free Waitlist</a>  
          </div>  
        </div>  

        <!-- Right: Diagnostic Details & Chemical Breakdown -->  
        <div class="md:col-span-7 space-y-6">  
          <!-- Verdict Card -->  
          <div class="card-luxury p-6 bg-white/70">  
            <h3 class="font-serif text-lg text-[#2A2421] mb-3">The Brutally Honest Verdict</h3>  
            <p class="text-sm text-[#7C726E] font-light leading-relaxed">  
              {verdict}  
            </p>  
          </div>  

          <!-- Key Ingredients Analysis -->  
          <div class="card-luxury p-6 bg-white/70">  
            <h3 class="font-serif text-lg text-[#2A2421] mb-4">Toxic / Comedogenic Ingredients Flagged</h3>  
            <div class="space-y-6">  
              {ingredients_html}  
            </div>  
          </div>  

          <!-- Bio-Chemical Specifications -->  
          <div class="card-luxury p-6 bg-white/70">  
            <h3 class="font-serif text-lg text-[#2A2421] mb-4">Detailed Bio-Chemical Specifications</h3>  
            <div class="space-y-3 text-xs">  
              {specs_html}  
            </div>  
          </div>  
        </div>  

      </div>  
    </div>  
  </main>  

  <!-- Elegant Footer -->  
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

def generate_pages():
    os.makedirs("/Users/kyzl/remake-waitlist-app/products", exist_ok=True)
    
    for p in products_data:
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
        
        # Build ingredients HTML
        ing_items = []
        for ing in p["ingredients"]:
            ing_html = f'''<div class="border-l-2 border-red-300 pl-4 py-1">
                <div class="flex justify-between items-start">
                  <span class="font-semibold text-sm text-[#2A2421]">{ing["name"]}</span>
                  <span class="text-[10px] text-red-600 bg-red-50 border border-red-200 px-2 py-0.5 rounded-full font-bold uppercase tracking-wider">{ing["risk"]}</span>
                </div>
                <p class="text-xs text-[#7C726E] font-light mt-1 leading-relaxed">{ing["desc"]}</p>
              </div>'''
            ing_items.append(ing_html)
        ingredients_html = "\\n              ".join(ing_items)
        
        # Build specs HTML
        spec_items = []
        for label, val in p["metrics"].items():
            spec_html = f'''<div class="flex justify-between items-center py-2 border-b border-[#F5DDE3]/50">
                <span class="text-[#7C726E]">{label}:</span>
                <span class="font-medium text-[#2A2421]">{val}</span>
              </div>'''
            spec_items.append(spec_html)
        specs_html = "\\n              ".join(spec_items)
        
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
        
        path = f"/Users/kyzl/remake-waitlist-app/products/{slug}.html"
        with open(path, "w") as f:
            f.write(final_html)
        print(f"Generated: {path}")

if __name__ == "__main__":
    generate_pages()
