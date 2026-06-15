# vllm-project/vllm#40016: [Bug]:[SM90][FP8 blockwise] swap_ab path for small/non-multiple-of-4 M fails in can_implement() with kInvalid

| 字段 | 值 |
| --- | --- |
| Issue | [#40016](https://github.com/vllm-project/vllm/issues/40016) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;gemm_linear;hardware_porting;quantization |
| 子分类 |  |
| Operator 关键词 | cuda;fp8;kernel;operator;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:[SM90][FP8 blockwise] swap_ab path for small/non-multiple-of-4 M fails in can_implement() with kInvalid

### Issue 正文摘录

### Your current environment # Describe the Bug This appears to be a separate SM90 FP8 blockwise issue, independent from the decode-side performance investigation in `#38697`. On SM90, FP8 blockwise currently hard-fails for cases such as `m=1` or `m=33` with: ```text m must be divisible by 4 ``` I tried porting the SM100/SM120-style `swap_ab` graceful handling to SM90. That removes the original hard check, and the new path is definitely exercised, but all minimal repro cases now fail earlier in CUTLASS `can_implement()` with: ```text cutlass_gemm_caller can_implement failed with kInvalid (Invalid status, code=11) ``` So the issue is no longer the old explicit `m % 4 == 0` guard. The failure has moved into the SM90 CUTLASS blockwise implementation itself. ## Minimal Repro Cases All of the following fail consistently in the new SM90 `swap_ab` path: - `m=1, n=256, k=128` - `m=1, n=16384, k=1024` - `m=33, n=1024, k=1024` - `m=33, n=8192, k=128` Before the port, these were blocked by the explicit `m must be divisible by 4` check. After the port, they all reach `ops.cutlass_scaled_mm(...)`, but fail in `can_implement()` with `kInvalid`. ## Findings I compared the SM90 host-side `swap_ab...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: That removes the original hard check, and the new path is definitely exercised, but all minimal repro cases now fail earlier in CUTLASS `can_implement()` with: ```text cutlass_gemm_caller can_implement failed with kInva...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]:[SM90][FP8 blockwise] swap_ab path for small/non-multiple-of-4 M fails in can_implement() with kInvalid bug ### Your current environment # Describe the Bug This appears to be a separate SM90 FP8 blockwise issue, i...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [Bug]:[SM90][FP8 blockwise] swap_ab path for small/non-multiple-of-4 M fails in can_implement() with kInvalid bug ### Your current environment # Describe the Bug This appears to be a separate SM90 FP8 blockwise issue, i...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: is definitely exercised, but all minimal repro cases now fail earlier in CUTLASS `can_implement()` with: ```text cutlass_gemm_caller can_implement failed with kInvalid (Invalid status, code=11) ``` So the issue is no lo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]:[SM90][FP8 blockwise] swap_ab path for small/non-multiple-of-4 M fails in can_implement() with kInvalid bug ### Your current environment # Describe the Bug This appears to be a separate SM90 FP8 blockwise issue, i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
