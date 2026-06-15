# vllm-project/vllm#15105: [Bug]: Extremely slow inference + big waste of memory on 0.8.0

| 字段 | 值 |
| --- | --- |
| Issue | [#15105](https://github.com/vllm-project/vllm/issues/15105) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;gemm;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;oom;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Extremely slow inference + big waste of memory on 0.8.0

### Issue 正文摘录

### Your current environment 2xRTX3090 32GB RAM Driver Version: 570.124.04 nvcc --version: ``` nvcc: NVIDIA (R) Cuda compiler driver Copyright (c) 2005-2024 NVIDIA Corporation Built on Thu_Mar_28_02:18:24_PDT_2024 Cuda compilation tools, release 12.4, V12.4.131 Build cuda_12.4.r12.4/compiler.34097967_0 ``` ### 🐛 Describe the bug Hello! I've encountered an unpleasant bug: When I run Qwen QwQ in AWQ or GPTQ 4-bit quantization on version 0.8.0, the text generation speed is only 7 tokens per second, whereas on version 0.7.3 it was consistently 45 tokens per second. Additionally, memory consumption has sharply increased—while using the same context window that I used with 0.7.3, Qwen now throws a "CUDA out of memory" error. The issue was only resolved by adding the parameter `--disable-mm-preprocessor-cache`, which allowed Qwen AWQ to barely fit into two 3090 GPUs, consuming exactly 24068 MiB on each. On version 0.7.3, this number was only 19-20 GB. Please help me, I would be very grateful! The command I use to run both versions 0.8.0 and 0.7.3 is the same (except for the --disable-mm-preprocessor-cache option): ```bash CUDA_VISIBLE_DEVICES=0,1 CUDA_DEVICE_ORDER=PCI_BUS_ID CUDA_LAUNCH_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ory on 0.8.0 bug ### Your current environment 2xRTX3090 32GB RAM Driver Version: 570.124.04 nvcc --version: ``` nvcc: NVIDIA (R) Cuda compiler driver Copyright (c) 2005-2024 NVIDIA Corporation Built on Thu_Mar_28_02:18:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='Qwen_QwQ-32B-AWQ', task='auto', toke...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: type='auto', kv_cache_dtype='auto', max_model_len=30000, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: encountered an unpleasant bug: When I run Qwen QwQ in AWQ or GPTQ 4-bit quantization on version 0.8.0, the text generation speed is only 7 tokens per second, whereas on version 0.7.3 it was consistently 45 tokens per se...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: ``bash CUDA_VISIBLE_DEVICES=0,1 CUDA_DEVICE_ORDER=PCI_BUS_ID CUDA_LAUNCH_BLOCKING=1 vllm serve OPEA_QwQ-32B-int4-AutoRound-gptq-sym --dtype auto --api-key token-abc123 --host 0.0.0.0 --port 8000 --tensor-parallel-size 2...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
