# vllm-project/vllm#19490: [Bug] [TPU]: OOMing on Llama-8B on new vllm nightly docker

| 字段 | 值 |
| --- | --- |
| Issue | [#19490](https://github.com/vllm-project/vllm/issues/19490) |
| 状态 | closed |
| 标签 | bug;tpu;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;gemm;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] [TPU]: OOMing on Llama-8B on new vllm nightly docker

### Issue 正文摘录

### Your current environment OOMing on serving llama-8B-Instruct: ```text root@t1v-n-82109f0e-w-0:/opt# vllm serve meta-llama/Llama-3.1-8B-Instruct --max-model-len 8192 WARNING:root:libtpu.so and TPU device found. Setting PJRT_DEVICE=TPU. INFO 06-11 13:55:34 [__init__.py:244] Automatically detected platform tpu. INFO 06-11 13:55:34 [tpu.py:215] tpu_commons not found, using vLLM's TpuPlatform INFO 06-11 13:55:37 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform. INFO 06-11 13:55:38 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform. INFO 06-11 13:55:38 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform. INFO 06-11 13:55:39 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform. INFO 06-11 13:55:39 [api_server.py:1287] vLLM API server version 0.9.1rc2.dev5+g6cd4ae8ac INFO 06-11 13:55:39 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform. INFO 06-11 13:55:39 [cli_args.py:309] non-default args: {'model': 'meta-llama/Llama-3.1-8B-Ins...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug] [TPU]: OOMing on Llama-8B on new vllm nightly docker bug;tpu;stale ### Your current environment OOMing on serving llama-8B-Instruct: ```text root@t1v-n-82109f0e-w-0:/opt# vllm serve meta-llama/Llama-3.1-8B-Instruc...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug] [TPU]: OOMing on Llama-8B on new vllm nightly docker bug;tpu;stale ### Your current environment OOMing on serving llama-8B-Instruct: ```text root@t1v-n-82109f0e-w-0:/opt# vllm serve meta-llama/Llama-3.1-8B-Instruc...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ride_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=8192, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: kv_cache_dtype=auto, device_config=None, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug] [TPU]: OOMing on Llama-8B on new vllm nightly docker bug;tpu;stale ### Your current environment OOMing on serving llama-8B-Instruct: ```text root@t1v-n-82109f0e-w-0:/opt# vllm serve meta-llama/Llama-3.1-8B-Instruc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
