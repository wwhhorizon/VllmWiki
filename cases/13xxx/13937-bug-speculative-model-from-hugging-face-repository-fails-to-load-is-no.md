# vllm-project/vllm#13937: [Bug]: Speculative Model from Hugging Face Repository Fails to Load (is not a file error)

| 字段 | 值 |
| --- | --- |
| Issue | [#13937](https://github.com/vllm-project/vllm/issues/13937) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Speculative Model from Hugging Face Repository Fails to Load (is not a file error)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am trying to use speculative decoding in my OpenAI-compatible server using vLLM. My setup involves: - Loading the main model from a local path - Loading the speculative model from Hugging Face However, when attempting to start the server, I encounter the following error: ``` ValueError: yuhuili/EAGLE-Qwen2-72B-Instruct is not a file. ``` It appears that vLLM is treating the speculative model’s Hugging Face repository path as a file instead of fetching it properly. This issue does not occur when using the main model from Hugging Face; only the speculative model is affected. This is my command to start the server: ``` vllm serve /root/models/qwen/qwen2.5-72b-instruct.gguf -tp 4 \ --tokenizer Qwen/Qwen2.5-72B-Instruct \ --served-model-name qwen2.5-72b \ --enable-auto-tool-choice \ --tool-call-parser hermes \ --max-model-len 32768 \ --enable-prefix-caching \ --gpu-memory-utilization 0.8 \ -spec-draft-tp 4 \ --speculative_model yuhuili/EAGLE-Qwen2-72B-Instruct \ --num_speculative_tokens 5 ``` Error trace: ``` (VllmWorkerProcess pid=25189) INFO 02-27 00:42:39 model_runner.py:1109] Starting to load model yuhuili/EAGLE-Qwen2-72B-Instru...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Speculative Model from Hugging Face Repository Fails to Load (is not a file error) bug;stale ### Your current environment ### 🐛 Describe the bug I am trying to use speculative decoding in my OpenAI-compatible ser...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Speculative Model from Hugging Face Repository Fails to Load (is not a file error) bug;stale ### Your current environment ### 🐛 Describe the bug I am trying to use speculative decoding in my OpenAI-compatible ser...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
