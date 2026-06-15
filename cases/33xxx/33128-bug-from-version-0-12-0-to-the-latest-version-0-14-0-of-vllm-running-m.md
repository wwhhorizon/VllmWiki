# vllm-project/vllm#33128: [Bug]: From version 0.12.0 to the latest version 0.14.0 of vllm, running moe model of fp8 with deepgemm will be slower than 0.11.0.

| 字段 | 值 |
| --- | --- |
| Issue | [#33128](https://github.com/vllm-project/vllm/issues/33128) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;model_support;moe;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;fp8;moe |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: From version 0.12.0 to the latest version 0.14.0 of vllm, running moe model of fp8 with deepgemm will be slower than 0.11.0.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I use the H800 GPU and the official docker image. driver： 535.104.05 cuda：12.9 A single gpu running qwen3-30ba3b-fp8 model, or two gpus running qwen3-next-80ba3b model will be much slower. The performance has dropped by about a quarter. In the new version, the concurrency speed of 80ba3b is about 50tokens/s, while in the old version, it is about 90Tokens/s.. 30ba3b will be much slower, only 80 tokens/s. However, after 30ba3b closes deepgemm, the speed can be restored to 150 tokens/s. And 80ba3b,the speed can be restored to 130 tokens/s. The following is my startup command: vllm serve /data/models/Qwen3-Next-80B-A3B-Instruct-FP8 \ --host 0.0.0.0 \ --port 8080 \ --tensor-parallel-size 2 \ --max-model-len 60000 \ --enable-log-requests vllm serve /data/sft/Qwen3-30B-A3B-FP8 \ --host 0.0.0.0 \ --port 8080 \ --served-model-name default ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: From version 0.12.0 to the latest version 0.14.0 of vllm, running moe model of fp8 with deepgemm will be slower than 0.11.0. bug;stale ### Your current environment ### 🐛 Describe the bug I use the H800 GPU and th...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ersion 0.12.0 to the latest version 0.14.0 of vllm, running moe model of fp8 with deepgemm will be slower than 0.11.0. bug;stale ### Your current environment ### 🐛 Describe the bug I use the H800 GPU and the official do...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ug I use the H800 GPU and the official docker image. driver： 535.104.05 cuda：12.9 A single gpu running qwen3-30ba3b-fp8 model, or two gpus running qwen3-next-80ba3b model will be much slower. The performance has dropped...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ]: From version 0.12.0 to the latest version 0.14.0 of vllm, running moe model of fp8 with deepgemm will be slower than 0.11.0. bug;stale ### Your current environment ### 🐛 Describe the bug I use the H800 GPU and the of...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: From version 0.12.0 to the latest version 0.14.0 of vllm, running moe model of fp8 with deepgemm will be slower than 0.11.0. bug;stale ### Your current environment ### 🐛 Describe the bug I use the H800 GPU and th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
