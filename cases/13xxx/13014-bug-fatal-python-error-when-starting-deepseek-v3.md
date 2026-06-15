# vllm-project/vllm#13014: [Bug]: Fatal Python Error when Starting DeepSeek V3

| 字段 | 值 |
| --- | --- |
| Issue | [#13014](https://github.com/vllm-project/vllm/issues/13014) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Fatal Python Error when Starting DeepSeek V3

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I encountered a fatal Python error when trying to start DeepSeek V3 using two nodes (H800 *8) and tensor parallelism set to 16. The error appears to be related to pynccl_wrapper.py. The full traceback shows a segmentation fault and issues with the NCCL communication layer during distributed operations. my environment: - nvcc version: Build cuda_12.1.r12.1/compiler.32688072_0 - Driver Version: 535.129.03 - I use the official vllm image: https://hub.docker.com/layers/vllm/vllm-openai/v0.7.2 To reproduce, start a deepseek v3 model with TP16 ``` python3 \ -m vllm.entrypoints.openai.api_server \ --host 0.0.0.0 \ --port 8888 \ --served-model-name deepseekv3 \ --model /dev/shm/DeepSeek-V3 \ --trust-remote-code \ --max-num-batched-tokens 32768 \ --max-model-len 32768 \ --max-seq-len-to-capture 32768 \ --tensor-parallel-size 16 \ --swap-space 0 \ --max-num-seqs 64 ``` The error could happen during graph capture or serving. It may take hours to see the following fault. Then the frontend is still receiving new requests but it cannot output anything. ![Image](https://github.com/user-attachments/assets/905de9c8-983f-4c68-848f-fc61541f9603) ##...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: mmunication layer during distributed operations. my environment: - nvcc version: Build cuda_12.1.r12.1/compiler.32688072_0 - Driver Version: 535.129.03 - I use the official vllm image: https://hub.docker.com/layers/vllm...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: rying to start DeepSeek V3 using two nodes (H800 *8) and tensor parallelism set to 16. The error appears to be related to pynccl_wrapper.py. The full traceback shows a segmentation fault and issues with the NCCL communi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Fatal Python Error when Starting DeepSeek V3 bug;stale ### Your current environment ### 🐛 Describe the bug I encountered a fatal Python error when trying to start DeepSeek V3 using two nodes (H800 *8) and tensor...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nd_api;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;crash env_dependency Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: al vllm image: https://hub.docker.com/layers/vllm/vllm-openai/v0.7.2 To reproduce, start a deepseek v3 model with TP16 ``` python3 \ -m vllm.entrypoints.openai.api_server \ --host 0.0.0.0 \ --port 8888 \ --served-model-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
