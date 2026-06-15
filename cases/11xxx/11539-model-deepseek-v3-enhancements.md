# vllm-project/vllm#11539: [Model] DeepSeek-V3 Enhancements 

| 字段 | 值 |
| --- | --- |
| Issue | [#11539](https://github.com/vllm-project/vllm/issues/11539) |
| 状态 | closed |
| 标签 | performance;new-model;stale |
| 评论 | 52; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;model_support;moe;quantization;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | attention;cuda;kernel;moe;quantization |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Model] DeepSeek-V3 Enhancements 

### Issue 正文摘录

This issue tracks follow up enhancements after initial support for the Deepseek V3 model. Please feel free to chime in and contribute! - [x] Follow up #11523: enhance testing with shapes of production models and run it regularly on H100. * Solving via cutlas blockwise quantization kernels. - [x] Follow up #11502: - [x] Test and enable torch.compile - [ ] ~Refactor MoEMethodBase to unify and clean up the extra arguments of `scoring_func` and `e_correction_bias`~ - [x] Kernel tuning for 8xH200, MI300x, H100 (TP16 and TP8PP2 case) - Use https://github.com/vllm-project/vllm/blob/main/benchmarks/kernels/benchmark_moe.py, but adapt it for the w8a8 fused moe kernel. - [x] CUDA Graph support - [x] MLA #10927 @simon-mo - [ ] Support nextn prediction heads ([EAGLE](https://arxiv.org/abs/2401.15077) style prediction heads) - Original PR for EAGLE support #6830 Perf #9565 Discussion #11126 Docs #11417 - [ ] Support expert parallelism for MoE. - [ ] Support data parallelism for MLA.

## 现有链接修复摘要

#10927 [WIP] Deepseek V2 MLA

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: enhance testing with shapes of production models and run it regularly on H100. * Solving via cutlas blockwise quantization kernels. - [x] Follow up #11502: - [x] Test and enable torch.compile - [ ] ~Refactor MoEMethodBa...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ation kernels. - [x] Follow up #11502: - [x] Test and enable torch.compile - [ ] ~Refactor MoEMethodBase to unify and clean up the extra arguments of `scoring_func` and `e_correction_bias`~ - [x] Kernel tuning for 8xH20...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: up #11502: - [x] Test and enable torch.compile - [ ] ~Refactor MoEMethodBase to unify and clean up the extra arguments of `scoring_func` and `e_correction_bias`~ - [x] Kernel tuning for 8xH200, MI300x, H100 (TP16 and TP...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Model] DeepSeek-V3 Enhancements performance;new-model;stale This issue tracks follow up enhancements after initial support for the Deepseek V3 model. Please feel free to chime in and contribute! - [x] Follow up #11523:...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: feel free to chime in and contribute! - [x] Follow up #11523: enhance testing with shapes of production models and run it regularly on H100. * Solving via cutlas blockwise quantization kernels. - [x] Follow up #11502: -...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#10927](https://github.com/vllm-project/vllm/pull/10927) | mentioned | 0.45 | [WIP] Deepseek V2 MLA | r the w8a8 fused moe kernel. - [x] cuda graph support - [x] mla #10927 @simon-mo - [ ] support nextn prediction heads ([eagle](https://arxiv.org/abs/2401.15077) style prediction h |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
