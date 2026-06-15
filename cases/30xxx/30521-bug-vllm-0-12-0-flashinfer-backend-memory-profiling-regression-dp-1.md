# vllm-project/vllm#30521: [Bug]: vLLM 0.12.0 / Flashinfer Backend memory profiling regression (DP > 1)

| 字段 | 值 |
| --- | --- |
| Issue | [#30521](https://github.com/vllm-project/vllm/issues/30521) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;oom |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM 0.12.0 / Flashinfer Backend memory profiling regression (DP > 1)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Problem**: Data parallel deployments via Ray Serve that worked on vLLM 0.11.0 fail with cuda OOM errors on vLLM 0.12.0. The failure occurs during the `dummy_sampler_run` warmup phase before any inference requests are processed. **Setup**: - 4xT4 GPUs - Model: Qwen/Qwen2.5-0.5B-Instruct **Reproduction Script** ```python from ray import serve from ray.serve.llm import LLMConfig, build_dp_openai_app config = LLMConfig( model_loading_config={"model_id": "Qwen/Qwen2.5-0.5B-Instruct"}, engine_kwargs={ "data_parallel_size": 2, "tensor_parallel_size": 1, }, experimental_configs={"dp_size_per_node": 2}, ) app = build_dp_openai_app({"llm_config": config}) serve.run(app) ``` **Fails** on vllm 0.12.0 + T4 GPUs (+ Ray nightly image - only way to have 0.12 supported) **Works** on vllm 0.11.0 + T4 GPUs (+ Ray 2.5X image) ### Error Message ``` torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 446.00 MiB. GPU 0 has a total capacity of 14.57 GiB of which 412.75 MiB is free. RuntimeError: CUDA out of memory occurred when warming up sampler with 256 dummy requests. Please try lowering `max_num_seqs` or `gpu_memory_utilization` when ini...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: : Qwen/Qwen2.5-0.5B-Instruct **Reproduction Script** ```python from ray import serve from ray.serve.llm import LLMConfig, build_dp_openai_app config = LLMConfig( model_loading_config={"model_id": "Qwen/Qwen2.5-0.5B-Inst...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: vLLM 0.12.0 / Flashinfer Backend memory profiling regression (DP > 1) bug;stale ### Your current environment ### 🐛 Describe the bug **Problem**: Data parallel deployments via Ray Serve that worked on vLLM 0.11.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: before any inference requests are processed. **Setup**: - 4xT4 GPUs - Model: Qwen/Qwen2.5-0.5B-Instruct **Reproduction Script** ```python from ray import serve from ray.serve.llm import LLMConfig, build_dp_openai_app co...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: LLM 0.12.0 / Flashinfer Backend memory profiling regression (DP > 1) bug;stale ### Your current environment ### 🐛 Describe the bug **Problem**: Data parallel deployments via Ray Serve that worked on vLLM 0.11.0 fail wit...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: vLLM 0.12.0 / Flashinfer Backend memory profiling regression (DP > 1) bug;stale ### Your current environment ### 🐛 Describe the bug **Problem**: Data parallel deployments via Ray Serve that worked on vLLM 0.11.0...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
