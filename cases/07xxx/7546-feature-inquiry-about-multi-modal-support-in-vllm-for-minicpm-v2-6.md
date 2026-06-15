# vllm-project/vllm#7546: [Feature]: Inquiry about Multi-modal Support in VLLM for MiniCPM-V2.6

| 字段 | 值 |
| --- | --- |
| Issue | [#7546](https://github.com/vllm-project/vllm/issues/7546) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Inquiry about Multi-modal Support in VLLM for MiniCPM-V2.6

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I am currently exploring the capabilities of the VLLM library and am interested in understanding its support for multi-modal inputs, particularly for models like MiniCPM-V2.6. I would like to know if VLLM is designed to handle multi-image and video inputs for such models. ### Alternatives 1. **Model of Interest**: MiniCPM-V2.6 2. **Types of Input**: Multi-image and video 3. **Current Understanding**: - I have reviewed the documentation and initial examples provided with VLLM. - It seems that both `multiple 'image_url' input` and `list value in image_url` is currently not supported. - However, I am not sure if it supports the processing of multiple images or videos as input to a model like MiniCPM-V2.6. ## Questions 1. Does VLLM support the integration of MiniCPM-V2.6 for processing multi-image and video inputs? 2. If yes, could you provide an example or a guide on how to set up and use this feature? 3. If not, are there any plans to extend VLLM's capabilities to support such inputs in the future? ### Additional context ![image](https://github.com/user-attachments/assets/627dd626-dee1-41cb-b231-9c13163e9174)

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ed in understanding its support for multi-modal inputs, particularly for models like MiniCPM-V2.6. I would like to know if VLLM is designed to handle multi-image and video inputs for such models. ### Alternatives 1. **M...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ure]: Inquiry about Multi-modal Support in VLLM for MiniCPM-V2.6 feature request ### 🚀 The feature, motivation and pitch I am currently exploring the capabilities of the VLLM library and am interested in understanding i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
