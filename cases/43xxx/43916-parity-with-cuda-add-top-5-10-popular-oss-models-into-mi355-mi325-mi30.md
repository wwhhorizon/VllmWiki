# vllm-project/vllm#43916: [Parity with CUDA]: Add top 5-10 popular OSS models into mi355, mi325, mi300 into vLLM performance  & accuracy regression testing & dashboard

| 字段 | 值 |
| --- | --- |
| Issue | [#43916](https://github.com/vllm-project/vllm/issues/43916) |
| 状态 | open |
| 标签 | feature request;rocm |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Parity with CUDA]: Add top 5-10 popular OSS models into mi355, mi325, mi300 into vLLM performance  & accuracy regression testing & dashboard

### Issue 正文摘录

### 🚀 The feature, motivation and pitch hi @hongxiayang +viz @powderluv @chunfangamd @andyluo7 community vLLM CI has an performance regression for b200, h200, & gb200 yet no Mi300, mi355 this should be done for AMD too as there is regressions on AMD that could of been prevented https://github.com/vllm-project/vllm/issues/43153 https://vllm-ci-dashboard.vercel.app/compare?baseline=public.ecr.aws%2Fq9t5s3a7%2Fvllm-release-repo%3A800604bf53c05b7a11855b4202f2a7e3b6737e5c-x86_64-cu129&candidate=public.ecr.aws%2Fq9t5s3a7%2Fvllm-release-repo%3A799c3afa5d5b17b676d04e0b58a5628943bb4003-x86_64-cu129 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Parity with CUDA]: Add top 5-10 popular OSS models into mi355, mi325, mi300 into vLLM performance & accuracy regression testing & dashboard feature request;rocm ### 🚀 The feature, motivation and pitch hi @hongxiayang +...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: -10 popular OSS models into mi355, mi325, mi300 into vLLM performance & accuracy regression testing & dashboard feature request;rocm ### 🚀 The feature, motivation and pitch hi @hongxiayang +viz @powderluv @chunfangamd @...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: hi @hongxiayang +viz @powderluv @chunfangamd @andyluo7 community vLLM CI has an performance regression for b200, h200, & gb200 yet no Mi300, mi355 this should be done for AMD too as there is regressions on AMD that coul...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: -10 popular OSS models into mi355, mi325, mi300 into vLLM performance & accuracy regression testing & dashboard feature request;rocm ### 🚀 The feature, motivation and pitch hi @hongxiayang +viz @powderluv @chunfangamd @...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Parity with CUDA]: Add top 5-10 popular OSS models into mi355, mi325, mi300 into vLLM performance & accuracy regression testing & dashboard feature request;rocm ### 🚀 The feature, motivation and pitch hi @hongxiayang +...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
