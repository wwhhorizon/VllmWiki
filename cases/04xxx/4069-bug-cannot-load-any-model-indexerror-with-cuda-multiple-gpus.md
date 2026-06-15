# vllm-project/vllm#4069: [Bug]: Cannot Load any model. IndexError with CUDA, multiple GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#4069](https://github.com/vllm-project/vllm/issues/4069) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;model_support |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Cannot Load any model. IndexError with CUDA, multiple GPUs

### Issue 正文摘录

### Anything you want to discuss about vllm. Cannot load the Command-r-plus model. I installed vllm directly from the Git by building it. ``` 2024-04-14 17:03:26 | ERROR | stderr | Traceback (most recent call last): 2024-04-14 17:03:26 | ERROR | stderr | File "/project/vllm_worker.py", line 303, in 2024-04-14 17:03:26 | ERROR | stderr | engine = AsyncLLMEngine.from_engine_args(engine_args) 2024-04-14 17:03:26 | ERROR | stderr | File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 347, in from_engine_args 2024-04-14 17:03:26 | ERROR | stderr | engine = cls( 2024-04-14 17:03:26 | ERROR | stderr | File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 311, in __init__ 2024-04-14 17:03:26 | ERROR | stderr | self.engine = self._init_engine(*args, **kwargs) 2024-04-14 17:03:26 | ERROR | stderr | File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 421, in _init_engine 2024-04-14 17:03:26 | ERROR | stderr | return engine_class(*args, **kwargs) 2024-04-14 17:03:26 | ERROR | stderr | File "/usr/local/lib/python3.10/dist-packages/vllm/engine/llm_engine.py", line 121, in __init__ 2024-04-14 17:03:26...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: you want to discuss about vllm. Cannot load the Command-r-plus model. I installed vllm directly from the Git by building it. ``` 2024-04-14 17:03:26 | ERROR | stderr | Traceback (most recent call last): 2024-04-14 17:03...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Cannot Load any model. IndexError with CUDA, multiple GPUs ### Anything you want to discuss about vllm. Cannot load the Command-r-plus model. I installed vllm directly from the Git by building it. ``` 2024-04-14...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Cannot Load any model. IndexError with CUDA, multiple GPUs ### Anything you want to discuss about vllm. Cannot load the Command-r-plus model. I installed vllm directly from the Git by building it. ``` 2024-04-14...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 2024-04-14 17:03:26 | ERROR | stderr | return torch._dynamo.optimize(backend=backend, nopython=fullgraph, dynamic=dynamic, disable=disable)(model) 2024-04-14 17:03:26 | ERROR | stderr | File "/usr/local/lib/python3.10/d...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: | stderr | File "/usr/local/lib/python3.10/dist-packages/torch/_dynamo/eval_frame.py", line 782, in optimize 2024-04-14 17:03:26 | ERROR | stderr | compiler_config=backend.get_compiler_config() 2024-04-14 17:03:26 | ERR...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
