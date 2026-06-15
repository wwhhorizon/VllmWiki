# vllm-project/vllm#32680: [Bug]: hanging durling long video understanding

| 字段 | 值 |
| --- | --- |
| Issue | [#32680](https://github.com/vllm-project/vllm/issues/32680) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: hanging durling long video understanding

### Issue 正文摘录

**SUMMARY**: When performing inference at a 256K context length, the LLM engine hangs. This happens because the encoder cache is smaller than the acutal number of video tokens, causing `num_new_tokens` to always be zero during each scheduling step. @ywang96 🫡 https://github.com/vllm-project/vllm/blob/13f6630a9ea78bee4bd80bb6e842e55e374eec9a/vllm/v1/core/sched/scheduler.py#L1017-L1036 Diving into the calculation of the encoder cache size, I found it is related to: https://github.com/vllm-project/vllm/blob/13f6630a9ea78bee4bd80bb6e842e55e374eec9a/vllm/model_executor/models/qwen2_vl.py#L841-L848 The `max_video_tokens` is smaller than `max_pixels`. However, this is not a tight upper bound because the `num_frames` is fixed. For a different `num_frames`, the actual number of video tokens may exceed `max_video_tokens`, which causes the hang. https://github.com/vllm-project/vllm/blob/13f6630a9ea78bee4bd80bb6e842e55e374eec9a/vllm/model_executor/models/qwen2_vl.py#L1014-L1019 ```python # Calculation of Qwen3-VL video smart_resize h_bar = round(height / factor) * factor w_bar = round(width / factor) * factor t_bar = round(num_frames / temporal_factor) * temporal_factor if t_bar * h_bar * w_b...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: length, the LLM engine hangs. This happens because the encoder cache is smaller than the acutal number of video tokens, causing `num_new_tokens` to always be zero during each scheduling step. @ywang96 🫡 https://github.c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: com/vllm-project/vllm/blob/13f6630a9ea78bee4bd80bb6e842e55e374eec9a/vllm/model_executor/models/qwen2_vl.py#L841-L848 The `max_video_tokens` is smaller than `max_pixels`. However, this is not a tight upper bound because...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: n the constraint imposed by `max_pixels`, which should be acceptable for building the cache. ### 🐛 Describe the bug --- ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ct/vllm/blob/13f6630a9ea78bee4bd80bb6e842e55e374eec9a/vllm/v1/core/sched/scheduler.py#L1017-L1036 Diving into the calculation of the encoder cache size, I found it is related to: https://github.com/vllm-project/vllm/blo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
