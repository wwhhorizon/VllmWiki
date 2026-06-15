# vllm-project/vllm#14994: [Bug]: asyncio.exceptions.CancelledError and engine_client.dead_error

| 字段 | 值 |
| --- | --- |
| Issue | [#14994](https://github.com/vllm-project/vllm/issues/14994) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: asyncio.exceptions.CancelledError and engine_client.dead_error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I start the vllm engine like this: ```python model_name=config["model_name"] model_path = config["model_path"] max_model_len=config["max_model_len"] max_num_seqs=config["max_num_seqs"] max_num_batched_tokens= config["max_num_batched_tokens"] tp_size=config["tp_size"] nodes = config["nodes"] gpu_memory_utilization=config['gpu_memory_utilization'] served_model_name = [BaseModelPath(name=model_name, model_path=model_path)] engine_args=AsyncEngineArgs(max_num_seqs=max_num_seqs, gpu_memory_utilization=gpu_memory_utilization, model=model_path, served_model_name=served_model_name, tensor_parallel_size=tp_size, pipeline_parallel_size=nodes, max_model_len=max_model_len, max_num_batched_tokens=max_num_batched_tokens, enforce_eager=False, trust_remote_code=True, enable_chunked_prefill=True, device="cuda", distributed_executor_backend="ray" ) engine = AsyncLLMEngine.from_engine_args(engine_args) ``` and the key config info is: ```yaml model_name: "Deepseek-V3-671B" max_num_seqs: 32 max_model_len: 4096 max_num_batched_tokens: 4096 tp_size: 8 nodes: 1 gpu_memory_utilization: 0.98 ``` Error: After submitting many rounds of requests, the service...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: device="cuda", distributed_executor_backend="ray" ) engine = AsyncLLMEngine.from_engine_args(engine_args) ``` and the key config info is: ```yaml model_name: "Deepseek-V3-671B" max_num_seqs: 32 max_model_len: 4096 max_n...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: asyncio.exceptions.CancelledError and engine_client.dead_error bug;stale ### Your current environment ### 🐛 Describe the bug I start the vllm engine like this: ```python model_name=config["model_name"] model_path...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Bug]: asyncio.exceptions.CancelledError and engine_client.dead_error bug;stale ### Your current environment ### 🐛 Describe the bug I start the vllm engine like this: ```python model_name=config["model_name"] model_path...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: enable_chunked_prefill=True, device="cuda", distributed_executor_backend="ray" ) engine = AsyncLLMEngine.from_engine_args(engine_args) ``` and the key config info is: ```yaml model_name: "Deeps
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ### 🐛 Describe the bug I start the vllm engine like this: ```python model_name=config["model_name"] model_path = config["model_path"] max_model_len=config["max_model_len"] max_num_seqs=config["max_num_seqs"] max_num_bat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
