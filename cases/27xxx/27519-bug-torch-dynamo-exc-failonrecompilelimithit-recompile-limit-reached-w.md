# vllm-project/vllm#27519: [Bug]: torch._dynamo.exc.FailOnRecompileLimitHit: recompile_limit reached with fullgraph=True on 2x RTX2080Ti

| 字段 | 值 |
| --- | --- |
| Issue | [#27519](https://github.com/vllm-project/vllm/issues/27519) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: torch._dynamo.exc.FailOnRecompileLimitHit: recompile_limit reached with fullgraph=True on 2x RTX2080Ti

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The inference speed is very slow, and after a while, the "recompile limit reached" message is reported, and then vllm exits. vLLM log from console with env TORCH_LOGS=recompiles: [recompile_limit_reached.txt](https://github.com/user-attachments/files/23146040/recompile_limit_reached.txt) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: torch._dynamo.exc.FailOnRecompileLimitHit: recompile_limit reached with fullgraph=True on 2x RTX2080Ti bug;stale ### Your current environment ### 🐛 Describe the bug The inference speed is very slow, and after a w...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ilOnRecompileLimitHit: recompile_limit reached with fullgraph=True on 2x RTX2080Ti bug;stale ### Your current environment ### 🐛 Describe the bug The inference speed is very slow, and after a while, the "recompile limit...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: imitHit: recompile_limit reached with fullgraph=True on 2x RTX2080Ti bug;stale ### Your current environment ### 🐛 Describe the bug The inference speed is very slow, and after a while, the "recompile limit reached" messa...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf;slowdown env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf;slowdown env_dependency Your curr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
