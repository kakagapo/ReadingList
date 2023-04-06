# Algorithms for DNA Sequencing

## File formats used

- reference genomes in `FASTA` format (e.g. lambda_virus.fa)
- sequencing reads in `FASTQ` format (e.g. SRR835775_1.first1000.fastq)
- Python modules (e.g. kmer_index.py)

## Notes on how to use the data files

### Option 1

1) Download the file to the same computer as your Python program (use `wget` or `curl` to download from the shell command-line interface).
2) Put the file in the same directory with your Python program and then open it from your Python program using the Python open function.

### Option 2

If you use Jupyter, another way to do this (which we use in the practical sessions) is with a command that starts with `!wget`.  This is a shell command.  But if you are using `try.jupyter.org` note that the `!wget` command will not work ("unable to resolve host address").  In this case, we recommend you either (a) use `www.wakari.io` instead, or (b) use the "upload" button in the try.jupyter.org interface to upload the file to the server, then skip the command that begins with `!wget`.