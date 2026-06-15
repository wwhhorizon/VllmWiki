# vllm-project/vllm#9183: [Bug]: Qwen2.5-Math-7B-Instruct vllm output garbled code, but the probability of huggingface outputing garbled code is lower.

| 字段 | 值 |
| --- | --- |
| Issue | [#9183](https://github.com/vllm-project/vllm/issues/9183) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen2.5-Math-7B-Instruct vllm output garbled code, but the probability of huggingface outputing garbled code is lower.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hi! I'm now using Qwen2.5-Math-7B-Instruct to solve problems in the MATH dataset. And I found that the vLLM engine sometimes has weird outputs(garbled code). Here is the code ```python from vllm import LLM, SamplingParams ## VLLM output model_name = "Qwen2.5-Math-7B-Instruct" llm = LLM(model_name) text=' system\nPlease reason step by step, and put your final answer within \\boxed{{}}. \n user\nSimplify $\\tan 100^\\circ + 4 \\sin 100^\\circ.$ \n assistant\nTo simplify the expression \\(\\tan 100^\\circ + 4 \\sin 100^\\circ\\), we start by using the identity \\(\\tan 100^\\circ = \\tan (180^\\circ - 80^\\circ) = -\\tan 80^\\circ\\). Therefore, the expression becomes:\n\n\\[\n\\tan 100^\\circ + 4 \\sin 100^\\circ = -\\tan 80^\\circ + 4 \\sin 100^\\circ\n\\]\n\nNext, we use the identity \\(\\sin 100^\\circ = \\sin (180^\\circ - 80^\\circ) = \\sin 80^\\circ\\). So the expression further simplifies to:\n\n\\[\n-\\tan 80^\\circ + 4 \\sin 80^\\circ\n\\]\n\nWe can express \\(\\tan 80^\\circ\\) as \\(\\frac{\\sin 80^\\circ}{\\cos 80^\\circ}\\). Substituting this into the expression, we get:\n\n\\[\n-\\f...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: has weird outputs(garbled code). Here is the code ```python from vllm import LLM, SamplingParams ## VLLM output model_name = "Qwen2.5-Math-7B-Instruct" llm = LLM(model_name) text=' system\nPlease reason step by step, an...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen2.5-Math-7B-Instruct vllm output garbled code, but the probability of huggingface outputing garbled code is lower. bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hi
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: *. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: zip(model_inputs.input_ids, generated_ids) ] response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0] print(response) ``` The output with `transformers` looks good. I know that `t > 0` may cause som...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
