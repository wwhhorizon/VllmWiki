# vllm-project/vllm#25134: [Bug]: Eagle3 not support Qwen3-30B-A3B-FP8

| 字段 | 值 |
| --- | --- |
| Issue | [#25134](https://github.com/vllm-project/vllm/issues/25134) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Eagle3 not support Qwen3-30B-A3B-FP8

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```code vllm serve /home/models/Qwen3-30B-A3B-FP8 --speculative_config '{"method": "eagle3","model": "/home/models/Qwen3-30B-A3B-eagle3","num_speculative_tokens": 2}' --enforce-eager ``` ``` EngineCore_DP0 pid=2109652) INFO 09-18 12:03:11 [default_loader.py:268] Loading weights took 0.42 seconds (EngineCore_DP0 pid=2109652) INFO 09-18 12:03:11 [eagle.py:644] Assuming the EAGLE head shares the same vocab embedding with the target model. (EngineCore_DP0 pid=2109652) ERROR 09-18 12:03:12 [core.py:712] EngineCore failed to start. (EngineCore_DP0 pid=2109652) ERROR 09-18 12:03:12 [core.py:712] Traceback (most recent call last): (EngineCore_DP0 pid=2109652) ERROR 09-18 12:03:12 [core.py:712] File "/home/wangyxbh/vllm/vllm/v1/engine/core.py", line 703, in run_engine_core (EngineCore_DP0 pid=2109652) ERROR 09-18 12:03:12 [core.py:712] engine_core = EngineCoreProc(*args, **kwargs) (EngineCore_DP0 pid=2109652) ERROR 09-18 12:03:12 [core.py:712] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=2109652) ERROR 09-18 12:03:12 [core.py:712] File "/home/wangyxbh/vllm/vllm/v1/engine/core.py", line 502, in __init__ (EngineCore_DP0 pid=2109652)...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Eagle3 not support Qwen3-30B-A3B-FP8 bug;stale ### Your current environment ### 🐛 Describe the bug ```code vllm serve /home/models/Qwen3-30B-A3B-FP8 --speculative_config '{"method": "eagle3","model": "/home/model...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Eagle3 not support Qwen3-30B-A3B-FP8 bug;stale ### Your current environment ### 🐛 Describe the bug ```code vllm serve /home/models/Qwen3-30B-A3B-FP8 --speculative_config '{"method": "eagle3","model": "/home/model...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: Eagle3 not support Qwen3-30B-A3B-FP8 bug;stale ### Your current environment ### 🐛 Describe the bug ```code vllm serve /home/models/Qwen3-30B-A3B-FP8 --speculative_config '{"method": "eagle3","model": "/home/model...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
