# vllm-project/vllm#15664: [Bug]: VLLM 0.8.2 OOM error (No error in 0.7.3 version)

| 字段 | 值 |
| --- | --- |
| Issue | [#15664](https://github.com/vllm-project/vllm/issues/15664) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 36; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: VLLM 0.8.2 OOM error (No error in 0.7.3 version)

### Issue 正文摘录

### Your current environment Databricks VLLM version: 0.8.2 ### 🐛 Describe the bug I have been using VLLM for over 6 months with no problem, until recently which I started with vllm 0.8.2 version. I am installing the vllm using: `pip install --upgrade vllm` then any model I try to load I immediately get OOM with the following error: The Python process exited with exit code 137 (SIGKILL). This may have been cause by OOM error. The model can correctly be loaded with vllm==0.7.3 version. I have tried increasing and decreasing gpu_memory_utilization from 0.9 to 0.5 and 0.96 and I have changed max_num_seqs to 256, still no luck. I have tried even to set environmental variable through: export VLLM_USE_V1 = 1 and 0 for v0 version, still no luck. May I know what cause this problem with 0.8.2 version which did not exist in 0.7.3 version, and is there any solution for this problem. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: VLLM 0.8.2 OOM error (No error in 0.7.3 version) bug ### Your current environment Databricks VLLM version: 0.8.2 ### 🐛 Describe the bug I have been using VLLM for over 6 months with no problem, until recently whi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: em. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]: VLLM 0.8.2 OOM error (No error in 0.7.3 version) bug ### Your current environment Databricks VLLM version: 0.8.2 ### 🐛 Describe the bug I have been using VLLM for over 6 months with no problem, until recently whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: . I am installing the vllm using: `pip install --upgrade vllm` then any model I try to load I immediately get OOM with the following error: The Python process exited with exit code 137 (SIGKILL). This may have been caus...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
