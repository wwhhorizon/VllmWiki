# vllm-project/vllm#33294: [Bug]: Typo in detokenizer.py: read_offest should be read_offset breaks prompt_embeds

| 字段 | 值 |
| --- | --- |
| Issue | [#33294](https://github.com/vllm-project/vllm/issues/33294) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Typo in detokenizer.py: read_offest should be read_offset breaks prompt_embeds

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vLLM 0.14.1 has a typo in /vllm/v1/engine/detokenizer.py causing AttributeError when using --enable-prompt-embeds. Root Cause: Line ~215: Variable defined as read_offest (incorrect spelling) Line ~304: Code tries to access self.read_offset (correct spelling) Result: AttributeError: 'SlowIncrementalDetokenizer' object has no attribute 'read_offset' Error Trace: ```bash File "vllm/v1/engine/detokenizer.py", line 304, in decode_next read_offset=self.read_offset, AttributeError: ... Did you mean: 'read_offest'? ``` Fix: Change read_offest to read_offset throughout the file. Reproduction: ```bash vllm serve --enable-prompt-embeds ``` # Send request with prompt_embeds → crashes ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: hes ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Error Trace: ```bash File "vllm/v1/engine/detokenizer.py", line 304, in decode_next read_offset=self.read_offset, AttributeError: ... Did you mean: 'read_offest'? ``` Fix: Change read_offest to read_offset throughout th...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;mismatch;nan_inf env_dependency Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: its;speculative_decoding cuda;operator;sampling;triton build_error;crash;mismatch;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
