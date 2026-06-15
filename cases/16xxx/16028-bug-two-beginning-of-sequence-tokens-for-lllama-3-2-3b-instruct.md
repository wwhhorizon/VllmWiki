# vllm-project/vllm#16028: [Bug]: Two beginning of sequence tokens for Lllama-3.2-3B-Instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#16028](https://github.com/vllm-project/vllm/issues/16028) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: Two beginning of sequence tokens for Lllama-3.2-3B-Instruct

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug VLLM output includes two beginning of sequence tokens (128000) rather than one for Llama 3b in the `prompt_token_ids` field of the output: ```python from vllm import LLM model = LLM( model="meta-llama/Llama-3.2-3B-Instruct", ) messages = [[{"role": "system", "content":"This is a prompt"}, {"role": "user", "content": "User message"}]] vllm_out = model.chat( messages, SamplingParams(), ) print(vllm_out[0].prompt_token_ids) > [128000, 128000, 128006, 9125, 128007, 271, 38766, 1303, 33025, 2696, 25, 6790, 220, 2366, 18, 198, 15724, 2696, 25, 220, 2839, 5186, 220, 2366, 20, 271, 2028, 374, 264, 1633, 1633, 1317, 10137, 13, 128009, 128006, 882, 128007, 271, 1502, 1984, 128009, 128006, 78191, 128007, 271] from transformers import AutoTokenizer tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.2-3B-Instruct") print(tokenizer.apply_chat_template(messages)) > [[128000, 128006, 9125, 128007, 271, 38766, 1303, 33025, 2696, 25, 6790, 220, 2366, 18, 198, 15724, 2696, 25, 220, 2839, 5186, 220, 2366, 20, 271, 2028, 374, 264, 10137, 128009, 128006, 882, 128007, 271, 1502, 1984, 128009]] ``` See that `print(vllm_out[0].prompt_token_ids...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: a 3b in the `prompt_token_ids` field of the output: ```python from vllm import LLM model = LLM( model="meta-llama/Llama-3.2-3B-Instruct", ) messages = [[{"role": "system", "content":"This is a prompt"}, {"role": "user",...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ng. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Two beginning of sequence tokens for Lllama-3.2-3B-Instruct bug ### Your current environment ### 🐛 Describe the bug VLLM output includes two beginning of sequence tokens (128000) rather than one for Llama 3b in t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ted_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
