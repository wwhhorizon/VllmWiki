# vllm-project/vllm#37308: [Bug]: Severe Head-of-Line Blocking (147x TTFT) under Prefix Caching with Asymmetric Batches

| 字段 | 值 |
| --- | --- |
| Issue | [#37308](https://github.com/vllm-project/vllm/issues/37308) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Severe Head-of-Line Blocking (147x TTFT) under Prefix Caching with Asymmetric Batches

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Again**, we are fuzzing VLLM for a class project and found a few issues, after a while of triaging we think there is another issue is particularly of interest to report: ``` Model: Qwen/Qwen2.5-0.5B-Instruct vLLM version: (tested on current main) GPU: NVIDIA RTX A6000 CUDA version: 12.x Python: 3.10 ``` Launch command: ```bash python -m vllm.entrypoints.openai.api_server \ --model Qwen/Qwen2.5-0.5B-Instruct \ --port 8000 \ --gpu-memory-utilization 0.95 \ --max-model-len 32768 \ --enable-prefix-caching \ --disable-log-requests ``` When 4 large-prompt requests (2048 tokens) and 2 small-prompt requests (128 tokens) arrive concurrently within a 40ms window — all sharing the same cached prefix, the two small requests are **head-of-line blocked** behind the large requests' prefill and decode phases, producing a **14–147× TTFT regression**. The small requests (`prompt=128, max_tokens=32`) should complete in under 100ms on an idle server. Under this trace they observe p99 TTFT of **1400–14000ms**. The server reports healthy throughout. No errors, no crashes — the latency degradation is completely silent. This was found via automated fu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: larly of interest to report: ``` Model: Qwen/Qwen2.5-0.5B-Instruct vLLM version: (tested on current main) GPU: NVIDIA RTX A6000 CUDA version: 12.x Python: 3.10 ``` Launch command: ```bash python -m vllm.entrypoints.open...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: Qwen2.5-0.5B-Instruct vLLM version: (tested on current main) GPU: NVIDIA RTX A6000 CUDA version: 12.x Python: 3.10 ``` Launch command: ```bash python -m vllm.entrypoints.openai.api_server \ --model Qwen/Qwen2.5-0.5B-Ins...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: --max-model-len 32768 \ --enable-prefix-caching \ --disable-log-requests ``` When 4 large-prompt requests (2048 tokens) and 2 small-prompt requests (128 tokens) arrive concurrently within a 40ms window — all sharing the...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [Bug]: Severe Head-of-Line Blocking (147x TTFT) under Prefix Caching with Asymmetric Batches bug ### Your current environment ### 🐛 Describe the bug **Again**, we are fuzzing VLLM for a class project and found a few iss...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: nterest to report: ``` Model: Qwen/Qwen2.5-0.5B-Instruct vLLM version: (tested on current main) GPU: NVIDIA RTX A6000 CUDA version: 12.x Python: 3.10 ``` Launch command: ```bash python -m vllm.entrypoints.openai.api_ser...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
