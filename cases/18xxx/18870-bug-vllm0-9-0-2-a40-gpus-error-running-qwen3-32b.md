# vllm-project/vllm#18870: [Bug]: vllm0.9.0  2 A40 GPUs  Error running Qwen3-32B

| 字段 | 值 |
| --- | --- |
| Issue | [#18870](https://github.com/vllm-project/vllm/issues/18870) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm0.9.0  2 A40 GPUs  Error running Qwen3-32B

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # Launch command： export CUDA_VISIBLE_DEVICES=0,1 && vllm serve /data/Qwen/Qwen3-32B/ --api-key sk-xOnaVCLlbGokppfa1cC17c4aEfA043919d202f01C41bA818 --tensor-parallel-size 2 --max-model-len 32768 --port 20023 --served-model-name qwen3-32b --reasoning-parser qwen3 --enable-auto-tool-choice --tool-call-parser hermes # Full debug level log ``` DEBUG 05-29 01:16:05 [__init__.py:28] No plugins for group vllm.platform_plugins found. DEBUG 05-29 01:16:05 [__init__.py:34] Checking if TPU platform is available. DEBUG 05-29 01:16:05 [__init__.py:44] TPU platform is not available because: No module named 'libtpu' DEBUG 05-29 01:16:05 [__init__.py:51] Checking if CUDA platform is available. DEBUG 05-29 01:16:05 [__init__.py:71] Confirmed CUDA platform is available. DEBUG 05-29 01:16:05 [__init__.py:99] Checking if ROCm platform is available. DEBUG 05-29 01:16:05 [__init__.py:113] ROCm platform is not available because: No module named 'amdsmi' DEBUG 05-29 01:16:05 [__init__.py:120] Checking if HPU platform is available. DEBUG 05-29 01:16:05 [__init__.py:127] HPU platform is not available because habana_frameworks is not found. DEBUG 05-29 01:...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='xgrammar', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend='qwen3'), observab...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: lugins to load. INFO 05-29 01:16:10 [api_server.py:1289] vLLM API server version 0.9.0 INFO 05-29 01:16:10 [cli_args.py:300] non-default args: {'port': 20023, 'api_key': 'sk-xOnaVCLlbGokppfa1cC17c4aEfA043919d202f01C41bA...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ride_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=2, pipeline_parallel_size=1, disable...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: current environment ### 🐛 Describe the bug # Launch command： export CUDA_VISIBLE_DEVICES=0,1 && vllm serve /data/Qwen/Qwen3-32B/ --api-key sk-xOnaVCLlbGokppfa1cC17c4aEfA043919d202f01C41bA818 --tensor-parallel-size 2 --m...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: vllm0.9.0 2 A40 GPUs Error running Qwen3-32B bug ### Your current environment ### 🐛 Describe the bug # Launch command： export CUDA_VISIBLE_DEVICES=0,1 && vllm serve /data/Qwen/Qwen3-32B/ --api-key sk-xOnaVCLlbGok...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
