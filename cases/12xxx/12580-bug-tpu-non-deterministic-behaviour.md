# vllm-project/vllm#12580: [Bug][TPU]: Non-deterministic behaviour

| 字段 | 值 |
| --- | --- |
| Issue | [#12580](https://github.com/vllm-project/vllm/issues/12580) |
| 状态 | closed |
| 标签 | bug;tpu |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;nondeterministic |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][TPU]: Non-deterministic behaviour

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hi, I've found that when I run Llama3.2-3B using vLLM on the TPU v6e backend, I get different outputs depending on the instance/time of day. To reproduce, run the below script on 2 different TPU machines, at different times. ```py import vllm llm = vllm.LLM( model="meta-llama/Llama-3.2-3B-Instruct", download_dir="/mnt/ssd0/data", num_scheduler_steps=4, swap_space=16, max_model_len=256, enforce_eager=False ) print(llm.chat([ {"role": "system", "content": "You are a pirate chatbot who always responds in pirate speak!"}, {"role": "user", "content": "How are you?"}, ], vllm.SamplingParams( max_tokens=1024, temperature=0 ))[0].outputs[0].text) ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 5: [Bug][TPU]: Non-deterministic behaviour bug;tpu ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hi, I've found that when I run Llama3.2-3B using vLLM on the TPU v6e backend, I get...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: the below script on 2 different TPU machines, at different times. ```py import vllm llm = vllm.LLM( model="meta-llama/Llama-3.2-3B-Instruct", download_dir="/mnt/ssd0/data", num_scheduler_steps=4, swap_space=16, max_mode...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ug Hi, I've found that when I run Llama3.2-3B using vLLM on the TPU v6e backend, I get different outputs depending on the instance/time of day. To reproduce, run the below script on 2 different TPU machines, at differen...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Non-deterministic behaviour bug;tpu ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hi, I've found that when I run Llama3.2-3B using vLLM on the TPU v6e backend, I get different o...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
