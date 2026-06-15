# vllm-project/vllm#28041: [Bug]: online serving GPT-OSS does not stop at <|call|> token during reasoning (v0.11.0)

| 字段 | 值 |
| --- | --- |
| Issue | [#28041](https://github.com/vllm-project/vllm/issues/28041) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: online serving GPT-OSS does not stop at <\|call\|> token during reasoning (v0.11.0)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I start the GPT-OSS online serving with the following command: ``` vllm serve openai/gpt-oss-120b --enforce-eager --tensor-parallel-size=8 \ --pipeline-parallel-size=1 --max-model-len=65536 \ --gpu-memory-utilization=0.9 --trust-remote-code \ --tool-call-parser=openai --enable-auto-tool-choice --reasoning-parser=openai_gptoss ``` The client side queries with the chat completion end point: ``` completion = client.chat.completions.create( model=model, messages=messages, max_tokens=32768, temperature=1.0, tools=tools, tool_choice="auto", ) ``` After inserting some prints to the vllm code, I found that the model does not stop at the ` ` token, which should be the case for harmony according to https://cookbook.openai.com/articles/openai-harmony#special-tokens The output tokens from vllm is in the following structure: ``` analysis ... assistant commentary to=functions.my_function json ... _output ... _output ... ``` The model starts to hallucinate after the , while according to the https://cookbook.openai.com/articles/openai-harmony it should start with a new message with tool. The reason is that the stop_tokens_id is not properly pass...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: mony according to https://cookbook.openai.com/articles/openai-harmony#special-tokens The output tokens from vllm is in the following structure: ``` analysis ... assistant commentary to=functions.my_function json ... _ou...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ix. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: online serving GPT-OSS does not stop at <|call|> token during reasoning (v0.11.0) bug ### Your current environment ### 🐛 Describe the bug I start the GPT-OSS online serving with the following command: ``` vllm se...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: which doesn't, during the `to_sampling_params` methods in `ChatCompletionRequest`. It's still here in the current main branch https://github.com/vllm-project/vllm/blob/03c4c4aa9deb2ad09a95c7997d2e5578c8db68d6/vllm/entry...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: pport;sampling_logits;speculative_decoding cuda;kernel;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
