# vllm-project/vllm#20740: [Bug]: Gemma3-12b-it get a garbled response

| 字段 | 值 |
| --- | --- |
| Issue | [#20740](https://github.com/vllm-project/vllm/issues/20740) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma3-12b-it get a garbled response

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have input 10x images in gemma3 by switching vllm or huggingface backend. The issue is that the huggingface give the correct output, while vllm fails with random output as shown in above image. I pass all arguments through llama-factory commendline and the config is : ``` # llamafactory-cli webchat examples/inferencexx.yaml model_name_or_path: google/gemma-3-12b-it template: gemma3 infer_backend: vllm # choices: [huggingface, vllm, sglang] trust_remote_code: false # required, or mass code ?? # i encountered bug here before, if i remove following line, it'll directly output random text even i just feed single image flash_attn: sdpa infer_dtype: bfloat16 vllm_maxlen: 131072 vllm_config: {'limit_mm_per_prompt':{"image": 34, "video": 2, "audio": 2}} ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Gemma3-12b-it get a garbled response bug ### Your current environment ### 🐛 Describe the bug I have input 10x images in gemma3 by switching vllm or huggingface backend. The issue is that the huggingface give the
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. development attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: output random text even i just feed single image flash_attn: sdpa infer_dtype: bfloat16 vllm_maxlen: 131072 vllm_config: {'limit_mm_per_prompt':{"image": 34, "video": 2, "audio": 2}} ``` ### Before submitting a new issu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: g I have input 10x images in gemma3 by switching vllm or huggingface backend. The issue is that the huggingface give the correct output, while vllm fails with random output as shown in above image. I pass all arguments...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
