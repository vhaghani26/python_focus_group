# Session 11: Writing Our Own Function to Read FASTA Files 

By: Viktoria Haghani

Session Date: TBD

Last Updated: 2026-06-09

Reference materials include Dr. Ian Korf's [MCB 185 material](https://github.com/vhaghani26/Learning_Python/tree/master/MCB%20185%20(Korf%20Course)) and [Python Basics for Data Science](https://www.edx.org/course/python-basics-for-data-science?index=product&queryID=4d4d882866dc3e8628ed7728b4662847&position=1) course by IBM hosted on edX.

## What is a FASTA file?

FASTA is a text-based format for representing nucleotide or protein sequences. It consists of records where each sequence has:

1. **Header line** starting with `>` followed by an identifier/description
2. **Sequence lines** containing the actual bases (DNA/RNA) or amino acids

For example:

```
>seq1 Description of first sequence
ATGCGTACGT
CGTACGTAGC
>seq2 Second sequence
GGCCATATAA
```

The header tells us what the sequence represents; subsequent lines until the next `>` contain the sequence data. Sequences can span multiple lines. This is particularly relevant in the context of storing genomes and conducting alignments. In genomic analyses, the FASTA header provides the chromosome identifiers (like chr1 or specific accession numbers) that distinguish between different chromosomes and link sequence data to external databases for annotation. Without these, the software cannot correctly map reads, assemble genomes, or correlate genetic variants with biological functions. 

There are also multiple labels for FASTA file extensions, commonly `.fa`, `.fasta` and if it's gzipped (compressed), then it also has a `.gz` at the end.

Given the utility and commonplace of FASTA files, I think a good example of implementing a function together will be a function that is capable of reading in FASTA file data (thanks Ian Korf!). 

## Assigning and Initializing Variables

First, let's understand the core loop logic without worrying about reading in a file. We'll define a list that contains our FASTA lines:

```
lines = [
    ">SCP_Construct",
    "CTCGAGGTACTTATATAAGGGGGTGGGGGCGCGTTCGTCCTCAGTCGCGATCGAACACTC",
    "GAGCCGAGCAGACGTGCCTACGGACCG",
    ">CDKL5_sgRNA_1",
    "GGGGGAGAACATACTCGGGG",
    ">CDKL5_sgRNA_2",
    "AGAGCATCGGACCGAAGCGG",
    ">CDKL5_sgRNA_3",
    "CCCAGGTTGCTAGGGCTTGG"
]
```

Now, we will initialize the variables we care about and defining the variable we are reading in. We need to read in the sequence lines and we care about extracting (1) the name of the sequence and (2) the sequence associated with it.

```
def read_fasta(lines):
    # The name of the sequence
    name = None
    # The contents of the sequence
    seqs = []
```

### Reading Inputs

We have our basic set up, so now we can start to work on reading in our sample lines. We know that we need to iterate through the lines, so a for loop would be a good option to do so.

```
def read_fasta(lines):
    # The name of the sequence
    name = None
    # The contents of the sequence
    seqs = []
    
    # Iterate through sequence lines
    for line in lines:
        # Strip any whitespace or line break characters at the end of the line
        line = line.rstrip()
        print(line)
        
# Run function
read_fasta(lines)
```

**To run the function**, we can just tag on `read_fasta(lines)` at the end of our script. We see that we have our lines printing out now, but we need a way to categorize them. We know that in FASTA files, the sequence header lines start with `>`, so we can delineate the sequence headers based on lines that start with `>`. This sounds like a conditional: *if* the sequence starts with `>`, then we can call it a header.


```
def read_fasta(lines):
    # The name of the sequence
    name = None
    # The contents of the sequence
    seqs = []
    
    # Iterate through sequence lines
    for line in lines:
        # Strip any whitespace or line break characters at the end of the line
        line = line.rstrip()
        # Assign sequence headers as name
        if line.startswith('>'):
            name = line
            print(name)

# Run function
read_fasta(lines)
```

