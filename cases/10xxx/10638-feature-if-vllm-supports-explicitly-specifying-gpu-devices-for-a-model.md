# vllm-project/vllm#10638: [Feature]: if vllm supports explicitly specifying GPU devices for a model instance. 

| 字段 | 值 |
| --- | --- |
| Issue | [#10638](https://github.com/vllm-project/vllm/issues/10638) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: if vllm supports explicitly specifying GPU devices for a model instance. 

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Background I am working on a multi-agent inference process where each agent is assigned to use a separate model. When testing with two agents, I observed that vllm freezes when the second agent attempts to load its model. This prevents the second agent from functioning correctly. Expected Behavior To support multiple agents, each with its own model, without resource conflicts or freezing issues. Ideally, there would be a way to specify which GPUs are assigned to each model to ensure proper resource allocation. Current Behavior When initializing two LLM instances in separate agents, the first model loads successfully, but the second instance freezes during the loading process. Example of Desired Functionality I would like to know if vllm supports explicitly specifying GPU devices for a model instance. For example: ### Alternatives self.llm1 = LLM( model=model_name, tensor_parallel_size=tensor_parallel_size, limit_mm_per_prompt={"image": 25, "video": 1}, max_model_len=32700, gpu_memory_utilization=gpu_memory_utilization, device_config="cuda:0,cuda:1" # Explicitly assign GPUs ) self.llm2 = LLM( model=model_name, tensor_parallel_size=tensor_para...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 0, gpu_memory_utilization=gpu_memory_utilization, device_config="cuda:0,cuda:1" # Explicitly assign GPUs ) self.llm2 = LLM( model=model_name, tensor_parallel_size=tensor_parallel_size, limit_mm_per_prompt={"image": 25,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: if vllm supports explicitly specifying GPU devices for a model instance. feature request;stale ### 🚀 The feature, motivation and pitch Background I am working on a multi-agent inference process where each age...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: upports explicitly specifying GPU devices for a model instance. feature request;stale ### 🚀 The feature, motivation and pitch Background I am working on a multi-agent inference process where each agent is assigned to us...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature]: if vllm supports explicitly specifying GPU devices for a model instance. feature request;stale ### 🚀 The feature, motivation and pitch Background I am working on a multi-agent inference process where each age...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: rence process where each agent is assigned to use a separate model. When testing with two agents, I observed that vllm freezes when the second agent attempts to load its model. This prevents the second agent from functi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
