# vllm-project/vllm#40869: [Bug]: QWEN3.5-27B fails to mount LoRA

| 字段 | 值 |
| --- | --- |
| Issue | [#40869](https://github.com/vllm-project/vllm/issues/40869) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: QWEN3.5-27B fails to mount LoRA

### Issue 正文摘录

### Your current environment I used the Atlas 800I A2 (910B4 32G 4-card) to run Qwen3.5-27B and load Lora. The vLLM-ascend version is v0.18.0rc1. ### 🐛 Describe the bug (Worker_TP0 pid=1256) ERROR 04-22 02:12:02 [multiproc_executor.py:932] WorkerProc hit an exception. (Worker_TP0 pid=1256) ERROR 04-22 02:12:02 [multiproc_executor.py:932] Traceback (most recent call last): (Worker_TP0 pid=1256) ERROR 04-22 02:12:02 [multiproc_executor.py:932] File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 927, in worker_busy_loop (Worker_TP0 pid=1256) ERROR 04-22 02:12:02 [multiproc_executor.py:932] output = func(*args, **kwargs) (Worker_TP0 pid=1256) ERROR 04-22 02:12:02 [multiproc_executor.py:932] ^^^^^^^^^^^^^^^^^^^^^ (Worker_TP0 pid=1256) ERROR 04-22 02:12:02 [multiproc_executor.py:932] File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context (Worker_TP0 pid=1256) ERROR 04-22 02:12:02 [multiproc_executor.py:932] return func(*args, **kwargs) (Worker_TP0 pid=1256) ERROR 04-22 02:12:02 [multiproc_executor.py:932] ^^^^^^^^^^^^^^^^^^^^^ (Worker_TP0 pid=1256) ERROR 04-22 02:12:02 [multiproc_executor.py:932] File "...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: A2 (910B4 32G 4-card) to run Qwen3.5-27B and load Lora. The vLLM-ascend version is v0.18.0rc1. ### 🐛 Describe the bug (Worker_TP0 pid=1256) ERROR 04-22 02:12:02 [multiproc_executor.py:932] WorkerProc hit an exception. (...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ultiproc_executor.py:932] self.lora_manager.set_active_adapters(lora_requests, lora_mapping) (Worker_TP0 pid=1256) ERROR 04-22 02:12:02 [multiproc_executor.py:932] File "/vllm-workspace/vllm/vllm/lora/worker_manager.py"...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: QWEN3.5-27B fails to mount LoRA bug ### Your current environment I used the Atlas 800I A2 (910B4 32G 4-card) to run Qwen3.5-27B and load Lora. The vLLM-ascend version is v0.18.0rc1. ### 🐛 Describe the bug (Worker...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: peculative_tokens": 3, "enforce_eager": true}' \ --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY"}' \ --additional-config '{"enable_cpu_binding":true}' \ --async-scheduling \ --enable-lora --lora-modules mix-l...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: or.py:932] self.lora_manager.set_active_adapters(lora_requests, lora_mapping) (Worker_TP0 pid=1256) ERROR 04-22 02:12:02 [multiproc_executor.py:932] File "/vllm-workspace/vllm/vllm/lora/worker_manager.py", line 176, in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
