# vllm-project/vllm#42548: [Bug]: benchmark_serving_multi_turn.py produces 0 final-content tokens on reasoning models because thinking budget consumes max_tokens

| 字段 | 值 |
| --- | --- |
| Issue | [#42548](https://github.com/vllm-project/vllm/issues/42548) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;triton |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: benchmark_serving_multi_turn.py produces 0 final-content tokens on reasoning models because thinking budget consumes max_tokens

### Issue 正文摘录

## Your current environment ### 🐛 Describe the bug When `vllm/benchmarks/multi_turn/benchmark_serving_multi_turn.py` is run against a reasoning model (Qwen3-\*, gpt-oss-\*, DeepSeek-R1, etc.), the assistant's final content is empty or near-empty on the majority of turns, because the model's thinking phase consumes the entire per-turn `max_tokens` budget. The bench still exits 0 and writes a stats file, so the failure is silent, but `output_num_tokens` p50 is 0 and `finish_reason` is dominated by `length`, which makes throughput and output-length numbers meaningless. There are two pieces of the script involved: 1. [`send_turn()` L589-601](https://github.com/vllm-project/vllm/blob/main/benchmarks/multi_turn/benchmark_serving_multi_turn.py#L589-L601) sets per-turn `max_tokens` from the dataset's reference answer length when `--limit-max-tokens` is left at the default `NUM_TOKENS_FROM_DATASET`. For ShareGPT-style multi-turn datasets the median is around 50-100 tokens. 2. [`send_request()` L472-488](https://github.com/vllm-project/vllm/blob/main/benchmarks/multi_turn/benchmark_serving_multi_turn.py#L472-L488) builds the payload with only `model, messages, seed, temperature, min_tokens,...

## 现有链接修复摘要

#42557 bench: add --disable-thinking and --extra-request-body to benchmark_serving_multi_turn

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ob/main/benchmarks/multi_turn/benchmark_serving_multi_turn.py#L472-L488) builds the payload with only `model, messages, seed, temperature, min_tokens, max_tokens`. There is no way to disable thinking from this script: n...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: 63) | 97.6% of turns produced 0 final-content tokens | | `Qwen/Qwen3-32B-FP8` (qwen3 reasoning parser) | sharegpt multi-turn | `output_num_tokens` p50 = 0 across all configs; same pattern in `genai-bench` c=1024 D(100,1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: hmark_serving_multi_turn.py produces 0 final-content tokens on reasoning models because thinking budget consumes max_tokens bug ## Your current environment ### 🐛 Describe the bug When `vllm/benchmarks/multi_turn/benchma...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug]: benchmark_serving_multi_turn.py produces 0 final-content tokens on reasoning models because thinking budget consumes max_tokens bug ## Your current environment ### 🐛 Describe the bug When `vllm/benchmarks/multi_t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: the visible content is empty. Observed on two independent setups (both H100, vLLM 0.18.0; bug also present in current main 0.20.0 since the code paths above are unchanged): | Model | Dataset | Observed | |---|---|---| |...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42557](https://github.com/vllm-project/vllm/pull/42557) | closes_keyword | 0.95 | bench: add --disable-thinking and --extra-request-body to benchmark_serving_multi_turn | Fixes #42548 ## Summary Reasoning models (Qwen3, DeepSeek-R1, gpt-oss) can silently produce 0 final-content tokens because the thinking phase consumes the full max_tokens bud |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
