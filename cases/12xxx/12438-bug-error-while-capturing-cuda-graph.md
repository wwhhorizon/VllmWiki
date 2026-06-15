# vllm-project/vllm#12438: [Bug]: Error while capturing CUDA graph

| 字段 | 值 |
| --- | --- |
| Issue | [#12438](https://github.com/vllm-project/vllm/issues/12438) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 |  |
| Operator 关键词 | attention;cache;cuda;kernel;operator |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error while capturing CUDA graph

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug # vLLM version My last commit is as follows: ``` commit 324960a95c00112ce6b9b858d9311da1597cfb8b (HEAD -> main, upstream/main, origin/main, origin/HEAD) [TPU][CI] Update torchxla version in requirement-tpu.txt (#12422) ``` It is just making an error right after I rebased my code to the latest version of vLLM. # What I did ``` python -m vllm.entrypoints.openai.api_server \ --model meta-llama/Llama-2-7b-hf \ --port 8087 \ --disable-custom-all-reduce \ --swap-space 0 \ --gpu-memory-utilization 0.8 ``` # Error message ``` Capturing CUDA graph shapes: 0%| | 0/35 [00:00<?, ?it/s] ERROR 01-26 05:16:05 engine.py:387] CUDA error: operation failed due to a previous error during capture ERROR 01-26 05:16:05 engine.py:387] CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. ERROR 01-26 05:16:05 engine.py:387] For debugging consider passing CUDA_LAUNCH_BLOCKING=1 ERROR 01-26 05:16:05 engine.py:387] Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. ERROR 01-26 05:16:05 engine.py:387] Traceback (most recent call last): ERROR...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ### Model Input Dumps _No response_ ### 🐛 Describe the bug # vLLM version My last commit is as follows: ``` commit 324960a95c00112ce6b9b858d9311da1597cfb8b (HEAD -> main, upstream/main, origin/main, origin/HEAD) [TPU][C...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: rror while capturing CUDA graph bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug # vLLM version My last commit is as follows: ``` commit 324960a95c00112ce6b9b858d9311da1597cfb8...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Error while capturing CUDA graph bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug # vLLM version My last commit is as follows: ``` commit 324960a95c00112ce6b9b858d9311da...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: 01-26 05:16:05 engine.py:387] For debugging consider passing CUDA_LAUNCH_BLOCKING=1 ERROR 01-26 05:16:05 engine.py:387] Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. ERROR 01-26 05:16:05 engine.py:...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: tadata) ERROR 01-26 05:16:05 engine.py:387] File "/vllm/vllm/attention/backends/xformers.py", line 529, in forward ERROR 01-26 05:16:05 engine.py:387] PagedAttention.write_to_paged_cache( ERROR 01-26 05:16:05 engine.py:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
