# vllm-project/vllm#17382: [Bug]: disable_log_stats=False does not work when using offline inference

| 字段 | 值 |
| --- | --- |
| Issue | [#17382](https://github.com/vllm-project/vllm/issues/17382) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: disable_log_stats=False does not work when using offline inference

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I initialize the LLM with the following code, and run the inference. However, disable_log_stats=False does not work as expected. There are no logs during inference. ```python from vllm import LLM, SamplingParams model = LLM( model=model_path, tensor_parallel_size=8, gpu_memory_utilization=0.9, disable_log_stats=False, ) model.chat(messages, sampling_params=sampling_params) ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: rk as expected. There are no logs during inference. ```python from vllm import LLM, SamplingParams model = LLM( model=model_path, tensor_parallel_size=8, gpu_memory_utilization=0.9, disable_log_stats=False, ) model.chat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: : disable_log_stats=False does not work when using offline inference bug;stale ### Your current environment ### 🐛 Describe the bug I initialize the LLM with the following code, and run the inference. However, disable_lo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nd_api;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Bug]: disable_log_stats=False does not work when using offline inference bug;stale ### Your current environment ### 🐛 Describe the bug I initialize the LLM with the following code, and run the inference. However, disab...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
