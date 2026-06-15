# vllm-project/vllm#27587: [Bug]: Qwen3vl RL rollout

| 字段 | 值 |
| --- | --- |
| Issue | [#27587](https://github.com/vllm-project/vllm/issues/27587) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3vl RL rollout

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug "/opt/conda/envs/torch-base/lib/python3.12/site-packages/vllm/multimodal/processing.py", line 1456, in _apply_hf_processor_text_mm (TaskRunner pid=210367) processed_data = self._call_hf_processor( (TaskRunner pid=210367) ^^^^^^^^^^^^^^^^^^^^^^^^ (TaskRunner pid=210367) File "/opt/conda/envs/torch-base/lib/python3.12/site-packages/vllm/model_executor/models/qwen3_vl.py", line 840, in _call_hf_processor (TaskRunner pid=210367) video_mm_kwargs["do_sample_frames"] = metadata.get( (TaskRunner pid=210367) ^^^^^^^^^^^^ (TaskRunner pid=210367) AttributeError: 'NoneType' object has no attribute 'get' (WorkerDict pid=20906, ip=28.45.33.49) WARNING 10-27 20:38:37 [hasher.py:71] No serialization method found for . Falling back to pickle. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen3vl RL rollout bug ### Your current environment ### 🐛 Describe the bug "/opt/conda/envs/torch-base/lib/python3.12/site-packages/vllm/multimodal/processing.py", line 1456, in _apply_hf_processor_text_mm (TaskR...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: le. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: cessor (TaskRunner pid=210367) video_mm_kwargs["do_sample_frames"] = metadata.get( (TaskRunner pid=210367) ^^^^^^^^^^^^ (TaskRunner pid=210367) AttributeError: 'NoneType' object has no attribute 'get' (WorkerDict pid=20...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
