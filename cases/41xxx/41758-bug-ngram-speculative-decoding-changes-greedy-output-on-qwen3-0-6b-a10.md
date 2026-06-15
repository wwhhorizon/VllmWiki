# vllm-project/vllm#41758: [Bug]: ngram speculative decoding changes greedy output on Qwen3-0.6B / A100

| 字段 | 值 |
| --- | --- |
| Issue | [#41758](https://github.com/vllm-project/vllm/issues/41758) |
| 状态 | open |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;model_support;sampling_logits;speculative_decoding |
| 子分类 | wrong_output |
| Operator 关键词 | cuda;sampling |
| 症状 | mismatch;nondeterministic |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ngram speculative decoding changes greedy output on Qwen3-0.6B / A100

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I found a deterministic output difference between a no-speculative vLLM server and the same image/config with ngram speculative decoding enabled. Summary: - vLLM: `0.20.1` - Docker image: `vllm/vllm-openai@sha256:9eff9734a30b6713a8566217d36f8277630fd2d31cec7f0a0292835901a23aa4` - Model: `Qwen/Qwen3-0.6B` - Model revision: `c1899de289a04d12100db370d81485cdf75e47ca` - GPU: `NVIDIA A100-SXM4-40GB` - Driver: `580.105.08` - CUDA: `13.0` - Params: `temperature=0`, `top_p=1`, `seed=42`, `max_tokens=32` - Prompt: `"serving" * 48` - Prompt SHA-256: `f11888cdb5376f51784f3b231beaa61a69faac2d068ee29dcb7f002f79a0a5fb` - Baseline: same vLLM server without speculative decoding - Feature server: `--speculative-config '{"method":"ngram","num_speculative_tokens":4,"prompt_lookup_min":2,"prompt_lookup_max":5}'` Expected: With greedy decoding and the same model, prompt, seed, and sampling parameters, ngram speculative decoding should return the same final generated text as the no-speculative baseline. Observed: ```text baseline: '\nOkay, let\'s see. The user provided a string of "servingservingservingservingservingservingservingservingservings' ngra...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: g with ngram speculative decoding enabled. Summary: - vLLM: `0.20.1` - Docker image: `vllm/vllm-openai@sha256:9eff9734a30b6713a8566217d36f8277630fd2d31cec7f0a0292835901a23aa4` - Model: `Qwen/Qwen3-0.6B` - Model revision...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: ngram speculative decoding changes greedy output on Qwen3-0.6B / A100 bug ### Your current environment ### 🐛 Describe the bug I found a deterministic output difference between a no-speculative vLLM server and the...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: 0 bug ### Your current environment ### 🐛 Describe the bug I found a deterministic output difference between a no-speculative vLLM server and the same image/config with ngram speculative decoding enabled. Summary: - vLLM...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: ngram speculative decoding changes greedy output on Qwen3-0.6B / A100 bug ### Your current environment ### 🐛 Describe the bug I found a deterministic output difference between a no-speculative vLLM server and the...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: ngram speculative decoding changes greedy output on Qwen3-0.6B / A100 bug ### Your current environment ### 🐛 Describe the bug I found a deterministic output difference between a no-speculative vLLM server and the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
