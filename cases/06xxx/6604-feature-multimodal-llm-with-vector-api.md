# vllm-project/vllm#6604: [Feature]: MultiModal LLM with vector API

| 字段 | 值 |
| --- | --- |
| Issue | [#6604](https://github.com/vllm-project/vllm/issues/6604) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: MultiModal LLM with vector API

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Consider a scenario where a large model is deployed in the cloud, and the application is deployed on a computationally limited embedded device. If we want to support multimodal dialogue interaction with vision and language, each request would send an image (considering the dialogue history, there would be many images). Given network bandwidth and other factors, this would cause a lot of latency. Therefore, if the VLM's image encoder and projector are deployed on the embedded device, and if we could send the encoded vector instead during requests, the data transmission volume would be much smaller. This would reduce latency and improve the user experience. ### Alternatives The suggestted usage method is as follow ``` python # Refer to the HuggingFace repo for the correct format to use prompt = "USER: \nWhat is the content of this image?\nASSISTANT:" # Image encoded vector vector = np.array([x, x,x, x]) # Single prompt inference outputs = llm.generate({ "prompt": prompt, "multi_modal_data": {"vector": vector}, }) ``` For this usage, deploying only a single-model LLM model could support multi-modal model usage, and the modality is not limited....

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Feature]: MultiModal LLM with vector API feature request ### 🚀 The feature, motivation and pitch Consider a scenario where a large model is deployed in the cloud, and the application is deployed on a computationally li...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: f we could send the encoded vector instead during requests, the data transmission volume would be much smaller. This would reduce latency and improve the user experience. ### Alternatives The suggestted usage method is...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: MultiModal LLM with vector API feature request ### 🚀 The feature, motivation and pitch Consider a scenario where a large model is deployed in the cloud, and the application is deployed on a computationally li...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: s). Given network bandwidth and other factors, this would cause a lot of latency. Therefore, if the VLM's image encoder and projector are deployed on the embedded device, and if we could send the encoded vector instead...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
