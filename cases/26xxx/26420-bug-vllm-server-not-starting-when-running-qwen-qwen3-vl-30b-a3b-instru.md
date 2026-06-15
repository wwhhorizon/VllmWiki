# vllm-project/vllm#26420: [Bug]: vLLM server not starting when running Qwen/Qwen3-VL-30B-A3B-Instruct on 2 A6000 GPUs. 

| 字段 | 值 |
| --- | --- |
| Issue | [#26420](https://github.com/vllm-project/vllm/issues/26420) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;gemm;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM server not starting when running Qwen/Qwen3-VL-30B-A3B-Instruct on 2 A6000 GPUs. 

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running Qwen/Qwen3-VL-30B-A3B-Instruct on 2 A6000 GPUs with below given command: ```vllm serve Qwen/Qwen3-VL-30B-A3B-Instruct --limit-mm-per-prompt.video 0 --gpu-memory-utilization 0.8 --max-model-len 32000 --mm-processor-cache-gb 0 --tensor-parallel-size 2``` keeps giving the same log of ```[shm_broadcast.py:466] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation).``` ~~~ vllm serve Qwen/Qwen3-VL-30B-A3B-Instruct --tensor-parallel-size 2 --limit-mm-per-prompt.video 0 --max-model-len 32000 --gpu-memory-utilization 0.8 --mm-processor-cache-gb 0 INFO 10-09 16:53:54 [__init__.py:216] Automatically detected platform cuda. (APIServer pid=106121) INFO 10-09 16:54:04 [api_server.py:1839] vLLM API server version 0.11.0 (APIServer pid=106121) INFO 10-09 16:54:04 [utils.py:233] non-default args: {'model_tag': 'Qwen/Qwen3-VL-30B-A3B-Instruct', 'model': 'Qwen/Qwen3-VL-30B-A3B-Instruct', 'max_model_len': 32000, 'tensor_parallel_size': 2, 'gpu_memory_utilization': 0.8, 'limit_mm_per_prompt': {'video': 0}, 'mm_processor_cache_...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: arting when running Qwen/Qwen3-VL-30B-A3B-Instruct on 2 A6000 GPUs. bug;stale ### Your current environment ### 🐛 Describe the bug Running Qwen/Qwen3-VL-30B-A3B-Instruct on 2 A6000 GPUs with below given command: ```vllm...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ver pid=106121) INFO 10-09 16:54:04 [api_server.py:1839] vLLM API server version 0.11.0 (APIServer pid=106121) INFO 10-09 16:54:04 [utils.py:233] non-default args: {'model_tag': 'Qwen/Qwen3-VL-30B-A3B-Instruct', 'model'...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: vLLM server not starting when running Qwen/Qwen3-VL-30B-A3B-Instruct on 2 A6000 GPUs. bug;stale ### Your current environment ### 🐛 Describe the bug Running Qwen/Qwen3-VL-30B-A3B-Instruct on 2 A6000 GPUs with belo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser=''), observability_con...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: INFO 10-09 16:53:54 [__init__.py:216] Automatically detected platform cuda. (APIServer pid=106121) INFO 10-09 16:54:04 [api_server.py:1839] vLLM API server version 0.11.0 (APIServer pid=106121) INFO 10-09 16:54:04 [util...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
