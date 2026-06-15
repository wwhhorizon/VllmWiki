# vllm-project/vllm#13324: Can I use AsyncLLMEngine for multi-modal models? or should I use the MQLLMEngine

| 字段 | 值 |
| --- | --- |
| Issue | [#13324](https://github.com/vllm-project/vllm/issues/13324) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Can I use AsyncLLMEngine for multi-modal models? or should I use the MQLLMEngine

### Issue 正文摘录

### 📚 The doc issue I used to define the llm in my code as following: ``` engine_args = AsyncEngineArgs(..) engine = AsyncLLMEngine.from_engine_args(engine_args) ``` So can I used the same `AsyncLLMEngine` for mult-modal models that have imageurl or video urls? what should I consider or change in this case? ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Can I use AsyncLLMEngine for multi-modal models? or should I use the MQLLMEngine documentation;stale ### 📚 The doc issue I used to define the llm in my code as following: ``` engine_args = AsyncEngineArgs(..) engine = A...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ne for multi-modal models? or should I use the MQLLMEngine documentation;stale ### 📚 The doc issue I used to define the llm in my code as following: ``` engine_args = AsyncEngineArgs(..) engine = AsyncLLMEngine.from_eng...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
