# vllm-project/vllm#15381: [Bug]: Different logprobs output behaviour under vllm 0.8.0 and 0.8.1

| 字段 | 值 |
| --- | --- |
| Issue | [#15381](https://github.com/vllm-project/vllm/issues/15381) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Different logprobs output behaviour under vllm 0.8.0 and 0.8.1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I use VLLM by starting it as an OpenAI-compatible server. When requesting logprobs from it, vllm in version 0.8.0 and 0.8.1 shows a different behaviour than before. It can be reproduced with the following function: ``` from openai import OpenAI def openAI_test(url,model): client = OpenAI( base_url=url,api_key="dummy") openai_response = client.chat.completions.create( model=model, messages=[{"role": "user", "content": "What is the capital of Germany! "}], temperature=0.0, logprobs=True, #top_logprobs=1 ) print(openai_response.choices[0].logprobs) ``` I started a vllm server with the model `Qwen2.5-VL-7B-Instruct` and send with the above function a request to it. Print output with vllm 0.8.0 or 0.8.1: `ChoiceLogprobs(content=[ChatCompletionTokenLogprob(token='The', bytes=[84, 104, 101], logprob=-0.0005716835148632526, top_logprobs=[]), ChatCompletionTokenLogprob(token='Ġcapital', bytes=[196, 160, 99, 97, 112, 105, 116, 97, 108], logprob=-8.630380034446716e-05, top_logprobs=[]), ChatCompletionTokenLogprob(token='Ġof', bytes=[196, 160, 111, 102], logprob=-0.10054320842027664, top_logprobs=[]), ChatCompletionTokenLogprob(token='ĠGerma...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: s an OpenAI-compatible server. When requesting logprobs from it, vllm in version 0.8.0 and 0.8.1 shows a different behaviour than before. It can be reproduced with the following function: ``` from openai import OpenAI d...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: e following function: ``` from openai import OpenAI def openAI_test(url,model): client = OpenAI( base_url=url,api_key="dummy") openai_response = client.chat.completions.create( model=model, messages=[{"role": "user", "c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Bug]: Different logprobs output behaviour under vllm 0.8.0 and 0.8.1 bug;stale ### Your current environment ### 🐛 Describe the bug I use VLLM by starting it as an OpenAI-compatible server. When requesting logprobs from...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: at? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
