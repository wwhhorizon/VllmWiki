# vllm-project/vllm#11232: [Bug]: With ROCm and certain HF models that require 'trust-remote-code', you get VLLM_RPC_TIMEOUT and failure to finish loading.

| 字段 | 值 |
| --- | --- |
| Issue | [#11232](https://github.com/vllm-project/vllm/issues/11232) |
| 状态 | closed |
| 标签 | bug;rocm;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: With ROCm and certain HF models that require 'trust-remote-code', you get VLLM_RPC_TIMEOUT and failure to finish loading.

### Issue 正文摘录

### Your current environment ### Model Input Dumps ``` (VllmWorkerProcess pid=5932) /opt/miniconda3/envs/vllm/lib/python3.10/site-packages/transformers/models/auto/image_processing_auto.py:524: FutureWarning: The image_processor_class argument is deprecated and will be removed in v4.42. Please use `slow_image_processor_class`, or `fast_image_processor_class` instead (VllmWorkerProcess pid=5932) warnings.warn( /opt/miniconda3/envs/vllm/lib/python3.10/site-packages/transformers/models/auto/image_processing_auto.py:524: FutureWarning: The image_processor_class argument is deprecated and will be removed in v4.42. Please use `slow_image_processor_class`, or `fast_image_processor_class` instead warnings.warn( (VllmWorkerProcess pid=5934) /opt/miniconda3/envs/vllm/lib/python3.10/site-packages/transformers/models/auto/image_processing_auto.py:524: FutureWarning: The image_processor_class argument is deprecated and will be removed in v4.42. Please use `slow_image_processor_class`, or `fast_image_processor_class` instead (VllmWorkerProcess pid=5934) warnings.warn( (VllmWorkerProcess pid=5933) /opt/miniconda3/envs/vllm/lib/python3.10/site-packages/transformers/models/auto/image_processing_au...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: With ROCm and certain HF models that require 'trust-remote-code', you get VLLM_RPC_TIMEOUT and failure to finish loading. bug;rocm;stale ### Your current environment ### Model Input Dumps ``` (VllmWorkerProcess p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ntrypoints/openai/api_server.py", line 649, in run_server async with build_async_engine_client(args) as engine_client: File "/opt/miniconda3/envs/vllm/lib/python3.10/contextlib.py", line 199, in __aenter__ return await...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: With ROCm and certain HF models that require 'trust-remote-code', you get VLLM_RPC_TIMEOUT and failure to finish loading. bug;rocm;stale ### Your current environment ### Model Input Dumps ``` (VllmWorkerProcess p...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 634-py3.10-linux-x86_64.egg/vllm/scripts.py", line 201, in main args.dispatch_function(args) File "/opt/miniconda3/envs/vllm/lib/python3.10/site-packages/vllm-0.6.4.post2.dev266+g7be15d93.rocm634-py3.10-linux-x86_64.egg...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: -code', you get VLLM_RPC_TIMEOUT and failure to finish loading. bug;rocm;stale ### Your current environment ### Model Input Dumps ``` (VllmWorkerProcess pid=5932) /opt/miniconda3/envs/vllm/lib/python3.10/site-packages/t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
