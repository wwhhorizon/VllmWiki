# vllm-project/vllm#28415: [Installation]: Warning errors from ROCm when running on NVidia DGX Spark

| 字段 | 值 |
| --- | --- |
| Issue | [#28415](https://github.com/vllm-project/vllm/issues/28415) |
| 状态 | closed |
| 标签 | bug;installation;rocm |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Warning errors from ROCm when running on NVidia DGX Spark

### Issue 正文摘录

### Your current environment ```text (.venv) root@spark-bec1:~/vllm# vllm serve Qwen/Qwen2-7B-Instruct -tp 1 --speculative_config '{"model": "yuhuili/EAGLE-Qwen2-7B-Instruct","draft_tensor_parallel_size": 1, "num_speculative_tokens": 4, "method": "eagle"}' WARNING 11-10 14:09:21 [rocm.py:34] Failed to import from amdsmi with ModuleNotFoundError("No module named 'amdsmi'") WARNING 11-10 14:09:21 [rocm.py:45] Failed to import from vllm._rocm_C with ModuleNotFoundError("No module named 'vllm._rocm_C'") ``` ### How you are installing vllm ```sh Built from source ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Installation]: Warning errors from ROCm when running on NVidia DGX Spark bug;installation;rocm ### Your current environment ```text (.venv) root@spark-bec1:~/vllm# vllm serve Qwen/Qwen2-7B-Instruct -tp 1 --speculative_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: current environment ```text (.venv) root@spark-bec1:~/vllm# vllm serve Qwen/Qwen2-7B-Instruct -tp 1 --speculative_config '{"model": "yuhuili/EAGLE-Qwen2-7B-Instruct","draft_tensor_parallel_size": 1, "num_speculative_tok...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Installation]: Warning errors from ROCm when running on NVidia DGX Spark bug;installation;rocm ### Your current environment ```text (.venv) root@spark-bec1:~/vllm# vllm serve Qwen/Qwen2-7B-Instruct -tp 1 --speculative_c
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: .venv) root@spark-bec1:~/vllm# vllm serve Qwen/Qwen2-7B-Instruct -tp 1 --speculative_config '{"model": "yuhuili/EAGLE-Qwen2-7B-Instruct","draft_tensor_parallel_size": 1, "num_speculative_tokens": 4, "method": "eagle"}'...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
