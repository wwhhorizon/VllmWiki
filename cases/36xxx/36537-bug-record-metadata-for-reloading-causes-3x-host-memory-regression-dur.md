# vllm-project/vllm#36537: [Bug]: record_metadata_for_reloading causes ~3x host memory regression during torch.compile on XLA backends

| 字段 | 值 |
| --- | --- |
| Issue | [#36537](https://github.com/vllm-project/vllm/issues/36537) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;hardware_porting;model_support |
| 子分类 | cold_start |
| Operator 关键词 | cuda;triton |
| 症状 | build_error;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: record_metadata_for_reloading causes ~3x host memory regression during torch.compile on XLA backends

### Issue 正文摘录

### Your current environment - vLLM Version: 0.16.0 (also present in 0.17.0) - PyTorch version: 2.9.1 - torch-xla: 2.9.0+git8ee513e - Python version: 3.12.12 - OS: Ubuntu 22.04.5 LTS (x86_64) - Hardware: Tenstorrent Wormhole (n300) via torch_xla PJRT backend ### 🐛 Describe the bug `record_metadata_for_reloading()` (introduced in PR #32133 FYI @kylesayrs ) runs unconditionally during `initialize_model()` for all users, even though it only benefits the QeRL layerwise weight reloading use case. On `torch_xla` backends, this causes a 2-3x host memory regression during `torch.compile` tracing. The regression scales with model size, causing OOM in some cases on machines that do not have 500+ GB of ram. Even outside of the XLA-specific memory impact, `record_metadata_for_reloading` does unnecessary work at model initialization for the vast majority of users who never call `reload_weights()`. It iterates every module, creates meta tensor copies via `tensor.data.to("meta")`, and copies `__dict__` on every parameter — all eagerly, with no way to opt out. ### Impact Measured with Qwen3 models via `torch_xla` + PJRT backend (peak host RSS): | Model | v0.15.1 (before PR #32133) | v0.16.0 (afte...

## 现有链接修复摘要

#32133 [QeRL] Layerwise Reloading

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: rd_metadata_for_reloading causes ~3x host memory regression during torch.compile on XLA backends bug ### Your current environment - vLLM Version: 0.16.0 (also present in 0.17.0) - PyTorch version: 2.9.1 - torch-xla: 2.9...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ere memory impact appears specific to `torch_xla`'s graph capture mechanism. However, the unconditional metadata capture is still unnecessary overhead for all non-QeRL users. ### Reproduction The regression requires vLL...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: _reloading causes ~3x host memory regression during torch.compile on XLA backends bug ### Your current environment - vLLM Version: 0.16.0 (also present in 0.17.0) - PyTorch version: 2.9.1 - torch-xla: 2.9.0+git8ee513e -...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ed in PR #32133 FYI @kylesayrs ) runs unconditionally during `initialize_model()` for all users, even though it only benefits the QeRL layerwise weight reloading use case. On `torch_xla` backends, this causes a 2-3x hos...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: record_metadata_for_reloading causes ~3x host memory regression during torch.compile on XLA backends bug ### Your current environment - vLLM Version: 0.16.0 (also present in 0.17.0) - PyTorch version: 2.9.1 - tor...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#32133](https://github.com/vllm-project/vllm/pull/32133) | mentioned | 0.45 | [QeRL] Layerwise Reloading | peak rss) - **first bad**: `f857a03f6` — `[qerl] layerwise reloading (#32133)` (8.5 gb peak rss) `record_metadata_for_reloading()` is called from `initialize_model()` in `model_ex… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
