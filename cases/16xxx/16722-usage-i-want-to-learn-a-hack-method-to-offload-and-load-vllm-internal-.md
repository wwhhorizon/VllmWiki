# vllm-project/vllm#16722: [Usage]: I want to learn a hack method to offload and load vllm internal weights between CPU and GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#16722](https://github.com/vllm-project/vllm/issues/16722) |
| 状态 | open |
| 标签 | usage;unstale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: I want to learn a hack method to offload and load vllm internal weights between CPU and GPU

### Issue 正文摘录

### Your current environment my paltform seems not specified, I used vllm=0.7.2 ### How would you like to use vllm My program cannot use the sleep method for loading and unloading due to some limitations, so I want to explore another offload method. I found that both the model and kv_cache can be offload: ```python llm.llm_engine.model_executor.driver_worker.worker.model_runner.model = llm.llm_engine.model_executor.driver_worker.worker.model_runner.model.to("cpu") gpu_cache = llm.llm_engine.model_executor.driver_worker.worker.gpu_cache for i in range(len(gpu_cache)): for j in range(len(gpu_cache[i])): gpu_cache[i][j] = gpu_cache[i][j].to("cpu") ``` The above method can offload some of the weights, but there is still a large amount of unknown data in vram. I want to know what other data there is. Are there any feasible ways to hack the remaining content and offload it? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: GPU usage;unstale ### Your current environment my paltform seems not specified, I used vllm=0.7.2 ### How would you like to use vllm My program cannot use the sleep method for loading and unloading due to some limitatio...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: it? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Usage]: I want to learn a hack method to offload and load vllm internal weights between CPU and GPU usage;unstale ### Your current environment my paltform seems not specified, I used vllm=0.7.2 ### How would you like t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ions, so I want to explore another offload method. I found that both the model and kv_cache can be offload: ```python llm.llm_engine.model_executor.driver_worker.worker.model_runner.model = llm.llm_engine.model_executor...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: od to offload and load vllm internal weights between CPU and GPU usage;unstale ### Your current environment my paltform seems not specified, I used vllm=0.7.2 ### How would you like to use vllm My program cannot use the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
