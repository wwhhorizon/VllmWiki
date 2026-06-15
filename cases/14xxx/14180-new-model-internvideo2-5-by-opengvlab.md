# vllm-project/vllm#14180: [New Model]: InternVideo2.5 by OpenGVLab

| 字段 | 值 |
| --- | --- |
| Issue | [#14180](https://github.com/vllm-project/vllm/issues/14180) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: InternVideo2.5 by OpenGVLab

### Issue 正文摘录

### The model to consider. Hi, I was wondering if there are any plans to support or implement [OpenGVLab/InternVideo2_5_Chat_8](https://huggingface.co/OpenGVLab/InternVideo2_5_Chat_8B) in the near future. ### The closest model vllm already supports. I think the closest model that vllm already supports would be InternVL2.5 as I saw the InternVL2.5 in vllm supported models list. And since InternVideo2.5 was built on InternVL2.5, I think it would be a nice upgrade. ![Image](https://github.com/user-attachments/assets/279b8bc8-dc12-4848-bdca-08414c362144) https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/internvl.py I'm not sure whether `internvl.py` is an executor for intervnl2.5 as well. ### What's your difficulty of supporting the model you want? _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [New Model]: InternVideo2.5 by OpenGVLab new-model ### The model to consider. Hi, I was wondering if there are any plans to support or implement [OpenGVLab/InternVideo2_5_Chat_8](https://huggingface.co/OpenGVLab/InternV...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
