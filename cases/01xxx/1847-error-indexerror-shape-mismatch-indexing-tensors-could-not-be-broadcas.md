# vllm-project/vllm#1847: [Error] "IndexError: shape mismatch: indexing tensors could not be broadcast together with shapes"  when logprobs > 0

| 字段 | 值 |
| --- | --- |
| Issue | [#1847](https://github.com/vllm-project/vllm/issues/1847) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Error] "IndexError: shape mismatch: indexing tensors could not be broadcast together with shapes"  when logprobs > 0

### Issue 正文摘录

When I use `logprobs > 0`, the `IndexError` occurs after 500~1000 iters. ## Trace ``` Traceback (most recent call last): File "/path/to/repo/src/vllm-generate.py", line 179, in outputs = llm.generate( ^^^^^^^^^^^^^ File "/path/to/conda/env/lib/python3.11/site-packages/vllm/entrypoints/llm.py", line 157, in generate return self._run_engine(use_tqdm) ^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/path/to/conda/env/lib/python3.11/site-packages/vllm/entrypoints/llm.py", line 177, in _run_engine step_outputs = self.llm_engine.step() ^^^^^^^^^^^^^^^^^^^^^^ File "/path/to/conda/env/lib/python3.11/site-packages/vllm/engine/llm_engine.py", line 562, in step output = self._run_workers( ^^^^^^^^^^^^^^^^^^ File "/path/to/conda/env/lib/python3.11/site-packages/vllm/engine/llm_engine.py", line 700, in _run_workers output = executor(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^^^^^ File "/path/to/conda/env/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 115, in decorate_context return func(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^ File "/path/to/conda/env/lib/python3.11/site-packages/vllm/worker/worker.py", line 370, in execute_model output = self.model( ^^^^^^^^^^^ File "/path/to/conda/env/lib/python3....

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: de=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=1, quantization=None, seed=42) ```
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ib/python3.11/site-packages/vllm/worker/worker.py", line 370, in execute_model output = self.model( ^^^^^^^^^^^ File "/path/to/conda/env/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_c...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: dcast together with shapes [2199], [2171] ``` ## Other Info ### `vllm` version `vllm` version: `0.2.2` ### SamplingParams ``` sampling_params = SamplingParams(n=5, best_of=5, presence_penalty=0.0, frequency_penalty=0.0,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Error] "IndexError: shape mismatch: indexing tensors could not be broadcast together with shapes" when logprobs > 0 stale When I use `logprobs > 0`, the `IndexError` occurs after 500~1000 iters. ## Trace ``` Traceback...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Error] "IndexError: shape mismatch: indexing tensors could not be broadcast together with shapes" when logprobs > 0 stale When I use `logprobs > 0`, the `IndexError` occurs after 500~1000 iters. ## Trace ``` Traceback...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
