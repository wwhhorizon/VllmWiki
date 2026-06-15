# vllm-project/vllm#3012: Unable to specify GPU usage in VLLM code

| 字段 | 值 |
| --- | --- |
| Issue | [#3012](https://github.com/vllm-project/vllm/issues/3012) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Unable to specify GPU usage in VLLM code

### Issue 正文摘录

I am facing difficulties in specifying GPU usage for different models for LLM inference pipeline using vLLM. Specifically, I have 4 RTX 4090 GPUs available, and I aim to run a LLM with a size of 42GB on 2 RTX 4090 GPUs (~48GB) and a separate model with a size of 22GB on 1 RTX 4090 GPU(`24GB). This is my code for running 42GB model on two GPUs. ```python from vllm import LLM llm = LLM(model_name, max_model_len=50, tensor_parallel_size=2) output = llm.generate(text) ``` However, I haven't found a straightforward method within the VLLM library to specify which GPU should be used for each model.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Unable to specify GPU usage in VLLM code stale I am facing difficulties in specifying GPU usage for different models for LLM inference pipeline using vLLM. Specifically, I have 4 RTX 4090 GPUs available, and I aim to ru...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ent models for LLM inference pipeline using vLLM. Specifically, I have 4 RTX 4090 GPUs available, and I aim to run a LLM with a size of 42GB on 2 RTX 4090 GPUs (~48GB) and a separate model with a size of 22GB on 1 RTX 4...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ode stale I am facing difficulties in specifying GPU usage for different models for LLM inference pipeline using vLLM. Specifically, I have 4 RTX 4090 GPUs available, and I aim to run a LLM with a size of 42GB on 2 RTX...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Unable to specify GPU usage in VLLM code stale I am facing difficulties in specifying GPU usage for different models for LLM inference pipeline using vLLM. Specifically, I have 4 RTX 4090 GPUs available, and I aim to ru...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
