# vllm-project/vllm#14623: [Bug]: [V1] Detokenizer does not trunctate EOS/stop-token from output text

| 字段 | 值 |
| --- | --- |
| Issue | [#14623](https://github.com/vllm-project/vllm/issues/14623) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [V1] Detokenizer does not trunctate EOS/stop-token from output text

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The V1 engine core detects token-based stops (EOS, stop-token) but the detokenizer does not actually truncate the text of the EOS/stop-token from the output. This has the downstream effect of breaking tool-call unit tests due to control tokens polluting the model output. Reproduce: ``` pytest -v -s tests/tool_use/test_tool_calls.py::test_tool_call_and_choice[llama] ``` Should fail with an assertion that 0 tool calls were detected but one was expected. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;quantiza...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ed. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ect of breaking tool-call unit tests due to control tokens polluting the model output. Reproduce: ``` pytest -v -s tests/tool_use/test_tool_calls.py::test_tool_call_and_choice[llama] ``` Should fail with an assertion th...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: tool-call unit tests due to control tokens polluting the model output. Reproduce: ``` pytest -v -s tests/tool_use/test_tool_calls.py::test_tool_call_and_choice[llama] ``` Should fail with an assertion that 0 tool calls...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
