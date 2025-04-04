from src.vaultmind.storage import init_db, store_thought, get_all_thoughts
from src.vaultmind.analysis import analyze_thought
from src.echotwin.reflection import get_insight

class SubmitHandler:
    def __init__(self, thought_input, echo_label, timeline):
        self.thought_input = thought_input
        self.echo_label = echo_label
        self.timeline = timeline
        init_db()  # Initialize DB on startup
        self.update_timeline()

    def on_submit(self):
        thought = self.thought_input.toPlainText().strip()
        if thought:
            analysis = analyze_thought(thought)
            store_thought(thought, analysis["sentiment"], analysis["keywords"])
            insight = get_insight(thought, analysis)
            self.echo_label.setText(f"EchoTwin: {insight}")
            self.thought_input.clear()
            self.update_timeline()

    def update_timeline(self):
        thoughts = get_all_thoughts()
        if thoughts:
            timeline_text = "\n".join([f"{t[0]}: {t[1]} (Sentiment: {t[2]})" for t in thoughts])
            self.timeline.content.setText(timeline_text)
        else:
            self.timeline.content.setText("No thoughts recorded yet.")