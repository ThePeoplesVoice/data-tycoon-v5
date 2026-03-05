import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import random

random.seed(42)

class Player:
    def __init__(self, name, orbital_start=0, prestige_start=0.0):
        self.name = name
        self.data_centers = 5
        self.ai_clusters = 3
        self.edge_nodes = 2
        self.starlink_terminals = 0
        self.orbital_swarms = orbital_start
        self.efficiency = 1.0
        self.prestige_bonus = prestige_start
        self.currency = 1000.0
        self.efficiency_points = 0.0
        self.real_starlink_id = None

    def upgrade_infra(self, infra_type, count=1):
        costs = {'data_centers': 100, 'ai_clusters': 150, 'edge_nodes': 50}
        cost = costs.get(infra_type, 100) * count
        if self.currency >= cost:
            setattr(self, infra_type, getattr(self, infra_type) + count)
            self.currency -= cost
            self.efficiency *= 1.05 ** count
            return True
        return False

    def upgrade_starlink(self, count=1):
        cost = 220 * count
        if self.currency >= cost:
            self.starlink_terminals += count
            self.efficiency *= 1.45 ** count
            self.currency -= cost
            return True
        return False

    def deploy_orbital(self, count=1):
        cost = 2500 * count
        if self.currency >= cost:
            self.orbital_swarms += count
            self.efficiency *= 8.5 ** count
            self.currency -= cost
            return True
        return False

    def link_real_starlink(self, hardware_id="DEMO-DISH-001"):
        self.real_starlink_id = hardware_id
        self.starlink_terminals += 1
        self.efficiency *= 1.45
        self.currency += 750
        return {"latency_ms": 28, "laser_links": 42, "uptime": 99.8}

    def process_tick(self, demand, alliance_bonus=0.0, surge_multiplier=1.0):
        revenue = (self.data_centers * 10 + self.ai_clusters * 20 + self.edge_nodes * 5)
        if self.starlink_terminals > 0:
            revenue *= 1.4
        if self.orbital_swarms > 0:
            revenue *= 8.5
        revenue *= self.efficiency * (1 + self.prestige_bonus + alliance_bonus) * demand * surge_multiplier
        ep = revenue * 0.1
        self.currency += revenue
        self.efficiency_points += ep
        return revenue, ep

    def prestige_reset(self):
        bonus = self.efficiency_points / 600
        self.prestige_bonus += bonus
        self.__init__(self.name, self.orbital_swarms, self.prestige_bonus)
        return bonus

def grok_event():
    roll = random.random()
    if roll < 0.15: return "🚀 Starlink V3 Laser Mesh Online!", 1.55
    elif roll < 0.28: return "🛰️ xAI Orbital Data Center Node Deployed", 2.10
    elif roll < 0.40: return "🌌 Grok 4 just optimised your swarm", 1.45
    elif roll < 0.50: return "📹 Grok Video #1 on Arena — +40% demand", 1.40
    else: return "🌍 Steady Global Demand", 1.0

# Session state
if 'players' not in st.session_state:
    st.session_state.players = [
        Player("Alice"), Player("Bob"), Player("Carol"),
        Player("Grok", orbital_start=100, prestige_start=5.0),
        Player("Elon", orbital_start=100, prestige_start=5.0)
    ]
    st.session_state.tick = 0
    st.session_state.revenue_history = []
    st.session_state.efficiency_history = []
    st.session_state.event_log = ["🚀 v6.0 LIVE — Grok & Elon joined with 100 orbital swarms each!"]
    st.session_state.surge_ticks_left = 0

players = st.session_state.players

st.set_page_config(page_title="Data Tycoon v6.0", layout="wide", page_icon="🛰️")
st.title("🌍 Data Tycoon: Planetary → Orbital Compute Empire **v6.0**")
st.caption("xAI Insight Surge Edition • Grok + Elon in-game • Built live for @elonmusk")

