# vllm-project/vllm#33297: [CI Failure]: Entrypoints Integration Test (Responses API) for GPU utilization ValueError

| 字段 | 值 |
| --- | --- |
| Issue | [#33297](https://github.com/vllm-project/vllm/issues/33297) |
| 状态 | closed |
| 标签 | stale;ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: Entrypoints Integration Test (Responses API) for GPU utilization ValueError

### Issue 正文摘录

### Name of failing test `entrypoints/openai/responses/test_mcp_tools.py:287` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test > [2026-01-28T23:59:42Z] (EngineCore_DP0 pid=972) ERROR 01-28 15:59:42 [core.py:935] ValueError: Free memory on device cuda:0 (1.53/22.05 GiB) on startup is less than desired GPU memory utilization (0.9, 19.84 GiB). Decrease GPU memory utilization or reduce GPU memory used by other processes. https://buildkite.com/vllm/ci/builds/48519/steps/canvas?sid=019bfb44-bd6b-46a6-bca8-8e75e43994f9 > [2026-01-26T17:25:37Z] ^[[0;36m(EngineCore_DP0 pid=738)^[[0;0m ^[[31mERROR^[[0m ^[[90m01-26 09:25:37^[[0m ^[[90m[core.py:935]^[[0m ValueError: Free memory on device cuda:0 (1.54/22.05 GiB) on startup is less than desired GPU memory utilization (0.9, 19.84 GiB). Decrease GPU memory utilization or reduce GPU memory used by other processes. > ValueError: Free memory on device cuda:0 (1.54/22.05 GiB) on startup is less than desired GPU memory utilization (0.9, 19.84 GiB). Decrease GPU memory utilization or reduce GPU memory used by other processes. ### 📝 History...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Entrypoints Integration Test (Responses API) for GPU utilization ValueError stale;ci-failure ### Name of failing test `entrypoints/openai/responses/test_mcp_tools.py:287` ### Basic information - [x] Flaky
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: est_mcp_tools.py:287` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test > [2026-01-28T23:59:42Z] (EngineCo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 72) ERROR 01-28 15:59:42 [core.py:935] ValueError: Free memory on device cuda:0 (1.53/22.05 GiB) on startup is less than desired GPU memory utilization (0.9, 19.84 GiB). Decrease GPU memory utilization or reduce GPU mem...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: memory on device cuda:0 (1.53/22.05 GiB) on startup is less than desired GPU memory utilization (0.9, 19.84 GiB). Decrease GPU memory utilization or reduce GPU memory used by other processes. https://buildkite.com/vllm/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: test `entrypoints/openai/responses/test_mcp_tools.py:287` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing tes...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
