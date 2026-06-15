# vllm-project/vllm#2520: openapi running but "POST /v1/chat/completions HTTP/1.1" 404 Not Found

| 字段 | 值 |
| --- | --- |
| Issue | [#2520](https://github.com/vllm-project/vllm/issues/2520) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;operator;quantization |
| 症状 | oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> openapi running but "POST /v1/chat/completions HTTP/1.1" 404 Not Found

### Issue 正文摘录

I managed to install and get vllm working in windows wsl ubuntu, but I can't seem to get it to respond to any openapi requests. I keep getting the error message: "POST /v1/chat/completions HTTP/1.1" 404 Not Found I have forwarded ports in windows to wsl and textgen webui running in wsl works just fine with its openai api. ``` python -m vllm.entrypoints.api_server --model text-generation-webui/models/cognitivecomputations_dolphin-2.6-mistral-7b --tensor-parallel-size 2 2024-01-21 01:28:29,635 INFO worker.py:1724 -- Started a local Ray instance. INFO 01-21 01:28:30 llm_engine.py:70] Initializing an LLM engine with config: model='text-generation-webui/models/cognitivecomputations_dolphin-2.6-mistral-7b', tokenizer='text-generation-webui/models/cognitivecomputations_dolphin-2.6-mistral-7b', tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=2, quantization=None, enforce_eager=False, seed=0) INFO 01-21 01:28:57 llm_engine.py:275] # GPU blocks: 10974, # CPU blocks: 4096 WARNING 01-21 01:28:57 cache_engine.py:96] Using 'pin_memory=False' as WSL is detected...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=2, quantization=None, enforce_eager=False, seed...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ning but "POST /v1/chat/completions HTTP/1.1" 404 Not Found I managed to install and get vllm working in windows wsl ubuntu, but I can't seem to get it to respond to any openapi requests. I keep getting the error messag...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: t fine with its openai api. ``` python -m vllm.entrypoints.api_server --model text-generation-webui/models/cognitivecomputations_dolphin-2.6-mistral-7b --tensor-parallel-size 2 2024-01-21 01:28:29,635 INFO worker.py:172...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: r_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=2, quantization=None, enforce_eager=False,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: windows wsl ubuntu, but I can't seem to get it to respond to any openapi requests. I keep getting the error message: "POST /v1/chat/completions HTTP/1.1" 404 Not Found I have forwarded ports in windows to wsl and textge...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
