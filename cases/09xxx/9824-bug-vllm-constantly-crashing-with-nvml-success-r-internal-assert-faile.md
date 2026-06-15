# vllm-project/vllm#9824: [Bug]: vllm constantly crashing with NVML_SUCCESS == r INTERNAL ASSERT FAILED at "../c10/cuda/CUDACachingAllocator.cpp":838, please report a bug to PyTorch. 

| 字段 | 值 |
| --- | --- |
| Issue | [#9824](https://github.com/vllm-project/vllm/issues/9824) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;frontend_api;model_support;multimodal_vlm;sampling_logits |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;sampling |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm constantly crashing with NVML_SUCCESS == r INTERNAL ASSERT FAILED at "../c10/cuda/CUDACachingAllocator.cpp":838, please report a bug to PyTorch. 

### Issue 正文摘录

### Your current environment H100 40GB (using MIG) ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` INFO: 38.32.112.203:56266 - "GET /v1/models HTTP/1.1" 200 OK INFO 10-29 18:38:36 logger.py:36] Received request chat-9df53213134647568f9172ae453ed0b9: prompt: 'Who are you?', params: SamplingParams(n=1, best_of=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.0, top_p=1.0, top_k=-1, min_p=0.0, seed=None, use_beam_search=False, length_penalty=1.0, early_stopping=> INFO 10-29 18:38:36 async_llm_engine.py:201] Added request chat-9df53213134647568f9172ae453ed0b9. INFO 10-29 18:38:37 metrics.py:351] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 5 reqs, Swapped: 0 reqs, Pending: 1 reqs, GPU KV cache usage: 91.8%, CPU KV cache usage: 0.0%. ERROR 10-29 18:38:39 async_llm_engine.py:58] Engine background task failed ERROR 10-29 18:38:39 async_llm_engine.py:58] Traceback (most recent call last): ERROR 10-29 18:38:39 async_llm_engine.py:58] File "/usr/local/lib/python3.12/dist-packages/vllm/worker/model_runner_base.py", line 112, in _wrapper ERROR 10-29 18:38:39 async_llm_engine.py:58] return func(*args,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: bug in torch. However, vllm should shutdown cleanly not hang, so e.g. docker restart always can restart and recover. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and ask...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: o PyTorch. bug ### Your current environment H100 40GB (using MIG) ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` INFO: 38.32.112.203:56266 - "GET /v1/models HTTP/1.1" 200 OK INFO 10-29 18:38:36 logger.py...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: tantly crashing with NVML_SUCCESS == r INTERNAL ASSERT FAILED at "../c10/cuda/CUDACachingAllocator.cpp":838, please report a bug to PyTorch. bug ### Your current environment H100 40GB (using MIG) ### Model Input Dumps _...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: 134647568f9172ae453ed0b9. INFO 10-29 18:38:37 metrics.py:351] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 5 reqs, Swapped: 0 reqs, Pending: 1 reqs, GPU KV cache usage: 91.8%, C...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: -29 18:38:39 async_llm_engine.py:58] out = torch.empty(output_shape, dtype=x.dtype, device=x.device) ERROR 10-29 18:38:39 async_llm_engine.py:58] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 10-29 18:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
