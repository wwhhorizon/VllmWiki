# vllm-project/vllm#14790: [Bug]: GLM4V model gets lower precision score on TextVQA since vLLM does not process model's position ids correctly.

| 字段 | 值 |
| --- | --- |
| Issue | [#14790](https://github.com/vllm-project/vllm/issues/14790) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: GLM4V model gets lower precision score on TextVQA since vLLM does not process model's position ids correctly.

### Issue 正文摘录

### Your current environment vLLM: 0.7.3 Python 3.12.8 transformers: 4.48.2 ### 🐛 Describe the bug I compared the specific TextVQA result from vLLM with HuggingFace transformer. It turns out that vLLM gives a different answer (both not using sampling postprocess). ```text # Question: "what is this food place selling? Answer the question using a single word or phrase.” # huggingface transformer answer German sausages. # vLLM transformer Hot dogs and sausages. ``` I checked the code `glm4v.py` and `chatglm.py` under `vllm/model_executor/models` and found that vLLM does not preprocess image part in position ids as the source code of GLM4V does. For example, GLM4V's positon ids for a multimodal input including an image should be [0, 1, 2, 3, 3, 3, 3, 4, 5, 6] where 3 represents the image part; However, vLLM just gives [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]. I think this the main reason that causes the different answer therefore the lower score on TextVQA, and I hope that vLLM group can fix that. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: GLM4V model gets lower precision score on TextVQA since vLLM does not process model's position ids correctly. bug;stale ### Your current environment vLLM: 0.7.3 Python 3.12.8 transformers: 4.48.2 ### 🐛 Describe t...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: GLM4V model gets lower precision score on TextVQA since vLLM does not process model's position ids correctly. bug;stale ### Your current environment vLLM: 0.7.3 Python 3.12.8 transformers: 4.48.2 ### 🐛 Describe t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: GLM4V model gets lower precision score on TextVQA since vLLM does not process model's position ids correctly. bug;stale ### Your current environment vLLM: 0.7.3 Python 3.12.8 transformers: 4.48.2 ### 🐛 Describe t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: t. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: TextVQA since vLLM does not process model's position ids correctly. bug;stale ### Your current environment vLLM: 0.7.3 Python 3.12.8 transformers: 4.48.2 ### 🐛 Describe the bug I compared the specific TextVQA result fro...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
