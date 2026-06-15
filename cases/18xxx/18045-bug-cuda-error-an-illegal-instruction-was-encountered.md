# vllm-project/vllm#18045: [Bug]: CUDA error: an illegal instruction was encountered

| 字段 | 值 |
| --- | --- |
| Issue | [#18045](https://github.com/vllm-project/vllm/issues/18045) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;moe;operator |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: CUDA error: an illegal instruction was encountered

### Issue 正文摘录

### Your current environment 1、Docker image: vllm/vllm-openai:v0.8.5 2、Model: Qwen/Qwen3-235B-A22B-FP8 3、GPU：H20 4、Launch Parameters： `vllm serve /workspace/Qwen3-235B-A22B-FP8 --served-model-name=qwen3-235b --kv-cache-dtype fp8 --allow-credentials --trust-remote-code --gpu-memory-utilization=0.9 --port=30000 --host=0.0.0.0 --max-model-len=65536 --max-num-seqs=64 --tensor-parallel-size=4 --enable-expert-parallel --enable-reasoning --reasoning-parser deepseek_r1 --enable-auto-tool-choice --tool-call-parser hermes` ### 🐛 Describe the bug error logs: `INFO 05-12 19:01:18 [async_llm.py:252] Added request chatcmpl-3dd5c7cd8c134f3fa6e8fc27500cc840. (VllmWorker rank=3 pid=268) ERROR 05-12 19:01:18 [multiproc_executor.py:470] WorkerProc hit an exception. (VllmWorker rank=3 pid=268) ERROR 05-12 19:01:18 [multiproc_executor.py:470] Traceback (most recent call last): (VllmWorker rank=3 pid=268) ERROR 05-12 19:01:18 [multiproc_executor.py:470] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 465, in worker_busy_loop (VllmWorker rank=3 pid=268) ERROR 05-12 19:01:18 [multiproc_executor.py:470] output = func(*args, **kwargs) (VllmWorker rank=3 pid=268)...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #12 Implement preemption via recomputation & Refactor scheduling logic | #16 Add custom kernel for RMS normalization | #20 Optimize data movement | #21 Add ninja to dependency | #27 Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | #29 Memcpy kernel for flash attention | #32 Implement block copy kernel to optimize beam search

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: al instruction was encountered bug;stale ### Your current environment 1、Docker image: vllm/vllm-openai:v0.8.5 2、Model: Qwen/Qwen3-235B-A22B-FP8 3、GPU：H20 4、Launch Parameters： `vllm serve /workspace/Qwen3-235B-A22B-FP8 -...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: k=3 pid=268) ERROR 05-12 19:01:18 [multiproc_executor.py:470] return flashinfer_sample(probs, k, p, generators) (VllmWorker rank=3 pid=268) ERROR 05-12 19:01:18 [multiproc_executor.py:470] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: CUDA error: an illegal instruction was encountered bug;stale ### Your current environment 1、Docker image: vllm/vllm-openai:v0.8.5 2、Model: Qwen/Qwen3-235B-A22B-FP8 3、GPU：H20 4、Launch Parameters： `vllm serve /work...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ### Your current environment 1、Docker image: vllm/vllm-openai:v0.8.5 2、Model: Qwen/Qwen3-235B-A22B-FP8 3、GPU：H20 4、Launch Parameters： `vllm serve /workspace/Qwen3-235B-A22B-FP8 --served-model-name=qwen3-235b --kv-cache-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 1、Docker image: vllm/vllm-openai:v0.8.5 2、Model: Qwen/Qwen3-235B-A22B-FP8 3、GPU：H20 4、Launch Parameters： `vllm serve /workspace/Qwen3-235B-A22B-FP8 --served-model-name=qwen3-235b --kv-cache-dtype fp8 --allow-credentials...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | /local/lib/python3.12/dist-packages/torch/lib/libtorch_cuda.so) frame #4: <unknown function> + 0x10433c5 (0x7fa97b2673c5 in /usr/local/lib/python3.12/dist-packages/torch/lib/libto… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | ocal/lib/python3.12/dist-packages/torch/lib/libtorch_python.so) frame #6: <unknown function> + 0x6f30f (0x7fa9cd14d30f in /usr/local/lib/python3.12/dist-packages/torch/lib/libc10.… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | in /usr/local/lib/python3.12/dist-packages/torch/lib/libc10.so) frame #7: c10::tensorimpl::~tensorimpl() + 0x21b (0x7fa9cd14633b in /usr/local/lib/python3.12/dist-packages/torch/l… |
| [#12](https://github.com/vllm-project/vllm/pull/12) | mentioned | 0.45 | Implement preemption via recomputation & Refactor scheduling logic | /numpy/_core/_multiarray_umath.cpython-312-x86_64-linux-gnu.so) frame #12: /usr/bin/python3() [0x59bf80] frame #13: /usr/bin/python3() [0x53bea4] frame #14: /usr/bin/python3() [0x… |
| [#16](https://github.com/vllm-project/vllm/pull/16) | mentioned | 0.45 | Add custom kernel for RMS normalization | n/python3() [0x59bf5d] frame #15: /usr/bin/python3() [0x53bea4] frame #16: /usr/bin/python3() [0x59bf5d] frame #17: /usr/bin/python3() [0x53bea4] frame #18: /usr/bin/python3() [0x… |
| [#20](https://github.com/vllm-project/vllm/pull/20) | mentioned | 0.45 | Optimize data movement | n/python3() [0x59bf5d] frame #19: /usr/bin/python3() [0x59be14] frame #20: /usr/bin/python3() [0x59be14] frame #21: /usr/bin/python3() [0x57ccc0] frame #22: /usr/bin/python3() [0x… |
| [#21](https://github.com/vllm-project/vllm/pull/21) | mentioned | 0.45 | Add ninja to dependency | n/python3() [0x59be14] frame #20: /usr/bin/python3() [0x59be14] frame #21: /usr/bin/python3() [0x57ccc0] frame #22: /usr/bin/python3() [0x57bcf6] frame #23: /usr/bin/python3() [0x… |
| [#27](https://github.com/vllm-project/vllm/pull/27) | mentioned | 0.45 | Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | n/python3() [0x594d67] frame #26: /usr/bin/python3() [0x59bdd6] frame #27: _pyeval_evalframedefault + 0x50e7 (0x54cb27 in /usr/bin/python3) frame #28: pyeval_evalcode + 0x99 (0x61… |
| [#29](https://github.com/vllm-project/vllm/pull/29) | mentioned | 0.45 | Memcpy kernel for flash attention | rame #28: pyeval_evalcode + 0x99 (0x61d5b9 in /usr/bin/python3) frame #29: /usr/bin/python3() [0x6591db] frame #30: /usr/bin/python3() [0x654346] frame #31: pyrun_stringflags + 0x… |
| [#32](https://github.com/vllm-project/vllm/pull/32) | mentioned | 0.45 | Implement block copy kernel to optimize beam search | me #31: pyrun_stringflags + 0x63 (0x6503b3 in /usr/bin/python3) frame #32: pyrun_simplestringflags + 0x3e (0x6500be in /usr/bin/python3) frame #33: py_runmain + 0x4b2 (0x64d622 in… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
