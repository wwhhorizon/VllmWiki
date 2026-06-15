# vllm-project/vllm#39697: [Bug]: Qwen3.5 `thinking_token_budget` causes `reasoning_end_str` to leak into `content` field

| 字段 | 值 |
| --- | --- |
| Issue | [#39697](https://github.com/vllm-project/vllm/issues/39697) |
| 状态 | open |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5 `thinking_token_budget` causes `reasoning_end_str` to leak into `content` field

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using `thinking_token_budget` with a custom `reasoning_end_str` (`"I have to give the solution based on the reasoning directly now. "`), if the model has already begun generating its response at the moment the budget is exhausted, vLLM injects the `reasoning_end_str` mid-sentence in the content. Serving: ```python vllm serve Qwen/Qwen3.5-27B-GPTQ-Int4 --gpu-memory-utilization 0.4 --max-model-len 32768 --kv-cache-dtype fp8 --reasoning-parser qwen3 --reasoning-config '{"reasoning_start_str": " ", "reasoning_end_str": "I have to give the solution based on the reasoning directly now. "}' --language-model-only ``` Python script: ```python import httpx from openai import OpenAI httpx_client = httpx.Client(verify=False, timeout=None) client = OpenAI( base_url="my-endpoint", api_key="api_key", http_client=httpx_client, ) completion = client.chat.completions.create( model="Qwen/Qwen3.5-27B-GPTQ-Int4", messages=[ {"role": "system", "content": "Answer the user query"}, {"role": "user", "content": "What is 10*5-15?"}, ], extra_body={"thinking_token_budget": 280}, temperature=0, ) print("Reasoning:") print(completion.choices[0].message.r...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ng directly now. "}' --language-model-only ``` Python script: ```python import httpx from openai import OpenAI httpx_client = httpx.Client(verify=False, timeout=None) client = OpenAI( base_url="my-endpoint", api_key="ap...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: nce in the content. Serving: ```python vllm serve Qwen/Qwen3.5-27B-GPTQ-Int4 --gpu-memory-utilization 0.4 --max-model-len 32768 --kv-cache-dtype fp8 --reasoning-parser qwen3 --reasoning-config '{"reasoning_start_str": "...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3.5 `thinking_token_budget` causes `reasoning_end_str` to leak into `content` field bug ### Your current environment ### 🐛 Describe the bug When using `thinking_token_budget` with a custom `reasoning_end_str`...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ld. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: onse `content` field ``` Reasoning: Thinking Process: 1. **Analyze the Request:** The user is asking for the result of a simple arithmetic expression: $10 \times 5 - 15$. 2. **Identify the Operations:** The expression i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
