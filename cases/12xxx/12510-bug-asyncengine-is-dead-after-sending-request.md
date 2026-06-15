# vllm-project/vllm#12510: [Bug]: Asyncengine is dead after sending request!

| 字段 | 值 |
| --- | --- |
| Issue | [#12510](https://github.com/vllm-project/vllm/issues/12510) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;model_support;quantization;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | kernel;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Asyncengine is dead after sending request!

### Issue 正文摘录

### Your current environment vllm version 0.6.6.post1 on 1A100 (redhat OS) ### Model Input Dumps DISTRIBUTED_BACKEND is mp and the gpu utilize is 0.95 ### 🐛 Describe the bug I have this issue when sending requests to `ibnzterrell/Meta-Llama-3.3-70B-Instruct-AWQ-INT4` model with vllm version 0.6.6.post1 on 1A100 (redhat OS) ``` /usr/bin/ld: cannot find -lcuda: No such file or directory collect2: error: ld returned 1 exit status INFO 01-28 13:42:20 model_runner_base.py:120] Writing input of failed execution to /tmp/err_execute_model_input_20250128-134220.pkl... INFO 01-28 13:42:20 model_runner_base.py:149] Completed writing input of failed execution to /tmp/err_execute_model_input_20250128-134220.pkl. ERROR 01-28 13:42:20 async_llm_engine.py:68] Engine background task failed ERROR 01-28 13:42:20 async_llm_engine.py:68] Traceback (most recent call last): ERROR 01-28 13:42:20 async_llm_engine.py:68] File "/usr/local/lib/python3.10/dist-packages/vllm/worker/model_runner_base.py", line 116, in _wrapper ERROR 01-28 13:42:20 async_llm_engine.py:68] return func(*args, **kwargs) ERROR 01-28 13:42:20 async_llm_engine.py:68] File "/usr/local/lib/python3.10/dist-packages/vllm/worker/model_runn...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: dead after sending request! bug;stale ### Your current environment vllm version 0.6.6.post1 on 1A100 (redhat OS) ### Model Input Dumps DISTRIBUTED_BACKEND is mp and the gpu utilize is 0.95 ### 🐛 Describe the bug I have...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ue when sending requests to `ibnzterrell/Meta-Llama-3.3-70B-Instruct-AWQ-INT4` model with vllm version 0.6.6.post1 on 1A100 (redhat OS) ``` /usr/bin/ld: cannot find -lcuda: No such file or directory collect2: error: ld...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: st! bug;stale ### Your current environment vllm version 0.6.6.post1 on 1A100 (redhat OS) ### Model Input Dumps DISTRIBUTED_BACKEND is mp and the gpu utilize is 0.95 ### 🐛 Describe the bug I have this issue when sending...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ion 0.6.6.post1 on 1A100 (redhat OS) ### Model Input Dumps DISTRIBUTED_BACKEND is mp and the gpu utilize is 0.95 ### 🐛 Describe the bug I have this issue when sending requests to `ibnzterrell/Meta-Llama-3.3-70B-Instruct...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: llm_engine.py:68] logits = _apply_logits_processors(logits, sampling_metadata) ERROR 01-28 13:42:20 async_llm_engine.py:68] File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/layers/logits_processor.py",...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
