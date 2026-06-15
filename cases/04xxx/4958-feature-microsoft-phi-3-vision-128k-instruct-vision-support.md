# vllm-project/vllm#4958: [Feature]: microsoft/Phi-3-vision-128k-instruct Vision support

| 字段 | 值 |
| --- | --- |
| Issue | [#4958](https://github.com/vllm-project/vllm/issues/4958) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: microsoft/Phi-3-vision-128k-instruct Vision support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch https://huggingface.co/microsoft/Phi-3-vision-128k-instruct ### Alternatives _No response_ ### Additional context vllm is somewhat behind in vision support. idefics2 is supported by TGI and lllava next been out for months and not supported yet. There is a PR, is it close?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: support feature request ### 🚀 The feature, motivation and pitch https://huggingface.co/microsoft/Phi-3-vision-128k-instruct ### Alternatives _No response_ ### Additional context vllm is somewhat behind in vision support...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: microsoft/Phi-3-vision-128k-instruct Vision support feature request ### 🚀 The feature, motivation and pitch https://huggingface.co/microsoft/Phi-3-vision-128k-instruct ### Alternatives _No response_ ### Addit...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
