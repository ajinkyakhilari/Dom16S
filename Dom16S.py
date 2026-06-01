import os
import pandas as pd
import glob
import argparse  # <-- This is the missing import statement

# Function to process all TSV files for a specific group
def process_group(group_name, group_path):
    # Load all TSV files in the group directory
    files = glob.glob(os.path.join(group_path, '*.tsv'))
    df_list = []
    
    for file in files:
        df = pd.read_csv(file, sep='\t')
        df['sample'] = os.path.basename(file)  # Add a column to identify the sample by file name
        df_list.append(df)
    
    # Combine all dataframes into one
    combined_df = pd.concat(df_list, ignore_index=True)
    
    # Ensure the 'abundance' column is numeric, and coerce any non-numeric values to NaN
    combined_df['abundance'] = pd.to_numeric(combined_df['abundance'], errors='coerce')
    
    # Drop any rows where 'abundance' is NaN
    combined_df = combined_df.dropna(subset=['abundance'])
    
    # Calculate the total number of samples in the group
    total_samples = len(files)
    
    # Group by species and calculate the total abundance and prevalence across all samples
    group_df = combined_df.groupby(['species']).agg(
        total_abundance=('abundance', 'sum'),    # Sum of abundance across all samples
        prevalence=('sample', 'nunique')         # Count of unique samples where the species is present
    ).reset_index()
    
    # Calculate group abundance by dividing total abundance by the total number of samples in the group
    group_df['group_abundance'] = group_df['total_abundance'] / total_samples
    
    # Calculate actual abundance by multiplying group abundance by prevalence
    group_df['actual_abundance'] = group_df['group_abundance'] * group_df['prevalence']
    
    # Calculate the total actual abundance
    total_actual_abundance = group_df['actual_abundance'].sum()
    
    # Normalize the actual abundance by dividing each actual abundance by the total actual abundance
    group_df['normalized_actual_abundance'] = group_df['actual_abundance'] / total_actual_abundance
    
    # Sort by actual abundance to find the dominant organisms
    group_df = group_df.sort_values(by='actual_abundance', ascending=False)
    
    # Save the results to a new CSV file
    output_file = f'{group_name}_dominant_organisms.csv'
    group_df.to_csv(output_file, index=False)
    print(f'Dominant organisms for {group_name} saved to {output_file}')

# Main function to process all groups in the input directory
def process_all_groups(input_dir):
    # List all subdirectories (each representing a group)
    groups = [d for d in os.listdir(input_dir) if os.path.isdir(os.path.join(input_dir, d))]
    
    for group in groups:
        group_path = os.path.join(input_dir, group)
        process_group(group, group_path)

# Command-line interface
if __name__ == "__main__":
    import argparse  # Import argparse here if not at the top
    parser = argparse.ArgumentParser(description="Process 16S sequencing TSV files to identify dominant organisms by group.")
    parser.add_argument('input_directory', type=str, help='Path to the input directory containing group folders with TSV files')
    
    args = parser.parse_args()
    input_directory = args.input_directory
    
    # Run the script with the provided input directory
    process_all_groups(input_directory)

