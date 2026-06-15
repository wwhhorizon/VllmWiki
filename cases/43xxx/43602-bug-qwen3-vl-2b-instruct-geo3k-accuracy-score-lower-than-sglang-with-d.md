# vllm-project/vllm#43602: [Bug]: Qwen3-VL-2B-Instruct Geo3K accuracy score lower than SGLang with deterministic sampling

| 字段 | 值 |
| --- | --- |
| Issue | [#43602](https://github.com/vllm-project/vllm/issues/43602) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error;nondeterministic |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-VL-2B-Instruct Geo3K accuracy score lower than SGLang with deterministic sampling

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Summary I observe a large accuracy gap between vLLM and SGLang when serving Qwen3-VL-2B-Instruct on a VLM benchmark geo3k, even when using deterministic decoding and the official vLLM OpenAI-compatible /v1/chat/completions endpoint. The gap reproduces with: - same model: Qwen3-VL-2B-Instruct - same Geo3K test set: 601 samples - same sampling: - temperature=0 - top_p=1.0 - top_k=-1 - max_tokens=4096 - seed=42 - one worker per GPU - router policy: round_robin - 8 GPUs Results: | api | number | score | |---|---:|---:| | vLLM official /v1/chat/completions | 116 / 601 | 0.1930116472545757 | | vLLM /v1/chat/completions/render + /inference/v1/generate | 109 / 601 | 0.18136439267886856 | | SGLang /generate | 173 / 601 | 0.2878535773710483 | ## Environment OS: Linux GPU: NVIDIA H20-3e, 143771 MiB NVIDIA driver: 580.105.08 CUDA toolkit: 12.9, nvcc V12.9.86 Python: 3.12.13 vLLM: 0.21.0+cu129 SGLang: 0.5.10.post1 Torch: 2.11.0+cu129 torch.version.cuda: 12.9 Transformers: 5.8.1 Triton: 3.6.0 cuda-python: 12.9.0 flash-attn: 2.7.4.post1 Pillow: 12.2.0 pandas: 3.0.3 aiohttp: 3.13.5 ## vLLM official chat reproduction Start 8 single-GPU vLLM wo...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Qwen3-VL-2B-Instruct Geo3K accuracy score lower than SGLang with deterministic sampling bug ### Your current environment ### 🐛 Describe the bug ## Summary I observe a large accuracy gap between vLLM and SGLang wh...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: VLM benchmark geo3k, even when using deterministic decoding and the official vLLM OpenAI-compatible /v1/chat/completions endpoint. The gap reproduces with: - same model: Qwen3-VL-2B-Instruct - same Geo3K test set: 601 s...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: [Bug]: Qwen3-VL-2B-Instruct Geo3K accuracy score lower than SGLang with deterministic sampling bug ### Your current environment ### 🐛 Describe the bug ## Summary I observe a large accuracy gap between vLLM and SGLang wh...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: [Bug]: Qwen3-VL-2B-Instruct Geo3K accuracy score lower than SGLang with deterministic sampling bug ### Your current environment ### 🐛 Describe the bug ## Summary I observe a large accuracy gap between vLLM and SGLang wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 0.post1 Torch: 2.11.0+cu129 torch.version.cuda: 12.9 Transformers: 5.8.1 Triton: 3.6.0 cuda-python: 12.9.0 flash-attn: 2.7.4.post1 Pillow: 12.2.0 pandas: 3.0.3 aiohttp: 3.13.5 ## vLLM official chat reproduction Start 8...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
