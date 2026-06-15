# vllm-project/vllm#13903: [Feature]: T5Model has no vLLM implementation

| 字段 | 值 |
| --- | --- |
| Issue | [#13903](https://github.com/vllm-project/vllm/issues/13903) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: T5Model has no vLLM implementation

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I would like to use vLLM for T5 reranker. ``` (vllm_env) dromeuf@MAIA:~$ vllm serve castorini/monot5-large-msmarco --served-model-name monot5-large-msmarco --dtype auto --task score --host 0.0.0.0 --port 33437 --api-key vLLM ERROR 02-26 15:50:28 engine.py:389] T5Model has no vLLM implementation and the Transformers implementation is not compatible with vLLM. ``` Thanks for your great work, Kind regards, David. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nker. ``` (vllm_env) dromeuf@MAIA:~$ vllm serve castorini/monot5-large-msmarco --served-model-name monot5-large-msmarco --dtype auto --task score --host 0.0.0.0 --port 33437 --api-key vLLM ERROR 02-26 15:50:28 engine.py...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: T5Model has no vLLM implementation feature request;stale ### 🚀 The feature, motivation and pitch I would like to use vLLM for T5 reranker. ``` (vllm_env) dromeuf@MAIA:~$ vllm serve castorini/monot5-large-msma...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: astorini/monot5-large-msmarco --served-model-name monot5-large-msmarco --dtype auto --task score --host 0.0.0.0 --port 33437 --api-key vLLM ERROR 02-26 15:50:28 engine.py:389] T5Model has no vLLM implementation and the...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: T5Model has no vLLM implementation feature request;stale ### 🚀 The feature, motivation and pitch I would like to use vLLM for T5 reranker. ``` (vllm_env) dromeuf@MAIA:~$ vllm serve castorini/monot5-large-msma...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
