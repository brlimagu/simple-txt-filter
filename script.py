import argparse

def extract_delivery_rows(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            lines = infile.readlines()

        delivery_lines = [line for line in lines if 'delivery' in line.lower()]

        with open(output_file, 'w') as outfile:
            outfile.writelines(delivery_lines)

        print(f"Extraction complete. {len(delivery_lines)} rows containing 'delivery' were written to {output_file}.")

    except FileNotFoundError:
        print(f"The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract lines containing the word "delivery" from a text file.')
    parser.add_argument('input_file', type=str, help='The input text file.')
    parser.add_argument('output_file', type=str, help='The output text file.')
    
    args = parser.parse_args()
    
    extract_delivery_rows(args.input_file, args.output_file)
