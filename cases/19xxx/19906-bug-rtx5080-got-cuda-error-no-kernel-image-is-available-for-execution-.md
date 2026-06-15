# vllm-project/vllm#19906: [Bug]: RTX5080 got CUDA error: no kernel image is available for execution on the device

| 字段 | 值 |
| --- | --- |
| Issue | [#19906](https://github.com/vllm-project/vllm/issues/19906) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RTX5080 got CUDA error: no kernel image is available for execution on the device

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am trying to run Qwen/Qwen2.5-14B-Instruct-AWQ on my server. I am using below command to run it. ``` python3 -m vllm.entrypoints.openai.api_server --model Qwen/Qwen2.5-14B-Instruct-AWQ --port 8000 --tensor-parallel-size 2 --trust-remote-code --quantization awq ``` and then i got this error Got RuntimeError: Worker failed with error 'CUDA error: no kernel image is available for execution on the device CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect Full log here ``` INFO 06-20 12:26:06 [__init__.py:244] Automatically detected platform cuda. INFO 06-20 12:26:12 [api_server.py:1287] vLLM API server version 0.9.1 INFO 06-20 12:26:12 [cli_args.py:309] non-default args: {'model': 'Qwen/Qwen2.5-14B-Instruct-AWQ', 'trust_remote_code': True, 'quantization': 'awq', 'tensor_parallel_size': 2} INFO 06-20 12:26:27 [config.py:823] This model supports multiple tasks: {'reward', 'generate', 'classify', 'embed', 'score'}. Defaulting to 'generate'. INFO 06-20 12:26:32 [awq_marlin.py:120] Detected that the model can run with awq_marlin, however you specified quantization=awq e...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: platform cuda. INFO 06-20 12:26:12 [api_server.py:1287] vLLM API server version 0.9.1 INFO 06-20 12:26:12 [cli_args.py:309] non-default args: {'model': 'Qwen/Qwen2.5-14B-Instruct-AWQ', 'trust_remote_code': True, 'quanti...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: CUDA error: no kernel image is available for execution on the device bug;stale ### Your current environment ### 🐛 Describe the bug I am trying to run Qwen/Qwen2.5-14B-Instruct-AWQ on my server. I am using below command...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: RTX5080 got CUDA error: no kernel image is available for execution on the device bug;stale ### Your current environment ### 🐛 Describe the bug I am trying to run Qwen/Qwen2.5-14B-Instruct-AWQ on my server. I am u...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: -Instruct-AWQ --port 8000 --tensor-parallel-size 2 --trust-remote-code --quantization awq ``` and then i got this error Got RuntimeError: Worker failed with error 'CUDA error: no kernel image is available for execution...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
