# vllm-project/vllm#307: [Question] Usage with Multimodal LLM

| 字段 | 值 |
| --- | --- |
| Issue | [#307](https://github.com/vllm-project/vllm/issues/307) |
| 状态 | closed |
| 标签 | new-model;feature request |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Question] Usage with Multimodal LLM

### Issue 正文摘录

Dear Authors, Thank you so much for your wonderful work. I want to ask if I am running LLaVA(https://github.com/haotian-liu/LLaVA/blob/main/llava/model/llava.py), a multimodal LLM built upon LLaMA by adding an image encoder, what is the most convenient method to incorporate VLLM? I think I can follow the instructions in "https://vllm.readthedocs.io/en/latest/models/adding_model.html". Are there any more convenient ways?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Question] Usage with Multimodal LLM new-model;feature request Dear Authors, Thank you so much for your wonderful work. I want to ask if I am running LLaVA(https://github.com/haotian-liu/LLaVA/blob/main/llava/model/llav...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Question] Usage with Multimodal LLM new-model;feature request Dear Authors, Thank you so much for your wonderful work. I want to ask if I am running LLaVA(https://github.com/haotian-liu/LLaVA/blob/main/llava/model/llav...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: think I can follow the instructions in "https://vllm.readthedocs.io/en/latest/models/adding_model.html". Are there any more convenient ways?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
