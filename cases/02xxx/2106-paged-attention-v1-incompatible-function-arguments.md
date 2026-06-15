# vllm-project/vllm#2106: paged_attention_v1(): incompatible function arguments.

| 字段 | 值 |
| --- | --- |
| Issue | [#2106](https://github.com/vllm-project/vllm/issues/2106) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;quantization;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> paged_attention_v1(): incompatible function arguments.

### Issue 正文摘录

I start the server with the following command: `python -m vllm.entrypoints.api_server` output: ``` python -m vllm.entrypoints.api_server INFO 12-14 11:38:07 llm_engine.py:73] Initializing an LLM engine with config: model='facebook/opt-125m', tokenizer='facebook/opt-125m', tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=2048, download_dir=None, load_format=auto, tensor_parallel_size=1, quantization=None, seed=0) INFO 12-14 11:38:11 llm_engine.py:222] # GPU blocks: 22817, # CPU blocks: 7281 INFO: Started server process [142586] INFO: Waiting for application startup. INFO: Application startup complete. INFO: Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit) ``` Then i query it with: ``` curl http://localhost:8000/generate \ -d '{ "prompt": "San Francisco is a", "use_beam_search": true, "n": 4, "temperature": 0 }' ``` Error on the server: ``` INFO 12-14 11:30:02 llm_engine.py:649] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0% Exception in callback functools.partial( , req...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: rl http://localhost:8000/generate \ -d '{ "prompt": "San Francisco is a", "use_beam_search": true, "n": 4, "temperature": 0 }' ``` Error on the server: ``` INFO 12-14 11:30:02 llm_engine.py:649] Avg prompt throughput: 0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: er INFO 12-14 11:38:07 llm_engine.py:73] Initializing an LLM engine with config: model='facebook/opt-125m', tokenizer='facebook/opt-125m', tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=F...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=2048, download_dir=None, load_format=auto, tensor_parallel_size=1, quantization=None, seed=0) INFO 12-14 11:38:11...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: \ -d '{ "prompt": "San Francisco is a", "use_beam_search": true, "n": 4, "temperature": 0 }' ``` Error on the server: ``` INFO 12-14 11:30:02 llm_engine.py:649] Avg prompt throughput: 0.0 tokens/s, Avg generation throug...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: r_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=2048, download_dir=None, load_format=auto, tensor_parallel_size=1, quantization=None, seed=0) INFO 12-14 11:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
