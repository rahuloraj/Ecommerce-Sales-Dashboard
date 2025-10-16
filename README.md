# Sales Dashboard Generator

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![Libraries](https://img.shields.io/badge/Libraries-Pandas%20%7C%20Plotly-green.svg)
![License](https://img.shields.io/badge/License-MIT-orange.svg)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen.svg)

A Python script that automatically generates a static HTML sales dashboard from a CSV file using Pandas and Plotly.

---

## 📊 Overview

This project demonstrates a simple data analysis and visualization pipeline. The script reads raw sales data, calculates essential Key Performance Indicators (KPIs), visualizes daily revenue trends, and compiles everything into a clean, single-page HTML dashboard. It's a perfect example of how to quickly create insightful reports from data using Python.

## ✨ Key Features

-   **Automated Reporting:** Generates a complete HTML dashboard with a single command.
-   **KPI Calculation:** Automatically computes key metrics such as Total Revenue, Total Orders, and Average Order Value.
-   **Interactive Visualizations:** Creates an interactive bar chart for daily revenue using Plotly.
-   **Portable Output:** Produces a single `dashboard.html` file that is easy to share and requires no special software to view.
-   **Minimal Dependencies:** Built with popular and powerful data science libraries.

## 📸 Demo Screenshot

*(Here you can add a screenshot of the generated `dashboard.html` file)*

![Dashboard Screenshot](https://i.imgur.com/example-screenshot.png)
> **Note:** To add your own screenshot, take a picture of the `dashboard.html` file in your browser, upload it to your repository or an image hosting service, and replace the URL above.

## 🛠️ Tech Stack

-   **Language:** Python
-   **Core Libraries:**
    -   `pandas` (for data processing and analysis)
    -   `plotly` (for interactive data visualization)

## 🚀 Getting Started

Follow these instructions to run the dashboard generator on your local machine.

### Prerequisites

-   Python 3.7 or higher
-   pip (Python package installer)

### Installation & Usage

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/your-username/sales-dashboard-generator.git](https://github.com/your-username/sales-dashboard-generator.git)
    cd sales-dashboard-generator
    ```
    *(Replace `your-username` with your GitHub username)*

2.  **Set up the project structure:**
    The script expects the following directory structure. Create the `data` and `src` folders if they don't exist.
    ```
    sales-dashboard-generator/
    ├── data/
    │   └── sample_sales.csv   # Place your input data here
    └── src/
        └── dashboard.py       # The Python script
    ```

3.  **Navigate to the script's directory:**
    ```sh
    cd src
    ```

4.  **Create a virtual environment & install dependencies:**
    *(Assuming you have a `requirements.txt` file with `pandas` and `plotly` listed)*
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install pandas plotly
    ```

5.  **Run the script:**
    ```sh
    python dashboard.py
    ```

6.  **View the output:**
    The script will generate the dashboard in a `dist` folder at the root of the project. Open `dist/dashboard.html` in your web browser to see the result.

## 🧠 How It Works

The script follows a simple, logical flow:
1.  **Load Data:** Reads the `sample_sales.csv` file into a pandas DataFrame.
2.  **Calculate KPIs:** Computes total revenue, unique orders, and average order value.
3.  **Aggregate for Visualization:** Groups data by date to calculate daily revenue sums.
4.  **Create Chart:** Generates an interactive bar chart using `plotly.express`.
5.  **Generate HTML:** Writes a basic HTML structure and embeds the KPIs and the Plotly chart's HTML representation into a final `.html` file.

## 🔮 Future Enhancements

This project is a great starting point. Here are some ideas for taking it to the next level:
-   **Add More Charts:** Visualize sales by product category, customer location, or other dimensions.
-   **Use a Templating Engine:** Replace the manual HTML string writing with a more robust engine like Jinja2.
-   **Dynamic Dashboard:** Convert the script into a web application using Dash or Flask to allow for user inputs like date filtering.
-   **Configuration File:** Move hardcoded values like file paths to a `config.yaml` or `.json` file.
-   **Styling:** Improve the look and feel of the dashboard with CSS.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request.

## 📄 License

This project is licensed under the MIT License.

---

<p align="center">
  Developed by <b>Rahul Raj</b>
</p>