This correctly identified the header, but we see the output contains the '>' symbol. There are two ways we can address this (technically there are more, but these are the first two that come to mind):

1. Strip the first character of the name since we know the first character is always `>`
2. Use the replace function to replace `>` with nothing, effectively deleting it

We will go with the first approach since the header is always guaranteed to start with `>`:

```
def read_fasta(lines):
    # The name of the sequence
    name = None
    # The contents of the sequence
    seqs = []
    
    # Iterate through sequence lines
    for line in lines:
        # Strip any whitespace or line break characters at the end of the line
        line = line.rstrip()
        # Assign sequence headers as name
        if line.startswith('>'):
            # Remove > symbol by stripping the first character
            name = line[1:]
            print(name)

# Run function
read_fasta(lines)
```

Now we have all the sequence names being properly read in. We can shift focus to the sequences themselves now. Since we have a conditional, the line either starts with > and is a header, or it doesn't, and therefore is a sequence. We can continue our conditional by putting an `else` component to track the sequences.

```
def read_fasta(lines):
    # The name of the sequence
    name = None
    # The contents of the sequence
    seqs = []
    
    # Iterate through sequence lines
    for line in lines:
        # Strip any whitespace or line break characters at the end of the line
        line = line.rstrip()
        # Assign sequence headers as name
        if line.startswith('>'):
            # Remove > symbol by stripping the first character
            name = line[1:]
            print(name)
        else:
            seqs.append(line)
            print(seqs)

# Run function
read_fasta(lines)
```

Here, we see an obvious problem. Every time we append a sequence, it adds to the overall list instead of the list of sequence for that specific header. We also have to consider that FASTA files can have multiple lines of sequence per header, so we need to:

1. Associate sequences only with their specific header
2. Combine any sequences that span multiple lines (like for SCP_Construct) so that it's contained in the same list

We can fix this by resetting the `seqs` variable for every new line:

```
def read_fasta(lines):
    # The name of the sequence
    name = None
    # The contents of the sequence
    seqs = []
    
    # Iterate through sequence lines
    for line in lines:
        # Strip any whitespace or line break characters at the end of the line
        line = line.rstrip()
        # Assign sequence headers as name
        if line.startswith('>'):
            # Remove > symbol by stripping the first character
            name = line[1:]
            print(name)
            
            # Reset seqs
            seqs = []
        else:
            seqs.append(line)
            print(seqs)

# Run function
read_fasta(lines)
```

This fixed the proper sequence association with each sequence header, but we still see that any sequence with more than one line has two seqs outputs. We still need to fix this. We can concatenate the strings to make it a single output using the `join()` function. We also need to begin preparing our output, so let's start preparing the output. Because we initialize `name` as `None`, we can use a conditional so that if `name` is not `None` (we can shorten this to `if name`, then join the associated sequences:

```
def read_fasta(lines):
    # The name of the sequence
    name = None
    # The contents of the sequence
    seqs = []
    
    # Iterate through sequence lines
    for line in lines:
        # Strip any whitespace or line break characters at the end of the line
        line = line.rstrip()
        # Assign sequence headers as name
        if line.startswith('>'):
            # Remove > symbol by stripping the first character
            name = line[1:]
            # Reset seqs
            seqs = []
        else:
            seqs.append(line)

    # Format proper output
    if name:
        seq = ''.join(seqs)
    
# Run function
read_fasta(lines)
```

### Creating Outputs

When we run this, we don't see an output. For the function, we need to return values and then access them accordingly. Since we output two values, we need to assign two variables when we run the function. Since we also want to keep the information paired, it makes sense to use a dictionary here. Let's make a dictionary and populate it with `name` and `seq` and return the dictionary as the output of the function. Remember, since we have an output, we will need to store it in a variable to access it. Since it is a dictionary, we can use a for loop to iterate through the dictionary items.

