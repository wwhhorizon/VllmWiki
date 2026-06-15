# vllm-project/vllm#38692: [Bug]: parity with CUDA & parity with rocm sglang: vLLM router doesn't current support MoRI kvcache connector

| 字段 | 值 |
| --- | --- |
| Issue | [#38692](https://github.com/vllm-project/vllm/issues/38692) |
| 状态 | closed |
| 标签 | bug;feature request;rocm |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: parity with CUDA & parity with rocm sglang: vLLM router doesn't current support MoRI kvcache connector

### Issue 正文摘录

### Your current environment all the nightly images in https://hub.docker.com/r/vllm/vllm-openai-rocm/tags as of April 1st, 2026 `vllm/vllm-openai-rocm:v0.18.1` `vllm/vllm-openai-rocm:v0.18.0` ### 🐛 Describe the bug hi @hongxiayang +viz @powderluv @chunfangamd @andyluo7 @ChuanLi1101 vLLM router does not currently with with MoRI kvcache connector for ROCm disagg. Verus on the CUDA side, vLLM router works with the NVIDIA equivalent of MoRI kvcache connector aka NIXL. On ROCm vLLM stack, users can only currently use RIXL (the second class fork of NIXL, RIXL isn't included out of the box in the docker image unfortunately) or use the MORIIO kvcache toy proxy server which is not prod ready. On ROCm SGLang stack, the sglang equivalent of vLLM router is called sglang model gateway server is already supports MoRI kvcache transfer. Lets ensure that the ROCm vLLM experience is parity with ROCm SGlang experience https://github.com/sgl-project/sglang/pull/14626 Can you look into having vLLM router support MoRI kvcache transfer? thanks the expected user experience is that the python wheel from upstream pypi and the docker image should support it https://hub.docker.com/r/vllm/vllm-router/tags ht...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: parity with CUDA & parity with rocm sglang: vLLM router doesn't current support MoRI kvcache connector bug;feature request;rocm ### Your current environment all the nightly images in https://hub.docker.com/r/vllm...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: rocm ### Your current environment all the nightly images in https://hub.docker.com/r/vllm/vllm-openai-rocm/tags as of April 1st, 2026 `vllm/vllm-openai-rocm:v0.18.1` `vllm/vllm-openai-rocm:v0.18.0` ### 🐛 Describe the bu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ROCm SGLang stack, the sglang equivalent of vLLM router is called sglang model gateway server is already supports MoRI kvcache transfer. Lets ensure that the ROCm vLLM experience is parity with ROCm SGlang experience ht...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: parity with CUDA & parity with rocm sglang: vLLM router doesn't current support MoRI kvcache connector bug;feature request;rocm ### Your current environment all the nightly images in https://hub.docker.com/r/vllm...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: : vLLM router doesn't current support MoRI kvcache connector bug;feature request;rocm ### Your current environment all the nightly images in https://hub.docker.com/r/vllm/vllm-openai-rocm/tags as of April 1st, 2026 `vll...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
