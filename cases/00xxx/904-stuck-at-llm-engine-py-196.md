# vllm-project/vllm#904: stuck at llm_engine.py:196

| 字段 | 值 |
| --- | --- |
| Issue | [#904](https://github.com/vllm-project/vllm/issues/904) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> stuck at llm_engine.py:196

### Issue 正文摘录

``` 100%|████████████████████████████████████| 54584/54584 [00:06<00:00, 8619.58it/s] INFO 08-29 20:48:52 llm_engine.py:70] Initializing an LLM engine with config: model='llama2-MultiTQ-20230829-01', tokenizer='llama2-MultiTQ-20230829-01', tokenizer_mode=auto, trust_remote_code=False, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) INFO 08-29 20:48:52 tokenizer.py:29] For some LLaMA-based models, initializing the fast tokenizer may take a long time. To eliminate the initialization time, consider using 'hf-internal-testing/llama-tokenizer' instead of the original tokenizer. INFO 08-29 20:49:14 llm_engine.py:196] # GPU blocks: 1981, # CPU blocks: 512 ``` I use 54584 prompts, it stucks at llm_engine.py:196 for 30 more minutes.....did anyone know how to solve this?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: s] INFO 08-29 20:48:52 llm_engine.py:70] Initializing an LLM engine with config: model='llama2-MultiTQ-20230829-01', tokenizer='llama2-MultiTQ-20230829-01', tokenizer_mode=auto, trust_remote_code=False, dtype=torch.floa...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ama2-MultiTQ-20230829-01', tokenizer_mode=auto, trust_remote_code=False, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) INFO 08-29 20:48:52 tokeniz...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: r='llama2-MultiTQ-20230829-01', tokenizer_mode=auto, trust_remote_code=False, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) INFO 08-29 20:48:52 to...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: time. To eliminate the initialization time, consider using 'hf-internal-testing/llama-tokenizer' instead of the original tokenizer. INFO 08-29 20:49:14 llm_engine.py:196] # GPU blocks: 1981, # CPU blocks: 512 ``` I use...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
