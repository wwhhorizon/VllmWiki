# vllm-project/vllm#24802: [Usage]: A KeyError occurred while running Qwen3-235B-A22B-Q4_KM (and int4_int8mix)

| 字段 | 值 |
| --- | --- |
| Issue | [#24802](https://github.com/vllm-project/vllm/issues/24802) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: A KeyError occurred while running Qwen3-235B-A22B-Q4_KM (and int4_int8mix)

### Issue 正文摘录

### Your current environment Running the quantized version of Qwen3-235B-A22B using the version 0.10.1 of vllm will result in KeyError errors. We have tried Qwen3-235B-A22B-Q4_K-M and Qwen3-235B-A22B-Thinking-2507-GPTQ-Int4-Int8Mix. Error info: ``` KeyError: 'layers.0.mlp.gate.weight' ``` The following are the relevant commands and error messages: The command to run is: ``` vllm serve /home/Models/Qwen3-235B-A22B-Q4_K_M/Qwen3-235B-A22B-Q4_K_M.gguf \ --tokenizer /home/Models/Qwen3-235B-A22B-Q4_K_M \ --hf-config-path /home/Models/Qwen3-235B-A22B-Q4_K_M \ --tensor-parallel-size 4 --max-model-len 1024 --gpu-memory-utilization 0.98 ``` The error message in the simplified version is: ``` (VllmWorker TP2 pid=1179) ERROR 09-13 01:23:43 [multiproc_executor.py:559] WorkerProc failed to start. (VllmWorker TP2 pid=1179) ERROR 09-13 01:23:43 [multiproc_executor.py:559] Traceback (most recent call last): (VllmWorker TP2 pid=1179) ERROR 09-13 01:23:43 [multiproc_executor.py:559] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 533, in worker_main (VllmWorker TP2 pid=1179) ERROR 09-13 01:23:43 [multiproc_executor.py:559] worker = WorkerProc(*args, **kwar...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: int8mix) usage;stale ### Your current environment Running the quantized version of Qwen3-235B-A22B using the version 0.10.1 of vllm will result in KeyError errors. We have tried Qwen3-235B-A22B-Q4_K-M and Qwen3-235B-A22...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: or occurred while running Qwen3-235B-A22B-Q4_KM (and int4_int8mix) usage;stale ### Your current environment Running the quantized version of Qwen3-235B-A22B using the version 0.10.1 of vllm will result in KeyError error...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Usage]: A KeyError occurred while running Qwen3-235B-A22B-Q4_KM (and int4_int8mix) usage;stale ### Your current environment Running the quantized version of Qwen3-235B-A22B using the version 0.10.1 of vllm will result...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: `` INFO 09-13 01:22:32 [__init__.py:241] Automatically detected platform cuda. (APIServer pid=782) INFO 09-13 01:22:34 [api_server.py:1805] vLLM API server version 0.10.1.1 (APIServer pid=782) INFO 09-13 01:22:34 [utils...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
