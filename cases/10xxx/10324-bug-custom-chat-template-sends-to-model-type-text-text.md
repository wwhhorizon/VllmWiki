# vllm-project/vllm#10324: [Bug] custom chat template sends to model [{'type': 'text', 'text': '...'}]

| 字段 | 值 |
| --- | --- |
| Issue | [#10324](https://github.com/vllm-project/vllm/issues/10324) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;fp8;gemm;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] custom chat template sends to model [{'type': 'text', 'text': '...'}]

### Issue 正文摘录

### Your current environment ### Model Input Dumps ``` prompt: " system \n\nCutting Knowledge Date: December 2023\nToday Date: 14 Nov 2024\n\n[{'type': 'text', 'text': 'you are a helpful assistant'}] user \n\n[{'type': 'text', 'text': 'hello\\n'}] assistant \n\n", params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.7, top_p=1.0, top_k=-1, min_p=0.0, seed=None, stop=[], stop_token_ids=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=131004, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None), guided_decoding=GuidedDecodingParams(json=None, regex=None, choice=None, grammar=None, json_object=None, backend=None, whitespace_pattern=None) ``` ### 🐛 Describe the bug Hello. I created a simple container image that contains latest [tool_chat_template_llama3.2_json.jinja](https://github.com/vllm-project/vllm/blob/main/examples/tool_chat_template_llama3.2_json.jinja) ``` FROM docker.io/vllm/vllm-openai:v0.6.3.post1 COPY tool_chat_template_llama3.2_json.jinja vllm-workspace/tool_chat_template_llama3.2_json.jinja ``` The container...

## 现有链接修复摘要

#10164 [Bugfix][Frontend] Update Llama Chat Templates to also support Non-Tool use

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: okens=131004, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None), guided_decoding=GuidedDecodingParams(json=None, regex=None, ch...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: v0.6.3.post1-tools \ --model neuralmagic/Llama-3.2-90B-Vision-Instruct-FP8-dynamic \ --tensor-parallel-size 8 \ --served-model-name "Llama3.2 90B" \ --trust-remote-code \ --gpu-memory-utilization 0.95 \ --distributed-ex...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: rams(json=None, regex=None, choice=None, grammar=None, json_object=None, backend=None, whitespace_pattern=None) ``` ### 🐛 Describe the bug Hello. I created a simple container image that contains latest [tool_chat_templa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug] custom chat template sends to model [{'type': 'text', 'text': '...'}] bug ### Your current environment ### Model Input Dumps ``` prompt: " system \n\nCutting Knowledge Date: December 2023\nToday Date: 14 Nov 2024\...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#10164](https://github.com/vllm-project/vllm/pull/10164) | closes_keyword | 0.95 | [Bugfix][Frontend] Update Llama Chat Templates to also support Non-Tool use | FIX #10324 <details> <summary>Basic Chat</summary> ### Input ``` [ { "role": "user", "content": "What is vLLM?\n" } ] ``` ### Old ``` <\|begin_of_text\|><\|st |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
