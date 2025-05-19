from data_loader import load_data
from profiler import summarize_data
from reporter import build_prompt, generate_summary
from visualizer import run_all_plots
import warnings
warnings.filterwarnings("ignore")

def main():
    file_path = "dataset.csv"
    df = load_data(file_path)
    if df is None:
        return

    summary = summarize_data(df)
    prompt = build_prompt(summary)
    result = generate_summary(prompt)

    # Generate plots
    print("\nCreating visualizations...")
    run_all_plots(df)
    print("Plots saved in the 'plots/' directory.")

    print("\nAI-Powered Summary:\n")
    print(result)

if __name__ == "__main__":
    main()