```
def read_fasta(lines):
	# Initialize dictionary
	fasta_contents = {}
	
    # The name of the sequence
    name = None
    # The contents of the sequence
    seqs = []
    
    # Iterate through sequence lines
    for line in lines:
        # Strip any whitespace or line break characters at the end of the line
        line = line.rstrip()
        # Assign sequence headers as name
        if line.startswith('>'):
            # Remove > symbol by stripping the first character
            name = line[1:]
            # Reset seqs
            seqs = []
        else:
            seqs.append(line)

    # Format proper output
    if name:
        seq = ''.join(seqs)
		fasta_contents[name] = seq
		
	return fasta_contents
    
# Run function
for name, seq in read_fasta(lines).items():
	print(f'{name}: {seq}')
```

Oops! We see one output. Why is this? The problem is the **indentation** of the conditional. It does it only once instead of within the for loop, so we need to indent it.

```
def read_fasta(lines):
	# Initialize dictionary
	fasta_contents = {}
	
    # The name of the sequence
    name = None
    # The contents of the sequence
    seqs = []
    
    # Iterate through sequence lines
    for line in lines:
        # Strip any whitespace or line break characters at the end of the line
        line = line.rstrip()
        # Assign sequence headers as name
        if line.startswith('>'):
            # Remove > symbol by stripping the first character
            name = line[1:]
            # Reset seqs
            seqs = []
        else:
            seqs.append(line)

		# Format proper output
		if name:
			seq = ''.join(seqs)
			fasta_contents[name] = seq
		
	return fasta_contents
    
# Run function
for name, seq in read_fasta(lines).items():
	print(f'{name}: {seq}')
```

There we go! Now we're done! Just kidding; we're never done. Let's think about this a little more. We have our name and sequences paired now and being read in properly, but *how frequently do you read in sequences from a list in a python script?* The answer is never. You are probably reading it in from a fasta file directly.

### Reading File Inputs

Since we want to read it in from a fasta file directly, let's create a file called `sequences.fasta`. Inside the file, place the following content:

```
>SCP_Construct
CTCGAGGTACTTATATAAGGGGGTGGG
GGCGCGTTCGTCCTCAGTCGCGATCGA
ACACTCGAGCCGAGCAGACGTGCCTAC
GGACCG
>CDKL5_sgRNA_1
GGGGGAGAACATACTCGGGG
>CDKL5_sgRNA_2
AGAGCATCGGACCGAAGCGG
>CDKL5_sgRNA_3
CCCAGGTTGCTAGGGCTTGG
```

Now, we can delete our `lines` list since we will be reading in a file instead and format accordingly:

```
def read_fasta(fasta_file):
    # Initialize dictionary
    fasta_contents = {}
    
    # The name of the sequence
    name = None
    # The contents of the sequence
    seqs = []
    
	# Open the fasta file
	with open(fasta_file, 'r') as f:
		# Iterate through sequence lines
		for line in f:
			# Strip any whitespace or line break characters at the end of the line
			line = line.rstrip()
			# Assign sequence headers as name
			if line.startswith('>'):
				# Remove > symbol by stripping the first character
				name = line[1:]
				# Reset seqs
				seqs = []
			else:
				seqs.append(line)

			# Format proper output
			if name:
				seq = ''.join(seqs)
				fasta_contents[name] = seq
        
    return fasta_contents
    
# Run function
for name, seq in read_fasta("sequences.fasta").items():
    print(f'{name}: {seq}')
```

Since functions are typically written to be broadly applicable, we need to address all possibilities we can think of. In this case, whether the FASTA file ends in the `.fa` or `.fasta` extension, it will work. But, many FASTA files are gzipped to save space. We need to write some code to handle this case. Since this case may not always occur, we can use a conditional. In order to unzip something in a Python script, we also need to import the `gzip` module to help us. 

