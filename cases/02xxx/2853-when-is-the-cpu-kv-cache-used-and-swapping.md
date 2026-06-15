# vllm-project/vllm#2853: When is the CPU KV cache used and swapping?

| 字段 | 值 |
| --- | --- |
| Issue | [#2853](https://github.com/vllm-project/vllm/issues/2853) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> When is the CPU KV cache used and swapping?

### Issue 正文摘录

Hi authors, In your implementation, the GPU memory is leveraged to store the KV cache. However, it appears that when the GPU memory reaches its capacity, there isn't a mechanism in place to offload or swap this data to the CPU memory. 1. Could you please clarify under what conditions the CPU KV cache comes into play? 2. Could you please tell me how to invoke the CPU KV cache (or API) if I want to do swapping? ![Screenshot 2024-02-01 at 2 41 42 PM](https://github.com/vllm-project/vllm/assets/47625290/38ee7a92-486d-4e2a-a7f1-3c8af2424cd4) ![Screenshot 2024-02-13 at 1 53 57 PM](https://github.com/vllm-project/vllm/assets/47625290/618227a2-c599-4028-b47d-ae03e0762016)

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: When is the CPU KV cache used and swapping? Hi authors, In your implementation, the GPU memory is leveraged to store the KV cache. However, it appears that when the GPU memory reaches its capacity, there isn't a mechani...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e KV cache. However, it appears that when the GPU memory reaches its capacity, there isn't a mechanism in place to offload or swap this data to the CPU memory. 1. Could you please clarify under what conditions the CPU K...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ears that when the GPU memory reaches its capacity, there isn't a mechanism in place to offload or swap this data to the CPU memory. 1. Could you please clarify under what conditions the CPU KV cache comes into play? 2....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
