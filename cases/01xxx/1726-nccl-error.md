# vllm-project/vllm#1726: NCCL error

| 字段 | 值 |
| --- | --- |
| Issue | [#1726](https://github.com/vllm-project/vllm/issues/1726) |
| 状态 | closed |
| 标签 |  |
| 评论 | 24; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> NCCL error

### Issue 正文摘录

I'm trying to load model into LLM(model="meta-llama/Llama-2-7b-chat-hf") and I'm getting the error below ``` DistBackendError: NCCL error in: ../torch/csrc/distributed/c10d/NCCLUtils.hpp:219, invalid argument, NCCL version 2.14.3 ncclInvalidArgument: Invalid value for an argument. Last error: Invalid config blocking attribute value -2147483648 ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: NCCL error I'm trying to load model into LLM(model="meta-llama/Llama-2-7b-chat-hf") and I'm getting the error below ``` DistBackendError: NCCL error in: ../torch/csrc/distributed/c10d/NCCLUtils.hpp:219, invalid argument...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: meta-llama/Llama-2-7b-chat-hf") and I'm getting the error below ``` DistBackendError: NCCL error in: ../torch/csrc/distributed/c10d/NCCLUtils.hpp:219, invalid argument, NCCL version 2.14.3 ncclInvalidArgument: Invalid v...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ../torch/csrc/distributed/c10d/NCCLUtils.hpp:219, invalid argument, NCCL version 2.14.3 ncclInvalidArgument: Invalid value for an argument. Last error: Invalid config blocking attribute value -2147483648 ```
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: validArgument: Invalid value for an argument. Last error: Invalid config blocking attribute value -2147483648 ```

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
