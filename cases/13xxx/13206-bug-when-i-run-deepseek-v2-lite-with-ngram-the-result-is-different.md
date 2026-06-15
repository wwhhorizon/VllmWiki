# vllm-project/vllm#13206: [Bug]: when i run DeepSeek-V2-Lite with [ngram], the result is different

| 字段 | 值 |
| --- | --- |
| Issue | [#13206](https://github.com/vllm-project/vllm/issues/13206) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: when i run DeepSeek-V2-Lite with [ngram], the result is different

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug llm = LLM( model="/opt/apps/LLM_model/DeepSeek-Coder-V2-Lite-Instruct-modelscope", trust_remote_code=True, gpu_memory_utilization=0.7, tensor_parallel_size=4, max_model_len = 4096, disable_log_stats = False, speculative_model="[ngram]", num_speculative_tokens=7, ngram_prompt_lookup_max=5, ngram_prompt_lookup_min=2 ) sampling_params = SamplingParams(temperature=0, top_p=0.95,max_tokens=4096) when i open [ngram]， the result is different with before. but i set temperature=0, it should be same . i think there is something wrong with MOE module. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;hardware_porting;model_support;moe;sampling_logits;speculative_decoding cuda;moe;operator;sampling;triton build_erro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: le. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ]: when i run DeepSeek-V2-Lite with [ngram], the result is different bug;stale ### Your current environment ### 🐛 Describe the bug llm = LLM( model="/opt/apps/LLM_model/DeepSeek-Coder-V2-Lite-Instruct-modelscope", trust...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: port;moe;sampling_logits;speculative_decoding cuda;moe;operator;sampling;triton build_error env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: sor_parallel_size=4, max_model_len = 4096, disable_log_stats = False, speculative_model="[ngram]", num_speculative_tokens=7, ngram_prompt_lookup_max=5, ngram_prompt_lookup_min=2 ) sampling_params = SamplingParams(temper...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
