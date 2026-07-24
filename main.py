from analysis import (load_data , 
                      search_gene , 
                      show_all_variants , 
                      search_allele_id ,
                      clinical_statistics ,
                      variant_per_gene ,
                      plot_variants_per_gene ,
                      plot_clnical_significance ,
                      dashboard_summury ,
                      export_gene_report)

data = load_data("variants.csv")


while True: 
    
    print("\nVariant Analyser")
    print("1. Show all variants")
    print("2. Search variants by gene")
    print("3. Search variant by AlleleID")
    print("4. Clinical significance statistics")
    print("5. Variants per gene")
    print("6. Show variants per gene chart")
    print("7. Show clinical significance chart")
    print("8. Dahboard summury")
    print("9. Export gene report")
    print("10. Exit")
    
    choice = int(input("Choose an option: "))
    
    if choice == 1:
        
        print(show_all_variants(data))
        
    elif choice == 2:
        
        gene = input("Enter gene name: ").upper()
        
        results = search_gene(data,gene)
        
        if results.empty:
            print("No variants found for this gene.")
        else:
            print(results)
            print(f"\nFound {len(results)} variants for {gene}.")
    
    elif choice == 3:
        
        try:
            allele_id = int(input("Enter AlleleID: "))
            results = search_allele_id(data,allele_id)
            
            if results.empty:
                print("No variant found with this AlleleID.")
                break
            else:
                print(results)
                
        except ValueError:
            print("AlleleID must be a number.")
            
    if choice == 4:
        
        statistics = clinical_statistics(data)
        
        print("\nClinical Significance Statistics")
        print(statistics.head(10))
        
    elif choice == 5:
        
        statistics = variant_per_gene(data)
        
        print("\nVariants per Gene")
        print(statistics.head(10))
        
    elif choice == 6:
        
        plot_variants_per_gene(data)    
    
    elif choice == 7:
        
        plot_clnical_significance(data)
    
    elif choice == 8:
        
        total_variants, total_genes, common_gene, common_significance = (
            dashboard_summury(data)
        )
        
        print("\nVariant Dashboard")
        print("-------------------")
        print(f"Total variants: {total_variants}")
        print(f"Total genes: {total_genes}")
        print(f"Most common gene: {common_gene}")
        print(f"Most common clinical signficance: {common_significance}")
    
    elif choice == 9:
        
        gene = input("Enter gene name: ").upper()
        
        report_created = export_gene_report(data,gene)
        
        if report_created:
            print(f"Report created: {gene}_variants_report.csv")
        else:
            print("No variants found for this gene.")
    
    elif choice == 10:
        
        print("Exit.")
        break
    
    else:
        print("Invalid option.")