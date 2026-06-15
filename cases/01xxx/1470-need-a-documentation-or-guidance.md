# vllm-project/vllm#1470: Need a documentation or guidance

| 字段 | 值 |
| --- | --- |
| Issue | [#1470](https://github.com/vllm-project/vllm/issues/1470) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Need a documentation or guidance

### Issue 正文摘录

I want to process a pool of data via the model engine on a machine with a multiple GPUs. Say a 100'000 items. I start a model engine with a `llm = LLM(model, tensor_parallel_size=gpus,)`. When I pass my data to a `llm.generate(messages, params)` it starts processing my prompts and printing the progress. So the questions are: - sometimes processing hanges with a mistery error `Double free...smthng` (when I encounter it again, I can add full stacktrace), but if I call generate(prompt) again, I can see that this new request is added to a queue, so my previous requests are still processing (? waiting?), how can I trigger the processing again? - how can I get already processed requests output? I found a method `llm.llm_engine.step()` - which seems to return already processed calls result, but what if processing continues after it? To summarize. It would be great to have a mechanism or the documentation on how to: - trigger engine to start processing awaiting requests - get already processed prompts with its output - get waiting requests - abort all requests Sorry If I missed this information somewhere

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: acktrace), but if I call generate(prompt) again, I can see that this new request is added to a queue, so my previous requests are still processing (? waiting?), how can I trigger the processing again? - how can I get al...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: eed a documentation or guidance I want to process a pool of data via the model engine on a machine with a multiple GPUs. Say a 100'000 items. I start a model engine with a `llm = LLM(model, tensor_parallel_size=gpus,)`....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: are: - sometimes processing hanges with a mistery error `Double free...smthng` (when I encounter it again, I can add full stacktrace), but if I call generate(prompt) again, I can see that this new request is added to a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
