# vllm-project/vllm#14752: [Feature]: Suggestion of modifying raising ValueError when current_count > allowed_count for multimodal inputs

| 字段 | 值 |
| --- | --- |
| Issue | [#14752](https://github.com/vllm-project/vllm/issues/14752) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Suggestion of modifying raising ValueError when current_count > allowed_count for multimodal inputs

### Issue 正文摘录

### 🚀 The feature, motivation and pitch According to the code below, https://github.com/vllm-project/vllm/blob/b1cc4dfef57ac0f3e27575215f771f0c25706b81/vllm/entrypoints/chat_utils.py#L463-L477 when `current_count` becomes greater than `allowed_count`, it sends a message saying that "Error occurred." And the client doesn't receive any message about why the error is occurred. The reason is shown on the log of server side. ### Alternatives So I think, giving response with the last `allowed_count` item instead of error is better like below. ``` if current_count > allowed_count: self._items_by_modality[modality].append(item) self._items_by_modality[modality] = self._items_by_modality[modality][-allowed_count:] logger.warning(f"Total input for current modality({modality}):{current_count} " f"is bigger than {allowed_count}.\n" f"Select last {allowed_count} items.") ``` ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: n of modifying raising ValueError when current_count > allowed_count for multimodal inputs feature request ### 🚀 The feature, motivation and pitch According to the code below, https://github.com/vllm-project/vllm/blob/b...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ueError when current_count > allowed_count for multimodal inputs feature request ### 🚀 The feature, motivation and pitch According to the code below, https://github.com/vllm-project/vllm/blob/b1cc4dfef57ac0f3e27575215f7...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