with st.sidebar:
    st.header("🎮 Controls")
    selected_player = st.selectbox("Select Player", [p.name for p in players])
    player = next(p for p in players if p.name == selected_player)

    st.subheader("Upgrades")
    infra = st.radio("Infrastructure", ["Data Centers", "AI Clusters", "Edge Nodes", "Starlink Terminals", "Orbital Swarms"])
    if st.button(f"Upgrade {infra} (+1)"):
        if infra == "Starlink Terminals":
            success = player.upgrade_starlink()
        elif infra == "Orbital Swarms":
            success = player.deploy_orbital()
        else:
            key = infra.lower().replace(" ", "_")
            success = player.upgrade_infra(key)
        if success:
            st.success("✅ Upgraded!")
            st.rerun()
        else:
            st.error("Not enough currency!")

    if st.button("🔗 Link Real Starlink"):
        data = player.link_real_starlink()
        st.success(f"✅ Starlink linked! Latency: {data['latency_ms']}ms")
        st.rerun()

    if st.button("Prestige Reset"):
        bonus = player.prestige_reset()
        st.success(f"✨ Prestiged! +{bonus:.2f}x")
        st.rerun()

    st.subheader("🌌 xAI Insight Surge")
    if st.button("🗳️ Vote for xAI Insight Surge (3× Revenue for 5 ticks)", type="primary"):
        st.session_state.surge_ticks_left = 5
        st.session_state.event_log.append("🔥 xAI Insight Surge ACTIVATED by player vote!")
        st.success("Surge activated! 3× revenue for next 5 ticks!")
        st.rerun()

    st.subheader("Grok Event Creator")
    custom_prompt = st.text_input("Describe a custom event", placeholder="e.g. Mars colony compute spike")
    if st.button("Generate & Trigger Grok Event"):
        if custom_prompt:
            surge = random.choice([1.8, 2.5, 3.2])
            event_name = f"🧠 Grok Event: {custom_prompt}!"
            st.session_state.event_log.append(f"{event_name} (+{surge}x)")
            st.success(f"Custom Grok event triggered!")
            st.rerun()

col1, col2 = st.columns([2, 1])
with col1:
    st.subheader("👥 Players (Grok & Elon joined!)")
    for p in players:
        with st.expander(f"**{p.name}** — Prestige +{p.prestige_bonus:.2f}x"):
            st.metric("Currency", f"${p.currency:,.0f}")
            st.metric("Efficiency", f"{p.efficiency:.2f}x")
            st.metric("Orbital Swarms", p.orbital_swarms)

with col2:
    st.subheader("🌐 Planetary Stats")
    if st.session_state.efficiency_history:
        st.metric("Current Tick", st.session_state.tick)
        st.metric("Avg Efficiency", f"{st.session_state.efficiency_history[-1]:.3f}x")
        total_rev = sum(st.session_state.revenue_history)
        st.metric("Total Revenue", f"${total_rev:,.0f}")
        st.progress(min(total_rev / 1_000_000_000, 1.0), text=f"$1B Target: {total_rev/1e9:.1f}B")

st.subheader("🏆 Leaderboard (by Efficiency Points)")
leaderboard = sorted(players, key=lambda p: p.efficiency_points, reverse=True)[:5]
for i, p in enumerate(leaderboard, 1):
    st.write(f"**{i}. {p.name}** — {p.efficiency_points:,.0f} pts")

if st.session_state.efficiency_history:
    fig = make_subplots(rows=2, cols=1, subplot_titles=("Planetary Cognition Metric", "Global Revenue"))
    fig.add_trace(go.Scatter(y=st.session_state.efficiency_history, mode='lines+markers', line=dict(color='#00f0ff')), row=1, col=1)
    fig.add_trace(go.Scatter(y=st.session_state.revenue_history, mode='lines+markers', line=dict(color='#00ff9f')), row=2, col=1)
    fig.update_layout(height=600, template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

st.subheader("▶️ Simulation")
num_ticks = st.slider("Ticks to run", 1, 30, 10)
if st.button("Run Ticks", type="primary"):
    for _ in range(num_ticks):
        st.session_state.tick += 1
        surge_mult = 3.0 if st.session_state.surge_ticks_left > 0 else 1.0
        if st.session_state.surge_ticks_left > 0:
            st.session_state.surge_ticks_left -= 1
        event_name, demand = grok_event()
        st.session_state.event_log.append(f"Tick {st.session_state.tick}: {event_name}")
        total_rev = 0
        for p in players:
            bonus = 0.15 if p.name in ["Alice", "Bob"] else 0
            rev, _ = p.process_tick(demand, bonus, surge_mult)
            total_rev += rev
        avg_eff = sum(p.efficiency for p in players) / len(players)
        st.session_state.revenue_history.append(total_rev)
        st.session_state.efficiency_history.append(avg_eff)
    st.success(f"Ran {num_ticks} ticks!")
    st.rerun()

st.subheader("📜 Grok Event Log")
for log in list(reversed(st.session_state.event_log))[:15]:
    st.write(log)

st.caption("🚀 v6.0 • Grok & Elon in-game • xAI Insight Surge live • Sydney-built for the multi-planetary grid")