# vllm-project/vllm#7304: [Usage]: how to save sharded state?

| 字段 | 值 |
| --- | --- |
| Issue | [#7304](https://github.com/vllm-project/vllm/issues/7304) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cuda;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: how to save sharded state?

### Issue 正文摘录

### Your current environment I am trying to host large models that require multi gpu. I am trying to use the script to shard the model. I download model from huggingface, then run the script. ``` python3 examples/save_sharded_state.py --model /vllm-workspace/falcon-40b --tensor-parallel-size 4 --output /output --gpu-memory-utilization 0.93 024-08-08 14:42:48,643 INFO worker.py:1781 -- Started a local Ray instance. INFO 08-08 14:42:50 llm_engine.py:161] Initializing an LLM engine (v0.4.3) with config: model='/vllm-workspace/falcon-40b', speculative_config=None, tokenizer='/vllm-workspace/falcon-40b', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, rope_scaling=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=2048, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=4, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto, quantization_param_path=None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), seed=0, served_model_name=/vllm-workspace/falcon-40b) /opt/venv/lib/python3.10/site-packages/transformers/tokenization_utils_base.py:160...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: tention-2 backend because the vllm_flash_attn package is not found. `pip install vllm-flash-attn` for better performance. (RayWorkerWrapper pid=5687) INFO 08-08 14:42:58 selector.py:51] Using XFormers backend. INFO 08-0...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ne, rope_scaling=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=2048, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=4, disable_custom_all_reduce=False, q...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ded state? usage ### Your current environment I am trying to host large models that require multi gpu. I am trying to use the script to shard the model. I download model from huggingface, then run the script. ``` python...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), seed=0, served_model_name=/vllm-workspace/falcon-40b) /opt/venv/lib/python3.10/site-packages/transformers/tokenization_utils_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: =False, kv_cache_dtype=auto, quantization_param_path=None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), seed=0, served_model_name=/vllm-workspace/falcon-40b) /opt/venv/lib/pyth...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
