# vllm-project/vllm#20399: [Bug]:  ValueError: data_parallel_rank is not applicable in headless mode in commit 657f2f3

| 字段 | 值 |
| --- | --- |
| Issue | [#20399](https://github.com/vllm-project/vllm/issues/20399) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  ValueError: data_parallel_rank is not applicable in headless mode in commit 657f2f3

### Issue 正文摘录

### Your current environment I'm working on a dev setup, so collect_env.py is not an option; however, I found the root cause in a commit from 2 hours ago, which explains why I had no issues 2 hours ago. ### 🐛 Describe the bug When running vLLM in headless mode on a worker pod in a Kubernetes cluster, the command fails with the following error: `ValueError: data_parallel_rank is not applicable in headless mode` despite not explicitly setting the --data-parallel-rank or --data-parallel-start-rank flags in the command. The error originates from the run_headless function in vllm/entrypoints/cli/serve.py, specifically at this check: ``` https://github.com/vllm-project/vllm/blame/657f2f301a431542a731719fa8c6326deacc317d/vllm/entrypoints/cli/serve.py#L130 ` if parallel_config.data_parallel_rank is not None: raise ValueError("data_parallel_rank is not applicable in " "headless mode") ``` parallel_config.data_parallel_rank is being set to a non-None value internally, even though no rank-related flags are provided in the command. This prevents the headless worker from starting and connecting to the master node (vllm-inference-pytorchjob-final-master-0:29500) for data-parallel coordination....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: data_parallel_rank is not applicable in headless mode` despite not explicitly setting the --data-parallel-rank or --data-parallel-start-rank flags in the command. The error originates from the run_headless function in v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 31719fa8c6326deacc317d/vllm/entrypoints/cli/serve.py#L130 ` if parallel_config.data_parallel_rank is not None: raise ValueError("data_parallel_rank is not applicable in " "headless mode") ``` parallel_config.data_parall...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
