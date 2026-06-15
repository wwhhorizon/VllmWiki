# vllm-project/vllm#9198: [Bug]:  initializing multiple LLM classes simultaneously on the same GPU get an error

| 字段 | 值 |
| --- | --- |
| Issue | [#9198](https://github.com/vllm-project/vllm/issues/9198) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support |
| 子分类 | throughput |
| Operator 关键词 | cuda |
| 症状 | slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  initializing multiple LLM classes simultaneously on the same GPU get an error

### Issue 正文摘录

### Your current environment python: 3.8 cuda: 11.8 vllm: 0.5.5+cu118 ### Model Input Dumps _No response_ ### 🐛 Describe the bug my llm model is qwen2 1.5b，so i want to initialize multiple workers on one single GPU(T4，16G mem) for high throughput. but，when initializing multiple LLM classes simultaneously on the same GPU results in an error: **_ValueError: No available memory for the cache blocks. Try increasing gpu_memory_utilization when initializing the engine._** However, if initialized one by one sequentially, there is no problem. My code here，gpu_memory_utilization=0.4，so i can initialize 2 works. self.llm = LLM(model=model_path, tensor_parallel_size=1, enforce_eager=True, gpu_memory_utilization=0.4) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ame GPU get an error bug;stale ### Your current environment python: 3.8 cuda: 11.8 vllm: 0.5.5+cu118 ### Model Input Dumps _No response_ ### 🐛 Describe the bug my llm model is qwen2 1.5b，so i want to initialize multiple...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Your current environment python: 3.8 cuda: 11.8 vllm: 0.5.5+cu118 ### Model Input Dumps _No response_ ### 🐛 Describe the bug my llm model is qwen2 1.5b，so i want to initialize multiple workers on one single GPU(T4，16G m...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: nt to initialize multiple workers on one single GPU(T4，16G mem) for high throughput. but，when initializing multiple LLM classes simultaneously on the same GPU results in an error: **_ValueError: No available memory for...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: frequently asked questions. performance model_support cuda slowdown env_dependency Your current environment
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ame GPU results in an error: **_ValueError: No available memory for the cache blocks. Try increasing gpu_memory_utilization when initializing the engine._** However, if initialized one by one sequentially, there is no p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
