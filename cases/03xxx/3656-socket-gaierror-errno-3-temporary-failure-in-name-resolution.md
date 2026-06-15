# vllm-project/vllm#3656: socket.gaierror: [Errno -3] Temporary failure in name resolution

| 字段 | 值 |
| --- | --- |
| Issue | [#3656](https://github.com/vllm-project/vllm/issues/3656) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;quantization |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> socket.gaierror: [Errno -3] Temporary failure in name resolution

### Issue 正文摘录

### Your current environment python离线环境： 执行 >>> from vllm import LLM >>> llm = LLM(model="Qwen-14B-Chat-Int4",trust_remote_code=True) ### 🐛 Describe the bug 打印如下 WARNING 03-27 08:29:20 config.py:193] gptq quantization is not fully optimized yet. The speed can be slower than non-quantized models. INFO 03-27 08:29:20 llm_engine.py:87] Initializing an LLM engine with config: model='Qwen-14B-Chat-Int4', tokenizer='Qwen-14B-Chat-Int4', tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.float16, max_seq_len=2048, download_dir=None, load_format=auto, tensor_parallel_size=1, disable_custom_all_reduce=False, quantization=gptq, enforce_eager=False, kv_cache_dtype=auto, device_config=cuda, seed=0) WARNING 03-27 08:29:21 tokenizer.py:64] Using a slow tokenizer. This might cause a significant slowdown. Consider using a fast tokenizer instead. Traceback (most recent call last): File "/usr/local/lib/python3.8/dist-packages/vllm/utils.py", line 176, in get_ip s.connect(("dns.google", 80)) # Doesn't need to be reachable socket.gaierror: [Errno -3] Temporary failure in name resolution During handling of the above exception, another exception occurred: T...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: thon离线环境： 执行 >>> from vllm import LLM >>> llm = LLM(model="Qwen-14B-Chat-Int4",trust_remote_code=True) ### 🐛 Describe the bug 打印如下 WARNING 03-27 08:29:20 config.py:193] gptq quantization is not fully optimized yet. The...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: rrent environment python离线环境： 执行 >>> from vllm import LLM >>> llm = LLM(model="Qwen-14B-Chat-Int4",trust_remote_code=True) ### 🐛 Describe the bug 打印如下 WARNING 03-27 08:29:20 config.py:193] gptq quantization is not fully...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: esolution bug ### Your current environment python离线环境： 执行 >>> from vllm import LLM >>> llm = LLM(model="Qwen-14B-Chat-Int4",trust_remote_code=True) ### 🐛 Describe the bug 打印如下 WARNING 03-27 08:29:20 config.py:193] gptq...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: antization=gptq, enforce_eager=False, kv_cache_dtype=auto, device_config=cuda, seed=0) WARNING 03-27 08:29:21 tokenizer.py:64] Using a slow tokenizer. This might cause a significant slowdown. Consider using a fast token...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: e, load_format=auto, tensor_parallel_size=1, disable_custom_all_reduce=False, quantization=gptq, enforce_eager=False, kv_cache_dtype=auto, device_config=cuda, seed=0) WARNING 03-27 08:29:21 tokenizer.py:64] Using a slow...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
