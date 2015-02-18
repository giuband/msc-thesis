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
sns.set_context(font_scale=1, rc={'text.usetex': True})
plt.xlabel(r'Time (s)', fontsize=18)
plt.ylabel(r'Counts', fontsize=18)

# sns.distplot(bench_sliders_filters, kde=False)
# plt.plot()
# plt.title(r'1. Filtering for values of sliders', fontsize=18)
# plt.savefig('/home/giuseppe/Thesis/Figures/bench_sliders.pdf')

# sns.distplot(bench_subsampling, kde=False)
# plt.plot()
# plt.title(r"2. MonteCarlo Subsampling", fontsize=18)
# plt.savefig('/home/giuseppe/Thesis/Figures/bench_subsampling.pdf')

# sns.distplot(bench_bpm_filters, kde=False)
# plt.plot()
# plt.title(r"3. Filtering by additional music features (BPM, Key)", fontsize=18)
# plt.savefig('/home/giuseppe/Thesis/Figures/bench_bpm_filters.pdf')

# sns.distplot(bench_nn, kde=False)
# plt.plot()
# plt.title(r"4. Additional filtering by Euclidean distances", fontsize=18)
# plt.savefig('/home/giuseppe/Thesis/Figures/bench_nn.pdf')

# sns.distplot(bench_euclidean, kde=False)
# plt.plot()
# plt.title(r"4a. Computing Euclidean distances", fontsize=18)
# plt.savefig('/home/giuseppe/Thesis/Figures/bench_euclidean.pdf')

# sns.distplot(bench_skl, kde=False)
# plt.plot()
# plt.title(r"4b. Computing SKL distances", fontsize=18)
# plt.savefig('/home/giuseppe/Thesis/Figures/bench_skl.pdf')

# sns.distplot(bench_get_suitsegm, kde=False)
# plt.plot()
# plt.title(r"Computing distances to all filtered neighbors", fontsize=18)
# plt.savefig('/home/giuseppe/Thesis/Figures/bench_get_suitsegm.pdf')

# sns.distplot(bench_procedure, kde=False)
# plt.plot()
# plt.title(r"Time for the entire procedure", fontsize=18)
# plt.savefig('/home/giuseppe/Thesis/Figures/bench_procedure.pdf')

sns.distplot(bench_json_single, kde=False)
plt.plot()
plt.title(r"Time for accessing a single JSON file", fontsize=18)
plt.savefig('/home/giuseppe/Thesis/Figures/bench_json_single.pdf')