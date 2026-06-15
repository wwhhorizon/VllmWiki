# vllm-project/vllm#16763: [Bug]: qwen2.5-vl inference truncated

| 字段 | 值 |
| --- | --- |
| Issue | [#16763](https://github.com/vllm-project/vllm/issues/16763) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: qwen2.5-vl inference truncated

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug inference with qwen2.5-vl-32b or qwen2.5-vl-7b. the output always truncated . ![Image](https://github.com/user-attachments/assets/24e3b8b9-5cdb-40f3-a99f-5728ff92d3f9) I integrated models in dify . the input is from doc_extract node ,content like： "03.源IP DNS请求排名 bps\r\nSession#\r\n上行 下行 连接数\r\n2. Jan\r\n3. Jan\r\n4. Jan\r\n5. Jan\r\n6. Jan\r\n7. Jan\r\n8. Jan\r\n0\r\n5k\r\n10k\r\n15k\r\n20k\r\n25k\r\n0\r\n20k\r\n5k\r\n10k\r\n15k\r\n25k\r\n序号 目标IP 总请求数\ue65d 上行 下\r\n1" When truncating the results extracted from doc_extract and removing the table data above, the responses are normal. However, when the table data is included, the responses are mostly truncated. Here is is the parameters: ![Image](https://github.com/user-attachments/assets/796cede9-2153-44dc-b538-ddea7955ee5b) Here is the log of vllm requst : ； \n assistant\n', params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=1.0, repetition_penalty=1.0, temperature=0.4, top_p=0.7, top_k=-1, min_p=0.0, seed=None, stop=[' '], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=1301, min_tokens=0, logprobs=None, prompt_log...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: _tokens=1301, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None), prompt_token_ids: None, lora_request: No...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ne. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: qwen2.5-vl inference truncated bug;stale ### Your current environment ### 🐛 Describe the bug inference with qwen2.5-vl-32b or qwen2.5-vl-7b. the output always truncated . ![Image](https://github.com/user-attachme...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: qwen2.5-vl inference truncated bug;stale ### Your current environment ### 🐛 Describe the bug inference with qwen2.5-vl-32b or qwen2.5-vl-7b. the output always truncated . ![Image](https://github.com/user-attachme...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: el;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
