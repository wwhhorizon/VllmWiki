# vllm-project/vllm#11859: [Misc]: Batch Multi-Modal Online Inference 

| 字段 | 值 |
| --- | --- |
| Issue | [#11859](https://github.com/vllm-project/vllm/issues/11859) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Batch Multi-Modal Online Inference 

### Issue 正文摘录

### Anything you want to discuss about vllm. In the vllm docs, there is an example for sending a batch of multi-modal prompts to offline inference ``` # Batch inference image_1 = PIL.Image.open(...) image_2 = PIL.Image.open(...) outputs = llm.generate( [ { "prompt": "USER: \nWhat is the content of this image?\nASSISTANT:", "multi_modal_data": {"image": image_1}, }, { "prompt": "USER: \nWhat's the color of this image?\nASSISTANT:", "multi_modal_data": {"image": image_2}, } ] ) ``` However I could not find any similar documentation for Online Inference using the OpenAI-compatible server. Is this possible? I know you can batch inference text using client.completions.create, but it doesn't seem like there is anyway to do it with images. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: s. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Misc]: Batch Multi-Modal Online Inference stale ### Anything you want to discuss about vllm. In the vllm docs, there is an example for sending a batch of multi-modal prompts to offline inference ``` # Batch inference i...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
