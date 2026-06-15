# vllm-project/vllm#13076: [Bug]: RuntimeError: Expected index [32, 1543] to be smaller than self [31, 152065] apart from dimension 1 and to be smaller size than src [32, 1543]

| 字段 | 值 |
| --- | --- |
| Issue | [#13076](https://github.com/vllm-project/vllm/issues/13076) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: Expected index [32, 1543] to be smaller than self [31, 152065] apart from dimension 1 and to be smaller size than src [32, 1543]

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I run serving using vllm v1 engine, using qwen32B-instruct, using fp8 static quant. vllm==0.7.2 The error reports: ``` ERROR 02-11 07:01:54 core.py:210] EngineCore hit an exception: Traceback (most recent call last): ERROR 02-11 07:01:54 core.py:210] File "/usr/local/lib/python3.10/dist-packages/vllm/v1/engine/core.py", line 203, in run_engine_core ERROR 02-11 07:01:54 core.py:210] engine_core.run_busy_loop() ERROR 02-11 07:01:54 core.py:210] File "/usr/local/lib/python3.10/dist-packages/vllm/v1/engine/core.py", line 243, in run_busy_loop ERROR 02-11 07:01:54 core.py:210] outputs = self.step() ERROR 02-11 07:01:54 core.py:210] File "/usr/local/lib/python3.10/dist-packages/vllm/v1/engine/core.py", line 129, in step ERROR 02-11 07:01:54 core.py:210] output = self.model_executor.execute_model(scheduler_output) ERROR 02-11 07:01:54 core.py:210] File "/usr/local/lib/python3.10/dist-packages/vllm/v1/executor/abstract.py", line 77, in execute_model ERROR 02-11 07:01:54 core.py:210] output = self.collective_rpc("execute_model", ERROR 02-11 07:01:54 core.py:210] File "/usr/local/lib/python3.10/dist-packages/vllm/executor/uniproc_executor....

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: e bug I run serving using vllm v1 engine, using qwen32B-instruct, using fp8 static quant. vllm==0.7.2 The error reports: ``` ERROR 02-11 07:01:54 core.py:210] EngineCore hit an exception: Traceback (most recent call las...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: RuntimeError: Expected index [32, 1543] to be smaller than self [31, 152065] apart from dimension 1 and to be smaller size than src [32, 1543] bug ### Your current environment ### 🐛 Describe the bug I run serving...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nt ### 🐛 Describe the bug I run serving using vllm v1 engine, using qwen32B-instruct, using fp8 static quant. vllm==0.7.2 The error reports: ``` ERROR 02-11 07:01:54 core.py:210] EngineCore hit an exception: Traceback (...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 11 07:01:54 core.py:210] next_tokens = self.sampler(logits, sampling_metadata) ERROR 02-11 07:01:54 core.py:210] File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_imp...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: -11 07:01:54 core.py:210] output = self.model_executor.execute_model(scheduler_output) ERROR 02-11 07:01:54 core.py:210] File "/usr/local/lib/python3.10/dist-packages/vllm/v1/executor/abstract.py", line 77, in execute_m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
