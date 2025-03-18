from flask import request, render_template
import logging
from app.utils import analyze_logs

def register_routes(app):
    """
    Registers Flask routes with the application.
    """
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    @app.route("/", methods=["GET", "POST"])
    def index():
        """
        Handles the main webpage.
        - GET: Renders an empty form.
        - POST: Processes log content and displays word frequency analysis.
        """
        result = None
        try:
            if request.method == "POST":
                log_content = request.form.get("log_content", "").strip()
                if log_content:
                    result = analyze_logs(log_content)
                else:
                    logging.warning("Empty log content submitted.")
        except Exception as e:
            logging.error(f"Error processing request: {e}")

        return render_template("index.html", result=result)
