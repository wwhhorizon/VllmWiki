# vllm-project/vllm#35213: [RFC]: Disaggregate RendererClient from EngineClient as Foundation for Disaggregated Frontend

| 字段 | 值 |
| --- | --- |
| Issue | [#35213](https://github.com/vllm-project/vllm/issues/35213) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Disaggregate RendererClient from EngineClient as Foundation for Disaggregated Frontend

### Issue 正文摘录

### Motivation. `EngineClient` (protocol.py) is a single ABC mixing concerns that don't require an inference engine (tokenization, config, health checks) with concerns that do (inference, profiling, cache management, scheduler control, weight transfer). Any client that only needs CPU-only features is forced to implement or stub all GPU methods. This surfaced the need for a proper protocol split, as discussed in https://github.com/vllm-project/vllm/issues/34407#issuecomment-3934345231 **OpenAIServing Already Shows the Split** `OpenAIServing.__init__` (base for ALL serving) only extracts CPU-only fields: ```python class OpenAIServing ... self.model_config = engine_client.model_config self.renderer = engine_client.renderer self.io_processor = engine_client.io_processor self.input_processor = engine_client.input_processor ``` GPU methods (generate, encode) are only called from specific inference helper methods (`beam_search`, `_prepare_generators`, `_generate_with_builtin_tools`), which are only invoked by inference subclasses (`OpenAIServingChat`, `OpenAIServingCompletion`). Serving classes that don't do inference, like `OpenAIServingTokenization`, only need the CPU-only group. ### P...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: BC mixing concerns that don't require an inference engine (tokenization, config, health checks) with concerns that do (inference, profiling, cache management, scheduler control, weight transfer). Any client that only ne...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: (tokenization, config, health checks) with concerns that do (inference, profiling, cache management, scheduler control, weight transfer). Any client that only needs CPU-only features is forced to implement or stub all G...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ut_processor ``` GPU methods (generate, encode) are only called from specific inference helper methods (`beam_search`, `_prepare_generators`, `_generate_with_builtin_tools`), which are only invoked by inference subclass...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: encode) are only called from specific inference helper methods (`beam_search`, `_prepare_generators`, `_generate_with_builtin_tools`), which are only invoked by inference subclasses (`OpenAIServingChat`, `OpenAIServingC...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: h checks) with concerns that do (inference, profiling, cache management, scheduler control, weight transfer). Any client that only needs CPU-only features is forced to implement or stub all GPU methods. This surfaced th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
