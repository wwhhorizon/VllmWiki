# vllm-project/vllm#34851: [Feature]: Refactor Quark MoE and mxfp4 MoE to align with MoE oracle/MK

| 字段 | 值 |
| --- | --- |
| Issue | [#34851](https://github.com/vllm-project/vllm/issues/34851) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Refactor Quark MoE and mxfp4 MoE to align with MoE oracle/MK

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Tracking a couple of refactoring issues related to Quark moe and mxfp4 moe. Overall goal is to clean-up code and reduce duplication, aligning Quark/MXFP4 MoE implementations with the MoE oracle/MK flow. - [ ] https://github.com/vllm-project/vllm/issues/30621; https://github.com/vllm-project/vllm/pull/32120 - [x] https://github.com/vllm-project/vllm/pull/30357 - [x] https://github.com/vllm-project/vllm/pull/34285 - [x] Refactor w4a16 https://github.com/vllm-project/vllm/pull/38774 - [ ] Unittests & Refactor w4a8 https://github.com/vllm-project/vllm/pull/39136 - [ ] Refactor w4a4 - [ ] Refactor and introduce emulation backend. - [ ] Remove gpt-oss special handling in `QuarkW8A8Fp8MoEMethod`. @xuebwang-amd - [ ] Refactor `QuarkW8A8Fp8MoEMethod` to adopt FP8 MoE oracle cc @robertgshaw2-redhat , @mgoin ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Feature]: Refactor Quark MoE and mxfp4 MoE to align with MoE oracle/MK feature request ### 🚀 The feature, motivation and pitch Tracking a couple of refactoring issues related to Quark moe and mxfp4 moe. Overall goal is...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: lm/pull/39136 - [ ] Refactor w4a4 - [ ] Refactor and introduce emulation backend. - [ ] Remove gpt-oss special handling in `QuarkW8A8Fp8MoEMethod`. @xuebwang-amd - [ ] Refactor `QuarkW8A8Fp8MoEMethod` to adopt FP8 MoE o...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: - [ ] Refactor and introduce emulation backend. - [ ] Remove gpt-oss special handling in `QuarkW8A8Fp8MoEMethod`. @xuebwang-amd - [ ] Refactor `QuarkW8A8Fp8MoEMethod` to adopt FP8 MoE oracle cc @robertgshaw2-redhat , @m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: factor w4a4 - [ ] Refactor and introduce emulation backend. - [ ] Remove gpt-oss special handling in `QuarkW8A8Fp8MoEMethod`. @xuebwang-amd - [ ] Refactor `QuarkW8A8Fp8MoEMethod` to adopt FP8 MoE oracle cc @robertgshaw2...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
