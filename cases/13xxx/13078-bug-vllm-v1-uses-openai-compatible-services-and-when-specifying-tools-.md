# vllm-project/vllm#13078: [Bug]: vllm v1 uses OpenAI-compatible services, and when specifying tools through tool_choice, the returned response is incorrect.

| 字段 | 值 |
| --- | --- |
| Issue | [#13078](https://github.com/vllm-project/vllm/issues/13078) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;quantization;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm v1 uses OpenAI-compatible services, and when specifying tools through tool_choice, the returned response is incorrect.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # Problem When using `tool_choice` to specify a tool for the model to invoke, the model did not pass the parameters correctly; instead, it wrote the response into `function.arguments`. # Start the vllm service using the following command. vllm serve "Qwen/Qwen2.5-14B-Instruct-GPTQ-Int4" --host 0.0.0.0 \ --enable-auto-tool-choice \ --tool-call-parser hermes \ --quantization gptq \ --gpu-memory-utilization 0.85 \ --enforce_eager # HTTP request. ``` POST http://192.168.50.204:8000/v1/chat/completions HTTP/1.1 Host: 192.168.50.204:8000 Accept: application/json OpenAI-Beta: assistants=v2 User-Agent: OpenAI/2.1.0-beta.2 (.NET 8.0.12; Darwin 24.2.0 Darwin Kernel Version 24.2.0: Fri Dec 6 19:04:03 PST 2024; root:xnu-11215.61.5~2/RELEASE_ARM64_T8132) Authorization: Bearer 1 traceparent: 00-73751c46d78d3d1843bdaf8a3d2ace16-4e0374ccdd5efdb8-00 Content-Type: application/json Content-Length: 700 {"messages":[{"role":"assistant","content":"\u60A8\u597D\uFF01\u6709\u4EC0\u4E48\u53EF\u4EE5\u5E2E\u60A8\uFF1F"},{"role":"user","content":"\u4F60\u597D\n"}],"model":"Qwen/Qwen2.5-14B-Instruct-GPTQ-Int4","max_completion_tokens":10000,"presence_penalty"...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: vllm v1 uses OpenAI-compatible services, and when specifying tools through tool_choice, the returned response is incorrect. bug;stale ### Your current environment ### 🐛 Describe the bug # Problem When using `tool...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: using the following command. vllm serve "Qwen/Qwen2.5-14B-Instruct-GPTQ-Int4" --host 0.0.0.0 \ --enable-auto-tool-choice \ --tool-call-parser hermes \ --quantization gptq \ --gpu-memory-utilization 0.85 \ --enforce_eage...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 7E5\u8BC6\u5E93\u67E5\u627E\u7B54\u6848","name":"System-knowledge_base_search","parameters":{"type":"object","required":["question"],"properties":{"question":{"description":"\u95EE\u9898","type":"string"}}}}}],"tool_cho...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: fying tools through tool_choice, the returned response is incorrect. bug;stale ### Your current environment ### 🐛 Describe the bug # Problem When using `tool_choice` to specify a tool for the model to invoke, the model...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: be the bug # Problem When using `tool_choice` to specify a tool for the model to invoke, the model did not pass the parameters correctly; instead, it wrote the response into `function.arguments`. # Start the vllm servic...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
