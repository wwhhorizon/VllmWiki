# vllm-project/vllm#20710: [Performance]: Unexpected Inference Speed Gain at Concurrency 16 vs 1 on Llama-3.3-70B (FP8, B200, vLLM v0.9.0)

| 字段 | 值 |
| --- | --- |
| Issue | [#20710](https://github.com/vllm-project/vllm/issues/20710) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;model_support;quantization;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | cache;cuda;fp8;quantization |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Unexpected Inference Speed Gain at Concurrency 16 vs 1 on Llama-3.3-70B (FP8, B200, vLLM v0.9.0)

### Issue 正文摘录

### Proposal to improve performance Observed an unexpected inference speed gain when running LLaMA-3.3-70B (FP8, B200) with vLLM v0.9.0 under concurrency 16 compared to concurrency 1. Goal is to understand whether this is a known scheduling/dispatch behavior or something that can be optimized or improved under low concurrency (e.g., concurrency=1). ### Report of performance regression ### Summary While benchmarking the LLaMA-3.3-70B-Instruct model (FP8 quantized) on vLLM v0.9.0 with 2xB200 GPUs, I observed significantly higher output inference speed at concurrency 16 than at concurrency 1. ### Steps Taken - ✅ Re-ran genai-bench at concurrency=1 and concurrency=16 → speed gain confirmed - ✅ Verified e2e_latency and TTFT → e2e_latency is **lower** at concurrency=16 - ✅ Used benchmark_serving.py → concurrency=16 yields higher token throughput despite higher TTFT - ✅ Confirmed token count output is consistent ### Example Results (Fusion task, 512 in / 512 out) | Concurrency | TTFT | e2e_latency | Output Speed (tok/s) | |-------------|------|-------------|------------------------| | 1 | 0.05 | 8.29 | 35.04 | | 16 | 0.07 | 5.99 | 49.97 | ### Hypothesis Possibly related to internal batch...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: under low concurrency (e.g., concurrency=1). ### Report of performance regression ### Summary While benchmarking the LLaMA-3.3-70B-Instruct model (FP8 quantized) on vLLM v0.9.0 with 2xB200 GPUs, I observed significantly...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: Unexpected Inference Speed Gain at Concurrency 16 vs 1 on Llama-3.3-70B (FP8, B200, vLLM v0.9.0) performance;stale ### Proposal to improve performance Observed an unexpected inference speed gain when running LLaMA-3.3-7...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ected Inference Speed Gain at Concurrency 16 vs 1 on Llama-3.3-70B (FP8, B200, vLLM v0.9.0) performance;stale ### Proposal to improve performance Observed an unexpected inference speed gain when running LLaMA-3.3-70B (F...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ## Your current environment (if you think it is necessary) ```text vLLM version: v0.9.0 CUDA version: 12.1 GPU: 2x NVIDIA B200 (FP8) Container: vllm/vllm-openai:v0.9.0 Model: LLaMA-3.3-70B-Instruct Benchmarking tool: ge...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Performance]: Unexpected Inference Speed Gain at Concurrency 16 vs 1 on Llama-3.3-70B (FP8, B200, vLLM v0.9.0) performance;stale ### Proposal to improve performance Observed an unexpected inference speed gain when runn...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
