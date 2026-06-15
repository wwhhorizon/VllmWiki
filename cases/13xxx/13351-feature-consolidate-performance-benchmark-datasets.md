# vllm-project/vllm#13351: [Feature]: Consolidate performance benchmark datasets

| 字段 | 值 |
| --- | --- |
| Issue | [#13351](https://github.com/vllm-project/vllm/issues/13351) |
| 状态 | closed |
| 标签 | help wanted;good first issue;feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Consolidate performance benchmark datasets

### Issue 正文摘录

### 🚀 The feature, motivation and pitch On vLLM we have two main benchmark scripts ([benchmark_throughput.py](https://github.com/vllm-project/vllm/blob/main/benchmarks/benchmark_throughput.py) and [benchmark_serving.py](https://github.com/vllm-project/vllm/blob/main/benchmarks/benchmark_serving.py)) to measure the performance of vLLM. However, the dataset sampling functions are defined within each script itself and over time it'll be hard to maintain these and to add new datasets to both scripts as we want to have the flexibility to run benchmark on different datasets. ### Alternatives Ideally the dataset sampling should be defined in a separate file (e.g, `benchmark_dataset.py`) where we define the sampling functions for different datasets (sharegpt, sonnet, random, vision arena, etc), and the benchmark scripts themselves can simply import from benchmark_dataset depending on which dataset is specified at command line. This modularization brings us a number of benefits: - Ensure the alignment of dataset sampling between the two benchmarks in case we want to compare the performance between online serving and offline inference. - Ease the process of adding new types of benchmark dat...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Feature]: Consolidate performance benchmark datasets help wanted;good first issue;feature request ### 🚀 The feature, motivation and pitch On vLLM we have two main benchmark scripts ([benchmark_throughput.py](https://gi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: dom, vision arena, etc), and the benchmark scripts themselves can simply import from benchmark_dataset depending on which dataset is specified at command line. This modularization brings us a number of benefits: - Ensur...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ity to support user-defined custom datasets as long as they conform to a format that we pre-define. ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for rele...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: date performance benchmark datasets help wanted;good first issue;feature request ### 🚀 The feature, motivation and pitch On vLLM we have two main benchmark scripts ([benchmark_throughput.py](https://github.com/vllm-proj...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
