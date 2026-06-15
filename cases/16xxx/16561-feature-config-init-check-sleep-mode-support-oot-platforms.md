# vllm-project/vllm#16561: [Feature]: config init check sleep mode support oot platforms

| 字段 | 值 |
| --- | --- |
| Issue | [#16561](https://github.com/vllm-project/vllm/issues/16561) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: config init check sleep mode support oot platforms

### Issue 正文摘录

### 🚀 The feature, motivation and pitch As it is coded in /vllm/config.py ```Python if self.enable_sleep_mode and not current_platform.is_cuda(): raise ValueError("Sleep mode is only supported on CUDA devices.") ``` While there are oot platforms, which will support sleep mode (Ascend NPU has already done this in v0.7.3 branch) The above code makes it hard to support sleep mode in oot platforms. A possible solution is to add a method to base class Platform: `is_sleep_mode_available()`, oot Platform classes can override this method to indicate whether the platform supports sleep mode. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ```Python if self.enable_sleep_mode and not current_platform.is_cuda(): raise ValueError("Sleep mode is only supported on CUDA devices.") ``` While there are oot platforms, which will support sleep mode (Ascend NPU has...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: config init check sleep mode support oot platforms feature request ### 🚀 The feature, motivation and pitch As it is coded in /vllm/config.py ```Python if self.enable_sleep_mode and not current_platform.is_cud...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: config init check sleep mode support oot platforms feature request ### 🚀 The feature, motivation and pitch As it is coded in /vllm/config.py ```Python if self.enable_sleep_mode and not current_platform.is_cud...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
