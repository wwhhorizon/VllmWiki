# vllm-project/vllm#30039: [Bug] [ROCm]: Fusion pass failure `torch.ops.vllm.flashinfer_trtllm_fused_allreduce_norm.default`

| 字段 | 值 |
| --- | --- |
| Issue | [#30039](https://github.com/vllm-project/vllm/issues/30039) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | hardware_porting |
| 子分类 |  |
| Operator 关键词 | operator |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] [ROCm]: Fusion pass failure `torch.ops.vllm.flashinfer_trtllm_fused_allreduce_norm.default`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug https://github.com/vllm-project/vllm/pull/29631 PR broke the fusion pass as in the `if-else` condition it is trying to access It is causing the following error ``` (Worker_TP1 pid=517) ERROR 12-03 18:02:48 [multiproc_executor.py:822] File "/usr/local/lib/python3.12/dist-packages/vllm/compilation/fix_functionalization.py", line 108, in __call__ -- (Worker_TP1 pid=517) ERROR 12-03 18:02:48 [multiproc_executor.py:822] == torch.ops.vllm.flashinfer_trtllm_fused_allreduce_norm.default (Worker_TP1 pid=517) ERROR 12-03 18:02:48 [multiproc_executor.py:822] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker_TP1 pid=517) ERROR 12-03 18:02:48 [multiproc_executor.py:822] File "/usr/local/lib/python3.12/dist-packages/torch/_ops.py", line 1364, in __getattr__ (Worker_TP1 pid=517) ERROR 12-03 18:02:48 [multiproc_executor.py:822] raise AttributeError( (Worker_TP1 pid=517) ERROR 12-03 18:02:48 [multiproc_executor.py:822] torch._inductor.exc.InductorError: AttributeError: '_OpNamespace' 'vllm' object has no attribute ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot l...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ots of frequently asked questions. development hardware_porting operator build_error env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug] [ROCm]: Fusion pass failure `torch.ops.vllm.flashinfer_trtllm_fused_allreduce_norm.default` bug;rocm ### Your current environment ### 🐛 Describe the bug https://github.com/vllm-project/vllm/pull/29631 PR broke the...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug] [ROCm]: Fusion pass failure `torch.ops.vllm.flashinfer_trtllm_fused_allreduce_norm.default` bug;rocm ### Your current environment ### 🐛 Describe the bug https://github.com/vllm-project/vllm/pull/29631 PR broke the...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: om/vllm-project/vllm/pull/29631 PR broke the fusion pass as in the `if-else` condition it is trying to access It is causing the following error ``` (Worker_TP1 pid=517) ERROR 12-03 18:02:48 [multiproc_executor.py:822] F...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development hardware_porting operator build_error env_dependency Your current environ...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
