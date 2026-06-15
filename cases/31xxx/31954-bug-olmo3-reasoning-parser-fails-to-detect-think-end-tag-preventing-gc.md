# vllm-project/vllm#31954: [Bug] OLMo3 reasoning parser fails to detect </think> end tag, preventing GCD activation

| 字段 | 值 |
| --- | --- |
| Issue | [#31954](https://github.com/vllm-project/vllm/issues/31954) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | activation_norm;frontend_api;model_support;speculative_decoding |
| 子分类 | debug |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] OLMo3 reasoning parser fails to detect </think> end tag, preventing GCD activation

### Issue 正文摘录

### Description The OLMo3 reasoning parser (`olmo3_reasoning_parser.py`) fails to correctly detect when thinking ends, causing all generated tokens to be classified as thinking tokens. This prevents grammar-constrained decoding (GCD) from activating for the post-thinking structured output. ### Evidence From experiments with OLMo3-7B-Think + GCD + thinking=high on the math500 task: **Question 0 (Polar coordinates conversion):** ```json { "thinking_tokens": 1885, "total_tokens": 1885, "non_thinking_tokens": 0, "format_valid": false } ``` **Question 1 (Double sum problem):** ```json { "thinking_tokens": 5521, "total_tokens": 5521, "non_thinking_tokens": 0, "format_valid": false } ``` **Question 2 (Function evaluation):** ```json { "thinking_tokens": 2718, "total_tokens": 2718, "non_thinking_tokens": 0, "format_valid": false } ``` **Key observation:** `thinking_tokens == total_tokens` in ALL cases means vLLM classified the ENTIRE output as thinking, so GCD was never applied to enforce JSON structure. ### Expected Behavior With thinking mode + GCD: 1. Model generates: ` reasoning... {"answer": "A"}` 2. Thinking parser detects ` ` at token position N 3. Tokens 0-N: classified as thinkin...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: + thinking=high on the math500 task: **Question 0 (Polar coordinates conversion):** ```json { "thinking_tokens": 1885, "total_tokens": 1885, "non_thinking_tokens": 0, "format_valid": false } ``` **Question 1 (Double sum...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ng_tokens": 1885, "total_tokens": 1885, "non_thinking_tokens": 0, "format_valid": false } ``` **Question 1 (Double sum problem):** ```json { "thinking_tokens": 5521, "total_tokens": 5521, "non_thinking_tokens": 0, "form...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: /Olmo-3-7B-Think` - Thinking parser: `olmo3` - GCD backend: `xgrammar` - CUDA: 12.8 - GPU: NVIDIA L40S - Platform: Linux ### Additional Context This issue was discovered during systematic testing of thinking modes with...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: inking_tokens": 0, "format_valid": false } ``` **Question 2 (Function evaluation):** ```json { "thinking_tokens": 2718, "total_tokens": 2718, "non_thinking_tokens": 0, "format_valid": false } ``` **Key observation:** `t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: llm` - Model: `allenai/Olmo-3-7B-Think` - Thinking parser: `olmo3` - GCD backend: `xgrammar` - CUDA: 12.8 - GPU: NVIDIA L40S - Platform: Linux ### Additional Context This issue was discovered during systematic testing o...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
