# vllm-project/vllm#22126: [Feature]: Tensor parallelism for GLM-4.5

| 字段 | 值 |
| --- | --- |
| Issue | [#22126](https://github.com/vllm-project/vllm/issues/22126) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Tensor parallelism for GLM-4.5

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Not sure if its a vLLM or Tranformers thing that we need to update but I get this error when trying to load GLM-4.5-Air-FP8 with vLLM on two 6000 blackwell gpus: "transformers.models.glm4_moe.modeling_glm4_moe.Glm4MoeModel'> does not support tensor parallel yet!" ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Feature]: Tensor parallelism for GLM-4.5 feature request;stale ### 🚀 The feature, motivation and pitch Not sure if its a vLLM or Tranformers thing that we need to update but I get this error when trying to load GLM-4.5...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Tensor parallelism for GLM-4.5 feature request;stale ### 🚀 The feature, motivation and pitch Not sure if its a vLLM or Tranformers thing that we need to update but I get this error when trying to load GLM-4.5...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: t we need to update but I get this error when trying to load GLM-4.5-Air-FP8 with vLLM on two 6000 blackwell gpus: "transformers.models.glm4_moe.modeling_glm4_moe.Glm4MoeModel'> does not support tensor parallel yet!" ##...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: load GLM-4.5-Air-FP8 with vLLM on two 6000 blackwell gpus: "transformers.models.glm4_moe.modeling_glm4_moe.Glm4MoeModel'> does not support tensor parallel yet!" ### Alternatives _No response_ ### Additional context _No...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: -Air-FP8 with vLLM on two 6000 blackwell gpus: "transformers.models.glm4_moe.modeling_glm4_moe.Glm4MoeModel'> does not support tensor parallel yet!" ### Alternatives _No response_ ### Additional context _No response_ ##...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
