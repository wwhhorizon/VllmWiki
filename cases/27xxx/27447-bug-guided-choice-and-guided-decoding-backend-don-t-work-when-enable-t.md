# vllm-project/vllm#27447: [Bug]: `guided_choice` and `guided_decoding_backend` don't work when `enable_thinking=False` for Qwen3

| 字段 | 值 |
| --- | --- |
| Issue | [#27447](https://github.com/vllm-project/vllm/issues/27447) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: `guided_choice` and `guided_decoding_backend` don't work when `enable_thinking=False` for Qwen3

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### **Description** When setting ```python "chat_template_kwargs": {"enable_thinking": False} ``` both `guided_choice` and `guided_decoding_backend` stop working. However, when `enable_thinking=True`, they function correctly. This suggests that guided decoding logic (xgrammar / choice restriction) is currently **coupled to the reasoning mode** and bypassed when “thinking” is disabled. --- ### **Reproduction Steps** To reproduce, start a vLLM OpenAI-compatible server as follows: ```bash vllm serve Qwen/Qwen3-32B \ --dtype half \ --enable-reasoning \ --reasoning-parser qwen3 \ --enable-auto-tool-choice \ --tool-call-parser hermes \ --guided-decoding-backend xgrammar ``` Then run the following two Python scripts. --- ### **Case 1 — `guided_choice` ignored when `enable_thinking=False`** ```python from openai import OpenAI client = OpenAI( base_url="http:// /v1", api_key="EMPTY", ) completion = client.chat.completions.create( model="Qwen3-32B", messages=[{"role": "user", "content": "hello"}], extra_body={ "chat_template_kwargs": {"enable_thinking": False}, "guided_choice": ["hi", "hello", "hey"], }, ) print(completion.choices[0].messa...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: nd `guided_decoding_backend` don't work when `enable_thinking=False` for Qwen3 bug;stale ### Your current environment ### 🐛 Describe the bug ### **Description** When setting ```python "chat_template_kwargs": {"enable_th...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: `guided_choice` and `guided_decoding_backend` don't work when `enable_thinking=False` for Qwen3 bug;stale ### Your current environment ### 🐛 Describe the bug ### **Description** When setting ```python "chat_templ...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: passed when “thinking” is disabled. --- ### **Reproduction Steps** To reproduce, start a vLLM OpenAI-compatible server as follows: ```bash vllm serve Qwen/Qwen3-32B \ --dtype half \ --enable-reasoning \ --reasoning-pars...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ed_choice` ignored when `enable_thinking=False`** ```python from openai import OpenAI client = OpenAI( base_url="http:// /v1", api_key="EMPTY", ) completion = client.chat.completions.create( model="Qwen3-32B", messages=...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: compatible server as follows: ```bash vllm serve Qwen/Qwen3-32B \ --dtype half \ --enable-reasoning \ --reasoning-parser qwen3 \ --enable-auto-tool-choice \ --tool-call-parser hermes \ --guided-decoding-backend xgrammar...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
