# vllm-project/vllm#22858: [Bug]: Batch inference uses wrong model (or just bad Docker build?)

| 字段 | 值 |
| --- | --- |
| Issue | [#22858](https://github.com/vllm-project/vllm/issues/22858) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | cold_start |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Batch inference uses wrong model (or just bad Docker build?)

### Issue 正文摘录

### Your current environment I installed vLLM using the official Docker image via Singularity: ```bash singularity pull vllm-0100.sif docker://vllm/vllm-openai:v0.10.0 ``` ### 🐛 Describe the bug Now when I try to run `vllm.entrypoints.openai.run_batch` with the Qwen model (`--model Qwen/Qwen3-4B-Thinking-2507`), I get an error ``` ERROR 08-13 16:59:20 [serving_chat.py:140] Error with model object='error' message='The model `meta-llama/Meta-Llama-3-8B-Instruct` does not exist.' type='NotFoundError' param=None code=404 ``` I suspect this could be due to the Docker image using an unstable version of vLLM (`vLLM Version : 0.10.1.dev1+gbcc0a3cbe (git sha: bcc0a3cbe)` from the `collect_env.py` output), even though I specified the tag `vllm/vllm-openai:v0.10.0` in my pull command. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: Batch inference uses wrong model (or just bad Docker build?) bug ### Your current environment I installed vLLM using the official Docker image via Singularity: ```bash singularity pull vllm-0100.sif docker://vllm...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Batch inference uses wrong model (or just bad Docker build?) bug ### Your current environment I installed vLLM using the official Docker image via Singularity: ```bash singularity pull vllm-0100.sif docker://vllm...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ild;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding attention;cache;cuda;operator;quantization;sampling;triton build_error dtype;env_dependency;shap...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nd. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: speculative_decoding attention;cache;cuda;operator;quantization;sampling;triton build_error dtype;env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
