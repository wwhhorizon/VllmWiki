# vllm-project/vllm#43920: [Bug]: V1 structured outputs: a malformed grammar request after a valid one crashes EngineCore

| 字段 | 值 |
| --- | --- |
| Issue | [#43920](https://github.com/vllm-project/vllm/issues/43920) |
| 状态 | open |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: V1 structured outputs: a malformed grammar request after a valid one crashes EngineCore

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The V1 `StructuredOutputManager` initializes its backend (`XgrammarBackend` / `GuidanceBackend` / etc.) exactly once per engine process, on the first grammar request that reaches the scheduler, based on that request's `_backend` field. See the explicit comment in `vllm/v1/structured_output/__init__.py`: ```python # NOTE: We only support a single backend. We do NOT support different # backends on a per-request basis in V1 (for now, anyway...). # _backend is set in Processor._validate_structured_output if self.backend is None: backend = request.sampling_params.structured_outputs._backend if backend == "xgrammar": self.backend = XgrammarBackend(...) elif backend == "guidance": self.backend = GuidanceBackend(...) ... ``` The per-request auto-fallback in `SamplingParams._validate_structured_outputs` runs only on submission of *that* request. If the **first** grammar request has a grammar xgrammar accepts, the fallback chooses xgrammar and `XgrammarBackend` is cached for the lifetime of the engine. **All subsequent** grammar requests then go through `XgrammarBackend.compile_grammar` regardless of what their own auto-fallback would have...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: es the scheduler, based on that request's `_backend` field. See the explicit comment in `vllm/v1/structured_output/__init__.py`: ```python # NOTE: We only support a single backend. We do NOT support different # backends...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: requests bypass that protection. #### Reproducer Server (any V1 + chat model works; small public one used here so the full repro is ~2 minutes including model download and engine init): ```bash vllm serve Qwen/Qwen2.5-0...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: V1 structured outputs: a malformed grammar request after a valid one crashes EngineCore ### Your current environment ### 🐛 Describe the bug The V1 `StructuredOutputManager` initializes its backend (`XgrammarBacke...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ### 🐛 Describe the bug The V1 `StructuredOutputManager` initializes its backend (`XgrammarBackend` / `GuidanceBackend` / etc.) exactly once per engine process, on the first grammar request that reaches the scheduler, ba...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ss that protection. #### Reproducer Server (any V1 + chat model works; small public one used here so the full repro is ~2 minutes including model download and engine init): ```bash vllm serve Qwen/Qwen2.5-0.5B-Instruct...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