```
import gzip

def read_fasta(fasta_file):
    # Initialize dictionary
    fasta_contents = {}
    
    # The name of the sequence
    name = None
    # The contents of the sequence
    seqs = []
	
	# Unzip file if needed
	if fasta_file.endswith('.gz'):
		fhandle = gzip.open(fasta_file, 'rt')
	else:
		fhandle = open(fasta_file, 'rt')
			
	# Open the fasta file
	with fhandle:
		# Iterate through sequence lines
		for line in fhandle:
			# Strip any whitespace or line break characters at the end of the line
			line = line.rstrip()
			# Assign sequence headers as name
			if line.startswith('>'):
				# Remove > symbol by stripping the first character
				name = line[1:]
				# Reset seqs
				seqs = []
			else:
				seqs.append(line)

			# Format proper output
			if name:
				seq = ''.join(seqs)
				fasta_contents[name] = seq
        
    return fasta_contents
    
# Run function
for name, seq in read_fasta("sequences.fasta").items():
    print(f'{name}: {seq}')
```

To confirm that the `gzip` functionality works, let's gzip our file:

```
gzip sequences.fasta
```

And now replace the file name with `sequences.fasta.gz`:

```
import gzip

def read_fasta(fasta_file):
    # Initialize dictionary
    fasta_contents = {}
    
    # The name of the sequence
    name = None
    # The contents of the sequence
    seqs = []
	
	# Unzip file if needed
	if fasta_file.endswith('.gz'):
		fhandle = gzip.open(fasta_file, 'rt')
	else:
		fhandle = open(fasta_file, 'rt')
			
	# Open the fasta file
	with fhandle:
		# Iterate through sequence lines
		for line in fhandle:
			# Strip any whitespace or line break characters at the end of the line
			line = line.rstrip()
			# Assign sequence headers as name
			if line.startswith('>'):
				# Remove > symbol by stripping the first character
				name = line[1:]
				# Reset seqs
				seqs = []
			else:
				seqs.append(line)

			# Format proper output
			if name:
				seq = ''.join(seqs)
				fasta_contents[name] = seq
        
    return fasta_contents
    
# Run function
for name, seq in read_fasta("sequences.fasta.gz").items():
    print(f'{name}: {seq}')
```

It finally works! We now have the ability to access individual sequences and what they correspond to. If you are interested in *why* we spent our time writing this function, it's because this function can be used to:

- Count sequences and lengths (summary stats: number of records, min/mean/max length)
- Search for motifs or subsequences (e.g. find all records containing a PAM or primer-binding site)
- Compute GC content per sequence or sliding-window GC profiles
- Translate nucleotide sequences to amino acids and detect stop/start codons
- Filter sequences by length, GC content, or presence/absence of motifs
- Extract subsequences (e.g. primer regions, guide-RNA targets)
- Create consensus sequences from multiple alignments or merge overlapping fragments
- Generate k-mer frequency tables for taxonomy, assembly, or error-detection
- Identify and flag low-complexity or ambiguous sequences (Ns, homopolymers)
- Prepare inputs for alignment tools (write individual FASTA files, subset FASTA)
- Annotate sequences with metadata (IDs → sample/source) and export CSV/JSON
- Count motif occurrences across the dataset and produce per-sequence counts
- Screen for contamination by BLASTing selected sequences or querying local databases
- Design primers/sgRNAs by checking candidate sequences against off-targets and constraints
- Create plots and reports (length distribution histogram, GC content violin plot)
- Batch-run downstream analyses (e.g. ORF finding, variant calling from amplicons)

Overall, this session should have taught or shown you the following:
- How to choose the appropriate data types and tools for a task (now that we've built up your toolbox)
- That there are multiple ways to accomplish the same goal
- That using `print()` is useful for verifying intermediate results
- How to troubleshoot when things don't work as expected
- How to find and fix bugs in scripts
- How to read data from files
- How to import and use required modules
- How to sequentially build up complexity in a script
