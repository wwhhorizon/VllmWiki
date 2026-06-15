# vllm-project/vllm#32461: [Bug]: QWenBaseModel.embed_input_ids() got an unexpected keyword argument 'multimodal_embeddings'

| 字段 | 值 |
| --- | --- |
| Issue | [#32461](https://github.com/vllm-project/vllm/issues/32461) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: QWenBaseModel.embed_input_ids() got an unexpected keyword argument 'multimodal_embeddings'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When do the example of qwen_vl offline inference, it throws error: ```python python examples/offline_inference/vision_language.py --model-type qwen_vl (EngineCore_DP0 pid=393385) ERROR 01-16 05:25:33 [core.py:844] EngineCore encountered a fatal error. (EngineCore_DP0 pid=393385) ERROR 01-16 05:25:33 [core.py:844] Traceback (most recent call last): (EngineCore_DP0 pid=393385) ERROR 01-16 05:25:33 [core.py:844] File "/usr/local/lib64/python3/dist-packages/vllm/v1/engine/core.py", line 835, in run_engine_core (EngineCore_DP0 pid=393385) ERROR 01-16 05:25:33 [core.py:844] engine_core.run_busy_loop() (EngineCore_DP0 pid=393385) ERROR 01-16 05:25:33 [core.py:844] File "/usr/local/lib64/python3/dist-packages/vllm/v1/engine/core.py", line 862, in run_busy_loop (EngineCore_DP0 pid=393385) ERROR 01-16 05:25:33 [core.py:844] self._process_engine_step() (EngineCore_DP0 pid=393385) ERROR 01-16 05:25:33 [core.py:844] File "/usr/local/lib64/python3/dist-packages/vllm/v1/engine/core.py", line 891, in _process_engine_step (EngineCore_DP0 pid=393385) ERROR 01-16 05:25:33 [core.py:844] outputs, model_executed = self.step_fn() (EngineCore_DP0 pid=39...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: QWenBaseModel.embed_input_ids() got an unexpected keyword argument 'multimodal_embeddings' bug ### Your current environment ### 🐛 Describe the bug When do the example of qwen_vl offline inference, it throws error:
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 674 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ERROR 01-16 05:25:33 [core.py:844] return self.worker.execute_model(scheduler_output, *args, **kwargs) (EngineCore_DP0 pid=393385) ERROR 01-16 05:25:33 [core.py:844] File "/usr/local/lib64/python3/dist-packages/torch/ut...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
