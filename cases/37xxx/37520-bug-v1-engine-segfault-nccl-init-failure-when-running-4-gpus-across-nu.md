# vllm-project/vllm#37520: [Bug]: [V1 Engine] Segfault / NCCL init failure when running 4 GPUs across NUMA nodes (v0.17.0)

| 字段 | 值 |
| --- | --- |
| Issue | [#37520](https://github.com/vllm-project/vllm/issues/37520) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support |
| 子分类 | cold_start |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [V1 Engine] Segfault / NCCL init failure when running 4 GPUs across NUMA nodes (v0.17.0)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Description: I am encountering a critical regression with the new V1 engine in vLLM 0.17.0 related to multi-GPU execution across NUMA nodes. Environment: vLLM Version: 0.17.0 (Failing) vs 0.8.5 (Working) Model: Qwen3.5-27B (Please verify if it's 2B or 27B based on your actual test) GPU Configuration: 4x GPUs (Cross-NUMA topology) CUDA Version: [e.g., 12.4] Driver Version: [e.g., 550.xx] Command: python -m vllm.entrypoints.openai.api_server --model --tensor-parallel-size 4 Issue Description: Working Configuration: On vLLM 0.8.5, I can successfully run models (e.g., DeepSeek-R1-70B) using 4 GPUs (TP=4) without issues. Failing Configuration: On vLLM 0.17.0 (V1 engine), running Qwen3.5-27B with 4 GPUs results in a Segfault during NCCL initialization. Observed Behavior: tensor-parallel-size=1 or 2: Works fine. tensor-parallel-size=4: Crashes with Segfault encountered! File " ", line 0, in cuMemCreate. NUMA Topology Clue: I observed that I can only successfully utilize specific GPU pairs that reside on the same NUMA node (e.g., GPU 1+3 or GPU 2+4). Attempting to span across NUMA nodes (using all 4 GPUs) triggers the failure. ### Before...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: 17.0 related to multi-GPU execution across NUMA nodes. Environment: vLLM Version: 0.17.0 (Failing) vs 0.8.5 (Working) Model: Qwen3.5-27B (Please verify if it's 2B or 27B based on your actual test) GPU Configuration: 4x...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: MA nodes. Environment: vLLM Version: 0.17.0 (Failing) vs 0.8.5 (Working) Model: Qwen3.5-27B (Please verify if it's 2B or 27B based on your actual test) GPU Configuration: 4x GPUs (Cross-NUMA topology) CUDA Version: [e.g...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ed on your actual test) GPU Configuration: 4x GPUs (Cross-NUMA topology) CUDA Version: [e.g., 12.4] Driver Version: [e.g., 550.xx] Command: python -m vllm.entrypoints.openai.api_server --model --tensor-parallel-size 4 I...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: nt ### 🐛 Describe the bug Description: I am encountering a critical regression with the new V1 engine in vLLM 0.17.0 related to multi-GPU execution across NUMA nodes. Environment: vLLM Version: 0.17.0 (Failing) vs 0.8.5...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
