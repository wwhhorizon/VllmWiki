# vllm-project/vllm#29056: [Bug]: Cannot use Qwen3 Next autoround quant model with 0.11.1

| 字段 | 值 |
| --- | --- |
| Issue | [#29056](https://github.com/vllm-project/vllm/issues/29056) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support;moe;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | moe;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Cannot use Qwen3 Next autoround quant model with 0.11.1

### Issue 正文摘录

### Your current environment VLLM 0.11.1 Ubuntu 24.04 RTX 3090 24G ### 🐛 Describe the bug ``` vllm serve /mnt/models/Qwen3-Next-80B-A3B-Instruct-int4-mixed-AutoRound/ --served-model-name Qwen3-Next --tensor-parallel-size 4 --max-num-seqs 8 --gpu-memory-utilization 0.9 --dtype float16 --enable-expert-parallel ``` It works well with versions 0.11.0 and 0.11.1rc6. However, in 0.11.1, the following error occurs (it's too long to include here, so please see the linked details). [Gist](https://gist.github.com/ariable/78052a662012a58a51e4bc9cba0e106c) Thank you very much. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: Cannot use Qwen3 Next autoround quant model with 0.11.1 bug;stale ### Your current environment VLLM 0.11.1 Ubuntu 24.04 RTX 3090 24G ### 🐛 Describe the bug ``` vllm serve /mnt/models/Qwen3-Next-80B-A3B-Instruct-i...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: tion 0.9 --dtype float16 --enable-expert-parallel ``` It works well with versions 0.11.0 and 0.11.1rc6. However, in 0.11.1, the following error occurs (it's too long to include here, so please see the linked details). [...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: .11.1 bug;stale ### Your current environment VLLM 0.11.1 Ubuntu 24.04 RTX 3090 24G ### 🐛 Describe the bug ``` vllm serve /mnt/models/Qwen3-Next-80B-A3B-Instruct-int4-mixed-AutoRound/ --served-model-name Qwen3-Next --ten...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Cannot use Qwen3 Next autoround quant model with 0.11.1 bug;stale ### Your current environment VLLM 0.11.1 Ubuntu 24.04 RTX 3090 24G ### 🐛 Describe the bug ``` vllm serve /mnt/models/Qwen3-Next-80B-A3B-Instruct-i...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: 4 --max-num-seqs 8 --gpu-memory-utilization 0.9 --dtype float16 --enable-expert-parallel ``` It works well with versions 0.11.0 and 0.11.1rc6. However, in 0.11.1, the following error occurs (it's too long to include her...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
