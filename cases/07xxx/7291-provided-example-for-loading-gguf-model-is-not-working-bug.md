# vllm-project/vllm#7291: Provided example for loading GGUF model is not working [Bug]: 

| 字段 | 值 |
| --- | --- |
| Issue | [#7291](https://github.com/vllm-project/vllm/issues/7291) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Provided example for loading GGUF model is not working [Bug]: 

### Issue 正文摘录

### Your current environment ```text ``` ### 🐛 Describe the bug Hi @Isotr0py @mgoin, I ran the gguf inference example [gguf_inference](https://github.com/vllm-project/vllm/blob/main/examples/gguf_inference.py) and I was getting **NotImplementedError** error ![image](https://github.com/user-attachments/assets/85695b53-42f6-43c6-8c6c-42d70dd4e2c5) ![image](https://github.com/user-attachments/assets/348e84ef-020b-4f36-b72a-68ba3e402eba) Could you please help me for this?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Provided example for loading GGUF model is not working [Bug]: bug;stale ### Your current environment ```text ``` ### 🐛 Describe the bug Hi @Isotr0py @mgoin, I ran the gguf inference example [gguf_inference](https://gith...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Provided example for loading GGUF model is not working [Bug]: bug;stale ### Your current environment ```text ``` ### 🐛 Describe the bug Hi @Isotr0py @mgoin, I ran the gguf inference example [gguf_inference](https://gith...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
