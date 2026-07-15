# ReMake Waitlist Website Redesign Plan

> **For Hermes:** Execute this plan to transform the waitlist landing page from "AI slop" into a world-class premium beauty-tech experience.

**Goal:** Clean up and elevate `index.html` on the `remake-waitlist-app` repository by refining copy, polishing typography, replacing standard/generic emojis with custom, high-end CSS/HTML visual tags, and removing scientific or marketing jargon that ruins consumer trust.

**Architecture:** Single-page frontend modifications utilizing the existing custom Tailwind-based luxury design palette, with a heavy focus on pixel-perfect details, visual balance, and professional de-influencing copywriting.

**Tech Stack:** HTML5, CSS3, Tailwind CSS, Vanilla JS.

---

### Task 1: Clean Up Hero Section Copy and Badges
**Objective:** Replace the tacky AI-generated hero titles and subtitles with sleek, high-end equivalents. Eliminate the dollar discount references and cheesy counter phrases.

- **Files:**
  - Modify: `/Users/kyzl/remake-waitlist-app/index.html` (around lines 358-417)
- **Changes:**
  - Update top banner to: `STOP BREAKING OUT. JOIN THE ACNE-SAFE REVOLUTION TODAY.`
  - Change hero heading `REMAKE. stopping the pore-clogging slop.` to:
    `REMAKE.<br><span class="font-luxury text-elegant text-pink-solid">your skin's digital gatekeeper.</span>`
  - Change input placeholder `"Your premium email address"` to `"Email address"`.
  - Rewrite live counter line:
    `Limited Beta Program: Join <span class="font-semibold text-[#D98A96]" id="liveCounter">1,247</span> smart shoppers. First 200 get $20 off.`
    to:
    `Join <span class="font-semibold text-[#D98A96]" id="liveCounter">1,247</span> members protecting their skin barrier.`
  - Replace the crude star rating text `★★★★★` with clean text: `5.0 Rating` or beautiful CSS styled stars.

---

### Task 2: Remove AI-Slop Emojis in Product Comparisons & Modals
**Objective:** Eliminate emojis from the page and replace them with high-end designer visual accents, like glowing colored dots or clean custom inline pills.

- **Files:**
  - Modify: `/Users/kyzl/remake-waitlist-app/index.html` (around lines 630-730 and 1330-1350)
- **Changes:**
  - Replace `❌ NOT ACNE SAFE` with:
    ```html
    <span class="inline-flex items-center gap-1.5 text-[9px] text-[#C96F6F] font-bold uppercase tracking-widest mb-1">
      <span class="w-1.5 h-1.5 rounded-full bg-[#C96F6F] animate-pulse"></span>NOT ACNE SAFE
    </span>
    ```
  - Replace `✓ 100% ACNE SAFE` with:
    ```html
    <span class="inline-flex items-center gap-1.5 text-[9px] text-[#6E8E75] font-bold uppercase tracking-widest mb-1">
      <span class="w-1.5 h-1.5 rounded-full bg-[#6E8E75]"></span>100% ACNE SAFE
    </span>
    ```
  - Remove `✓` and `⚠` in the JavaScript-generated and static verdicts. Make the bold word `Verdict:` clean and modern.
  - In JS `analyzeIngredients` (around lines 1330-1355), replace `Acne-safe Bestie!` or emojis with:
    `0 Pore-Cloggers Detected. Clean formulation.`

---

### Task 3: Simplify and Polish the Beauty DNA & FAQ Copy
**Objective:** Replace academic and scientific jargon in FAQs and descriptions with clear, straightforward consumer-focused value copy.

- **Files:**
  - Modify: `/Users/kyzl/remake-waitlist-app/index.html` (around lines 730-880)
- **Changes:**
  - Change the header subtitle from `your customized aesthetic profile.` to `Your personalized aesthetic profile.`
  - In FAQ answer for shade matching (around line 867), replace:
    `We use advanced color science (ΔE calculations) combined with high-contrast, lighting-compensated neural analysis...`
    with:
    `We use advanced spectral color analysis to isolate and identify your exact skin tone from a single photo, calibrating for ambient lighting automatically.`
  - Clean up formatting of the modal breakdown list (removing stars, extra checkmarks, or indicators that make it look busy).

---

### Task 4: Verify and Build
**Objective:** Open the updated landing page in the browser tool, ensure all scripts work perfectly, and verify that the layout displays flawless typography and cohesive spacing.

- **Step 1:** Run browser checks.
- **Step 2:** Ensure no syntax errors or script breaking.
- **Step 3:** Commit and push the final polished page to GitHub.
