# vllm-project/vllm#27118: [Bug]: Qwen3-VL-Thinking / Qwen3-Thinking-2507 reasoning parser doesn't account for <think> (start token) appended to input / chat template

| 字段 | 值 |
| --- | --- |
| Issue | [#27118](https://github.com/vllm-project/vllm/issues/27118) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3-VL-Thinking / Qwen3-Thinking-2507 reasoning parser doesn't account for <think> (start token) appended to input / chat template

### Issue 正文摘录

### Your current environment I'm using `vllm=0.11.0`. ### 🐛 Describe the bug # Problem Summary I believe there's an issue where the `qwen3` reasoning parser is too strict. # Evidence 1. https://docs.vllm.ai/en/latest/api/vllm/reasoning/qwen3_reasoning_parser.html > Qwen3 has stricter requirements - it needs both start and end tokens to be present, unlike other models that work with just the end token. 2. https://github.com/QwenLM/Qwen3 > Qwen3-Thinking-2507 supports only thinking mode. **Additionally, to enforce model thinking, the default chat template automatically includes .** Therefore, it is normal for the model's output to contain only without an explicit opening tag. 3. I believe Qwen3-VL-Thinking has the same issue based on personal experience with the model. # Relevant Issue https://github.com/vllm-project/vllm/issues/21130 (I think this is why the `deepseek_r1` parser instead) # Possible Solution Create a new reasoning parser class for Qwen3-2507 / Qwen3-VL. I think the reasoning parser class for Seed3 works out of the box (https://docs.vllm.ai/en/latest/api/vllm/reasoning/step3_reasoning_parser.html#vllm.reasoning.step3_reasoning_parser) ### Before submitting a new issu...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen3-VL-Thinking / Qwen3-Thinking-2507 reasoning parser doesn't account for <think> (start token) appended to input / chat template bug;stale ### Your current environment I'm using `vllm=0.11.0`. ### 🐛 Describe...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e, it is normal for the model's output to contain only without an explicit opening tag. 3. I believe Qwen3-VL-Thinking has the same issue based on personal experience with the model. # Relevant Issue https://github.com/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: er) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: account for <think> (start token) appended to input / chat template bug;stale ### Your current environment I'm using `vllm=0.11.0`. ### 🐛 Describe the bug # Problem Summary I believe there's an issue where the `qwen3` r...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: reasoning parser is too strict. # Evidence 1. https://docs.vllm.ai/en/latest/api/vllm/reasoning/qwen3_reasoning_parser.html > Qwen3 has stricter requirements - it needs both start and end tokens to be present, unlike ot...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
