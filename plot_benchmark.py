# IPython log file

# IPython log file

import json
import matplotlib
import matplotlib.pyplot as plt
with open('/home/giuseppe/benchmark.json') as data_file:
    data_json = json.load(data_file)

bench_sliders_filters = data_json["bench_sliders_filters"]
bench_subsampling = data_json["bench_subsampling"]
bench_bpm_filters = data_json["bench_bpm_filters"]
bench_nn = data_json["bench_nn"]
bench_get_suitsegm = data_json["bench_get_suitsegm"]
bench_skl = data_json["bench_skl"]
bench_euclidean = data_json["bench_euclidean"]
bench_procedure = data_json["bench_procedure"]
bench_json_single = data_json["bench_json_single"]

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
import seaborn as sns
sns.set_context(rc={'text.usetex': True})
plt.xlabel(r'Time (s)')
plt.ylabel(r'Counts')

# sns.distplot(bench_sliders_filters, kde=False)
# plt.plot()
# plt.title(r'1. Filtering for values of sliders')
# plt.savefig('/home/giuseppe/Thesis/Figures/bench_sliders.pdf')

# sns.distplot(bench_subsampling, kde=False)
# plt.plot()
# plt.title(r"2. MonteCarlo Subsampling", fontsize=11)
# plt.savefig('/home/giuseppe/Thesis/Figures/bench_subsampling.pdf')

# sns.distplot(bench_bpm_filters, kde=False)
# plt.plot()
# plt.title(r"3. Filtering by additional music features (BPM, Key)", fontsize=11)
# plt.savefig('/home/giuseppe/Thesis/Figures/bench_bpm_filters.pdf')

# sns.distplot(bench_nn, kde=False)
# plt.plot()
# plt.title(r"4. Additional filtering by Euclidean distances", fontsize=11)
# plt.savefig('/home/giuseppe/Thesis/Figures/bench_nn.pdf')

# sns.distplot(bench_euclidean, kde=False)
# plt.plot()
# plt.title(r"4a. Computing Euclidean distances", fontsize=11)
# plt.savefig('/home/giuseppe/Thesis/Figures/bench_euclidean.pdf')

sns.distplot(bench_skl, kde=False)
plt.plot()
plt.title(r"4b. Computing SKL distances", fontsize=11)
plt.savefig('/home/giuseppe/Thesis/Figures/bench_skl.pdf')