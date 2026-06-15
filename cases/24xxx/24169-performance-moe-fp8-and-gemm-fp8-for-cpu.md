# vllm-project/vllm#24169: [Performance]: MoE FP8 and Gemm FP8 for CPU

| 字段 | 值 |
| --- | --- |
| Issue | [#24169](https://github.com/vllm-project/vllm/issues/24169) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: MoE FP8 and Gemm FP8 for CPU

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression We implemented a single-node vllm inference solution for the DeepSeek-R1 671B model based on a hybrid CPU-GPU architecture, handling some of the expert MoE computation tasks on Xeon Sapphirerapids processors. Since x86 processors do not support FP8 native floating-point computation, we leveraged the ktransformers MoE operator framework to extend the functionality of online conversion of DeepSeek-R1's FP8 weights to BF16 format, seamlessly providing support for the DeepSeek-R1 671B model on Sapphirerapids processors. In July, we discovered that the new version of VLLM also added support for Moe FP8 and Gemm FP8 for cpu. We tested the torch.ops._C.fused_experts_cpu operator based on the DeepSeek-R1 671B model. The test results showed that for input data batch sizes of 1/2/4/8, the average Moe computational latency amortized to per expert and per input tensor for a single model layer was about 45% higher than our implementation. Does anyone know the main reason for the higher computational latency in the Moe FP8 and Gemm FP8 for cpu of the VLLM version? ### Misc discussion on performance _No respon...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Performance]: MoE FP8 and Gemm FP8 for CPU performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression We implemented a single-node vllm inference solution for the DeepSeek-...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: roposal to improve performance _No response_ ### Report of performance regression We implemented a single-node vllm inference solution for the DeepSeek-R1 671B model based on a hybrid CPU-GPU architecture, handling some...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Performance]: MoE FP8 and Gemm FP8 for CPU performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression We implemented a single-node vllm inference solution for the DeepSeek-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: plemented a single-node vllm inference solution for the DeepSeek-R1 671B model based on a hybrid CPU-GPU architecture, handling some of the expert MoE computation tasks on Xeon Sapphirerapids processors. Since x86 proce...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: sformers MoE operator framework to extend the functionality of online conversion of DeepSeek-R1's FP8 weights to BF16 format, seamlessly providing support for the DeepSeek-R1 671B model on Sapphirerapids processors. In...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
