from google.adk.agents import LlmAgent, ParallelAgent

MODEL = "groq/llama-3.1-8b-instant"

# -----------------------------
# Technical Agent
# -----------------------------
technical_agent = LlmAgent(
    name="TechnicalAgent",
    model=MODEL,
    instruction=(
        "Explain the given topic from a technical perspective.\n"
        "Use correct terminology and technical depth."
    ),
    output_key="technical_output"
)

# -----------------------------
# Business Agent
# -----------------------------
business_agent = LlmAgent(
    name="BusinessAgent",
    model=MODEL,
    instruction=(
        "Explain the given topic from a business impact perspective.\n"
        "Focus on cost, scalability, and real-world usage."
    ),
    output_key="business_output"
)

# -----------------------------
# Student Agent
# -----------------------------
student_agent = LlmAgent(
    name="StudentAgent",
    model=MODEL,
    instruction=(
        "Explain the given topic in very simple terms for a beginner."
    ),
    output_key="student_output"
)

# -----------------------------
# Parallel Workflow Agent
# -----------------------------
parallel_agent = ParallelAgent(
    name="ParallelExplanationAgent",
    sub_agents=[
        technical_agent,
        business_agent,
        student_agent
    ],
    description="Runs multiple explanation agents in parallel"
)

# Root agent
root_agent = parallel_agent
