# vllm-project/vllm#1848: [Error] "ValueError: operands could not be broadcast together with shapes ..."  when using `prompt_token_ids`

| 字段 | 值 |
| --- | --- |
| Issue | [#1848](https://github.com/vllm-project/vllm/issues/1848) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Error] "ValueError: operands could not be broadcast together with shapes ..."  when using `prompt_token_ids`

### Issue 正文摘录

When I use `prompt_token_ids` of - `list` type - long prompt sequence length (>2048) the `ValueError` occurs before any iteration. ## Trace ``` ERROR worker.py:406 -- Unhandled error (suppress with 'RAY_IGNORE_UNHANDLED_ERRORS=1'): ray::RayWorker.execute_method() (pid=3863266, ip=..., actor_id=d2000cf13a6bc32e72a4173301000000, repr= ) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/path/to/conda/env/lib/python3.11/site-packages/vllm/engine/ray_utils.py", line 32, in execute_method return executor(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^^^^^ File "/path/to/conda/env/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 115, in decorate_context return func(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^ File "/path/to/conda/env/lib/python3.11/site-packages/vllm/worker/worker.py", line 366, in execute_model input_tokens, input_positions, input_metadata = self._prepare_inputs( ^^^^^^^^^^^^^^^^^^^^^ File "/path/to/conda/env/lib/python3.11/site-packages/vllm/worker/worker.py", line 176, in _prepare_inputs prompt_tokens = seq_data.get_token_ids() ^^^^^^^^^^^^^^^^^^^^^^^^ File "/path/to/conda/env/lib/python3.11/site-packages/vllm/sequence.py", line 85, in get_tok...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: de=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=1, quantization=None, seed=42) ```
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: oadcast together with shapes (2245,) (0,) ``` ## Other Info ### `vllm` version `vllm` version: `0.2.2` ### SamplingParams ``` sampling_params = SamplingParams(n=5, best_of=5, presence_penalty=0.0, frequency_penalty=0.0,...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: py", line 366, in execute_model input_tokens, input_positions, input_metadata = self._prepare_inputs( ^^^^^^^^^^^^^^^^^^^^^ File "/path/to/conda/env/lib/python3.11/site-packages/vllm/worker/worker.py", line 176, in _pre...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ib/python3.11/site-packages/vllm/worker/worker.py", line 366, in execute_model input_tokens, input_positions, input_metadata = self._prepare_inputs( ^^^^^^^^^^^^^^^^^^^^^ File "/path/to/conda/env/lib/python3.11/site-pac...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: enalty=1.0, temperature=0.3, top_p=0.95, top_k=-1, min_p=0.0, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=['Question:', 'Question', 'USER:', 'USER', 'ASSISTANT:', 'ASSISTANT', 'Instruction:', '...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
