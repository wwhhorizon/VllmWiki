# vllm-project/vllm#19489: [Bug]: Phi-4-mini-instruct / Phi-4-multimodal-instruct produces gibberish when input <4096 tokens and output is >4096 tokens

| 字段 | 值 |
| --- | --- |
| Issue | [#19489](https://github.com/vllm-project/vllm/issues/19489) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cache;cuda;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Phi-4-mini-instruct / Phi-4-multimodal-instruct produces gibberish when input <4096 tokens and output is >4096 tokens

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Phi-4-mini-instruct models deployed with vLLM v0.9.1 (and before) generates gibberish when the provided input has less than 4096 tokens and the response exceeds 4096 tokens (all tokens produces after the 4096-th are gibberish). If the response stays under 4096 tokens, or the input is already above the 4096 threshold, then the problem does not occur. Similar issue #6135 was closed due to inactivity but contains valuable information, see also related TGI issue [#2185](https://github.com/huggingface/text-generation-inference/issues/2185). # Minimal working example Here is a dummy Phi-4 prompt of 3995 tokens [\[Prompt_phi-4.txt\]](https://github.com/user-attachments/files/20690703/Prompt_phi-4.txt) for which the output is: Using Phi-4 tokenizer, we can see that the last token `voltage` of `such as dynamic voltage` is the 4096-th token. Different prompt with approximately the same number of tokens lead to the same issue. I tried with vllm images `vllm/vllm-openai:v0.9.0.1` and `vllm/vllm-openai:v0.9.1` (latest) with: ``` docker run --rm --runtime nvidia --gpus all --mount type=bind,src= /Phi-4-mini-instruct,dst=/Phi-4-mini-instruct -p...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Phi-4-mini-instruct / Phi-4-multimodal-instruct produces gibberish when input <4096 tokens and output is >4096 tokens bug;stale ### Your current environment ### 🐛 Describe the bug Phi-4-mini-instruct models deplo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: m/vllm-openai:v0.9.0.1` and `vllm/vllm-openai:v0.9.1` (latest) with: ``` docker run --rm --runtime nvidia --gpus all --mount type=bind,src= /Phi-4-mini-instruct,dst=/Phi-4-mini-instruct -p 8000:8000 --ipc=host vllm/vllm...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ue. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: so reduces the token limit where the problem arises. - I tried different kv cache dtype values, it does not solve the issue. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: roduces gibberish when input <4096 tokens and output is >4096 tokens bug;stale ### Your current environment ### 🐛 Describe the bug Phi-4-mini-instruct models deployed with vLLM v0.9.1 (and before) generates gibberish wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
