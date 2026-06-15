# vllm-project/vllm#1949: torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 3.50 GiB. GPU 0 has a total capacty of 23.64 GiB of which 1.42 GiB is free. Process 2722 has 22.22 GiB memory in use. Of the allocated memory 20.13 GiB is allocated by PyTorch, and 1.75 GiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting max_split_size_mb to avoid fragmentation.  See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF

| 字段 | 值 |
| --- | --- |
| Issue | [#1949](https://github.com/vllm-project/vllm/issues/1949) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;gemm_linear;model_support;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization |
| 症状 | crash;oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 3.50 GiB. GPU 0 has a total capacty of 23.64 GiB of which 1.42 GiB is free. Process 2722 has 22.22 GiB memory in use. Of the allocated memory 20.13 GiB is allocated by PyTorch, and 1.75 GiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting max_split_size_mb to avoid fragmentation.  See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF

### Issue 正文摘录

Cannot allocate memory using AWQ and Mistral based model. ``` WARNING 12-06 19:09:20 config.py:140] awq quantization is not fully optimized yet. The speed can be slower than non-quantized models. INFO 12-06 19:09:20 llm_engine.py:73] Initializing an LLM engine with config: model='TheBloke/dolphin-2.1-mistral-7B-AWQ', tokenizer='TheBloke/dolphin-2.1-mistral-7B-AWQ', tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=1, quantization=awq, seed=0) Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained. Traceback (most recent call last): File "app.py", line 140, in engine = AsyncLLMEngine.from_engine_args(engine_args) File "/usr/local/lib/python3.8/dist-packages/vllm/engine/async_llm_engine.py", line 495, in from_engine_args engine = cls(parallel_config.worker_use_ray, File "/usr/local/lib/python3.8/dist-packages/vllm/engine/async_llm_engine.py", line 269, in __init__ self.engine = self._init_engine(*args, **kwargs) File "/usr/local/lib/python3.8/dist-packages/vllm/engine/async_llm_engine.py",...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: , load_format=auto, tensor_parallel_size=1, quantization=awq, seed=0) Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained. Traceback (most recent call las...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: and Mistral based model. ``` WARNING 12-06 19:09:20 config.py:140] awq quantization is not fully optimized yet. The speed can be slower than non-quantized models. INFO 12-06 19:09:20 llm_engine.py:73] Initializing an LL...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 3.50 GiB. GPU 0 has a total capacty of 23.64 GiB of which 1.42 GiB is free. Process 2722 has 22.22 GiB memory in use. Of the allocated memory 20.13 GiB...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: TORCH_CUDA_ALLOC_CONF Cannot allocate memory using AWQ and Mistral based model. ``` WARNING 12-06 19:09:20 config.py:140] awq quantization is not fully optimized yet. The speed can be slower than non-quantized models. I...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: r_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=1, quantization=awq, seed=0) Special tokens...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
