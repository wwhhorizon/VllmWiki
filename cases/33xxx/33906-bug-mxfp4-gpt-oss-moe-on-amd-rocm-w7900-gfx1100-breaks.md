# vllm-project/vllm#33906: [Bug]: mxfp4 (gpt-oss moe) on AMD rocm (W7900/gfx1100) breaks

| 字段 | 值 |
| --- | --- |
| Issue | [#33906](https://github.com/vllm-project/vllm/issues/33906) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: mxfp4 (gpt-oss moe) on AMD rocm (W7900/gfx1100) breaks

### Issue 正文摘录

### Your current environment This is in the vllm/vllm-openai-rocm docker container from today (sha256:4c7fbd92fe07e4dab956d283b5d61b971f6242516647df6af06fdcbc34fddc2c). ### 🐛 Describe the bug Starting VLLM to serve openai/gpt-oss-120b (or variations provided by AMD) results in this error while handling the mxfp4 compilation: ```text [05.02.2026, 11:58:32] ker_TP1: /app/triton/third_party/amd/lib/TritonAMDGPUToLLVM/DotOpToLLVM/MFMA.cpp:869: llvm::LogicalResult mlir::triton::AMD::convertScaledMFMA(mlir::triton::DotScaledOp, mlir::triton::DotScaledOp::Adaptor, con[05.02.2026, 11:58:32] st mlir::LLVMTypeConverter*, mlir::ConversionPatternRewriter&): Assertion `isa (op.getA().getType().getEncoding()) && isa (op.getB().getType().getEncoding()) && "B[05.02.2026, 11:58:32] oth lhs and rhs should be in DotOperand layout."' failed. ``` This system contains 2 W7900 and we add `-tp 2` to use both of them. [log.txt](https://github.com/user-attachments/files/25094828/log.txt) I think this is related to the work that was planned in #26303 (but got auto-closed) and might also be related to #30828. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and a...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: cm ### Your current environment This is in the vllm/vllm-openai-rocm docker container from today (sha256:4c7fbd92fe07e4dab956d283b5d61b971f6242516647df6af06fdcbc34fddc2c). ### 🐛 Describe the bug Starting VLLM to serve o...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: mxfp4 (gpt-oss moe) on AMD rocm (W7900/gfx1100) breaks bug;rocm ### Your current environment This is in the vllm/vllm-openai-rocm docker container from today (sha256:4c7fbd92fe07e4dab956d283b5d61b971f6242516647df...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: mxfp4 (gpt-oss moe) on AMD rocm (W7900/gfx1100) breaks bug;rocm ### Your current environment This is in the vllm/vllm-openai-rocm docker container from today (sha256:4c7fbd92fe07e4dab956d283b5d61b971f6242516647df...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: mxfp4 (gpt-oss moe) on AMD rocm (W7900/gfx1100) breaks bug;rocm ### Your current environment This is in the vllm/vllm-openai-rocm docker container from today (sha256:4c7fbd92fe07e4dab956d283b5d61b971f6242516647df...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ing the mxfp4 compilation: ```text [05.02.2026, 11:58:32] ker_TP1: /app/triton/third_party/amd/lib/TritonAMDGPUToLLVM/DotOpToLLVM/MFMA.cpp:869: llvm::LogicalResult mlir::triton::AMD::convertScaledMFMA(mlir::triton::DotS...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
