# vllm-project/vllm#16321: [Bug]: issues with guided generation for tool calls (xgrammar)

| 字段 | 值 |
| --- | --- |
| Issue | [#16321](https://github.com/vllm-project/vllm/issues/16321) |
| 状态 | closed |
| 标签 | bug;structured-output;stale;tool-calling |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;model_support;quantization |
| 子分类 | install |
| Operator 关键词 | quantization |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: issues with guided generation for tool calls (xgrammar)

### Issue 正文摘录

### Your current environment docker ### 🐛 Describe the bug Example code from the https://docs.vllm.ai/en/latest/features/tool_calling.html doesn't work. I run vllm server in docker ``` docker run --gpus all --runtime=nvidia \ -v ~/.cache/huggingface:/root/.cache/huggingface \ -p 8000:8000 \ --ipc=host \ vllm/vllm-openai:latest \ --model Qwen/Qwen2.5-3B-Instruct-GPTQ-Int8 \ --enable-auto-tool-choice \ --tool-call-parser hermes ``` with code from the example but I changed ``` tool_choice="required" ``` But I got an error ``` openai.BadRequestError: Error code: 400 - {'object': 'error', 'message': 'The provided JSON schema contains features not supported by xgrammar.', 'type': 'BadRequestError', 'param': None, 'code': 400}= ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ) bug;structured-output;stale;tool-calling ### Your current environment docker ### 🐛 Describe the bug Example code from the https://docs.vllm.ai/en/latest/features/tool_calling.html doesn't work. I run vllm server in do...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: r in docker ``` docker run --gpus all --runtime=nvidia \ -v ~/.cache/huggingface:/root/.cache/huggingface \ -p 8000:8000 \ --ipc=host \ vllm/vllm-openai:latest \ --model Qwen/Qwen2.5-3B-Instruct-GPTQ-Int8 \ --enable-aut...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: None, 'code': 400}= ``` development ci_build;frontend_api;model_support;quantization quantization dtype Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: s with guided generation for tool calls (xgrammar) bug;structured-output;stale;tool-calling ### Your current environment docker ### 🐛 Describe the bug Example code from the https://docs.vllm.ai/en/latest/features/tool_c...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ### 🐛 Describe the bug Example code from the https://docs.vllm.ai/en/latest/features/tool_calling.html doesn't work. I run vllm server in docker ``` docker run --gpus all --runtime=nvidia \ -v ~/.cache/huggingface:/root...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
