# vllm-project/vllm#13329: [Bug]: issue about the gguf model's --compilation-config options

| 字段 | 值 |
| --- | --- |
| Issue | [#13329](https://github.com/vllm-project/vllm/issues/13329) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: issue about the gguf model's --compilation-config options

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug GPU environment: Tesla V100-SXM2-16GB [x2] I tried to reason about the Nemo gguf quantization model with the --compilation-config option introduced in version 0.7.0 and it obviously failed. So I'm wondering if the gguf quantization model doesn't support --compilation-config right now? Also, how can I use this --compilation-config option? Attach the command to the api server: ```text TORCH_LOGS="+dynamo" TORCHDYNAMO_VERBOSE=1 VLLM_LOGGING_LEVEL=DEBUG vllm serve ./Mistral-Nemo-Instruct-2407-Q4_K_M.gguf --tokenizer ./Mistral-Nemo-Instruct-2407 --tensor-parallel-size 2 --dtype half --kv-cache-dtype auto --max-model-len 4096 --gpu-memory-utilization 0.95 -O3 ``` And the Error logs: ```text DEBUG 02-15 11:05:16 __init__.py:26] No plugins for group vllm.platform_plugins found. INFO 02-15 11:05:16 __init__.py:183] Automatically detected platform cuda. WARNING 02-15 11:05:16 cuda.py:32] You are using a deprecated `pynvml` package. Please install `nvidia-ml-py` instead, and make sure to uninstall `pynvml`. When both of them are installed, `pynvml` will take precedence and cause errors. See https://pypi.org/project/pynvml for more informati...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: [Bug]: issue about the gguf model's --compilation-config options bug;stale ### Your current environment ### 🐛 Describe the bug GPU environment: Tesla V100-SXM2-16GB [x2] I tried to reason about the Nemo gguf quantizatio...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: uf quantization model with the --compilation-config option introduced in version 0.7.0 and it obviously failed. So I'm wondering if the gguf quantization model doesn't support --compilation-config right now? Also, how c...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ronment: Tesla V100-SXM2-16GB [x2] I tried to reason about the Nemo gguf quantization model with the --compilation-config option introduced in version 0.7.0 and it obviously failed. So I'm wondering if the gguf quantiza...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: issue about the gguf model's --compilation-config options bug;stale ### Your current environment ### 🐛 Describe the bug GPU environment: Tesla V100-SXM2-16GB [x2] I tried to reason about the Nemo gguf quantizatio...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: dtype='half', kv_cache_dtype='auto', max_model_len=4096, guided_decoding_backend='xgrammar', logits_processor_pattern=None, distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel_size=2, max_parall...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
