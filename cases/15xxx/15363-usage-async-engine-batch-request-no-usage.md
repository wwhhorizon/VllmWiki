# vllm-project/vllm#15363: [Usage]: Async engine batch request no usage

| 字段 | 值 |
| --- | --- |
| Issue | [#15363](https://github.com/vllm-project/vllm/issues/15363) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Async engine batch request no usage

### Issue 正文摘录

### Your current environment Hi i have and it does not handle batch requests correctly. The example in the documents is for only one request: https://docs.vllm.ai/en/latest/api/engine/async_llm_engine.html engine.async( [prompt1] )->[gen1] not engine.async( [prompt1, prompt2, prompt3] )->[gen1,gen2,gen3]. I dont see how it can do the conversion ### How would you like to use vllm Your current environment A100, nvidia 12.1.... just run simple inference async with a standard llm model How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. Hi i have been using async engine for inference and its nice to handle all of this in a queue, which emulates the requests. My question is can i handle a batch of requests? Considering its a wrapper around LLM engine i do not see why not so that each request is engine.async( [prompt1, prompt2, prompt3] )->[gen1,gen2,gen3] instead of engine.async( [prompt1] )->[gen1]. I want to make sure i am able to maintain the queue and not cause issues in the requests received. Finally one more suggestion....perhaps i can copy and paste the engine.async code with the wrapper and mod...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: prompt2, prompt3] )->[gen1,gen2,gen3]. I dont see how it can do the conversion ### How would you like to use vllm Your current environment A100, nvidia 12.1.... just run simple inference async with a standard llm model...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: onversion ### How would you like to use vllm Your current environment A100, nvidia 12.1.... just run simple inference async with a standard llm model How would you like to use vllm I want to run inference of a [specific...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 100, nvidia 12.1.... just run simple inference async with a standard llm model How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. Hi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Async engine batch request no usage usage ### Your current environment Hi i have and it does not handle batch requests correctly. The example in the documents is for only one request: https://docs.vllm.ai/en/la...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ple in the documents is for only one request: https://docs.vllm.ai/en/latest/api/engine/async_llm_engine.html engine.async( [prompt1] )->[gen1] not engine.async( [prompt1, prompt2, prompt3] )->[gen1,gen2,gen3]. I dont s...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
