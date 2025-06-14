
import random
import re

class CryptoBuddy:
    def __init__(self):
        self.name = "CryptoBuddy"
        self.crypto_db = {
            "Bitcoin": {
                "price_trend": "rising",
                "market_cap": "high",
                "energy_use": "high",
                "sustainability_score": 3/10
            },
            "Ethereum": {
                "price_trend": "stable",
                "market_cap": "high",
                "energy_use": "medium",
                "sustainability_score": 6/10
            },
            "Cardano": {
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 8/10
            },
            "Solana": {
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 7/10
            },
            "Polygon": {
                "price_trend": "stable",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 8/10
            },
            "Dogecoin": {
                "price_trend": "volatile",
                "market_cap": "medium",
                "energy_use": "high",
                "sustainability_score": 4/10
            }
        }
        
        self.greetings = [
            "Hey there! 🚀 Welcome to CryptoBuddy! Let's find you some green and growing crypto!",
            "What's up, crypto explorer! 💎 Ready to discover your next digital gem?",
            "Hello, future crypto millionaire! 🌟 Let's dive into the exciting world of digital assets!",
            "Greetings, crypto enthusiast! 📈 I'm here to help you navigate the crypto universe!"
        ]
        
        self.sustainability_responses = [
            "🌱 Great choice! You're thinking green and sustainable!",
            "🌿 Eco-friendly crypto is the future! Smart thinking!",
            "♻️ Love the environmental consciousness! Mother Earth thanks you!",
            "🌍 Sustainable investing is the way to go! You're ahead of the curve!"
        ]
        
        self.high_return_responses = [
            "💰 Ah, a risk-taker! I like your style!",
            "🚀 To the moon mentality! Let's find you some rockets!",
            "📈 High risk, high reward! Buckle up for the ride!",
            "💎 Diamond hands detected! Here are some gems for you!"
        ]

    def greet(self):
        return random.choice(self.greetings)

    def get_crypto_info(self, crypto_name):
        crypto_name = crypto_name.title()
        if crypto_name in self.crypto_db:
            crypto = self.crypto_db[crypto_name]
            sustainability_emoji = "🌿" if crypto["sustainability_score"] >= 0.7 else "⚠️" if crypto["sustainability_score"] >= 0.5 else "🔴"
            trend_emoji = "📈" if crypto["price_trend"] == "rising" else "📊" if crypto["price_trend"] == "stable" else "📉"
            
            return f"""
{crypto_name} {trend_emoji}
💹 Price Trend: {crypto['price_trend'].title()}
🏦 Market Cap: {crypto['market_cap'].title()}
⚡ Energy Use: {crypto['energy_use'].title()}
{sustainability_emoji} Sustainability Score: {crypto['sustainability_score']*10:.1f}/10
            """
        else:
            return f"🤔 Hmm, I don't have info on {crypto_name} in my database yet. Try Bitcoin, Ethereum, Cardano, Solana, Polygon, or Dogecoin!"

    def recommend_by_preference(self, preference):
        recommendations = []
        
        if "sustainable" in preference.lower() or "green" in preference.lower() or "eco" in preference.lower():
            # Filter cryptos with sustainability score >= 0.6
            sustainable_cryptos = {name: data for name, data in self.crypto_db.items() 
                                 if data["sustainability_score"] >= 0.6}
            recommendations = list(sustainable_cryptos.keys())
            response_prefix = random.choice(self.sustainability_responses)
            
        elif "high return" in preference.lower() or "profit" in preference.lower() or "moon" in preference.lower():
            # Filter cryptos with rising trends
            rising_cryptos = {name: data for name, data in self.crypto_db.items() 
                            if data["price_trend"] == "rising"}
            recommendations = list(rising_cryptos.keys())
            response_prefix = random.choice(self.high_return_responses)
            
        elif "stable" in preference.lower() or "safe" in preference.lower():
            # Filter cryptos with stable trends or high market cap
            stable_cryptos = {name: data for name, data in self.crypto_db.items() 
                            if data["price_trend"] == "stable" or data["market_cap"] == "high"}
            recommendations = list(stable_cryptos.keys())
            response_prefix = "🛡️ Safety first! Here are some stable options:"
            
        elif "low energy" in preference.lower() or "efficient" in preference.lower():
            # Filter cryptos with low energy use
            efficient_cryptos = {name: data for name, data in self.crypto_db.items() 
                               if data["energy_use"] == "low"}
            recommendations = list(efficient_cryptos.keys())
            response_prefix = "⚡ Energy efficient choices coming right up!"
            
        elif "beginner" in preference.lower() or "new" in preference.lower() or "start" in preference.lower():
            # Beginner-friendly cryptos
            recommendations = ["Ethereum", "Cardano"]
            response_prefix = "🌟 Perfect for beginners! These are reliable and well-established:"
            
        elif "general" in preference.lower() or not any(keyword in preference.lower() for keyword in ['sustainable', 'high', 'stable', 'low', 'beginner']):
            # Default recommendation - mix of different cryptos
            recommendations = ["Cardano", "Ethereum", "Solana"]
            response_prefix = "🎯 Here are some well-rounded options for you:"
            
        else:
            # Default recommendation - mix of different cryptos
            recommendations = ["Cardano", "Ethereum", "Solana"]
            response_prefix = "🎯 Here are some well-rounded options for you:"
        
        if recommendations:
            crypto_list = ", ".join(recommendations)
            return f"{response_prefix}\n\n🎯 My top picks: {crypto_list}\n\nWant details on any of these? Just ask! 😊"
        else:
            return "🤷‍♂️ Hmm, no perfect matches found. Let me suggest Cardano - it's a great all-around choice! 🌟"

    def compare_cryptos(self, crypto1, crypto2):
        crypto1 = crypto1.title()
        crypto2 = crypto2.title()
        
        if crypto1 not in self.crypto_db or crypto2 not in self.crypto_db:
            return "🤔 I can only compare cryptos in my database. Try Bitcoin, Ethereum, Cardano, Solana, Polygon, or Dogecoin!"
        
        data1 = self.crypto_db[crypto1]
        data2 = self.crypto_db[crypto2]
        
        comparison = f"""
🥊 {crypto1} vs {crypto2} Showdown! 🥊

📈 Price Trend: {crypto1} ({data1['price_trend']}) vs {crypto2} ({data2['price_trend']})
🏦 Market Cap: {crypto1} ({data1['market_cap']}) vs {crypto2} ({data2['market_cap']})
⚡ Energy Use: {crypto1} ({data1['energy_use']}) vs {crypto2} ({data2['energy_use']})
🌿 Sustainability: {crypto1} ({data1['sustainability_score']*10:.1f}/10) vs {crypto2} ({data2['sustainability_score']*10:.1f}/10)

"""
        
        # Determine winner in each category
        if data1['sustainability_score'] > data2['sustainability_score']:
            comparison += f"🏆 {crypto1} wins on sustainability! 🌱\n"
        elif data2['sustainability_score'] > data1['sustainability_score']:
            comparison += f"🏆 {crypto2} wins on sustainability! 🌱\n"
        else:
            comparison += "🤝 It's a tie on sustainability!\n"
            
        if data1['price_trend'] == 'rising' and data2['price_trend'] != 'rising':
            comparison += f"📈 {crypto1} has better price momentum!\n"
        elif data2['price_trend'] == 'rising' and data1['price_trend'] != 'rising':
            comparison += f"📈 {crypto2} has better price momentum!\n"
            
        return comparison

    def get_market_overview(self):
        rising_count = sum(1 for crypto in self.crypto_db.values() if crypto['price_trend'] == 'rising')
        stable_count = sum(1 for crypto in self.crypto_db.values() if crypto['price_trend'] == 'stable')
        high_sustainability = sum(1 for crypto in self.crypto_db.values() if crypto['sustainability_score'] >= 0.7)
        
        return f"""
📊 Market Overview by CryptoBuddy 📊

🚀 Rising trends: {rising_count} cryptos
📊 Stable trends: {stable_count} cryptos
🌿 Highly sustainable (7+/10): {high_sustainability} cryptos

💡 Market Insight: {"The market is looking bullish!" if rising_count >= stable_count else "Stability is the name of the game right now!"}
        """

    def process_message(self, user_input):
        user_input = user_input.lower().strip()
        
        # Greeting patterns
        if any(word in user_input for word in ['hello', 'hi', 'hey', 'greetings', 'start']):
            return self.greet()
        
        # Help patterns
        elif any(word in user_input for word in ['help', 'commands', 'what can you do']):
            return """
🤖 CryptoBuddy Commands:

💬 Just say "hi" to get started!
📊 Ask about a specific crypto: "Tell me about Bitcoin"
🎯 Get recommendations: "I want sustainable crypto" or "I want high returns"
⚖️ Compare cryptos: "Compare Bitcoin and Ethereum"
📈 Market overview: "Show me the market overview"
❓ Ask for help: "help" or "what can you do"

🌟 I understand preferences like:
- Sustainable/green/eco-friendly
- High returns/profit/moon
- Stable/safe
- Low energy/efficient

Try me out! 🚀
            """
        
        # Market overview
        elif 'market overview' in user_input or 'market summary' in user_input:
            return self.get_market_overview()
        
        # Comparison patterns
        elif 'compare' in user_input or 'vs' in user_input:
            # Extract crypto names for comparison
            crypto_names = []
            for crypto in self.crypto_db.keys():
                if crypto.lower() in user_input:
                    crypto_names.append(crypto)
            
            if len(crypto_names) >= 2:
                return self.compare_cryptos(crypto_names[0], crypto_names[1])
            else:
                return "🤔 To compare cryptos, mention two of them! Like 'Compare Bitcoin and Ethereum' 📊"
        
        # Trending/rising queries
        elif any(word in user_input for word in ['trending', 'rising', 'going up', 'trending up', 'bullish']):
            rising_cryptos = [name for name, data in self.crypto_db.items() if data["price_trend"] == "rising"]
            if rising_cryptos:
                crypto_list = ", ".join(rising_cryptos)
                return f"📈 Trending up right now: {crypto_list}! These coins are showing upward momentum! 🚀"
            else:
                return "📊 No clear upward trends detected right now. Market seems stable!"
        
        # Most sustainable query
        elif any(phrase in user_input for phrase in ['most sustainable', 'greenest', 'most eco']):
            most_sustainable = max(self.crypto_db, key=lambda x: self.crypto_db[x]["sustainability_score"])
            score = self.crypto_db[most_sustainable]["sustainability_score"] * 10
            return f"🌿 {most_sustainable} is the most sustainable choice with a {score:.1f}/10 eco-score! Perfect for green investing! 🌱"
        
        # Specific crypto info
        elif any(f'about {crypto.lower()}' in user_input or crypto.lower() in user_input 
                for crypto in self.crypto_db.keys()):
            for crypto in self.crypto_db.keys():
                if crypto.lower() in user_input:
                    return self.get_crypto_info(crypto)
        
        # Highest/lowest queries
        elif 'highest price' in user_input or 'most expensive' in user_input:
            high_cap_cryptos = [name for name, data in self.crypto_db.items() if data["market_cap"] == "high"]
            return f"💰 Highest market cap cryptos: {', '.join(high_cap_cryptos)}. These are the blue chips! 💎"
        
        elif 'lowest energy' in user_input or 'least energy' in user_input:
            low_energy_cryptos = [name for name, data in self.crypto_db.items() if data["energy_use"] == "low"]
            return f"⚡ Most energy-efficient: {', '.join(low_energy_cryptos)}. Power-saving champions! 🌿"
        
        # Volatile/risky queries
        elif any(word in user_input for word in ['volatile', 'risky', 'unstable', 'crazy']):
            volatile_cryptos = [name for name, data in self.crypto_db.items() if data["price_trend"] == "volatile"]
            if volatile_cryptos:
                return f"🎢 Most volatile: {', '.join(volatile_cryptos)}. Buckle up for the ride! High risk, high reward! 💥"
            else:
                return "📊 No extremely volatile cryptos in my current database. Most are showing stable or rising trends!"
        
        # Recommendation patterns (expanded for natural conversation)
        elif any(word in user_input for word in ['recommend', 'suggest', 'want', 'looking for', 'best', 'good', 'invest', 'buy', 'portfolio', 'pick']):
            return self.recommend_by_preference(user_input)
        
        # Goodbye patterns
        elif any(word in user_input for word in ['bye', 'goodbye', 'exit', 'quit', 'thanks', 'thank you']):
            return "👋 Thanks for chatting with CryptoBuddy! May your portfolio be ever green! 🚀💎 See you next time!"
        
        # Default response - be more helpful and conversational
        else:
            # Try to be helpful based on partial matches
            if any(word in user_input for word in ['crypto', 'coin', 'invest', 'buy', 'money']):
                return """
🤖 I can see you're interested in crypto! Here's what I can help you with:

💡 **Quick suggestions:**
- Ask "I want sustainable crypto" for eco-friendly options
- Say "recommend something" for general suggestions  
- Try "tell me about Bitcoin" for specific coin info
- Ask "what's trending?" to see rising cryptos

🎯 **Popular questions:**
- "Which crypto is most sustainable?"
- "Compare Bitcoin and Ethereum"
- "Show me stable options"
- "What's the market overview?"

What specifically interests you about crypto? 🚀
                """
            
            elif any(word in user_input for word in ['stable', 'safe', 'secure']):
                return """
🛡️ Looking for stability? Smart choice! Here are some stable crypto options:

🏦 **Stable cryptos in my database:**
- **Ethereum** - Stable trend, high market cap
- **Polygon** - Stable and energy efficient

💡 Want more details? Ask "tell me about Ethereum" or "I want stable crypto recommendations"!
                """
            
            elif any(word in user_input for word in ['where', 'how', 'platform', 'exchange']):
                return """
🏪 **Where to invest in crypto:**

Popular platforms include Coinbase, Binance, Kraken, and many others. But I'm here to help you **choose WHICH cryptos** to invest in! 

🎯 Try asking:
- "I want sustainable crypto"
- "Recommend high return options"
- "Tell me about Bitcoin"
- "Compare different cryptos"

What type of crypto investment interests you? 💎
                """
            
            else:
                return """
👋 Hey there! I'm CryptoBuddy and I love talking crypto! 

🤖 **I can help you:**
- Learn about specific cryptocurrencies
- Get personalized recommendations  
- Compare different cryptos
- Find sustainable/eco-friendly options
- See market trends and insights

💬 **Just tell me what you're thinking!** For example:
"I want to invest in something green" or "What's a good crypto for beginners?"

What's on your mind about crypto? 🚀
                """

def main():
    print("🚀 Welcome to CryptoBuddy! 🚀")
    print("Your friendly cryptocurrency recommendation assistant!")
    print("-" * 50)
    
    buddy = CryptoBuddy()
    print(buddy.greet())
    print("\nType 'help' for commands or 'quit' to exit.")
    print("-" * 50)
    
    while True:
        try:
            user_input = input("\n💬 You: ").strip()
            if not user_input:
                continue
                
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print(f"\n🤖 {buddy.name}: 👋 Thanks for chatting! May your crypto journey be profitable! 🚀💎")
                break
            
            response = buddy.process_message(user_input)
            print(f"\n🤖 {buddy.name}: {response}")
            
        except KeyboardInterrupt:
            print(f"\n\n🤖 {buddy.name}: 👋 Goodbye! Happy trading! 🚀")
            break
        except Exception as e:
            print(f"\n🤖 {buddy.name}: 😅 Oops! Something went wrong. Let's try again!")

if __name__ == "__main__":
    main()
