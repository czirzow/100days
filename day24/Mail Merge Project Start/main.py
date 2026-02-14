#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".


starting_letters_file = "Input/Letters/starting_letter.txt"
invited_names_file = "Input/Names/invited_names.txt"
ready_to_send_dir = "Output/ReadyToSend/"


# Get the list of invited names
invited_names = []
with open(invited_names_file) as f:
    # as we iterate the file lines, clean them up a little.
    invited_names = [ name.strip() for name in f ]

# set up the template
template = ""
with open(starting_letters_file) as f:
    template = f.read()

for name in invited_names:
    output_file = f"{ready_to_send_dir}{name}.txt"
    with open(output_file, mode='w') as output:
        # replace the text '[name]' with {name}
        output.write(template.replace('[name]', name))

