# vllm-project/vllm#30061: [Bug]: Value error, Tensor parallel size (2) cannot be larger than the number of available GPUs (1).

| 字段 | 值 |
| --- | --- |
| Issue | [#30061](https://github.com/vllm-project/vllm/issues/30061) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;scheduler_memory;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Value error, Tensor parallel size (2) cannot be larger than the number of available GPUs (1).

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The following is the detailed error. The reason for the error is traced to vllm/config/parallel. py. There is a problem with the processing logic on line 566 ``` gpu_count = cuda_device_count_stateless() raise ValueError( f"Tensor parallel size ({self.world_size}) cannot be " f"larger than the number of available GPUs ({gpu_count})." ) ``` The historical code can run successfully： ``` if not ray_found: raise ValueError( "Unable to load Ray: " f"{ray_utils.ray_import_err}. Ray is " "required for multi-node inference, " "please install Ray with `pip install " "ray`." ) backend = "ray" ``` The following is the detailed error ``` INFO 12-04 21:21:11 [scheduler.py:216] Chunked prefill is enabled with max_num_batched_tokens=2048. (APIServer pid=2382) INFO 12-04 21:21:11 [api_server.py:1977] vLLM API server version 0.11.2 (APIServer pid=2382) INFO 12-04 21:21:11 [utils.py:253] non-default args: {'model_tag': '/models/Qwen3-VL-30B-A3B-Instruct', 'host': '0.0.0.0', 'uvicorn_log_level': 'debug', 'model': '/models/Qwen3-VL-30B-A3B-Instruct', 'served_model_name': ['Qwen3-VL-30B-A3B-Instruct'], 'tensor_parallel_size': 2, 'gpu_memory_utilizati...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: "Unable to load Ray: " f"{ray_utils.ray_import_err}. Ray is " "required for multi-node inference, " "please install Ray with `pip install " "ray`." ) ba
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: lowing is the detailed error. The reason for the error is traced to vllm/config/parallel. py. There is a problem with the processing logic on line 566 ``` gpu_count = cuda_device_count_stateless() raise ValueError( f"Te...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: lel size (2) cannot be larger than the number of available GPUs (1). bug;stale ### Your current environment ### 🐛 Describe the bug The following is the detailed error. The reason for the error is traced to vllm/config/p...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: " "ray`." ) backend = "ray" ``` The following is the detailed error ``` INFO 12-04 21:21:11 [scheduler.py:216] Chunked prefill is enabled with max_num_batched_tokens=2048. (APIServer pid=2382) INFO 12-04 21:21:11 [api_s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: em with the processing logic on line 566 ``` gpu_count = cuda_device_count_stateless() raise ValueError( f"Tensor parallel size ({self.world_size}) cannot be " f"larger than the number of available GPUs ({gpu_count})."

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
