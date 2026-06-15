# vllm-project/vllm#35300: [Feature]: Add ISA-level smoke tests using Intel SDE to catch instruction set mismatches

| 字段 | 值 |
| --- | --- |
| Issue | [#35300](https://github.com/vllm-project/vllm/issues/35300) |
| 状态 | closed |
| 标签 | cpu |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add ISA-level smoke tests using Intel SDE to catch instruction set mismatches

### Issue 正文摘录

### Motivation vLLM's CPU backend compiles ISA-specific C kernels (AVX2, AVX512, AVX512BF16, AMX, NEON, VSX) selected at build time via environment variables. The default CI image is built with `AVX512BF16 + AVX512VNNI + AMXBF16` enabled (see [`.buildkite/image_build/image_build_cpu.sh`](https://github.com/vllm-project/vllm/blob/main/.buildkite/image_build/image_build_cpu.sh#L28-L30)). **No test currently verifies the binary works on CPUs with different ISA levels.** Running the resulting binary on a CPU missing required instructions causes a `SIGILL` (illegal instruction) segfault -- not a clear error message. This is not hypothetical. Multiple existing issues document this exact failure mode: | Issue | Problem | |-------|---------| | [#18660](https://github.com/vllm-project/vllm/issues/18660) | Pre-built CPU Docker image crashes with SIGILL (`vinserti64x4`) on non-AVX512 CPUs | | [#33991](https://github.com/vllm-project/vllm/issues/33991), [#33784](https://github.com/vllm-project/vllm/issues/33784) | `mla_decode.cpp` BFloat16 has no AVX2 fallback -- compile fails on non-AVX512 x86_64 | | [#10478](https://github.com/vllm-project/vllm/issues/10478), [#19494](https://github.com/vll...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: catch instruction set mismatches cpu ### Motivation vLLM's CPU backend compiles ISA-specific C kernels (AVX2, AVX512, AVX512BF16, AMX, NEON, VSX) selected at build time via environment variables. The default CI image is...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: l SDE to catch instruction set mismatches cpu ### Motivation vLLM's CPU backend compiles ISA-specific C kernels (AVX2, AVX512, AVX512BF16, AMX, NEON, VSX) selected at build time via environment variables. The default CI...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: vLLM's CPU backend compiles ISA-specific C kernels (AVX2, AVX512, AVX512BF16, AMX, NEON, VSX) selected at build time via environment variables. The default CI image is built with `AVX512BF16 + AVX512VNNI + AMXBF16` enab...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Feature]: Add ISA-level smoke tests using Intel SDE to catch instruction set mismatches cpu ### Motivation vLLM's CPU backend compiles ISA-specific C kernels (AVX2, AVX512, AVX512BF16, AMX, NEON, VSX) selected at build...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: /19494), [#12778](https://github.com/vllm-project/vllm/issues/12778) | brgemm/oneDNN JIT kernels crash at runtime on AVX2-only CPUs | | [#32932](https://github.com/vllm-project/vllm/issues/32932) | ARM BF16 dispatch fai...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
