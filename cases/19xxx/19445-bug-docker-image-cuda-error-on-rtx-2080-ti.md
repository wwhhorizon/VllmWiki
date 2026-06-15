# vllm-project/vllm#19445: [Bug]: Docker image CUDA error on RTX 2080 Ti

| 字段 | 值 |
| --- | --- |
| Issue | [#19445](https://github.com/vllm-project/vllm/issues/19445) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda;quantization |
| 症状 | crash;import_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Docker image CUDA error on RTX 2080 Ti

### Issue 正文摘录

### Your current environment ``` ψ python3 collect_env.py Traceback (most recent call last): File "/home/arkadi/collect_env.py", line 17, in import regex as re ModuleNotFoundError: No module named 'regex' ``` ### 🐛 Describe the bug The project-provided Docker `vllm/vllm-openai` 0.6.4.post1, v0.8.4, v0.8.5.post1, v0.9.0.1, v0.9.1 images doesn't work on a system with RTX 2080 Ti > NVIDIA-SMI 570.133.07 Driver Version: 570.133.07 CUDA Version: 12.8 The container runtime is configured correctly. Ollama, Whisper, Riva works no problem in Containerd environment. > time=2025-06-10T18:53:03.106Z level=INFO source=types.go:130 msg="inference compute" id=GPU-30de6d51-b12f-ca41-1081-26dbd109b1c2 library=cuda variant=v12 compute=7.5 driver=12.8 name="NVIDIA GeForce RTX 2080 Ti" total="10.6 GiB" available="10.4 GiB" ``` INFO 06-10 11:43:59 [__init__.py:244] Automatically detected platform cuda. WARNING 06-10 11:44:03 [utils.py:1416] argument 'device' is deprecated INFO 06-10 11:44:03 [api_server.py:1287] vLLM API server version 0.9.1rc1 INFO 06-10 11:44:03 [cli_args.py:309] non-default args: {'model': 'Qwen/Qwen2.5-7B-Instruct-AWQ', 'max_model_len': 16000, 'max_seq_len_to_capture': 16000, 'ser...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug]: Docker image CUDA error on RTX 2080 Ti bug;stale ### Your current environment ``` ψ python3 collect_env.py Traceback (most recent call last): File "/home/arkadi/collect_env.py", line 17, in import regex as re M
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: Docker image CUDA error on RTX 2080 Ti bug;stale ### Your current environment ``` ψ python3 collect_env.py Traceback (most recent call last): File "/home/arkadi/collect_env.py", line 17, in import regex as re Mod...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ver Version: 570.133.07 CUDA Version: 12.8 The container runtime is configured correctly. Ollama, Whisper, Riva works no problem in Containerd environment. > time=2025-06-10T18:53:03.106Z level=INFO source=types.go:130...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Docker image CUDA error on RTX 2080 Ti bug;stale ### Your current environment ``` ψ python3 collect_env.py Traceback (most recent call last): File "/home/arkadi/collect_env.py", line 17, in import regex as re Mod...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: v_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig (backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
