# vllm-project/vllm#39525: [CI Failure]: Kernels FusedMoE Layer Test (2 B200s) has been broken since it was added on 04/06/25

| 字段 | 值 |
| --- | --- |
| Issue | [#39525](https://github.com/vllm-project/vllm/issues/39525) |
| 状态 | open |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Kernels FusedMoE Layer Test (2 B200s) has been broken since it was added on 04/06/25

### Issue 正文摘录

### Name of failing test kernels/moe/test_moe_layer.py ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [x] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Looking at https://vllm-ci-dashboard.vercel.app/jobs, the `Kernels FusedMoE Layer Test (2 B200s)` seems to have been red since it was added on 04/06/25. The failure appears to be caused by an FI import. ``` 1775802312805 /usr/local/lib/python3.12/dist-packages/flashinfer/data/include/flashinfer/trtllm/common/cudaUtils.h:25:10: fatal error: cublasLt.h: No such file or directory 1775802312805 25 | #include 1775802312805 | ^~~~~~~~~~~~ ``` ### 📝 History of failing test AFAICT, this group has never passed. ### CC List. _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Kernels FusedMoE Layer Test (2 B200s) has been broken since it was added on 04/06/25 ci-failure ### Name of failing test kernels/moe/test_moe_layer.py ### Basic information - [ ] Flaky test - [ ] Can repr
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [CI Failure]: Kernels FusedMoE Layer Test (2 B200s) has been broken since it was added on 04/06/25 ci-failure ### Name of failing test kernels/moe/test_moe_layer.py ### Basic information - [ ] Flaky test - [ ] Can repro...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: an FI import. ``` 1775802312805 /usr/local/lib/python3.12/dist-packages/flashinfer/data/include/flashinfer/trtllm/common/cudaUtils.h:25:10: fatal error: cublasLt.h: No such file or directory 1775802312805 25 | #include...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: moe/test_moe_layer.py ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [x] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Looking at https://vllm-ci-dashboa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ure ### Name of failing test kernels/moe/test_moe_layer.py ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [x] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
