# vllm-project/vllm#21542: [Bug]: Failing to initialize engine on qwen3 on B200 with VLLM_USE_DEEP_GEMM=1

| 字段 | 值 |
| --- | --- |
| Issue | [#21542](https://github.com/vllm-project/vllm/issues/21542) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Failing to initialize engine on qwen3 on B200 with VLLM_USE_DEEP_GEMM=1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Attempting to start the server (v0.10.0+#21472) on a GCP A4 B200 node, I get an engine assertion `RuntimeError: Failed: Assertion error csrc/jit_kernels/impls/smxx_layout.hpp:136 'mn % 4 == 0 and num_groups == 1'` Command line (also occurs on DeepSeek R1): ``` vllm serve Qwen/Qwen3-30B-A3B-FP8 --port 8000 --enforce-eager --disable-log-requests --enable-expert-parallel --tensor-parallel-size 1 --data-parallel-size 2 --trust-remote-code ``` ``` (EngineCore_0 pid=36448) ERROR 07-24 12:28:24 [core.py:632] EngineCore failed to start. (EngineCore_0 pid=36448) ERROR 07-24 12:28:24 [core.py:632] Traceback (most recent call last): (EngineCore_0 pid=36448) ERROR 07-24 12:28:24 [core.py:632] File "/app/vllm/vllm/v1/engine/core.py", line 621, in run_engine_core (EngineCore_0 pid=36448) ERROR 07-24 12:28:24 [core.py:632] engine_core = DPEngineCoreProc(*args, **kwargs) (EngineCore_0 pid=36448) ERROR 07-24 12:28:24 [core.py:632] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_0 pid=36448) ERROR 07-24 12:28:24 [core.py:632] File "/app/vllm/vllm/v1/engine/core.py", line 881, in __init__ (EngineCore_0 pid=36448) ERROR 07-24 12:28:24 [core.py:632] su...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 5: [Bug]: Failing to initialize engine on qwen3 on B200 with VLLM_USE_DEEP_GEMM=1 bug ### Your current environment ### 🐛 Describe the bug Attempting to start the server (v0.10.0+#21472) on a GCP A4 B200 node, I get an engi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: nd line (also occurs on DeepSeek R1): ``` vllm serve Qwen/Qwen3-30B-A3B-FP8 --port 8000 --enforce-eager --disable-log-requests --enable-expert-parallel --tensor-parallel-size 1 --data-parallel-size 2 --trust-remote-code...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Failing to initialize engine on qwen3 on B200 with VLLM_USE_DEEP_GEMM=1 bug ### Your current environment ### 🐛 Describe the bug Attempting to start the server (v0.10.0+#21472) on a GCP A4 B200 node, I get an engi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding cuda;fp8;moe;opera...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Failing to initialize engine on qwen3 on B200 with VLLM_USE_DEEP_GEMM=1 bug ### Your current environment ### 🐛 Describe the bug Attempting to start the server (v0.10.0+#21472) on a GCP A4 B200 node, I get an engi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
