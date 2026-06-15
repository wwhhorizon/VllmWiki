# vllm-project/vllm#12480: [RFC]: [V1] TPU support and multiple architecture support

| 字段 | 值 |
| --- | --- |
| Issue | [#12480](https://github.com/vllm-project/vllm/issues/12480) |
| 状态 | closed |
| 标签 | RFC;stale;v1 |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: [V1] TPU support and multiple architecture support

### Issue 正文摘录

### Motivation. We are in process of adding Google TPU support to the vLLM V1. Here is the WIP PR [https://github.com/vllm-project/vllm/pull/11936](https://github.com/vllm-project/vllm/pull/11936). Since this is the first time we add another hardware backend to V1, the PR has some refactor to avoid code duplications, which requires discussion and feedback. ### Proposed Change. Here is the summary of changes this PR introduces: 1. Refactors the common logic of model_runner to **model_runner_base.py** in the folllowing way (Virtual functions in italic): \_\_init\_\_() => Has common config init get_model() => Just simply returns model get_kv_cache_spec() => Common logic for KV cache management _initialize_kv_cache()_ => Virtual API _execute_model()_ => Virtual API _load_model()_ => Virtual API _dummy_run()_ => Virtual API _profile_run()_ => Virtual API _capture_model()_ => Virtual API 2. Refactors common logic of worker to **worker_base.py** in the following way (Virtual functions in italic): \_\_init\_\_() => Has common config init, HF init, torch profiler init load_model() => Calls load_model() of model_runner compile_or_warm_up_model() => Calls capture model based on enforce_eager...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: summary of changes this PR introduces: 1. Refactors the common logic of model_runner to **model_runner_base.py** in the folllowing way (Virtual functions in italic): \_\_init\_\_() => Has common config init get_model()...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [RFC]: [V1] TPU support and multiple architecture support RFC;stale;v1 ### Motivation. We are in process of adding Google TPU support to the vLLM V1. Here is the WIP PR [https://github.com/vllm-project/vllm/pull/11936](...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: load_model()_ => Virtual API _dummy_run()_ => Virtual API _profile_run()_ => Virtual API _capture_model()_ => Virtual API 2. Refactors common logic of worker to **worker_base.py** in the following way (Virtual functions...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: vllm/pull/11936). Since this is the first time we add another hardware backend to V1, the PR has some refactor to avoid code duplications, which requires discussion and feedback. ### Proposed Change. Here is the summary...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: er init load_model() => Calls load_model() of model_runner compile_or_warm_up_model() => Calls capture model based on enforce_eager param and sets random seed get_model() => Calls get_model() of model_runner get_kv_cach...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
