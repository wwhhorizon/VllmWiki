# vllm-project/vllm#7413: [Bug]: Pipeline parallelism is only supported through AsyncLLMEngine as performance will be severely degraded otherwise.

| 字段 | 值 |
| --- | --- |
| Issue | [#7413](https://github.com/vllm-project/vllm/issues/7413) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 |  |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Pipeline parallelism is only supported through AsyncLLMEngine as performance will be severely degraded otherwise.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python from vllm import LLMEngine, EngineArgs from vllm.sampling_params import SamplingParams model_dir = '/home/share/models/modelscope/hub/qwen/Qwen2-0.5B' args=EngineArgs(model_dir) args.tensor_parallel_size = 1 args.pipeline_parallel_size = 2 args.gpu_memory_utilization = 0.1 engine = LLMEngine.from_engine_args(args) sampling_params = SamplingParams() query = 'hello' engine.add_request( inputs = query, params = sampling_params, request_id="1" ) while engine.has_unfinished_requests(): results_generator = engine.step() print(results_generator[0].outputs[0].text) ``` Error ``` NotImplementedError: Pipeline parallelism is only supported through AsyncLLMEngine as performance will be severely degraded otherwise. ``` Is there any way to use LLMEngine while setting the ```pipeline parallel>1```?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Your current environment ### 🐛 Describe the bug ```python from vllm import LLMEngine, EngineArgs from vllm.sampling_params import SamplingParams model_dir = '/home/share/models/modelscope/hub/qwen/Qwen2-0.5B' args=Engin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Pipeline parallelism is only supported through AsyncLLMEngine as performance will be severely degraded otherwise. bug;stale ### Your current environment ### 🐛 Describe the bug ```python from vllm import LLMEngine...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: rt LLMEngine, EngineArgs from vllm.sampling_params import SamplingParams model_dir = '/home/share/models/modelscope/hub/qwen/Qwen2-0.5B' args=EngineArgs(model_dir) args.tensor_parallel_size = 1 args.pipeline_parallel_si...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: h AsyncLLMEngine as performance will be severely degraded otherwise. bug;stale ### Your current environment ### 🐛 Describe the bug ```python from vllm import LLMEngine, EngineArgs from vllm.sampling_params import Sampli...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _build;distributed_parallel;hardware_porting;model_support cuda;operator;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
