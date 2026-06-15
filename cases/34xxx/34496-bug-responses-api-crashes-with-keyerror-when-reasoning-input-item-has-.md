# vllm-project/vllm#34496: [Bug]: Responses API crashes with KeyError when reasoning input item has no `content` field

| 字段 | 值 |
| --- | --- |
| Issue | [#34496](https://github.com/vllm-project/vllm/issues/34496) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Responses API crashes with KeyError when reasoning input item has no `content` field

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When sending a multi-turn request to the Responses API (`POST /v1/responses`) that includes a `reasoning` input item **without** the optional `content` field, vLLM crashes with a `500 Internal Server Error`. Per the [OpenAI API specification](https://platform.openai.com/docs/api-reference/responses/create), `ResponseReasoningItem.content` is **optional** (`Optional[List[Content]] = None`). Clients like `langchain-openai` omit this field when constructing multi-turn input from previous responses — for example, they include `{"type": "reasoning", "id": "...", "summary": [...]}` without a `content` key. The root cause is in `vllm/entrypoints/openai/parser/harmony_utils.py:224-227`: ```python elif response_msg["type"] == "reasoning": content = response_msg["content"] # KeyError if "content" key is missing assert len(content) == 1 # AssertionError if content is [] or None msg = Message.from_role_and_content(Role.ASSISTANT, content[0]["text"]) ``` This code: 1. Uses `response_msg["content"]` instead of `.get("content")` — raises `KeyError` when the key is absent 2. Asserts `len(content) == 1` — fails for `None` or empty list 3. Does no...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: vLLM crashes with a `500 Internal Server Error`. Per the [OpenAI API specification](https://platform.openai.com/docs/api-reference/responses/create), `ResponseReasoningItem.content` is **optional** (`Optional[List[Conte...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: sh) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: chat/completions`) with `reasoning_content` works correctly for the same model and input. This bug only affects the Responses API. ### Test results for different `content` formats | Input format | Result | |---|---| | `...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: urrent environment ### 🐛 Describe the bug When sending a multi-turn request to the Responses API (`POST /v1/responses`) that includes a `reasoning` input item **without** the optional `content` field, vLLM crashes with...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
