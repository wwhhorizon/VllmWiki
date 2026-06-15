# vllm-project/vllm#27893: [Bug]: AsyncTP pass has poor perf on B200

| 字段 | 值 |
| --- | --- |
| Issue | [#27893](https://github.com/vllm-project/vllm/issues/27893) |
| 状态 | open |
| 标签 | bug;help wanted;torch.compile;keep-open |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: AsyncTP pass has poor perf on B200

### Issue 正文摘录

### Your current environment main ### 🐛 Describe the bug When running a model with quant_fp8 + flashinfer on B200s, the matmul kernel that gets used is `flashinfer_scaled_fp8_mm` which turns into a `vllm.bmm_fp8` op in the graph. This doesn't work with the AsyncTP pass in the torch.compile compilation as there doesn't exist a pattern/replacement for this. Following the other patterns, I wrote one for `bmm_fp8`: https://github.com/vllm-project/vllm/pull/26933/commits/b0ab87b121acd1d4c52f3fbee12c3a447ea8f6b4 However, perf is a lot worse: This might be because we're replacing the bmm_fp8 + reduce_scatter with `torch.ops.symm_mem.patched_fused_scaled_matmul_reduce_scatter`, but this op does not have a B200 specific implementation (it just calls into [`aten._scaled_mm`](https://github.com/pytorch/pytorch/blob/main/torch/distributed/_symmetric_memory/__init__.py#L1324)) cc @ProExpertProg @cascade812 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ent environment main ### 🐛 Describe the bug When running a model with quant_fp8 + flashinfer on B200s, the matmul kernel that gets used is `flashinfer_scaled_fp8_mm` which turns into a `vllm.bmm_fp8` op in the graph. Th...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: AsyncTP pass has poor perf on B200 bug;help wanted;torch.compile;keep-open ### Your current environment main ### 🐛 Describe the bug When running a model with quant_fp8 + flashinfer on B200s, the matmul kernel tha...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: AsyncTP pass has poor perf on B200 bug;help wanted;torch.compile;keep-open ### Your current environment main ### 🐛 Describe the bug When running a model with quant_fp8 + flashinfer on B200s, the matmul kernel tha...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ent main ### 🐛 Describe the bug When running a model with quant_fp8 + flashinfer on B200s, the matmul kernel that gets used is `flashinfer_scaled_fp8_mm` which turns into a `vllm.bmm_fp8` op in the graph. This doesn't w...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: # Your current environment main ### 🐛 Describe the bug When running a model with quant_fp8 + flashinfer on B200s, the matmul kernel that gets used is `flashinfer_scaled_fp8_mm` which turns into a `vllm.bmm_fp8` op in th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
