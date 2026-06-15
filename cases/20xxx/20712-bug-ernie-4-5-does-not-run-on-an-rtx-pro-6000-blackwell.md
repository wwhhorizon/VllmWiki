# vllm-project/vllm#20712: [Bug]: ERNIE-4.5 does not run on an RTX Pro 6000 Blackwell

| 字段 | 值 |
| --- | --- |
| Issue | [#20712](https://github.com/vllm-project/vllm/issues/20712) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;kernel;moe;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ERNIE-4.5 does not run on an RTX Pro 6000 Blackwell

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Serving ERNIE-4.5-21B-A3B does not work on an RTX Pro 6000 Blackwell card. This is using the pip install of vllm 0.9.2 in its own venv. ``` $ vllm serve ERNIE-4.5-21B-A3B-PT/ --trust-remote-code Loading safetensors checkpoint shards: 0% Completed | 0/11 [00:00 {tt.divisibility = 16 : i32}, %arg1: !tt.ptr {tt.divisibility = 16 : i32}, %arg2: !tt.ptr {tt.divisibility = 16 : i32}, %arg3: !tt.ptr {tt.divisibility = 16 : i32}, %arg4: !tt.ptr {tt.divisibility = 16 : i32}, %arg5: !tt.ptr {tt.divisibility = 16 : i32}, %arg6: !tt.ptr {tt.divisibility = 16 : i32}, %arg7: i32 {tt.divisibility = 16 : i32}, %arg8: i32 {tt.divisibility = 16 : i32}, %arg9: i32 {tt.divisibility = 16 : i32}, %arg10: i32 {tt.divisibility = 16 : i32}, %arg11: i32 {tt.divisibility = 16 : i32}, %arg12: i32 {tt.divisibility = 16 : i32}, %arg13: i32 {tt.divisibility = 16 : i32}, %arg14: i32 {tt.divisibility = 16 : i32}, %arg15: i32 {tt.divisibility = 16 : i32}, %arg16: i32 {tt.divisibility = 16 : i32}, %arg17: i32 {tt.divisibility = 16 : i32}, %arg18: i32 {tt.divisibility = 16 : i32}, %arg19: i32 {tt.divisibility = 16 : i32}) attributes {noinline = false} { %c31_i32 =...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: B does not work on an RTX Pro 6000 Blackwell card. This is using the pip install of vllm 0.9.2 in its own venv. ``` $ vllm serve ERNIE-4.5-21B-A3B-PT/ --trust-remote-code Loading safetensors checkpoint shards: 0% Comple...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: ERNIE-4.5 does not run on an RTX Pro 6000 Blackwell bug;stale ### Your current environment ### 🐛 Describe the bug Serving ERNIE-4.5-21B-A3B does not work on an RTX Pro 6000 Blackwell card. This is using the pip i...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 5: /venv/vllm/lib/python3.12/site-packages/vllm/model_executor/layers/fused_moe/fused_moe.py:262:0: error: Failures have been detected while processing an MLIR pass pipeline /home/llm/venv/vllm/lib/python3.12/site-packages...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ources: { mlir_reproducer: { pipeline: "builtin.module(convert-triton-to-tritongpu{num-ctas=1 num-warps=4 target=cuda:120 threads-per-warp=32}, tritongpu-coalesce, tritongpu-F32DotTC, triton-nvidia-gpu-plan-cta, tritong...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: i32}, %arg19: i32 {tt.divisibility = 16 : i32}) attributes {noinline = false} { %c31_i32 = arith.constant 31 : i32 %cst = arith.constant dense : tensor %c63_i32 = arith.constant 63 : i32 %cst_0 = arith.constant dense :...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
