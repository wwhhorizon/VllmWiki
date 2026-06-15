# vllm-project/vllm#2725: [BUG] Compile source code error for ROCM platform when using #include <hip/hip_bf16.h>

| 字段 | 值 |
| --- | --- |
| Issue | [#2725](https://github.com/vllm-project/vllm/issues/2725) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [BUG] Compile source code error for ROCM platform when using #include <hip/hip_bf16.h>

### Issue 正文摘录

As mentioned in #https://github.com/vllm-project/vllm/issues/2646 Building for ROCM platform will cause multiple definition error, **This is caused by The function in being defined without _static inline_ , which will cause multi definition error when using this header file in multi .cu/.hip files.** #https://github.com/ROCm/HIP/issues/3403 The error will be fixed in future releases of ROCM, but till ROCM-6.0.2, this has not been fixed yet, maybe we need to find a way to bypass this. Maybe using hip_bfloat16 instead of __hip_bfloat16? #https://github.com/ROCm/ROCm/issues/2534, but needs some code modification.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: Compile source code error for ROCM platform when using #include <hip/hip_bf16.h> As mentioned in #https://github.com/vllm-project/vllm/issues/2646 Building for ROCM platform will cause multiple definition error, **This...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [BUG] Compile source code error for ROCM platform when using #include <hip/hip_bf16.h> As mentioned in #https://github.com/vllm-project/vllm/issues/2646 Building for ROCM platform will cause multiple definition error, *...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [BUG] Compile source code error for ROCM platform when using #include <hip/hip_bf16.h> As mentioned in #https://github.com/vllm-project/vllm/issues/2646 Building for ROCM platform will cause multiple definition error, *...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
