# vllm-project/vllm#16808: [Bug]: Cannot use FlashAttention-2 backend for head size 88 for serving llama4

| 字段 | 值 |
| --- | --- |
| Issue | [#16808](https://github.com/vllm-project/vllm/issues/16808) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Cannot use FlashAttention-2 backend for head size 88 for serving llama4

### Issue 正文摘录

### Your current environment I am using vllm 0.8.4 ### 🐛 Describe the bug Trying to run Llama-4-Scout-17B-16E-Instruct and then `Cannot use FlashAttention-2 backend for head size 88.` ``` INFO 04-17 20:54:09 [cuda.py:292] Using Flash Attention backend. INFO 04-17 20:54:22 [__init__.py:239] Automatically detected platform cuda. (VllmWorkerProcess pid=3329) INFO 04-17 20:54:26 [multiproc_worker_utils.py:225] Worker ready; awaiting tasks (VllmWorkerProcess pid=3329) INFO 04-17 20:54:29 [cuda.py:292] Using Flash Attention backend. INFO 04-17 20:54:32 [utils.py:993] Found nccl from library libnccl.so.2 (VllmWorkerProcess pid=3329) INFO 04-17 20:54:32 [utils.py:993] Found nccl from library libnccl.so.2 INFO 04-17 20:54:32 [pynccl.py:69] vLLM is using nccl==2.26.2 (VllmWorkerProcess pid=3329) INFO 04-17 20:54:32 [pynccl.py:69] vLLM is using nccl==2.26.2 (VllmWorkerProcess pid=3329) INFO 04-17 20:54:34 [parallel_state.py:959] rank 1 in world size 2 is assigned as DP rank 0, PP rank 1, TP rank 0 INFO 04-17 20:54:34 [parallel_state.py:959] rank 0 in world size 2 is assigned as DP rank 0, PP rank 0, TP rank 0 INFO 04-17 20:54:34 [model_runner.py:1110] Starting to load model /usr/Llama-4-Scou...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: Cannot use FlashAttention-2 backend for head size 88 for serving llama4 bug;stale ### Your current environment I am using vllm 0.8.4 ### 🐛 Describe the bug Trying to run Llama-4-Scout-17B-16E-Instruct and then `C...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: se FlashAttention-2 backend for head size 88.` ``` INFO 04-17 20:54:09 [cuda.py:292] Using Flash Attention backend. INFO 04-17 20:54:22 [__init__.py:239] Automatically detected platform cuda. (VllmWorkerProcess pid=3329...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Cannot use FlashAttention-2 backend for head size 88 for serving llama4 bug;stale ### Your current environment I am using vllm 0.8.4 ### 🐛 Describe the bug Trying to run Llama-4-Scout-17B-16E-Instruct and then `C...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: not use FlashAttention-2 backend for head size 88 for serving llama4 bug;stale ### Your current environment I am using vllm 0.8.4 ### 🐛 Describe the bug Trying to run Llama-4-Scout-17B-16E-Instruct and then `Cannot use...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ) WARNING 04-17 20:54:36 [registry.py:434] No model architectures are specified WARNING 04-17 20:54:36 [registry.py:434] No model architectures are specified ``` ### Before submitting a new issue... - [x] Make sure you...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
