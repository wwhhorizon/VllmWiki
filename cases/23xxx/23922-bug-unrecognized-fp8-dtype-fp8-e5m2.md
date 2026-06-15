# vllm-project/vllm#23922: [Bug]: Unrecognized FP8 dtype: fp8_e5m2

| 字段 | 值 |
| --- | --- |
| Issue | [#23922](https://github.com/vllm-project/vllm/issues/23922) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;model_support;quantization;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cuda;fp8 |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unrecognized FP8 dtype: fp8_e5m2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Vllm version vllm-openai:v0.10.1.1 ## CUDA version 12.8 ## Hardware 8*H20 ## start params: vllm serve /nvme0/qwen3-235b --trust-remote-code -tp 8 --served-model-name qwen3-235b-instruct-2507 --kv-cache-dtype fp8_e5m2 --enable-auto-tool-choice --tool-call-parser hermes --max-model-len 131072 --gpu-memory-utilization 0.9 ## model qwen3-235b ## error log [1;36m(VllmWorker TP5 pid=411)[0;0m ERROR 08-29 02:12:59 [multiproc_executor.py:596] WorkerProc hit an exception. [1;36m(VllmWorker TP5 pid=411)[0;0m ERROR 08-29 02:12:59 [multiproc_executor.py:596] Traceback (most recent call last): [1;36m(VllmWorker TP5 pid=411)[0;0m ERROR 08-29 02:12:59 [multiproc_executor.py:596] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 591, in worker_busy_loop [1;36m(VllmWorker TP5 pid=411)[0;0m ERROR 08-29 02:12:59 [multiproc_executor.py:596] output = func(*args, **kwargs) [1;36m(VllmWorker TP5 pid=411)[0;0m ERROR 08-29 02:12:59 [multiproc_executor.py:596] ^^^^^^^^^^^^^^^^^^^^^ [1;36m(VllmWorker TP5 pid=411)[0;0m ERROR 08-29 02:12:59 [multiproc_executor.py:596] File "/usr/local/lib/python3.12/dist-packages/...

## 现有链接修复摘要

#23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Unrecognized FP8 dtype: fp8_e5m2 bug;stale ### Your current environment ### 🐛 Describe the bug ## Vllm version vllm-openai:v0.10.1.1 ## CUDA version 12.8 ## Hardware 8*H20 ## start params: vllm serve /nvme0/qwen3...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: g;stale ### Your current environment ### 🐛 Describe the bug ## Vllm version vllm-openai:v0.10.1.1 ## CUDA version 12.8 ## Hardware 8*H20 ## start params: vllm serve /nvme0/qwen3-235b --trust-remote-code -tp 8 --served-m...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: y:596] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/attention/backends/flash_attn.py", line 320, in build [1;36m(VllmWorker TP5 pid=411)[0;0m ERROR 08-29 02:12:59 [multiproc_executor.py:596] scheduler_metadata...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Unrecognized FP8 dtype: fp8_e5m2 bug;stale ### Your current environment ### 🐛 Describe the bug ## Vllm version vllm-openai:v0.10.1.1 ## CUDA version 12.8 ## Hardware 8*H20 ## start params: vllm serve /nvme0/qwen3...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: nt ### 🐛 Describe the bug ## Vllm version vllm-openai:v0.10.1.1 ## CUDA version 12.8 ## Hardware 8*H20 ## start params: vllm serve /nvme0/qwen3-235b --trust-remote-code -tp 8 --served-model-name qwen3-235b-instruct-2507...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#23942](https://github.com/vllm-project/vllm/pull/23942) | mentioned | 0.6 | [CI]  Add `aiter` to matching list of issue auto labeller for `rocm` tag | el: NO (0 matches) #23923: Should have ROCm label: NO (0 matches) #23922: Should have ROCm label: NO (0 matches) #23921: Should have ROCm label: NO (0 matches) #23916: Should hav |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
