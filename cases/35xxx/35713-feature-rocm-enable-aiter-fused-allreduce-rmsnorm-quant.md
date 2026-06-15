# vllm-project/vllm#35713: [Feature] [ROCm]: Enable AITER `fused_allreduce_rmsnorm_quant`

| 字段 | 值 |
| --- | --- |
| Issue | [#35713](https://github.com/vllm-project/vllm/issues/35713) |
| 状态 | open |
| 标签 | feature request;rocm;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | activation_norm;ci_build;distributed_parallel;frontend_api;hardware_porting;quantization |
| 子分类 |  |
| Operator 关键词 | activation;operator;quantization |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature] [ROCm]: Enable AITER `fused_allreduce_rmsnorm_quant`

### Issue 正文摘录

### 🚀 The feature, motivation and pitch 1. Enable All Reduce + RMSNorm + quant Fusion pass for ROCm using AITER Ops https://github.com/ROCm/aiter/blob/71378cf4a886a4dd702b8d8c868ea5bebc735903/aiter/dist/parallel_state.py#L161C5-L161C34 2. Enable `pytest -v -s tests/compile/passes/distributed/test_fusion_all_reduce.py` ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#36425 [ROCm] Enable AITER fused allreduce + RMSNorm compilation pass

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ter/dist/parallel_state.py#L161C5-L161C34 2. Enable `pytest -v -s tests/compile/passes/distributed/test_fusion_all_reduce.py` ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a n...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature] [ROCm]: Enable AITER `fused_allreduce_rmsnorm_quant` feature request;rocm;stale ### 🚀 The feature, motivation and pitch 1. Enable All Reduce + RMSNorm + quant Fusion pass for ROCm using AITER Ops https://githu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature] [ROCm]: Enable AITER `fused_allreduce_rmsnorm_quant` feature request;rocm;stale ### 🚀 The feature, motivation and pitch 1. Enable All Reduce + RMSNorm + quant Fusion pass for ROCm using AITER Ops https://githu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Feature] [ROCm]: Enable AITER `fused_allreduce_rmsnorm_quant` feature request;rocm;stale ### 🚀 The feature, motivation and pitch 1. Enable All Reduce + RMSNorm + quant Fusion pass for ROCm using AITER Ops https://githu...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Feature] [ROCm]: Enable AITER `fused_allreduce_rmsnorm_quant` feature request;rocm;stale ### 🚀 The feature, motivation and pitch 1. Enable All Reduce + RMSNorm + quant Fusion pass for ROCm using AITER Ops https://githu...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36425](https://github.com/vllm-project/vllm/pull/36425) | closes_keyword | 0.95 | [ROCm] Enable AITER fused allreduce + RMSNorm compilation pass | Closes #35712 Related to #35713 ## Test plan - [ ] Run `test_rocm_aiter_allreduce_fusion.py` on 2+ ROCm GPUs (MI300X or MI355X) with AITER installed - [ ] Verify pattern matching |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
