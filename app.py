"""
Simple test application for vulnerability scanning.
This is a simplified version for testing Backline's SCA remediation.
"""

import os
from flask import Flask, jsonify
import numpy as np
import pandas as pd
from tqdm import tqdm
import yaml
from PIL import Image
import requests
from jinja2 import Template
from sqlalchemy import create_engine
import typer
from af_internal_utils import get_config, format_output

app = Flask(__name__)
cli = typer.Typer()


@app.route("/")
def index():
    """Health check endpoint."""
    config = get_config()
    return jsonify({"status": "ok", "message": "Test application running", "config": config})


@app.route("/data")
def get_data():
    """Sample data endpoint using pandas and numpy."""
    data = pd.DataFrame({
        "values": np.random.randn(10),
        "categories": ["A", "B"] * 5
    })
    return jsonify(data.to_dict())


@app.route("/template")
def render_template():
    """Sample template rendering using Jinja2."""
    template = Template("Hello {{ name }}!")
    return template.render(name="World")


@cli.command()
def run_server(port: int = 5000):
    """Run the Flask development server."""
    app.run(host="0.0.0.0", port=port, debug=False)


@cli.command()
def process_data(input_file: str):
    """Process data from a file."""
    print(f"Processing {input_file}...")
    for i in tqdm(range(100)):
        pass  # Simulate processing
    print("Done!")


@cli.command()
def load_config(config_path: str = "config.yaml"):
    """Load configuration from YAML file."""
    if os.path.exists(config_path):
        with open(config_path) as f:
            config = yaml.safe_load(f)
            print(f"Loaded config: {config}")
    else:
        print(f"Config file not found: {config_path}")


@cli.command()
def show_info():
    """Display application info using internal utils."""
    config = get_config()
    print(format_output(config))


if __name__ == "__main__":
    cli()
