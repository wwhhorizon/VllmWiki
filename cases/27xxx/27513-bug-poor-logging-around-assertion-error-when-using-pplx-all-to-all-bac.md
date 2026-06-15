# vllm-project/vllm#27513: [Bug]: Poor logging around assertion error when using PPLX all-to-all backend with microbatching (MoE)

| 字段 | 值 |
| --- | --- |
| Issue | [#27513](https://github.com/vllm-project/vllm/issues/27513) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;distributed_parallel;model_support;moe;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | cache;cuda;kernel;moe |
| 症状 | crash |
| 根因提示 | dtype;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Poor logging around assertion error when using PPLX all-to-all backend with microbatching (MoE)

### Issue 正文摘录

### Your current environment My setup is using a PPLX backend with DP local 8, 2 P and 2 D workers (32 GPUs) and EP using LWS as a multi-node deployment. Backend: VLLM_ALL2ALL_BACKEND=pplx vLLM version: v0.11.0 Model: `deepseek-ai/DeepSeek-R1-0528` Deployment: 2 P and 2 D workers, Data Parallel Local size 8, Expert Parallel and LWS to deploy across multiple nodes (32 GPUs, 4 nodes - cks cluster) ### 🐛 Describe the bug When using the above setup, I get the following error message: ```log wide-ep-llm-d-prefill-0 vllm-worker (APIServer pid=1) INFO 10-25 18:33:29 [model.py:547] Resolved architecture: DeepseekV3ForCausalLM wide-ep-llm-d-prefill-0 vllm-worker (APIServer pid=1) `torch_dtype` is deprecated! Use `dtype` instead! wide-ep-llm-d-prefill-0 vllm-worker (APIServer pid=1) INFO 10-25 18:33:29 [model.py:1510] Using max model len 163840 wide-ep-llm-d-prefill-0 vllm-worker (APIServer pid=1) INFO 10-25 18:33:30 [arg_utils.py:1293] Defaulting to mp-based distributed executor backend for async scheduling. wide-ep-llm-d-prefill-0 vllm-worker (APIServer pid=1) INFO 10-25 18:33:30 [scheduler.py:205] Chunked prefill is enabled with max_num_batched_tokens=8192. wide-ep-llm-d-prefill-0 vllm-w...

## 现有链接修复摘要

#31423 [UX] Improve DBO/microbatching error message for unsupported backends

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: LWS as a multi-node deployment. Backend: VLLM_ALL2ALL_BACKEND=pplx vLLM version: v0.11.0 Model: `deepseek-ai/DeepSeek-R1-0528` Deployment: 2 P and 2 D workers, Data Parallel Local size 8, Expert Parallel and LWS to depl...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: Poor logging around assertion error when using PPLX all-to-all backend with microbatching (MoE) bug;stale ### Your current environment My setup is using a PPLX backend with DP local 8, 2 P and 2 D workers (32 GPU...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: llm-worker (APIServer pid=1) INFO 10-25 18:33:29 [model.py:547] Resolved architecture: DeepseekV3ForCausalLM wide-ep-llm-d-prefill-0 vllm-worker (APIServer pid=1) `torch_dtype` is deprecated! Use `dtype` instead! wide-e...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: de deployment. Backend: VLLM_ALL2ALL_BACKEND=pplx vLLM version: v0.11.0 Model: `deepseek-ai/DeepSeek-R1-0528` Deployment: 2 P and 2 D workers, Data Parallel Local size 8, Expert Parallel and LWS to deploy across multipl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: on error when using PPLX all-to-all backend with microbatching (MoE) bug;stale ### Your current environment My setup is using a PPLX backend with DP local 8, 2 P and 2 D workers (32 GPUs) and EP using LWS as a multi-nod...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#31423](https://github.com/vllm-project/vllm/pull/31423) | closes_keyword | 0.95 | [UX] Improve DBO/microbatching error message for unsupported backends | Fixes #27513 ## Changes The previous error message was unclear about: 1. What DBO/microbatching actually is 2. Why certain backends don't support it 3. How to resolve the issue |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
