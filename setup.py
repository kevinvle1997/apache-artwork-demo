# Run and print a shell command.
def run(cmd):
  print('>> {}'.format(cmd))
  print('')

# Install apache-beam.
run('pip install --quiet apache-beam')

# Copy the input file into the local file system.
run('mkdir -p data')
run('gsutil cp gs://dataflow-samples/shakespeare/kinglear.txt data/')