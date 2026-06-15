# vllm-project/vllm#9415: [Bug]:  RuntimeError: Error in model execution (input dumped to /tmp/err_execute_model_input_20241016-170451.pkl): view size is not compatible with input tensor's size and stride (at least one dimension spans across two contiguous subspaces). Use .reshape(...) instead.

| 字段 | 值 |
| --- | --- |
| Issue | [#9415](https://github.com/vllm-project/vllm/issues/9415) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  RuntimeError: Error in model execution (input dumped to /tmp/err_execute_model_input_20241016-170451.pkl): view size is not compatible with input tensor's size and stride (at least one dimension spans across two contiguous subspaces). Use .reshape(...) instead.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug vllm/model_executor/models/glm4_vision_encoder.py The 100 lines of the file should be modified to： output, _ = self.dense(out.transpose(1, 2).**reshape**(B, L, -1)) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: 16-170451.pkl): view size is not compatible with input tensor's size and stride (at least one dimension spans across two contiguous subspaces). Use .reshape(...) instead. bug;stale ### Your current environment ### Model...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 1)) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: RuntimeError: Error in model execution (input dumped to /tmp/err_execute_model_input_20241016-170451.pkl): view size is not compatible with input tensor's size and stride (at least one dimension spans across two...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: n spans across two contiguous subspaces). Use .reshape(...) instead. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug vllm/model_executor/models/glm4_vision_encoder.py Th...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
