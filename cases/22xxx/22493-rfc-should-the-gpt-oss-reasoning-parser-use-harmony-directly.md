# vllm-project/vllm#22493: [RFC]: Should the gpt-oss reasoning parser use harmony directly?

| 字段 | 值 |
| --- | --- |
| Issue | [#22493](https://github.com/vllm-project/vllm/issues/22493) |
| 状态 | closed |
| 标签 | RFC;stale;gpt-oss |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Should the gpt-oss reasoning parser use harmony directly?

### Issue 正文摘录

### Motivation. Currently, the [GPT-OSS Reasoning Parser](https://github.com/vllm-project/vllm/blob/31f09c615f4f067dba765ce5fe7d00d880212a6d/vllm/reasoning/gptoss_reasoning_parser.py) can't really be used directly to extract reasoning content. The comment on L22 says: ``` The GptOss model uses harmony to extract reasoning content and this parser is only used for detecting the end of the reasoning content. ``` However, to unify behavior with other Reasoning Parsers, it may be worth using harmony to extract the reasoning content. OpenAI's harmony library also states "If you are not using gpt-oss directly but through an API or a provider like HuggingFace, Ollama, or vLLM, you will not have to be concerned about this as your inference solution will handle the formatting." This is not really the case as it currently stands (at least for offline inference). ### Proposed Change. Implement the core functionality of other reasoning parsers using harmony directly. ### Feedback Period. _No response_ ### CC List. @heheda12345 @aarnphm @simon-mo @WoosukKwon @robertgshaw2-redhat ### Any Other Things. I'm implementing this currently (outside of vllm) and it's pretty straightforward. Happy to put...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [RFC]: Should the gpt-oss reasoning parser use harmony directly? RFC;stale;gpt-oss ### Motivation. Currently, the [GPT-OSS Reasoning Parser](https://github.com/vllm-project/vllm/blob/31f09c615f4f067dba765ce5fe7d00d88021...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ly. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [RFC]: Should the gpt-oss reasoning parser use harmony directly? RFC;stale;gpt-oss ### Motivation. Currently, the [GPT-OSS Reasoning Parser](https://github.com/vllm-project/vllm/blob/31f09c615f4f067dba765ce5fe7d00d88021...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: lm) and it's pretty straightforward. Happy to put up a PR and write some tests for this if folks agree it's good to include natively. ### Before submitting a new issue... - [x] Make sure you already searched for relevan...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
