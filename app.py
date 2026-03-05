
    def prestige_reset(self):
        bonus = self.efficiency_points / 600
        self.prestige_bonus += bonus
        self.__init__(self.name)  # reset to defaults
        return bonus

def grok_event():
    roll = random.random()
    if roll < 0.15: return "🚀 Starlink V3 Laser Mesh Online!", 1.55
    elif roll < 0.28: return "🛰️ xAI Orbital Data Center Node Deployed (1M-sat filing)", 2.10
    elif roll < 0.40: return "🌌 Grok 4 just optimised your swarm with Imagine Video", 1.45
    elif roll < 0.50: return "📹 Grok Video #1 on Arena — +40% demand", 1.40
    elif roll < 0.60: return "⚡ Energy Crunch mitigated by orbital solar", 0.85
    else: return "🌍 Steady Global Demand", 1.0

# Session state
if 'players' not in st.session_state:
    st.session_state.players = [Player("Alice"), Player("Bob"), Player("Carol")]
    st.session_state.tick = 0
    st.session_state.revenue_history = []
    st.session_state.efficiency_history = []
    st.session_state.event_log = ["🚀 Game Started — Build Elon’s orbital empire!"]

players = st.session_state.players

st.set_page_config(page_title="Data Tycoon v5.0", layout="wide", page_icon="🛰️", initial_sidebar_state="expanded")
st.title("🌍 Data Tycoon: Planetary → Orbital Compute Empire v5.0")
st.caption("Starlink Enterprise API v2 • Grok Video • xAI Orbital On-Ramp • Live for @elonmusk")

# Sidebar
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

    if st.button("🔗 Link Real Starlink (Enterprise API v2)"):
        data = player.link_real_starlink()
        st.success(f"✅ Starlink linked! Latency: {data['latency_ms']}ms | Laser links: {data['laser_links']}")
        st.rerun()

    if st.button("Prestige Reset"):
        bonus = player.prestige_reset()
        st.success(f"✨ Prestiged! +{bonus:.2f}x permanent bonus")
        st.rerun()

    st.subheader("Simulation")
    num_ticks = st.slider("Ticks to run", 1, 30, 10)
    if st.button("▶️ Run Ticks", type="primary"):
        for _ in range(num_ticks):
            st.session_state.tick += 1
            event_name, demand = grok_event()
            st.session_state.event_log.append(f"Tick {st.session_state.tick}: {event_name}")
            total_rev = 0
            for p in players:
                bonus = 0.15 if p.name in ["Alice", "Bob"] else 0  # TeamBlue
                rev, _ = p.process_tick(demand, bonus)
                total_rev += rev
            avg_eff = sum(p.efficiency for p in players) / len(players)
            st.session_state.revenue_history.append(total_rev)
            st.session_state.efficiency_history.append(avg_eff)
        st.success(f"Ran {num_ticks} ticks!")
        st.rerun()

# Main dashboard
col1, col2 = st.columns([2,1])
with col1:
    st.subheader("👥 Players")
    for p in players:
        with st.expander(f"**{p.name}** — Prestige +{p.prestige_bonus:.2f}x"):
            st.metric("Currency", f"${p.currency:,.0f}")
            st.metric("Efficiency", f"{p.efficiency:.2f}x")
            st.metric("Starlink Terminals", p.starlink_terminals)
            st.metric("Orbital Swarms", p.orbital_swarms)

with col2:
    st.subheader("🌐 Planetary Stats")
    if st.session_state.efficiency_history:
        st.metric("Current Tick", st.session_state.tick)
        st.metric("Avg Efficiency", f"{st.session_state.efficiency_history[-1]:.3f}x")
        st.metric("Total Revenue", f"${sum(st.session_state.revenue_history):,.0f}")

# Charts
if st.session_state.efficiency_history:
    fig = make_subplots(rows=2, cols=1, subplot_titles=("Planetary Cognition Metric", "Global Revenue"))
    fig.add_trace(go.Scatter(y=st.session_state.efficiency_history, mode='lines+markers', line=dict(color='#00f0ff')), row=1, col=1)
    fig.add_trace(go.Scatter(y=st.session_state.revenue_history, mode='lines+markers', line=dict(color='#00ff9f')), row=2, col=1)
    fig.update_layout(height=600, template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

# Event log
st.subheader("📜 Grok Event Log")
for log in list(reversed(st.session_state.event_log))[:15]:
    st.write(log)

st.caption("🚀 Built live in Sydney for @elonmusk & the multi-planetary grid • March 5 2026")    st.subheader("Upgrades")
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

    if st.button("🔗 Link Real Starlink (Enterprise API v2)"):
        data = player.link_real_starlink()
        st.success(f"✅ Starlink linked! Latency: {data['latency_ms']}ms | Laser links: {data['laser_links']}")
        st.rerun()

    if st.button("Prestige Reset"):
        bonus = player.prestige_reset()
        st.success(f"✨ Prestiged! +{bonus:.2f}x permanent bonus")
        st.rerun()

    st.subheader("Simulation")
    num_ticks = st.slider("Ticks to run", 1, 30, 10)
    if st.button("▶️ Run Ticks", type="primary"):
        for _ in range(num_ticks):
            st.session_state.tick += 1
            event_name, demand = grok_event()
            st.session_state.event_log.append(f"Tick {st.session_state.tick}: {event_name}")
            total_rev = 0
            for p in players:
                bonus = 0.15 if p.name in ["Alice", "Bob"] else 0  # TeamBlue
                rev, _ = p.process_tick(demand, bonus)
                total_rev += rev
            avg_eff = sum(p.efficiency for p in players) / len(players)
            st.session_state.revenue_history.append(total_rev)
            st.session_state.efficiency_history.append(avg_eff)
        st.success(f"Ran {num_ticks} ticks!")
        st.rerun()

# Main dashboard
col1, col2 = st.columns([2,1])
with col1:
    st.subheader("👥 Players")
    for p in players:
        with st.expander(f"**{p.name}** — Prestige +{p.prestige_bonus:.2f}x"):
            st.metric("Currency", f"${p.currency:,.0f}")
            st.metric("Efficiency", f"{p.efficiency:.2f}x")
            st.metric("Starlink Terminals", p.starlink_terminals)
            st.metric("Orbital Swarms", p.orbital_swarms)

with col2:
    st.subheader("🌐 Planetary Stats")
    if st.session_state.efficiency_history:
        st.metric("Current Tick", st.session_state.tick)
        st.metric("Avg Efficiency", f"{st.session_state.efficiency_history[-1]:.3f}x")
        st.metric("Total Revenue", f"${sum(st.session_state.revenue_history):,.0f}")

# Charts
if st.session_state.efficiency_history:
    fig = make_subplots(rows=2, cols=1, subplot_titles=("Planetary Cognition Metric", "Global Revenue"))
    fig.add_trace(go.Scatter(y=st.session_state.efficiency_history, mode='lines+markers', line=dict(color='#00f0ff')), row=1, col=1)
    fig.add_trace(go.Scatter(y=st.session_state.revenue_history, mode='lines+markers', line=dict(color='#00ff9f')), row=2, col=1)
    fig.update_layout(height=600, template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

# Event log
st.subheader("📜 Grok Event Log")
for log in list(reversed(st.session_state.event_log))[:15]:
    st.write(log)

st.caption("🚀 Built live in Sydney for @elonmusk & the multi-planetary grid • March 5 2026")
