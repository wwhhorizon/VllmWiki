# vllm-project/vllm#16481: [Urgent]: Parameter Change

| 字段 | 值 |
| --- | --- |
| Issue | [#16481](https://github.com/vllm-project/vllm/issues/16481) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Urgent]: Parameter Change

### Issue 正文摘录

### Your current environment During training, For the version 0.8.3. vllm_model = LLM(model='blah blah', blah blah) model = huggingface model (assuming vllm_model and model architecture and the weight name is exactly same) optimizer = Adam(model.parameters(), blah blah) for iter in range(training_iterations): loss = blah blah() loss.backward() optimizer.step() %% what i wanna do is to change the param of vLLM for the param of updated model params during training iterations. %% I don't know how to do it. Please let me know. The below is my imagination vllm_model.load_weights(model.parameters()) ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ange usage;stale ### Your current environment During training, For the version 0.8.3. vllm_model = LLM(model='blah blah', blah blah) model = huggingface model (assuming vllm_model and model architecture and the weight n...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Your current environment During training, For the version 0.8.3. vllm_model = LLM(model='blah blah', blah blah) model = huggingface model (assuming vllm_model and model architecture and the weight name is exactly same)...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ', blah blah) model = huggingface model (assuming vllm_model and model architecture and the weight name is exactly same) optimizer = Adam(model.parameters(), blah blah) for iter in range(training_iterations): loss = bla...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Urgent]: Parameter Change usage;stale ### Your current environment During training, For the version 0.8.3. vllm_model = LLM(model='blah blah', blah blah) model = huggingface model (assuming vllm_model and model archite...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
