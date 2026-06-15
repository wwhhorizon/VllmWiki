# vllm-project/vllm#33014: [Bug]: LoRA loading fails with Fused MoE when data parallelism (DP > 1) is enabled

| 字段 | 值 |
| --- | --- |
| Issue | [#33014](https://github.com/vllm-project/vllm/issues/33014) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: LoRA loading fails with Fused MoE when data parallelism (DP > 1) is enabled

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Fused MoE lora doesnt load the lora weights correctly when dp is enabled. In particular, it seems to try and load into a sharded tensor. Working ```bash uv run vllm serve --model Qwen/Qwen3-30B-A3B-Instruct-2507 --max-model-len 2048 -dp 1 --api-server-count 1 --enforce-eager --lora-modules my-lora=Jackmin108/Qwen3-30B-A3B-LoRA --enable-lora ``` Error ``` uv run vllm serve --model Qwen/Qwen3-30B-A3B-Instruct-2507 --max-model-len 2048 -dp 2 --api-server-count 1 --enforce-eager --lora-modules my-lora=Jackmin108/Qwen3-30B-A3B-LoRA --enable-lora ``` ``` (EngineCore_DP0 pid=1655130) ERROR 01-24 23:36:52 [core.py:1022] Invocation of add_lora method failed (EngineCore_DP0 pid=1655130) ERROR 01-24 23:36:52 [core.py:1022] Traceback (most recent call last): (EngineCore_DP0 pid=1655130) ERROR 01-24 23:36:52 [core.py:1022] File "/real_nvme_home/jackmin_home/vllm/vllm/v1/engine/core.py", line 1019, in _handle_client_request (EngineCore_DP0 pid=1655130) ERROR 01-24 23:36:52 [core.py:1022] result = method(*self._convert_msgspec_args(method, args)) (EngineCore_DP0 pid=1655130) ERROR 01-24 23:36:52 [core.py:1022] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding cuda;moe;operator;s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: LoRA loading fails with Fused MoE when data parallelism (DP > 1) is enabled bug;stale ### Your current environment ### 🐛 Describe the bug Fused MoE lora doesnt load the lora weights correctly when dp is enabled....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ading fails with Fused MoE when data parallelism (DP > 1) is enabled bug;stale ### Your current environment ### 🐛 Describe the bug Fused MoE lora doesnt load the lora weights correctly when dp is enabled. In particular,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: try and load into a sharded tensor. Working ```bash uv run vllm serve --model Qwen/Qwen3-30B-A3B-Instruct-2507 --max-model-len 2048 -dp 1 --api-server-count 1 --enforce-eager --lora-modules my-lora=Jackmin108/Qwen3-30B-...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: LoRA loading fails with Fused MoE when data parallelism (DP > 1) is enabled bug;stale ### Your current environment ### 🐛 Describe the bug Fused MoE lora doesnt load the lora weights correctly when dp is enabled....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
