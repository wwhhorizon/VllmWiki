# vllm-project/vllm#9191: [Bug]: AttributeError: '_OpNamespace' '_C_cache_ops' object has no attribute 'reshape_and_cache'

| 字段 | 值 |
| --- | --- |
| Issue | [#9191](https://github.com/vllm-project/vllm/issues/9191) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: AttributeError: '_OpNamespace' '_C_cache_ops' object has no attribute 'reshape_and_cache'

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Run `benchmark_latency.py --device cuda` from `main` branch git log --oneline ``` a3691b6b (HEAD -> main, origin/main, origin/HEAD) [Core][Frontend] Add Support for Inference Time mm_processor_kwargs (#9131) 8c746226 [Frontend] API support for beam search for MQLLMEngine (#9117) e1faa2a5 [misc] improve ux on readme (#9147) 80b57f00 [Intel GPU] Fix xpu decode input (#9145) 04c12f81 [misc] update utils to support comparing multiple settings (#9140) 8eeb8570 Add Slack to README (#9137) ``` Stacktrace ``` /home/dlovison/miniconda3/envs/vllm-env/bin/python /home/dlovison/github/vllm/benchmarks/benchmark_latency.py --device cuda WARNING 10-09 09:48:06 _custom_ops.py:18] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") /home/dlovison/github/vllm/vllm/connections.py:8: RuntimeWarning: Failed to read commit hash: No module named 'vllm._version' from vllm.version import __version__ as VLLM_VERSION Namespace(model='facebook/opt-125m', speculative_model=None, num_speculative_tokens=None, speculative_draft_tensor_parallel_size=None, tokenizer=None, quantization=None, tenso...

## 现有链接修复摘要

#9131 [Core][Frontend] Add Support for Inference Time mm_processor_kwargs | #9145 [Intel GPU] Fix xpu decode input

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: amespace' '_C_cache_ops' object has no attribute 'reshape_and_cache' bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Run `benchmark_latency.py --device cuda` from `main`...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: cy.py --device cuda WARNING 10-09 09:48:06 _custom_ops.py:18] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") /home/dlovison/github/vllm/vllm/connections.py:8: RuntimeWarning: Failed...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: t ### Model Input Dumps _No response_ ### 🐛 Describe the bug Run `benchmark_latency.py --device cuda` from `main` branch git log --oneline ``` a3691b6b (HEAD -> main, origin/main, origin/HEAD) [Core][Frontend] Add Suppo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ne, gpu_memory_utilization=0.9, load_format='auto', distributed_executor_backend=None, otlp_traces_endpoint=None) INFO 10-09 09:48:12 llm_engine.py:237] Initializing an LLM engine (vdev) with config: model='facebook/opt...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: okens=None, speculative_draft_tensor_parallel_size=None, tokenizer=None, quantization=None, tensor_parallel_size=1, input_len=32, output_len=128, batch_size=8, n=1, use_beam_search=False, num_iters_warmup=10, num_iters=...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#9131](https://github.com/vllm-project/vllm/pull/9131) | mentioned | 0.45 | [Core][Frontend] Add Support for Inference Time mm_processor_kwargs | [core][frontend] add support for inference time mm_processor_kwargs (#9131) 8c746226 [frontend] api support for beam search for mqllmengine (#9117) e1faa2a5 [misc] improve ux on r… |
| [#9145](https://github.com/vllm-project/vllm/pull/9145) | mentioned | 0.45 | [Intel GPU] Fix xpu decode input  | ove ux on readme (#9147) 80b57f00 [intel gpu] fix xpu decode input (#9145) 04c12f81 [misc] update utils to support comparing multiple settings (#9140) 8eeb8570 add slack to readme… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
