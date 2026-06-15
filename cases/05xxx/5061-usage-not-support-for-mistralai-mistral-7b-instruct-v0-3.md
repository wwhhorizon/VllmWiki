# vllm-project/vllm#5061: [Usage]: not support for mistralai/Mistral-7B-Instruct-v0.3

| 字段 | 值 |
| --- | --- |
| Issue | [#5061](https://github.com/vllm-project/vllm/issues/5061) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | attention;cuda;operator;quantization |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: not support for mistralai/Mistral-7B-Instruct-v0.3

### Issue 正文摘录

### Your current environment vllm version: 0.4.2 ``` CUDA_VISIBLE_DEVICES=6 python -m vllm.entrypoints.openai.api_server \ > --model mistralai/Mistral-7B-Instruct-v0.3 \ > --dtype auto --api-key "yyy" --port 1703 ``` error message: > INFO 05-26 20:11:31 llm_engine.py:100] Initializing an LLM engine (v0.4.2) with config: model='mistralai/Mistral-7B-Instruct-v0.3', speculative_config=None, tokenizer='mistralai/Mistral-7B-Instruct-v0.3', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto, quantization_param_path=None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), seed=0, served_model_name=mistralai/Mistral-7B-Instruct-v0.3) > You set `add_prefix_space`. The tokenizer needs to be converted from the slow tokenizers > INFO 05-26 20:11:32 utils.py:660] Found nccl from library /home/chenyanan/.config/vllm/nccl/cu12/libnccl.so.2.18.1 > INFO 05-26 20:11:35 selector.py:27] Using FlashAtt...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: tralai/Mistral-7B-Instruct-v0.3 usage ### Your current environment vllm version: 0.4.2 ``` CUDA_VISIBLE_DEVICES=6 python -m vllm.entrypoints.openai.api_server \ > --model mistralai/Mistral-7B-Instruct-v0.3 \ > --dtype a...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: api_server \ > --model mistralai/Mistral-7B-Instruct-v0.3 \ > --dtype auto --api-key "yyy" --port 1703 ``` error message: > INFO 05-26 20:11:31 llm_engine.py:100] Initializing an LLM engine (v0.4.2) with config: model='...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: SIBLE_DEVICES=6 python -m vllm.entrypoints.openai.api_server \ > --model mistralai/Mistral-7B-Instruct-v0.3 \ > --dtype auto --api-key "yyy" --port 1703 ``` error message: > INFO 05-26 20:11:31 llm_engine.py:100] Initia...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), seed=0, served_model_name=mistralai/Mistral-7B-Instruct-v0.3) > You set `add_prefix_space`. The tokenizer needs to be convert...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: struct-v0.3 usage ### Your current environment vllm version: 0.4.2 ``` CUDA_VISIBLE_DEVICES=6 python -m vllm.entrypoints.openai.api_server \ > --model mistralai/Mistral-7B-Instruct-v0.3 \ > --dtype auto --api-key "yyy"...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
