# vllm-project/vllm#1421: Llama-2 13B run on 2 RTX4090 GPU error

| 字段 | 值 |
| --- | --- |
| Issue | [#1421](https://github.com/vllm-project/vllm/issues/1421) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Llama-2 13B run on 2 RTX4090 GPU error

### Issue 正文摘录

hi, when i run Llama-2-13b-chat-hf on 2 RTX4090 GPUs, someting wrong. pytorch 2.0.1 cuda11.8 vllm0.2.1 python -m vllm.entrypoints.api_server --model llama2/Llama-2-13b-chat-hf/ --tensor-parallel-size 2 error: param[:loaded_weight.shape[0]].copy_(loaded_weight) RuntimeError: The size of tensor a (5120) must match the size of tensor b (4096) at non-singleton dimension 1 log: 2023-10-19 17:44:09,548 INFO worker.py:1642 -- Started a local Ray instance. INFO 10-19 17:44:12 llm_engine.py:72] Initializing an LLM engine with config: model='llama2/Llama-2-13b-chat-hf/', tokenizer='llama2/Llama-2-13b-chat-hf/', tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=2, quantization=None, seed=0) INFO 10-19 17:44:12 tokenizer.py:31] For some LLaMA V1 models, initializing the fast tokenizer may take a long time. To reduce the initialization time, consider using 'hf-internal-testing/llama-tokenizer' instead of the original tokenizer. Traceback (most recent call last): File "/usr/lib/python3.8/runpy.py", line 194, in _run_module_as_main return _run_code(code, main_globa...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: Llama-2 13B run on 2 RTX4090 GPU error hi, when i run Llama-2-13b-chat-hf on 2 RTX4090 GPUs, someting wrong. pytorch 2.0.1 cuda11.8 vllm0.2.1 python -m vllm.entrypoints.api_server --model llama2/Llama-2-13b-chat-hf/ --t
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=2, quantization=None, seed=0) INFO 10-19 17:44:12...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Llama-2 13B run on 2 RTX4090 GPU error hi, when i run Llama-2-13b-chat-hf on 2 RTX4090 GPUs, someting wrong. pytorch 2.0.1 cuda11.8 vllm0.2.1 python -m vllm.entrypoints.api_server --model llama2/Llama-2-13b-chat-hf/ --t...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: r_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=2, quantization=None, seed=0) INFO 10-19 17:...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ong time. To reduce the initialization time, consider using 'hf-internal-testing/llama-tokenizer' instead of the original tokenizer. Traceback (most recent call last): File "/usr/lib/python3.8/runpy.py", line 194, in _r...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
