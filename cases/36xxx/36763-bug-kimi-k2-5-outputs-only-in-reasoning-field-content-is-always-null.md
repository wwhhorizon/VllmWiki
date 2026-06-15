# vllm-project/vllm#36763: [Bug]: Kimi-K2.5 outputs only '!!!!!!!!!!' in reasoning field, content is always null

| 字段 | 值 |
| --- | --- |
| Issue | [#36763](https://github.com/vllm-project/vllm/issues/36763) |
| 状态 | closed |
| 标签 |  |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | frontend_api;model_support;sampling_logits |
| 子分类 |  |
| Operator 关键词 | sampling |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Kimi-K2.5 outputs only '!!!!!!!!!!' in reasoning field, content is always null

### Issue 正文摘录

### Your current environment - Model: moonshotai/Kimi-K2.5 - Parsers: `--reasoning-parser kimi_k2` `--tool-call-parser kimi_k2` - vLLM image tested: `cu130-nightly` and `cu130-nightly-fff3711a244dd9e2915323e31c20768d922e90b5` - GPUs: 8xB300 Nvidia --- ### 🐛 Describe the bug The model responds to requests but produces entirely unusable output: the `reasoning` field contains only repeated exclamation marks in a loop, and `content` is `null`. The `finish_reason` is `length`, meaning the model consumes the entire token budget generating `!` characters. ```json { "content": null, "reasoning": " !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" } ``` --- ### Steps to reproduce **Via curl:** ```bash curl https:// /v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "model": "moonshotai/Kimi-K2.5", "messages": [{"role": "user", "content": "how are you?"}], "chat_template_kwargs": {"thinking": false}, "max_tokens": 1024, "temperature": 0.6 }' ``` **Via Python client:** ```python response = client.chat.completions.create( model="moonshotai/Kimi-K2.5", messages=messages, max_tokens=4096, extra_body={"chat_template_kwargs": {"thinking": False}} ) ``` Same result in...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: reasoning field, content is always null ### Your current environment - Model: moonshotai/Kimi-K2.5 - Parsers: `--reasoning-parser kimi_k2` `--tool-call-parser kimi_k2` - vLLM image tested: `cu130-nightly` and `cu130-nig...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" } ``` --- ### Steps to reproduce **Via curl:** ```bash curl https:// /v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "model": "moonshotai/Kimi-K2.5", "m...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: uses `**kwargs` in `apply_chat_template`. vLLM, by a deliberate safety decision (PR [#25794](https://github.com/vllm-project/vllm/pull/25794)), only injects explicitly declared arguments — so `add_generation_prompt` is...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: : `--reasoning-parser kimi_k2` `--tool-call-parser kimi_k2` - vLLM image tested: `cu130-nightly` and `cu130-nightly-fff3711a244dd9e2915323e31c20768d922e90b5` - GPUs: 8xB300 Nvidia --- ### 🐛 Describe the bug The model re...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ime ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
