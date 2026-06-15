# vllm-project/vllm#9706: [Bug]: Inconsistent evaluations when enabling / disabling chunked_prefill?

| 字段 | 值 |
| --- | --- |
| Issue | [#9706](https://github.com/vllm-project/vllm/issues/9706) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Inconsistent evaluations when enabling / disabling chunked_prefill?

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hi, I'm trying to use lm_eval_harness to evaluate Llama 3.1 8B Instruct with vllm as its backend. Here are two runs that I have: Run 1 ``` bash lm_eval \ --model vllm \ --model_args pretrained=meta-llama/Meta-Llama-3.1-8B-Instruct,gpu_memory_utilization=0.6 \ --tasks scrolls_narrativeqa_llama_16k \ --gen_kwargs temperature=0 \ --apply_chat_template \ --limit 256 \ --batch_size auto ``` With output: ``` vllm (pretrained=meta-llama/Meta-Llama-3.1-8B-Instruct,enable_chunked_prefill=False), gen_kwargs: (temperature=0), limit: 256.0, num_fewshot: None, batch_size: auto | Tasks |Version|Filter|n-shot|Metric| |Value | |Stderr| |-----------------------------|------:|------|-----:|------|---|-----:|---|------| |scrolls_narrativeqa_llama_16k| 2|none | 0|f1 |↑ |6.1901|± | N/A| ``` Run 2 ```bash lm_eval \ --model vllm \ --model_args pretrained=meta-llama/Meta-Llama-3.1-8B-Instruct,gpu_memory_utilization=0.6,enable_chunked_prefill=False \ --tasks scrolls_narrativeqa_llama_16k \ --gen_kwargs temperature=0 \ --apply_chat_template \ --limit 256 \ --batch_size auto ``` With output: ```bash vllm (pretrained=meta...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 56.0, num_fewshot: None, batch_size: auto | Tasks |Version|Filter|n-shot|Metric| |Value | |Stderr| |-----------------------------|------:|------|-----:|------|---|-----:|---|------| |scrolls_narrativeqa_llama_16k| 2|non...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: isabling chunked_prefill? bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hi, I'm trying to use lm_eval_harness to evaluate Llama 3.1 8B Instruct with vllm as its backen...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Inconsistent evaluations when enabling / disabling chunked_prefill? bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hi, I'm trying to use lm_eval_harness to evalu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: o use lm_eval_harness to evaluate Llama 3.1 8B Instruct with vllm as its backend. Here are two runs that I have: Run 1 ``` bash lm_eval \ --model vllm \ --model_args pretrained=meta-llama/Meta-Llama-3.1-8B-Instruct,gpu_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ng! ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
