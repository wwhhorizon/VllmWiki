# vllm-project/vllm#20463: [New Model]: jinaai/jina-embeddings-v4

| 字段 | 值 |
| --- | --- |
| Issue | [#20463](https://github.com/vllm-project/vllm/issues/20463) |
| 状态 | closed |
| 标签 | new-model;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: jinaai/jina-embeddings-v4

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi, when i run the vllm serve to launch jina-embeddings-v4 model, where my deploy script is : export VLLM_USE_V1=0 MODEL_PATH="./chkpt/jina-embeddings-v4/" vllm serve $MODEL_PATH --served-model-name model --trust-remote-code --task embed I met the follow error: ValueError: JinaEmbeddingsV4Model has no vLLM implementation and the Transformers implementation is not compatible with vLLM. Try setting VLLM_USE_V1=0. looking forward to your helpful reply ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ply ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [New Model]: jinaai/jina-embeddings-v4 new-model;stale ### Your current environment ### 🐛 Describe the bug Hi, when i run the vllm serve to launch jina-embeddings-v4 model, where my deploy script is : export VLLM_USE_V1
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [New Model]: jinaai/jina-embeddings-v4 new-model;stale ### Your current environment ### 🐛 Describe the bug Hi, when i run the vllm serve to launch jina-embeddings-v4 model, where my deploy script is : export VLLM_USE_V1...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
