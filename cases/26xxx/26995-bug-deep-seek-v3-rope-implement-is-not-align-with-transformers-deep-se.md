# vllm-project/vllm#26995: [Bug]: deep seek v3 rope implement is not align with transformers deep seek v3 rope

| 字段 | 值 |
| --- | --- |
| Issue | [#26995](https://github.com/vllm-project/vllm/issues/26995) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: deep seek v3 rope implement is not align with transformers deep seek v3 rope

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm deep seek v3 modeling rope implement is here: https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/rotary_embedding/deepseek_scaling_rope.py however, I checked the transformers deep seek modeling and hf deep seek modeling, both of them will do transpose for q_rope and k rope please see link below: transformer deep seek modeling: https://github.com/huggingface/transformers/blob/e20df45bf676d80bdddb9757eeeafe6c0c81ecfa/src/transformers/models/deepseek_v3/modeling_deepseek_v3.py#L283 hf deep seek modeling: https://huggingface.co/deepseek-ai/DeepSeek-R1/blob/main/modeling_deepseek.py#L339 Here is code for transpose q in deep seek rope q = q.view(b, h, s, d // 2, 2).transpose(4, 3).reshape(b, h, s, d) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: # Your current environment ### 🐛 Describe the bug vllm deep seek v3 modeling rope implement is here: https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/rotary_embedding/deepseek_scaling_rope.py ho...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: odeling, both of them will do transpose for q_rope and k rope please see link below: transformer deep seek modeling: https://github.com/huggingface/transformers/blob/e20df45bf676d80bdddb9757eeeafe6c0c81ecfa/src/transfor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: d) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: k v3 rope implement is not align with transformers deep seek v3 rope bug;stale ### Your current environment ### 🐛 Describe the bug vllm deep seek v3 modeling rope implement is here: https://github.com/vllm-project/vllm/...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
