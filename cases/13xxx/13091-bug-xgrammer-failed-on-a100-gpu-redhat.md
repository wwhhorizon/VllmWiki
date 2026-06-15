# vllm-project/vllm#13091: [Bug]: xgrammer failed on A100 GPU (Redhat)

| 字段 | 值 |
| --- | --- |
| Issue | [#13091](https://github.com/vllm-project/vllm/issues/13091) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;kernel;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: xgrammer failed on A100 GPU (Redhat)

### Issue 正文摘录

### Your current environment - vllm==0.6.6.post1 - FROM nvidia/cuda:12.1.0-runtime-ubuntu22.04 - Python 3.9 - RedHat ### How would you like to use vllm The issue occurs when running the model on an A100 GPU on RedHat, but it works on a T4 GPU on RedHat and an A10 on Ubuntu. The problem is likely related to compatibility issues with xgrammar’s use of Triton, CUDA, or NVIDIA drivers on the A100 GPU in the RedHat environment. ``` /usr/bin/ld: cannot find -lcuda: No such file or directory collect2: error: ld returned 1 exit status INFO 01-28 17:10:28 model_runner_base.py:120] Writing input of failed execution to /tmp/err_execute_model_input_20250128-171028.pkl... INFO 01-28 17:10:28 model_runner_base.py:149] Completed writing input of failed execution to /tmp/err_execute_model_input_20250128-171028.pkl. ERROR 01-28 17:10:28 async_llm_engine.py:68] Engine background task failed ERROR 01-28 17:10:28 async_llm_engine.py:68] Traceback (most recent call last): ERROR 01-28 17:10:28 async_llm_engine.py:68] File "/usr/local/lib/python3.10/dist-packages/vllm/worker/model_runner_base.py", line 116, in _wrapper ERROR 01-28 17:10:28 async_llm_engine.py:68] return func(*args, **kwargs) ERROR 01-28...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: e 80, in __init__ ERROR 01-28 17:10:28 async_llm_engine.py:68] mod = compile_module_from_src(Path(os.path.join(dirname, "driver.c")).read_text(), "cuda_utils") ERROR 01-28 17:10:28 async_llm_engine.py:68] File "/usr/loc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: xgrammer failed on A100 GPU (Redhat) usage;stale ### Your current environment - vllm==0.6.6.post1 - FROM nvidia/cuda:12.1.0-runtime-ubuntu22.04 - Python 3.9 - RedHat ### How would you like to use vllm The issue o...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: problem is likely related to compatibility issues with xgrammar’s use of Triton, CUDA, or NVIDIA drivers on the A100 GPU in the RedHat environment. ``` /usr/bin/ld: cannot find -lcuda: No such file or directory collect2...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: llm_engine.py:68] logits = _apply_logits_processors(logits, sampling_metadata) ERROR 01-28 17:10:28 async_llm_engine.py:68] File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/layers/logits_processor.py",...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: t ### How would you like to use vllm The issue occurs when running the model on an A100 GPU on RedHat, but it works on a T4 GPU on RedHat and an A10 on Ubuntu. The problem is likely related to compatibility issues with...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
