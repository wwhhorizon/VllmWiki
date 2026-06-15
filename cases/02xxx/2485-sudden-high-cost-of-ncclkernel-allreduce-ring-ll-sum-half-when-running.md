# vllm-project/vllm#2485: sudden high cost of ncclKernel_AllReduce_RING_LL_Sum_half when running on 2 A100

| 字段 | 值 |
| --- | --- |
| Issue | [#2485](https://github.com/vllm-project/vllm/issues/2485) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> sudden high cost of ncclKernel_AllReduce_RING_LL_Sum_half when running on 2 A100

### Issue 正文摘录

Hi all I'm running the latest vllm (0.2.7) on a 8*A100 machine. When I set CUDA_VISIBLE_DEVICES=2,3, and run vllm server_api, the performance sometimes gets low in a sudden. When it occurs, the GPU util falls from 70% to 20%, and the token throughput gets very low. that's strange. Here is the normal state: ![image](https://github.com/vllm-project/vllm/assets/26128514/737bb6d9-44bb-4f57-a0f8-0eae88d185cb) Here is the abnormal state: ![image](https://github.com/vllm-project/vllm/assets/26128514/dd8eda47-948d-4813-8bf3-24a6396742c1) When I test the time cost, the ncclKernel_AllReduce_RING_LL_Sum_half takes 78.5%. ``` Time (%) Total Time (ns) Instances Avg (ns) Med (ns) Min (ns) Max (ns) StdDev (ns) GridXYZ BlockXYZ Name -------- --------------- --------- --------- -------- -------- -------- ----------- -------------- -------------- ---------------------------------------------------------------------------------------------------- 78.5 10751311 4 2687827.8 116416.5 101729 10416749 5152630.4 24 1 1 544 1 1 ncclKernel_AllReduce_RING_LL_Sum_half(ncclDevComm *, unsigned long, ncclWork *) 6.8 936679 2 468339.5 468339.5 468003 468676 475.9 54 6 1 256 1 1 ampere_fp16_s16816gemm_fp16_256x128...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: den high cost of ncclKernel_AllReduce_RING_LL_Sum_half when running on 2 A100 Hi all I'm running the latest vllm (0.2.7) on a 8*A100 machine. When I set CUDA_VISIBLE_DEVICES=2,3, and run vllm server_api, the performance...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: lReduce_RING_LL_Sum_half when running on 2 A100 Hi all I'm running the latest vllm (0.2.7) on a 8*A100 machine. When I set CUDA_VISIBLE_DEVICES=2,3, and run vllm server_api, the performance sometimes gets low in a sudde...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: Avg (ns) Med (ns) Min (ns) Max (ns) StdDev (ns) GridXYZ BlockXYZ Name -------- --------------- --------- --------- -------- -------- -------- ----------- -------------- -------------- -----------------------------
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: 468676 475.9 54 6 1 256 1 1 ampere_fp16_s16816gemm_fp16_256x128_ldg8_f2f_stages_64x3_tn 4.6 625797 2 312898.5 312898.5 312802 312995 136.5 30 6 1 256 1 1 ampere_fp16_s16816gemm_fp16_256x128_ldg8_f2f_stages_6

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
