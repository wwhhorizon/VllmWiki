# vllm-project/vllm#5951: [Usage]: Can't support Phi-3-medium-* models with more than 2 GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#5951](https://github.com/vllm-project/vllm/issues/5951) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | cuda;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Can't support Phi-3-medium-* models with more than 2 GPUs

### Issue 正文摘录

### Your current environment When I set `VLLM_TENSOR_PARALLEL_SIZE = 2`, it works well. But when I change it to 4, vllm can not support Phi3-medium-*. ``` torch=2.3.0 vllm=0.5.0.post1 transformers=4.42.0.dev0 ``` I also see the same problem in other issues and discussion [https://github.com/vllm-project/vllm/discussions/5500](https://github.com/vllm-project/vllm/discussions/5500) ### 🐛 Describe the bug Models and parameters ``` INFO 06-28 07:44:00 llm_engine.py:161] Initializing an LLM engine (v0.5.0.post1) with config: model='/data/zhaopengfeng/models/Phi-3-mediu m-4k-instruct', speculative_config=None, tokenizer='/data/zhaopengfeng/models/Phi-3-medium-4k-instruct', skip_tokenizer_init=False, tokeni zer_mode=auto, revision=None, rope_scaling=None, rope_theta=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.float16, ma x_seq_len=4096, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=4, disable_custom_all_reduce=True, quantization=None, enforce_eager=True, kv_cache_dtype=auto, quantization_param_path=None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding _backend='outlines'), seed=0, served_model_name=/data/zhaopengfeng/models...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: Can't support Phi-3-medium-* models with more than 2 GPUs usage ### Your current environment When I set `VLLM_TENSOR_PARALLEL_SIZE = 2`, it works well. But when I change it to 4, vllm can not support Phi3-mediu...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: =None, rope_theta=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.float16, ma x_seq_len=4096, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=4, disable_custom_all_reduce=True, qu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ith config: model='/data/zhaopengfeng/models/Phi-3-mediu m-4k-instruct', speculative_config=None, tokenizer='/data/zhaopengfeng/models/Phi-3-medium-4k-instruct', skip_tokenizer_init=False, tokeni zer_mode=auto, revision...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: one, device_config=cuda, decoding_config=DecodingConfig(guided_decoding _backend='outlines'), seed=0, served_model_name=/data/zhaopengfeng/models/Phi-3-medium-4k-instruct) ``` Error infomation ```(RayWorkerWrapper pid=5...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ment frontend_api;model_support;quantization cuda;quantization dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
