# vllm-project/vllm#10023: [Bug]: Issue while passing chat template of llama3.2 11b to vllm server 

| 字段 | 值 |
| --- | --- |
| Issue | [#10023](https://github.com/vllm-project/vllm/issues/10023) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;gemm;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Issue while passing chat template of llama3.2 11b to vllm server 

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am setting up the vllm server for llama3.2 11b VLM model. Following is the command I am using vllm serve meta-llama/Llama-3.2-11B-Vision --host 172.17.0.2 --port 6006 --gpu-memory-utilization 0.9 --trust-remote-code --limit-mm-per-prompt image=2 --max-model-len 8000 --max-num-seqs 16 --enforce-eager --chat-template /workspace/llm_test_dev/src/llama3.2/vllm_server/tool_chat_template_llama3.2_json.jinja The reason to add chat template was, when I did it without it I could setup the server successfully but when I try to infer using OpenAI like client, it throws error that openai.BadRequestError: Error code: 400 - {'object': 'error', 'message': 'As of transformers v4.44, default chat template is no longer allowed, so you must provide a chat template if the tokenizer does not define one.', 'type': 'BadRequestError', 'param': None, 'code': 400} But even though adding chat template to the the cli commad, it is throwing error as ValueError: The supplied chat template string (/workspace/llm_test_dev/src/llama3.2/vllm_server/tool_chat_template_llama3.2_json.jinja) appears path-like, but doesn't exist!...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Issue while passing chat template of llama3.2 11b to vllm server bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am setting up the vllm server for llama3.2 11b VLM mo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;speculative_decoding cuda;gemm;operator;quan...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ks! ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: try to infer using OpenAI like client, it throws error that openai.BadRequestError: Error code: 400 - {'object': 'error', 'message': 'As of transformers v4.44, default chat template is no longer allowed, so you must pro...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: al_vlm;quantization;speculative_decoding cuda;gemm;operator;quantization;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
