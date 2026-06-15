# vllm-project/vllm#16282: [RFC]: How to handle the compilation of PyTorch/XLA in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#16282](https://github.com/vllm-project/vllm/issues/16282) |
| 状态 | closed |
| 标签 | RFC;tpu |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: How to handle the compilation of PyTorch/XLA in vLLM

### Issue 正文摘录

### Motivation. vLLM currently utilizes PyTorch/XLA to provide TPU backend support. However, PyTorch/XLA differs significantly from native PyTorch in terms of usage. PyTorch/XLA is a compilation only framework, it doesn't have a real eager mode. In particular, for LLM serving services, recompilation should be avoided once the server is running. When compiling, it's important to consider which code might create PyTorch operations (e.g., tensor.copy(), tensor[:index], torch.ones(...)) and when graph capture and compilation is triggered (e.g., xm.mark_step(), xla_tensor.cpu(), if xla_tensor:, torch.compile(backend="openxla")). Due to the complexity of PyTorch/XLA, this document will only provide basic rules to simplify vLLM development on TPU. ### Ways to avoid recompilation The model executor has two primary components: - preparing the model and sampler inputs - executing the model and sampler. #### Step 1 It is recommended to avoid TPU operations when preparing the model and sampler inputs. CPU tensors can be prepared and transferred to the XLA device using cpu_tensor.to(xla_device), which only triggers CPU to TPU transfers and avoids compilation. #### Step 2 The TPU execution shou...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: tion should be avoided once the server is running. When compiling, it's important to consider which code might create PyTorch operations (e.g., tensor.copy(), tensor[:index], torch.ones(...)) and when graph capture and...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ;tpu ### Motivation. vLLM currently utilizes PyTorch/XLA to provide TPU backend support. However, PyTorch/XLA differs significantly from native PyTorch in terms of usage. PyTorch/XLA is a compilation only framework, it...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: o simplify vLLM development on TPU. ### Ways to avoid recompilation The model executor has two primary components: - preparing the model and sampler inputs - executing the model and sampler. #### Step 1 It is recommende...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: (4 at the moment): - the main model - selecting hidden states for each request - sampler - encoder. Each subgraph should be decorated in a torch.compile. This is used to make sure that we have the same subgraph topology...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
