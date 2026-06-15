# vllm-project/vllm#5102: [Bug]: [WSL] no response when vllm.entrypoints.openai.api_server run

| 字段 | 值 |
| --- | --- |
| Issue | [#5102](https://github.com/vllm-project/vllm/issues/5102) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda;quantization |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [WSL] no response when vllm.entrypoints.openai.api_server run

### Issue 正文摘录

### Your current environment ```text (vLLM) USERNAME-wsl@USERNAME:~$ python -m vllm.entrypoints.openai.api_server --model MODELNAME ... ``` ### 🐛 Describe the bug INFO 05-29 21:12:40 llm_engine.py:100] Initializing an LLM engine (v0.4.2) with config: model='MODELS, speculative_config=None, tokenizer='TOKENIZER', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=4096, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto, quantization_param_path=None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), seed=0, served_model_name=MODELNAME) INFO 05-29 21:12:40 utils.py:660] Found nccl from library /home/USERNAME/.config/vllm/nccl/cu12/libnccl.so.2.18.1 WARNING 05-29 21:12:41 utils.py:465] Using 'pin_memory=False' as WSL is detected. This may slow down the performance. INFO 05-29 21:12:41 selector.py:27] Using FlashAttention-2 backend. ....and no response anymore. [ v ] Firewire Checked [ v ] can't see(grep)vllm port why no response? why stucked...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=4096, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, disable_custom_all_reduce=False, q...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: USERNAME-wsl@USERNAME:~$ python -m vllm.entrypoints.openai.api_server --model MODELNAME ... ``` ### 🐛 Describe the bug INFO 05-29 21:12:40 llm_engine.py:100] Initializing an LLM engine (v0.4.2) with config: model='MODEL...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), seed=0, served_model_name=MODELNAME) INFO 05-29 21:12:40 utils.py:660] Found nccl from library /home/USERNAME/.config/vllm/nc...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: odel_support;quantization attention;cuda;quantization slowdown dtype;env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: =False, kv_cache_dtype=auto, quantization_param_path=None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), seed=0, served_model_name=MODELNAME) INFO 05-29 21:12:40 utils.py:660] F...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
