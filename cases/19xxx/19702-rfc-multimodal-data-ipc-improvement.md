# vllm-project/vllm#19702: [RFC]: Multimodal data IPC improvement

| 字段 | 值 |
| --- | --- |
| Issue | [#19702](https://github.com/vllm-project/vllm/issues/19702) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Multimodal data IPC improvement

### Issue 正文摘录

### Motivation. ### Summary Currently vllm interprocess communication can account for considerable amount of overhead in some cases, this RFC is aiming at reducing these overhead by using a shared memory based approach for interprocess communication. ### Background According to the profiling result on our internal vision model in a TP>1 setting, the GPU stays idle during engine to worker communication. ![Image](https://github.com/user-attachments/assets/4669088c-ddd6-4947-bb30-1c1bce0985a5) The major overhead is two parts 1. IPC between engine and worker process through socket 2. serialization and deserialization through pickle A similar issue is posted here https://github.com/vllm-project/vllm/issues/16626 ### Proposed Change. After initial discussion with @ywang96 and @njhill , proposing this change to address the following communication overhead 1. IPC between engine and worker processes 2. Serialization and deserialization before and after 1. 3. Extra multimodal data transmission: first from P0 to engine, then engine to workers ### Design **Step 1.** For addressing 1. engine and worker processes can transmit mm data through a shared memory buffer instead of socket, there’s an...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ion and deserialization before and after 1. 3. Extra multimodal data transmission: first from P0 to engine, then engine to workers ### Design **Step 1.** For addressing 1. engine and worker processes can transmit mm dat...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [RFC]: Multimodal data IPC improvement RFC ### Motivation. ### Summary Currently vllm interprocess communication can account for considerable amount of overhead in some cases, this RFC is aiming at reducing these overhe...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: pproach for interprocess communication. ### Background According to the profiling result on our internal vision model in a TP>1 setting, the GPU stays idle during engine to worker communication. ![Image](https://github....
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: data and only keep the mm_hashes for RPC call. Similar to when P0 gets a cache hit, we can [set mm data to None](https://github.com/vllm-project/vllm/blob/main/vllm/v1/engine/mm_input_cache.py#L58) in the engine process...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: considerable amount of overhead in some cases, this RFC is aiming at reducing these overhead by using a shared memory based approach for interprocess communication. ### Background According to the profiling result on ou...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
