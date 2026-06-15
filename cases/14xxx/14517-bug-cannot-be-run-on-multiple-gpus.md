# vllm-project/vllm#14517: [Bug]: Cannot be run on multiple GPUs.

| 字段 | 值 |
| --- | --- |
| Issue | [#14517](https://github.com/vllm-project/vllm/issues/14517) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Cannot be run on multiple GPUs.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I tried running qwq-32b-gptq-int4 locally, and if it's a single GPU, it can run normally with the following command: ``` vllm serve /mnt/data/models/qwq-32b-gptq-int4 \ --gpu-memory-utilization 0.95 \ --max-model-len 3100 \ --dtype half \ --tensor-parallel-size 1 \ --enforce_eager \ --trust-remote-code \ --served-model-name "qwq-32b-gptq-int4" \ --host 0.0.0.0 \ --port 8000 ``` However, when using multiple GPUs, an error occurred. The command is: ``` export CUDA_VISIBLE_DEVICES=0,1 vllm serve /mnt/data/models/qwq-32b-gptq-int4 \ --gpu-memory-utilization 0.95 \ --max-model-len 3100 \ --dtype half \ --tensor-parallel-size 2 \ --enforce_eager \ --trust-remote-code \ --served-model-name "qwq-32b-gptq-int4" \ --host 0.0.0.0 \ --port 8000 ``` log： ``` INFO 03-09 19:52:13 __init__.py:207] Automatically detected platform cuda. INFO 03-09 19:52:13 api_server.py:912] vLLM API server version 0.7.3 INFO 03-09 19:52:13 api_server.py:913] args: Namespace(subparser='serve', model_tag='/mnt/data/models/qwq-32b-gptq-int4', config='', host='0.0.0.0', port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_metho...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: Cannot be run on multiple GPUs. bug;stale ### Your current environment ### 🐛 Describe the bug I tried running qwq-32b-gptq-int4 locally, and if it's a single GPU, it can run normally with the following command: `...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ed platform cuda. INFO 03-09 19:52:13 api_server.py:912] vLLM API server version 0.7.3 INFO 03-09 19:52:13 api_server.py:913] args: Namespace(subparser='serve', model_tag='/mnt/data/models/qwq-32b-gptq-int4', config='',...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ent environment ### 🐛 Describe the bug I tried running qwq-32b-gptq-int4 locally, and if it's a single GPU, it can run normally with the following command: ``` vllm serve /mnt/data/models/qwq-32b-gptq-int4 \ --gpu-memor...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: dtype='half', kv_cache_dtype='auto', max_model_len=3100, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: it can run normally with the following command: ``` vllm serve /mnt/data/models/qwq-32b-gptq-int4 \ --gpu-memory-utilization 0.95 \ --max-model-len 3100 \ --dtype half \ --tensor-parallel-size 1 \ --enforce_eager \ --tr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
