# KindBites
> Our Slogan: Don't waste it, KindBite it 😉

## Inspiration
Every year in the U.S.,**millions of pounds** of perfectly edible food go to waste—**84.3%** of unused restaurant food is discarded, while just **1.4% is donated**. At the same time, food insecurity affects millions of families. Our team was inspired to **bridge this gap**. 

With **KindBites**, we set out to build a smart, accessible solution that empowers restaurants to donate food with confidence, connects those in need to local supplies, and improves food sustainability.

## What it does
**KindBites** is a web platform that connects restaurants with surplus food to individuals and food shelters in need. Here's how it works:

1. Restaurants upload/take pictures of their available produce.
2. A computer vision (CV) model using HuggingFace API scans the food image to assess freshness and safety, preventing spoiled or unsafe food from entering the system.
3. Verified listings are then posted on a marketplace, where users can browse, claim, and arrange pickups of available food.

This ensures trust, accountability, and simplicity for both donors and recipients. 

## How we built it
**KindBites** consists of 3 core components:
- **Marketplace**: A central hub where restaurants post verified food items and users can browse and claim donations.
- **Educational Articles**: A learning space that helps users recognize signs of food spoilage and understand safe food handling.
- **RAG Chatbot**: A retrieval-augmented generation chatbot that answers real-time questions about food safety and sustainability tips using a custom MongoDB knowledge base.

We combined HuggingFace and Streamlit for CV modeling, and a RAG-based NLP framework to make the experience interactive and intelligent.

## Challenges we ran into
- **Equity and Accessibility**: Designing for users with lower digital literacy or language barriers required us to think critically about how to make KindBites inclusive and usable for all.

## Accomplishments that we're proud of
- Built a **dual-access platform** that serves both donors (restaurants) and recipients (individuals and shelters), making food redistribution more accessible.
- Integrated a **real-time CV model** to verify food safety—building trust and ensuring quality for all users.
- Designed an **educational ecosystem** through articles and an AI-powered chatbot to raise awareness about food sustainability and empower everyday action.

## What's next for KindBites
To increase accessibility and scale our impact, we would like to:
- Add **GPS-based navigation**, helping users find the nearest pickup locations quickly and efficiently.
- **Gamify** sustainability actions, rewarding users who regularly donate or collect food.
- Introduce freshness and location filters to enhance the food browsing experience.