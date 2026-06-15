# vllm-project/vllm#15356: [Bug]: Executor performance degradation

| 字段 | 值 |
| --- | --- |
| Issue | [#15356](https://github.com/vllm-project/vllm/issues/15356) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;triton |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Executor performance degradation

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am currently using `vllm serve` to create an online server and using this server as a Scheduler to send and execute `ExecuteModelRequest` to one `LLM` instances created with `self.llm = LLM(model=self.model, gpu_memory_utilization=self.gpu_memory_utilization, enforce_eager=self.enforce_eager, tensor_parallel_size=self.tp_size)`. The inference is then performed by calling `self.llm.llm_engine.model_executor.execute_model(req)`. However, when I test using `vllm/benchmarks/benchmark_serving.py`, I notice a significant drop in inference performance, with both TTFT and TPOT increasing substantially, while directly using `vllm serve` for inference does not exhibit this issue. Is it possible that `vllm` has implemented some caching or optimizations above the Executor layer in the `LLMEngine`? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;scheduler_memory cuda;triton env_dependency Your current environment
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: `self.llm.llm_engine.model_executor.execute_model(req)`. However, when I test using `vllm/benchmarks/benchmark_serving.py`, I notice a significant drop in inference performance, with both TTFT and TPOT increasing substa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e`? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: using `vllm serve` to create an online server and using this server as a Scheduler to send and execute `ExecuteModelRequest` to one `LLM` instances created with `self.llm = LLM(model=self.model, gpu_memory_utilization=s...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rallel;frontend_api;hardware_porting;model_support;scheduler_memory cuda;triton env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
