# vllm-project/vllm#11471: [Usage]: About '--chat-template' parameters for model google/paligemma2-3b-ft-docci-448

| 字段 | 值 |
| --- | --- |
| Issue | [#11471](https://github.com/vllm-project/vllm/issues/11471) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: About '--chat-template' parameters for model google/paligemma2-3b-ft-docci-448

### Issue 正文摘录

### Your current environment I use [template_llava.jinja](https://github.com/vllm-project/vllm/blob/v0.6.5/examples/template_llava.jinja) to launch the model google/paligemma2-3b-ft-docci-448. Despite working, I wonder 1) how to decide on a template for a specific model and 2) whether my setting is correct for the model google/paligemma2-3b-ft-docci-448? ```text vllm serve google/paligemma2-3b-ft-docci-448 --chat-template template_llava.jinja --host 0.0.0.0 --port 8001 --enforce-eager --dtype auto ``` on a ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: About '--chat-template' parameters for model google/paligemma2-3b-ft-docci-448 usage ### Your current environment I use [template_llava.jinja](https://github.com/vllm-project/vllm/blob/v0.6.5/examples/template_llava.jin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: About '--chat-template' parameters for model google/paligemma2-3b-ft-docci-448 usage ### Your current environment I use [template_llava.jinja](https://github.com/vllm-project/vllm/blob/v0.6.5/examples/template_...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: late template_llava.jinja --host 0.0.0.0 --port 8001 --enforce-eager --dtype auto ``` on a ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Usage]: About '--chat-template' parameters for model google/paligemma2-3b-ft-docci-448 usage ### Your current environment I use [template_llava.jinja](https://github.com/vllm-project/vllm/blob/v0.6.5/examples/template_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
