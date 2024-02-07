import os

def analyze_text(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()

            # Counting words, lines, and characters
            word_count = len(content.split())
            line_count = content.count('\n') + 1
            char_count = len(content)

            print(f"Word count: {word_count}")
            print(f"Line count: {line_count}")
            print(f"Character count: {char_count}")

            return content
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def modify(file_name, content, old_word, new_word):
    if content is not None:
        modified_content = content.replace(old_word, new_word)

        try:
            with open(file_name, 'w') as file:
                file.write(modified_content)
            print("File modified and saved successfully.")
        except Exception as e:
            print(f"Error writing to file: {e}")

file_name = "sample.txt"  # file path name
old_word = "ongoing"      # Enter word that you want to replace
new_word = "Completed"    # Replace with the new word

# Analyze text
content = analyze_text(file_name)

# Modify and write back to the file
modify(file_name, content, old_word, new_word)
