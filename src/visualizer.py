import os
import matplotlib.pyplot as plt
import seaborn as sns

def generate_screening_visuals(df, role_name):
    """
    Generates colorful graphs and pie charts for the resume screening results.
    """
    if df.empty:
        print("No data available to generate visualizations.")
        return

    # Set the style for seaborn to make it colorful and modern
    sns.set_theme(style="whitegrid", palette="pastel")
    
    # Create an output directory for visuals if it doesn't exist
    output_dir = "reports"
    os.makedirs(output_dir, exist_ok=True)
    
    role_safe_name = role_name.replace(" ", "_").lower()
    
    print(f"\nGenerating colorful visualizations for {role_name}...")
    
    # ---------------------------------------------------------
    # 1. Bar Chart: Candidate Scores Comparison
    # ---------------------------------------------------------
    plt.figure(figsize=(10, 6))
    
    # Melt the dataframe for a grouped bar chart
    df_melted = df.melt(id_vars=["Candidate"], value_vars=["TF-IDF Sim Score", "Skill Match %"],
                        var_name="Metric", value_name="Score")
    
    sns.barplot(x="Candidate", y="Score", hue="Metric", data=df_melted, palette="Set2")
    plt.title(f"Candidate Evaluation Scores for {role_name}", fontsize=16, fontweight='bold', color='navy')
    plt.ylabel("Score (%)", fontsize=12, fontweight='bold')
    plt.xlabel("Candidate", fontsize=12, fontweight='bold')
    plt.xticks(rotation=45)
    plt.legend(title="Metrics", title_fontsize='11', fontsize='10')
    plt.tight_layout()
    
    # Save the bar chart
    bar_chart_path = os.path.join(output_dir, f"{role_safe_name}_scores_bar.png")
    plt.savefig(bar_chart_path, dpi=300)
    plt.close()
    
    # ---------------------------------------------------------
    # 2. Pie Chart: Skill match breakdown for the Top Candidate
    # ---------------------------------------------------------
    top_candidate = df.iloc[0]
    match_pct = top_candidate["Skill Match %"]
    missing_pct = 100 - match_pct if match_pct <= 100 else 0
    
    plt.figure(figsize=(8, 8))
    labels = ['Matched Skills', 'Missing Skills']
    sizes = [match_pct, missing_pct]
    
    # Explode the matched skills slice for emphasis
    explode = (0.1, 0)
    
    # Colorful pie chart with shadow
    plt.pie(sizes, explode=explode, labels=labels, colors=sns.color_palette('pastel')[0:2],
            autopct='%1.1f%%', shadow=True, startangle=140, 
            textprops={'fontsize': 14, 'color': 'darkslategray', 'fontweight': 'bold'})
    
    plt.title(f"Skill Match Breakdown\nTop Candidate: {top_candidate['Candidate']} ({role_name})", 
              fontsize=16, fontweight='bold', color='navy')
    
    # Save the pie chart
    pie_chart_path = os.path.join(output_dir, f"{role_safe_name}_top_candidate_pie.png")
    plt.savefig(pie_chart_path, dpi=300)
    plt.close()
    
    print(f"Visualizations successfully saved to the '{output_dir}' directory.")
