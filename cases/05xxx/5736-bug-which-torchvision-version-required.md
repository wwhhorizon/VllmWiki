# vllm-project/vllm#5736: [Bug]: which torchvision version required

| 字段 | 值 |
| --- | --- |
| Issue | [#5736](https://github.com/vllm-project/vllm/issues/5736) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization |
| 子分类 |  |
| Operator 关键词 | cuda;quantization |
| 症状 | crash;import_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: which torchvision version required

### Issue 正文摘录

/vllm_2$ python examples/phi3v_example.py WARNING 06-21 14:53:06 ray_utils.py:46] Failed to import Ray with ModuleNotFoundError("No module named 'ray'"). For multi-node inference, please install Ray with `pip install ray`. /home/sapidblue/SapidBlue/invoice_data_extraction/vllm_2/venv/lib/python3.10/site-packages/huggingface_hub/file_download.py:1132: FutureWarning: `resume_download` is deprecated and will be removed in version 1.0.0. Downloads always resume when possible. If you want to force a new download, use `force_download=True`. warnings.warn( INFO 06-21 14:53:08 llm_engine.py:164] Initializing an LLM engine (v0.5.0.post1) with config: model='microsoft/Phi-3-vision-128k-instruct', speculative_config=None, tokenizer='microsoft/Phi-3-vision-128k-instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, rope_scaling=None, rope_theta=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=8128, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto, quantization_param_path=None, device_config=cpu, decoding_config=DecodingC...

## 现有链接修复摘要

#5772 [Bugfix] Add phi3v resize for dynamic shape and fix torchvision requirement

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: pidBlue/invoice_data_extraction/vllm_2/venv/lib/python3.10/site-packages/huggingface_hub/file_download.py:1132: FutureWarning: `resume_download` is deprecated and will be removed in version 1.0.0. Downloads always resum...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: which torchvision version required bug /vllm_2$ python examples/phi3v_example.py WARNING 06-21 14:53:06 ray_utils.py:46] Failed to import Ray with ModuleNotFoundError("No module named 'ray'"). For multi-node infe...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: =None, rope_theta=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=8128, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, disable_custom_all_reduce=False, q...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: tokenizer='microsoft/Phi-3-vision-128k-instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, rope_scaling=None, rope_theta=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16,...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: =None, device_config=cpu, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None), seed=0, served_model_name=microsoft/Phi-3-vision-128k-in...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#5772](https://github.com/vllm-project/vllm/pull/5772) | closes_keyword | 0.95 | [Bugfix] Add phi3v resize for dynamic shape and fix torchvision requirement | FIX #5736 - Add image resize for phi3v to avoid error when passing dynamic shape image input (ref: #5767) - Add `torchvision` to cuda/cpu requirements.txt to prevent make user co |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
