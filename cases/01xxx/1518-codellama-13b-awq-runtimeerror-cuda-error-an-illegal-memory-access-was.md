# vllm-project/vllm#1518: codellama-13b-awq RuntimeError: CUDA error: an illegal memory access was encountered

| 字段 | 值 |
| --- | --- |
| Issue | [#1518](https://github.com/vllm-project/vllm/issues/1518) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | cold_start |
| Operator 关键词 | cuda;kernel;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> codellama-13b-awq RuntimeError: CUDA error: an illegal memory access was encountered

### Issue 正文摘录

When I use the above method for inference with Codellama, I encounter CUDA kernel errors. Please help me understand why? @TheBloke WARNING: WatchFiles detected changes in 'fastapi_vllm_codellama.py'. Reloading... INFO 10-31 16:58:55 llm_engine.py:72] Initializing an LLM engine with config: model='./CodeLlama-13B-AWQ', tokenizer='./CodeLlama-13B-AWQ', tokenizer_mode=auto, revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=16384, download_dir=None, load_format=auto, tensor_parallel_size=1, quantization=awq, seed=0) INFO 10-31 16:58:55 tokenizer.py:30] For some LLaMA V1 models, initializing the fast tokenizer may take a long time. To reduce the initialization time, consider using 'hf-internal-testing/llama-tokenizer' instead of the original tokenizer. Process SpawnProcess-46: Traceback (most recent call last): File "/mnt/gpu/code/miniconda/envs/code/lib/python3.10/multiprocessing/process.py", line 315, in _bootstrap self.run() File "/mnt/gpu/code/miniconda/envs/code/lib/python3.10/multiprocessing/process.py", line 108, in run self._target(*self._args, **self._kwargs) File "/mnt/gpu/code/miniconda/envs/code/lib/python3.10/site-packages/uvicorn/_subprocess.py", li...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: hon3.10/site-packages/uvicorn/server.py", line 61, in run return asyncio.run(self.serve(sockets=sockets)) File "/mnt/gpu/code/miniconda/envs/code/lib/python3.10/asyncio/runners.py", line 44, in run return loop.run_until...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: codellama-13b-awq RuntimeError: CUDA error: an illegal memory access was encountered When I use the above method for inference with Codellama, I encounter CUDA kernel errors. Please help me understand why? @TheBloke WAR...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: a-13B-AWQ', tokenizer_mode=auto, revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=16384, download_dir=None, load_format=auto, tensor_parallel_size=1, quantization=awq, seed=0) INFO 10-31 16:58:55...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: eLlama-13B-AWQ', tokenizer_mode=auto, revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=16384, download_dir=None, load_format=auto, tensor_parallel_size=1, quantization=awq, seed=0) INFO 10-31 16:...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ong time. To reduce the initialization time, consider using 'hf-internal-testing/llama-tokenizer' instead of the original tokenizer. Process SpawnProcess-46: Traceback (most recent call last): File "/mnt/gpu/code/minico...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
