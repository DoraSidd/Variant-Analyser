import pandas as pd
import matplotlib.pyplot as plt 

def load_data(filename):
    data = pd.read_csv(filename)
    return data

def search_gene(data,gene):
    results = data[data["GeneSymbol"] == gene]
    return results

def show_all_variants(data):
    return data

def search_allele_id(data,allele_id):
    results = data[data["AlleleID"] == allele_id]
    return results

def clinical_statistics(data):
    statistics = data["ClinicalSignificance"].value_counts()
    return statistics

def variant_per_gene(data):
    statistics = data["GeneSymbol"].value_counts()
    return statistics

def plot_variants_per_gene(data):
    statistics = data["GeneSymbol"].value_counts()
    statistics.plot(kind="bar")
    
    plt.title("Variants per Gene")
    plt.xlabel("Gene")
    plt.ylabel("Number of Variants")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("Variants_per_gene.png")
    plt.show()
    
def plot_clnical_significance(data):
    statistics = data["ClinicalSignificance"].value_counts().head(5)
    
    plt.figure(figsize=(8,8))
    plt.pie(statistics,
            labels=statistics.index,
            autopct="%1.1f%%",
            startangle=90)
    plt.title("Top 5 Clinical Significance Categories")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("Clinical_significance.png")
    plt.show()
    
def dashboard_summury(data):
    total_variants = len(data)
    total_genes = data["GeneSymbol"].nunique()
    
    most_comon_gene = data["GeneSymbol"].value_counts().idxmax()
    most_common_significance = (data["ClinicalSignificance"].value_counts().idxmax())
    
    return (total_variants,
            total_genes,
            most_comon_gene,
            most_common_significance)
    
def export_gene_report(data,gene):
    results = data[data["GeneSymbol"] == gene]
    
    if results.empty:
        return False
    
    filename = f"{gene}_variants_report.csv"
    results.to_csv(filename,index=False)
    
    return True
