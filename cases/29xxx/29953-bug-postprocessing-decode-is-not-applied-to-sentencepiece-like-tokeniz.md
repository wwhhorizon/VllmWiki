# vllm-project/vllm#29953: [Bug]: postprocessing (decode) is not applied to sentencepiece like tokenizer

| 字段 | 值 |
| --- | --- |
| Issue | [#29953](https://github.com/vllm-project/vllm/issues/29953) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: postprocessing (decode) is not applied to sentencepiece like tokenizer

### Issue 正文摘录

### Your current environment na ### 🐛 Describe the bug Sentencepiece tokenizer distinguish tokens that is start of words or not using "▁" symbol. They have decoder that postprocess outputs by replacing "▁" to " " and removing preceding single space etc. But it looks like vLLM detokenizer doesn't do this (may be I couldn't find it). So the result of hf transformers and vllm become different even though generated tokens are the same. (▁ is easily removed by setting skip_special_tokens=True, but preceding space cannot be removed and maybe other decoding logics) Is this intended let users handle those postprocessing job or is this a bug? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: not using "▁" symbol. They have decoder that postprocess outputs by replacing "▁" to " " and removing preceding single space etc. But it looks like vLLM detokenizer doesn't do this (may be I couldn't find it). So the re...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ug? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: etokenizer doesn't do this (may be I couldn't find it). So the result of hf transformers and vllm become different even though generated tokens are the same. (▁ is easily removed by setting skip_special_tokens=True, but...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: postprocessing (decode) is not applied to sentencepiece like tokenizer bug ### Your current environment na ### 🐛 Describe the bug Sentencepiece tokenizer distinguish tokens that is start of words or not using "▁"...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
