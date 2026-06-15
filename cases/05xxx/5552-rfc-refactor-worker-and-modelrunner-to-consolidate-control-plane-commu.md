# vllm-project/vllm#5552: [RFC]: Refactor Worker and ModelRunner to consolidate control plane communication

| 字段 | 值 |
| --- | --- |
| Issue | [#5552](https://github.com/vllm-project/vllm/issues/5552) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Refactor Worker and ModelRunner to consolidate control plane communication

### Issue 正文摘录

### Motivation. Currently, both the Worker and the ModelRunner classes contain multi-GPU control plane communication code, i.e. `broadcast_tensor_dict` calls. They look something like this: ```python class Worker: def execute_model(self, execute_model_req=None): # Do some broadcast here. ... return self.model_runner.execute_model(execute_model_req) class ModelRunner: def execute_model(self, execute_model_req=None): # Do some more broadcast here. ... return model_executable(...) ``` Because the ModelRunner class contains both model execution code and multi-GPU control plane communication code, it makes it difficult to improve upon the performance: - Cannot swap out the control plane mechanism, e.g., using NCCL vs CPU-based serialization to move the inputs from the LLMEngine to the Workers - Cannot switch to an SPMD design, where the rank 0 worker is moved off of the driver and executes the same code as the rest of the workers - Difficult to overlap GPU data movement with other compute on Workers, because these are all done ad-hoc in different ModelRunner implementations. - Difficult to optimize control plane performance, because the broadcast calls are scattered throughout the code...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: te a `WorkerInput` and a `ModelInput` respectively from the `ExecuteModelRequest`. The contract is that `ExecuteModelRequest` contains CPU-only metadata, while any tensors in `WorkerInput` and `ModelInput` should alread...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: plane communication vs. single-GPU logic. Each ModelRunner needs to explicitly state what inputs it requires by defining a ModelInput (subclass). This requires a bit more developer effort but should make it easier to in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: improve upon the performance: - Cannot swap out the control plane mechanism, e.g., using NCCL vs CPU-based serialization to move the inputs from the LLMEngine to the Workers - Cannot switch to an SPMD design, where the...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: elRequest`. The contract is that `ExecuteModelRequest` contains CPU-only metadata, while any tensors in `WorkerInput` and `ModelInput` should already be on the correct device. Now, the ModelRunnerBase class looks approx...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [RFC]: Refactor Worker and ModelRunner to consolidate control plane communication RFC ### Motivation. Currently, both the Worker and the ModelRunner classes contain multi-GPU control plane communication code, i.e. `broa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
