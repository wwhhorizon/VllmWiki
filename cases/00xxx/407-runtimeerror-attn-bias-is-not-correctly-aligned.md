# vllm-project/vllm#407: RuntimeError: attn_bias is not correctly aligned

| 字段 | 值 |
| --- | --- |
| Issue | [#407](https://github.com/vllm-project/vllm/issues/407) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | attention;cache;cuda;operator;sampling |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> RuntimeError: attn_bias is not correctly aligned

### Issue 正文摘录

Unable to handle request for model mosaicml/mpt-30b-chat ```INFO 07-09 00:49:58 llm_engine.py:60] Initializing an LLM engine with config: model='mosaicml/mpt-30b-chat', tokenizer='mosaicml/mpt-30b-chat', tokenizer_mode=auto, dtype=torch.bfloat16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) INFO 07-09 00:50:38 llm_engine.py:131] # GPU blocks: 716, # CPU blocks: 195 INFO: Started server process [89934] INFO: Waiting for application startup. INFO: Application startup complete. INFO: Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit) INFO 07-09 00:50:42 async_llm_engine.py:117] Received request cmpl-41fa40b022f54beaa423ec71c5c090e9: prompt: 'hello', sampling params: SamplingParams(n=1, best_of=1, presence_penalty=0.0, frequency_penalty=0.0, temperature=0.0, top_p=1.0, top_k=-1, use_beam_search=False, stop=[], ignore_eos=False, max_tokens=7, logprobs=None), prompt token ids: None. INFO 07-09 00:50:42 scheduler.py:269] Throughput: 0.0 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.1%, CPU KV cache usage: 0.0% INFO 07-09 00:50:42 async_llm_engine.py:196] Aborted request cmpl-41fa40b022f54...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: frequency_penalty=0.0, temperature=0.0, top_p=1.0, top_k=-1, use_beam_search=False, stop=[], ignore_eos=False, max_tokens=7, logprobs=None), prompt token ids: None. INFO 07-09 00:50:42 scheduler.py:269] Throughput: 0.0...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ion.py", line 352, in multi_query_kv_attention out = xops.memory_efficient_attention_forward( File "/home/ubuntu/miniconda3/envs/vllm/lib/python3.10/site-packages/xformers/ops/fmha/__init__.py", line 213, in memory_effi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: l/mpt-30b-chat', tokenizer='mosaicml/mpt-30b-chat', tokenizer_mode=auto, dtype=torch.bfloat16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) INFO 07-09 00:50:38 llm_en...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: RuntimeError: attn_bias is not correctly aligned bug Unable to handle request for model mosaicml/mpt-30b-chat ```INFO 07-09 00:49:58 llm_engine.py:60] Initializing an LLM engine with config: model='mosaicml/mpt-30b-chat...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: 0b-chat', tokenizer_mode=auto, dtype=torch.bfloat16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) INFO 07-09 00:50:38 llm_engine.py:131] # GPU blocks: 716, # CPU bloc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
