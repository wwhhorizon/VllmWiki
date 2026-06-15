# vllm-project/vllm#14222: [Usage]: Getting intermediate outputs to store on disk

| 字段 | 值 |
| --- | --- |
| Issue | [#14222](https://github.com/vllm-project/vllm/issues/14222) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Getting intermediate outputs to store on disk

### Issue 正文摘录

### Your current environment I want to know something simple: is it supported to get intermediate outputs (i.e. like the snippet below in huggingface) and if so how? ```python with torch.no_grad(): outputs = model(**inputs, output_hidden_states=True) return outputs.hidden_states # <----- I want this ``` Maybe I haven't searched enough but it doesn't seem to be documented how to do it (which leads me to believe it cannot be done). One out of a couple different workflows are fine with me: 1. Some kind of hook that writes to a memory buffer or file (i.e. on disk) in pt, safetensors, or basically any format 2. Return the intermediate values in python 3. Return the intermediate values in C++ somehow 4. Have the ability to set hooks and documentation that makes it clear how to do this without erasure or errors in the return values (i.e. due to overwriting or any other such thing) ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentatio...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: it supported to get intermediate outputs (i.e. like the snippet below in huggingface) and if so how? ```python with torch.no_grad(): outputs = model(**inputs, output_hidden_states=True) return outputs.hidden_states # <-...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: g) ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: return outputs.hidden_states # <----- I want this ``` Maybe I haven't searched enough but it doesn't seem to be documented how to do it (which leads me to believe it cannot be done). One out of a couple different workfl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Getting intermediate outputs to store on disk usage;stale ### Your current environment I want to know something simple: is it supported to get intermediate outputs (i.e. like the snippet below in huggingface) a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
