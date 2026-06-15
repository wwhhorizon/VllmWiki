# vllm-project/vllm#9127: [Bug]: Error Encountered in vLLM Benchmarking with Input Length greater than 8192 in Llama 3.1 405B Model

| 字段 | 值 |
| --- | --- |
| Issue | [#9127](https://github.com/vllm-project/vllm/issues/9127) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error Encountered in vLLM Benchmarking with Input Length greater than 8192 in Llama 3.1 405B Model

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug An issue has been identified when running throughput benchmarking for the Llama 3.1 405B model using the benchmark_throughput.py script with combined input and output lengths exceeding 8192. Despite Llama 3.1 supporting up to 128K prompt length, the benchmark script fails to accept input lengths over 8192 without encountering errors. **Please let me know if there are any specific configuration settings that might enable handling of larger prompt lengths without these errors.** ### Steps to reproduce: 1. Run benchmarking using below command `python benchmarks/benchmark_throughput.py --backend vllm --model "meta-llama/Llama-3.1-405B-Instruct" --input-len=7937 --output-len=256 --num-prompts=1 --tensor-parallel-size=8` ### Output ``` ARNING 10-07 11:54:43 rocm.py:13] `fork` method is not supported by ROCm. VLLM_WORKER_MULTIPROC_METHOD is overridden to `spawn` instead. /opt/conda/envs/py_3.10/lib/python3.10/site-packages/torchvision-0.16.1+fdea156-py3.10-linux-x86_64.egg/torchvision/io/image.py:13: UserWarning: Failed to load image Python extension: '/opt/conda/envs/py_3.10/lib/python3.10/site-packa...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: 2 without encountering errors. **Please let me know if there are any specific configuration settings that might enable handling of larger prompt lengths without these errors.** ### Steps to reproduce: 1. Run benchmarkin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: Encountered in vLLM Benchmarking with Input Length greater than 8192 in Llama 3.1 405B Model bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug An issue has been identified when...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: kv_cache_dtype='auto', quantization_param_path=None, device='auto', num_scheduler_steps=1, use_v2_block_manager=False, enable_prefix_caching=False, enable_chunked_prefill=False, max_num_batched_tokens=None, download_dir...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: lama-3.1-405B-Instruct', tokenizer='meta-llama/Llama-3.1-405B-Instruct', quantization=None, tensor_parallel_size=8, n=1, num_prompts=1, seed=0, hf_max_batch_size=None, trust_remote_code=False, max_model_len=None, dtype=...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: rompts=1 --tensor-parallel-size=8` ### Output ``` ARNING 10-07 11:54:43 rocm.py:13] `fork` method is not supported by ROCm. VLLM_WORKER_MULTIPROC_METHOD is overridden to `spawn` instead. /opt/conda/envs/py_3.10/lib/pyth...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
