# vllm-project/vllm#25192: [Bug]: Make Whisper model compatible with cuda graphs

| 字段 | 值 |
| --- | --- |
| Issue | [#25192](https://github.com/vllm-project/vllm/issues/25192) |
| 状态 | closed |
| 标签 | bug;help wanted;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Make Whisper model compatible with cuda graphs

### Issue 正文摘录

### 🐛 Describe the bug As discussed in https://github.com/vllm-project/vllm/issues/24946, the next thing that would make a significant impact on Whisper performance with V1 would be to get it working with cudagraphs. Right now it's not supported.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Bug]: Make Whisper model compatible with cuda graphs bug;help wanted;stale ### 🐛 Describe the bug As discussed in https://github.com/vllm-project/vllm/issues/24946, the next thing that would make a significant impact o...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Make Whisper model compatible with cuda graphs bug;help wanted;stale ### 🐛 Describe the bug As discussed in https://github.com/vllm-project/vllm/issues/24946, the next thing that would make a significant impact o...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Make Whisper model compatible with cuda graphs bug;help wanted;stale ### 🐛 Describe the bug As discussed in https://github.com/vllm-project/vllm/issues/24946, the next thing that would make a significant impact o...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
