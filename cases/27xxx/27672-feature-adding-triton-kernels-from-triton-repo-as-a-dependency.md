# vllm-project/vllm#27672: [Feature]: Adding `triton_kernels` from Triton repo as a dependency

| 字段 | 值 |
| --- | --- |
| Issue | [#27672](https://github.com/vllm-project/vllm/issues/27672) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;moe |
| 子分类 | install |
| Operator 关键词 | cuda;kernel;moe;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Adding `triton_kernels` from Triton repo as a dependency

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The `triton_kernels` package in the Triton repository exposes some operations to execute the MoE layer operations. These kernels are integrated into vLLM already, look at, https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py On Hopper, using the `triton_kernels` is the most performant option to run gpt_oss models. On Blackwell, using `triton_kernels` is one of the performant options to run gpt_oss models. ### Proposal: At the moment, users will have to install `triton_kernels` manually from `triton_kernels @ git+https://github.com/triton-lang/triton.git@v3.5.0#subdirectory=python/triton_kernels`. It would be good to add the `triton_kernels` package as a direct dependency so users can start using it out of the box with a `vllm` install. ### Issues: The PR https://github.com/vllm-project/vllm/pull/27370 tried to add the dependency by adding an entry to the `requirements/cuda.txt` file. But this resulted in installation issues - see https://github.com/vllm-project/vllm/issues/27573 The crux of the problem is that, `triton_kernels` is a sub-directory in the Triton repository. It looks...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Feature]: Adding `triton_kernels` from Triton repo as a dependency feature request ### 🚀 The feature, motivation and pitch The `triton_kernels` package in the Triton repository exposes some operations to execute the Mo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: n/vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py On Hopper, using the `triton_kernels` is the most performant option to run gpt_oss models. On Blackwell, using `triton_kernels` is one of the performa...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Feature]: Adding `triton_kernels` from Triton repo as a dependency feature request ### 🚀 The feature, motivation and pitch The `triton_kernels` package in the Triton repository exposes some operations to execute the Mo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: M already, look at, https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py On Hopper, using the `triton_kernels` is the most performant option to run gpt_oss mo...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: package in the Triton repository exposes some operations to execute the MoE layer operations. These kernels are integrated into vLLM already, look at, https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/l...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
