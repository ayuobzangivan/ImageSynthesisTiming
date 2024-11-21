import time
start_time = time.time()
for inp, tar in test_dataset.take(1):
  generate_images(generator, inp, tar)
end_time = time.time()
execution_time = end_time - start_time
print("Execution time: {:.5f} seconds".format(execution_time))
