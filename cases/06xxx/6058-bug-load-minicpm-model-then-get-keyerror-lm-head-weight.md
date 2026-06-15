# vllm-project/vllm#6058: [Bug]: load minicpm model, then get KeyError: 'lm_head.weight'

| 字段 | 值 |
| --- | --- |
| Issue | [#6058](https://github.com/vllm-project/vllm/issues/6058) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: load minicpm model, then get KeyError: 'lm_head.weight'

### Issue 正文摘录

### Your current environment vllm-0.5.0 vllm-flash-attn-2.5.9 transformers-4.42.3 torch-2.3.0 xformers-0.0.26.post1 flash-attn-2.5.6 cuda 11.6 ### 🐛 Describe the bug 2024-07-02 14:26:25,987 INFO worker.py:1771 -- Started a local Ray instance. INFO 07-02 14:26:26 llm_engine.py:161] Initializing an LLM engine (v0.5.0) with config: model='/mnt/data/user/luca_model/klara/models/unified_ai_platform_sft_white/v20240702122118/train-model', speculative_config=None, tokenizer='/mnt/data/user/luca_model/klara/models/unified_ai_platform_sft_white/v20240702122118/train-model', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, rope_scaling=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=4096, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=2, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto, quantization_param_path=None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), seed=42, served_model_name=/mnt/data/user/luca_model/klara/models/unified_ai_platform_sft_white/v20240702122118/train-model) /home/jeeves/.local/lib/python3.10/site-package...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: '/home/jeeves/.local/lib/python3.10/site-packages/torchvision/image.so: undefined symbol: _ZN3c1017RegisterOperatorsD1Ev'If you don't plan on using image functionality from `torchvision.io`, you can ignore this warning....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: one, rope_scaling=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=4096, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=2, disable_custom_all_reduce=False, q...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: load minicpm model, then get KeyError: 'lm_head.weight' bug ### Your current environment vllm-0.5.0 vllm-flash-attn-2.5.9 transformers-4.42.3 torch-2.3.0 xformers-0.0.26.post1 flash-attn-2.5.6 cuda 11.6 ### 🐛 Des...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: klara/models/unified_ai_platform_sft_white/v20240702122118/train-model', speculative_config=None, tokenizer='/mnt/data/user/luca_model/klara/models/unified_ai_platform_sft_white/v20240702122118/train-model', skip_tokeni...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), seed=42, served_model_name=/mnt/data/user/luca_model/klara/models/unified_ai_platform_sft_white/v20240702122118/train-model)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
