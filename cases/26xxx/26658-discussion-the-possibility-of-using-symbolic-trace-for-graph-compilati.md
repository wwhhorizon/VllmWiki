# vllm-project/vllm#26658: [Discussion]: The possibility of using symbolic_trace for graph compilation

| 字段 | 值 |
| --- | --- |
| Issue | [#26658](https://github.com/vllm-project/vllm/issues/26658) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Discussion]: The possibility of using symbolic_trace for graph compilation

### Issue 正文摘录

Recently there's an interest (raised from @houseroad ) to see if we can use some simpler tracing methods from PyTorch (simpler than Dynamo). To be specific, it is about `torch.fx.symbolic_trace` . I did some simple investigation, and find that `torch.fx.symbolic_trace` is not enough. `torch.fx.symbolic_trace` works by inspecting the function argument, and runs the function using fake arguments. It will silently drop any conditional branch, and only select the branch being executed, recording all operations in the input arguments. A simple failure case is: ```python import torch from dataclasses import dataclass from typing import Optional, Union @dataclass class IntermediateTensors: """For all pipeline stages except the last, we need to return the hidden states and residuals to be sent to the next stage. This data structure contains the hidden states and residuals for a request. Each stage also needs to handle its own kv_connector_output. """ tensors: dict[str, torch.Tensor] def __init__(self, tensors): # manually define this function, so that # Dynamo knows `IntermediateTensors()` comes from this file. # Otherwise, dataclass will generate this function by evaluating # a string, a...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: interest (raised from @houseroad ) to see if we can use some simpler tracing methods from PyTorch (simpler than Dynamo). To be specific, it is about `torch.fx.symbolic_trace` . I did some simple investigation, and find...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: : if not isinstance(other, self.__class__): return False if self.tensors.keys() != other.tensors.keys(): return False return all(torch.equal(self.tensors[k], other.tensors[k]) for k in self.tensors) def __repr__(self) -...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: e this function by evaluating # a string, and we will lose the information about the source file. self.tensors = tensors def __getitem__(self, key: Union[str, slice]): if isinstance(key, str): return self.tensors[key] e...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: le Python code rather than Bytecode, involving @zou3519 @anijain2305 @ProExpertProg . We can continue the discussion there. Dynamo is very powerful, but we just need to make it more transparent and controllable :)
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: . This data structure contains the hidden states and residuals for a request. Each stage also needs to handle its own kv_connector_output. """ tensors: dict[str, torch.Tensor] def __init__(self, tensors): # manually def...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
