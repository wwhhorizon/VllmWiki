# vllm-project/vllm#21092: [Performance]: MoE Parameters on Qwen3-30B-A3B using vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#21092](https://github.com/vllm-project/vllm/issues/21092) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;moe;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;moe;operator;triton |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: MoE Parameters on Qwen3-30B-A3B using vLLM

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance When using vLLM for inference with the Qwen3-30B-A3B model (which uses an MoE architecture), I tested several MoE-related parameters. However, I observed that enabling these parameters actually reduced generation performance (higher latency and lower throughput), compared to not using them at all. I expected --enable-expert-parallel and --enable-eplb to improve load distribution and efficiency, but in practice, they seemed to add communication overhead without measurable benefits. ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 3.19.3 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.7.0+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to buil...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: e-expert-parallel and --enable-eplb to improve load distribution and efficiency, but in practice, they seemed to add communication overhead without measurable benefits. ### Your current environment (if you think it is n...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: using vLLM for inference with the Qwen3-30B-A3B model (which uses an MoE architecture), I tested several MoE-related parameters. However, I observed that enabling these parameters actually reduced generation performance...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Performance]: MoE Parameters on Qwen3-30B-A3B using vLLM performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance When us...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: roposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance When using vLLM for inference with the Qwen3-30B-A3B model (which uses an MoE architectu...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Performance]: MoE Parameters on Qwen3-30B-A3B using vLLM performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance When us...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
