# vllm-project/vllm#15773: [Doc]: vllm==0.8.2 V1 does not yet support Pooling models.

| 字段 | 值 |
| --- | --- |
| Issue | [#15773](https://github.com/vllm-project/vllm/issues/15773) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 25; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: vllm==0.8.2 V1 does not yet support Pooling models.

### Issue 正文摘录

### 📚 The doc issue sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="facebook/opt-125m") outputs = llm.generate(prompts, sampling_params) show error: ValueError: V1 does not yet support Pooling models. link:https://docs.vllm.ai/en/latest/getting_started/quickstart.html#offline-batched-inference ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: arams) show error: ValueError: V1 does not yet support Pooling models. link:https://docs.vllm.ai/en/latest/getting_started/quickstart.html#offline-batched-inference ### Suggest a potential alternative/fix _No response_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Doc]: vllm==0.8.2 V1 does not yet support Pooling models. documentation;stale ### 📚 The doc issue sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="facebook/opt-125m") outputs = llm.generat...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Doc]: vllm==0.8.2 V1 does not yet support Pooling models. documentation;stale ### 📚 The doc issue sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="facebook/opt-125m") outputs = llm.generat...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: V1 does not yet support Pooling models. link:https://docs.vllm.ai/en/latest/getting_started/quickstart.html#offline-batched-inference ### Suggest a potential alternative/fix _No response_ ### Before submitting a new iss...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
