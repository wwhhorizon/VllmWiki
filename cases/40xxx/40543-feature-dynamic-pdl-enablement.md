# vllm-project/vllm#40543: [Feature]: Dynamic PDL Enablement

| 字段 | 值 |
| --- | --- |
| Issue | [#40543](https://github.com/vllm-project/vllm/issues/40543) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;hardware_porting |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;kernel;triton |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Dynamic PDL Enablement

### Issue 正文摘录

### 🚀 The feature, motivation and pitch There are two undocumented flags that improve low-latency performance on Hopper and Blackwell: - **TRTLLM_ENABLE_PDL**: Enable PDL in the DeepSeek fused QKV A Projection. - **TORCHINDUCTOR_ENABLE_PDL**: Enable PDL in all torch.compile'd triton kernels. PDL is a valuable feature, but unfortunately adds some slight host overhead which can hurt in the prefill phase. We want to enable this only during FULL cuda graph execution, but not during PIECEWISE or NONE graph modes. This adds a fair bit of complexity to the implementation. I am not sure if this can be implemented simply by just decorating `set_forward_context` or similar, since I don't know if/how torch.compile caches the compiled kernels; I am concerned that the piecewise graph capture might pre-populate torch's caches with non-PDL kernels and those would be used during the FULL graph capture. _I'm not sure this is the case, but it seems probable and I don't see a clear path around it_. ### Alternatives Alternatively, we can just leave it up to the caller to provide these flags or add them to the `--performance-mode latency` feature set. Either way, we'll need to document this. ### Addit...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: KV A Projection. - **TORCHINDUCTOR_ENABLE_PDL**: Enable PDL in all torch.compile'd triton kernels. PDL is a valuable feature, but unfortunately adds some slight host overhead which can hurt in the prefill phase. We want...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: There are two undocumented flags that improve low-latency performance on Hopper and Blackwell: - **TRTLLM_ENABLE_PDL**: Enable PDL in the DeepSeek fused QKV A Projection. - **TORCHINDUCTOR_ENABLE_PDL**: Enable PDL in al...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Dynamic PDL Enablement feature request ### 🚀 The feature, motivation and pitch There are two undocumented flags that improve low-latency performance on Hopper and Blackwell: - **TRTLLM_ENABLE_PDL**: Enable PD...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: motivation and pitch There are two undocumented flags that improve low-latency performance on Hopper and Blackwell: - **TRTLLM_ENABLE_PDL**: Enable PDL in the DeepSeek fused QKV A Projection. - **TORCHINDUCTOR_ENABLE_PD...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ction. - **TORCHINDUCTOR_ENABLE_PDL**: Enable PDL in all torch.compile'd triton kernels. PDL is a valuable feature, but unfortunately adds some slight host overhead which can hurt in the prefill phase. We want to enable...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
