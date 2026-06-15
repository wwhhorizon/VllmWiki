# vllm-project/vllm#24062: 20-series GPUs do not support the `sinks` parameter; attempting to access it directly raises an error. Could you fix this

| 字段 | 值 |
| --- | --- |
| Issue | [#24062](https://github.com/vllm-project/vllm/issues/24062) |
| 状态 | closed |
| 标签 | stale;gpt-oss |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cache;cuda;operator;quantization |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> 20-series GPUs do not support the `sinks` parameter; attempting to access it directly raises an error. Could you fix this

### Issue 正文摘录

https://github.com/vllm-project/vllm/blob/a344a5aa0a58cc1758d9721e848ce1f5ca4b6c7f/vllm/attention/layer.py#L148 PS C:\Users\y> docker run --runtime nvidia --gpus all -v C:/Users/y/model/.cache/huggingface:/root/.cache/huggingface -p 8000:8000 --ipc=host vllm/vllm-openai:latest --model unsloth/gpt-oss-20b-unsloth-bnb-4bit INFO 09-01 19:03:21 [__init__.py:241] Automatically detected platform cuda. (APIServer pid=1) INFO 09-01 19:03:23 [api_server.py:1805] vLLM API server version 0.10.1.1 (APIServer pid=1) INFO 09-01 19:03:23 [utils.py:326] non-default args: {'model': 'unsloth/gpt-oss-20b-unsloth-bnb-4bit'} (APIServer pid=1) INFO 09-01 19:03:33 [__init__.py:711] Resolved architecture: GptOssForCausalLM (APIServer pid=1) INFO 09-01 19:03:33 [__init__.py:1750] Using max model len 131072 (APIServer pid=1) WARNING 09-01 19:03:34 [__init__.py:1171] bitsandbytes quantization is not fully optimized yet. The speed can be slower than non-quantized models. (APIServer pid=1) WARNING 09-01 19:03:34 [arg_utils.py:1770] Compute Capability ", line 198, in _run_module_as_main (APIServer pid=1) File " ", line 88, in _run_code (APIServer pid=1) File "/usr/local/lib/python3.12/dist-packages/vllm/entryp...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: c1758d9721e848ce1f5ca4b6c7f/vllm/attention/layer.py#L148 PS C:\Users\y> docker run --runtime nvidia --gpus all -v C:/Users/y/model/.cache/huggingface:/root/.cache/huggingface -p 8000:8000 --ipc=host vllm/vllm-openai:lat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: it INFO 09-01 19:03:21 [__init__.py:241] Automatically detected platform cuda. (APIServer pid=1) INFO 09-01 19:03:23 [api_server.py:1805] vLLM API server version 0.10.1.1 (APIServer pid=1) INFO 09-01 19:03:23 [utils.py:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: tempting to access it directly raises an error. Could you fix this stale;gpt-oss https://github.com/vllm-project/vllm/blob/a344a5aa0a58cc1758d9721e848ce1f5ca4b6c7f/vllm/attention/layer.py#L148 PS C:\Users\y> docker run...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: (APIServer pid=1) WARNING 09-01 19:03:34 [__init__.py:1171] bitsandbytes quantization is not fully optimized yet. The speed can be slower than non-quantized models. (APIServer pid=1) WARNING 09-01 19:03:34 [arg_utils.py...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: he/huggingface -p 8000:8000 --ipc=host vllm/vllm-openai:latest --model unsloth/gpt-oss-20b-unsloth-bnb-4bit INFO 09-01 19:03:21 [__init__.py:241] Automatically detected platform cuda. (APIServer pid=1) INFO 09-01 19:03:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
