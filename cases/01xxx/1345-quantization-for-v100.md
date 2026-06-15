# vllm-project/vllm#1345: Quantization for V100

| 字段 | 值 |
| --- | --- |
| Issue | [#1345](https://github.com/vllm-project/vllm/issues/1345) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Quantization for V100

### Issue 正文摘录

Similar to #1252 , do we have any plans for supporting V100. For now I can see that the place need to be modified is ldmatrix instruction and m16n8k16, as an example we may need to load the matrix manually and perform the mma in a smaller size, for example, maybe we need something similar to these ```c++ #if defined(__CUDA_ARCH__) && __CUDA_ARCH__ == 700 // Manually loading each fragment, ldmatrix only available on sm_75 and after __asm__ __volatile__( "ld.shared.b16 %0, [%4];\n" "ld.shared.b16 %1, [%4 + 2];\n" "ld.shared.b16 %2, [%4 + 4];\n" "ld.shared.b16 %3, [%4 + 6];\n" : "=r"(((unsigned *)(B_shared_warp + (ax1_0 * 8)))[0]), "=r"(((unsigned *)(B_shared_warp + (ax1_0 * 8)))[1]), "=r"(((unsigned *)(B_shared_warp + (ax1_0 * 8)))[2]), "=r"(((unsigned *)(B_shared_warp + (ax1_0 * 8)))[3]) : "r"(addr) ); #else __asm__ __volatile__( "ldmatrix.sync.aligned.m8n8.x4.trans.shared.b16" "{%0, %1, %2, %3}, [%4];\n" : "=r"(((unsigned *)(B_shared_warp + (ax1_0 * 8)))[0]), "=r"(((unsigned *)(B_shared_warp + (ax1_0 * 8)))[1]), "=r"(((unsigned *)(B_shared_warp + (ax1_0 * 8)))[2]), "=r"(((unsigned *)(B_shared_warp + (ax1_0 * 8)))[3]) : "r"(addr) ); #endif ``` and ```c++ #if defined(__CUDA_ARCH__)...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: example we may need to load the matrix manually and perform the mma in a smaller size, for example, maybe we need something similar to these ```c++ #if defined(__CUDA_ARCH__) && __CUDA_ARCH__ == 700 // Manually loading...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: shared_warp + (ax1_0 * 8)))[3]) : "r"(addr) ); #else __asm__ __volatile__( "ldmatrix.sync.aligned.m8n8.x4.trans.shared.b16" "{%0, %1, %2, %3}, [%4];\n" : "=r"(((unsigned *)(B_shared_warp + (ax1_0 * 8)))[0]), "=r"(((unsi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: Quantization for V100 stale Similar to #1252 , do we have any plans for supporting V100. For now I can see that the place need to be modified is ldmatrix instruction and m16n8k16, as an example we may need to load the ma
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Quantization for V100 stale Similar to #1252 , do we have any plans for supporting V100. For now I can see that the place need to be modified is ldmatrix instruction and m16n8k16, as an example we may need to load the m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
