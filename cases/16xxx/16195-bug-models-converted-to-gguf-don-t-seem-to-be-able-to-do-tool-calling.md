# vllm-project/vllm#16195: [Bug]: Models converted to GGUF don't seem to be able to do tool calling

| 字段 | 值 |
| --- | --- |
| Issue | [#16195](https://github.com/vllm-project/vllm/issues/16195) |
| 状态 | closed |
| 标签 | bug;stale;tool-calling |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Models converted to GGUF don't seem to be able to do tool calling

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When a model is converted to the GGUF format with no quantization, it can no longer work when async tool calling is requested. This is through the OpenAI API server. This is the steps to reproduce the problem: ``` huggingface-cli download meta-llama/Llama-3.2-3B-Instruct --local-dir Llama-3.2-3B-Instruct --include "*" ./llama.cpp/convert_hf_to_gguf.py Llama-3.2-3B-Instruct --outfile Llama-3.2-3B-Instruct.gguf No quantization run. Only in GGUF format. /bin/env python3 -m vllm.entrypoints.openai.api_server \ --host 0.0.0.0 --port 8000 \ --chat-template templates/tool_chat_template_llama3.2_json.jinja \ --model ~/Llama-3.2-3B-Instruct.gguf \ --max-model-len 102400 \ --gpu_memory_utilization 0.95 \ --quantization "fp8" \ --served-model-name llama-3.2 \ --enable-auto-tool-choice \ --tool-call-parser llama3_json ERROR 04-07 11:42:35 [llama_tool_parser.py:101] Error in extracting tool call from response. ERROR 04-07 11:42:35 [llama_tool_parser.py:101] Traceback (most recent call last): ERROR 04-07 11:42:35 [llama_tool_parser.py:101] File "/home/llm/miniconda3/lib/python3.12/site-packages/vllm/entrypoints/openai/tool_parsers/llama_tool_p...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: cent call last): File "/home/llm/mcp/./test.py", line 45, in asyncio.run(main()) File "/home/llm/miniconda3/lib/python3.12/asyncio/runners.py", line 194, in run return runner.run(main) ^^^^^^^^^^^^^^^^ File "/home/llm/m...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Models converted to GGUF don't seem to be able to do tool calling bug;stale;tool-calling ### Your current environment ### 🐛 Describe the bug When a model is converted to the GGUF format with no quantization, it c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ]: Models converted to GGUF don't seem to be able to do tool calling bug;stale;tool-calling ### Your current environment ### 🐛 Describe the bug When a model is converted to the GGUF format with no quantization, it can n...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 🐛 Describe the bug When a model is converted to the GGUF format with no quantization, it can no longer work when async tool calling is requested. This is through the OpenAI API server. This is the steps to reproduce the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: em. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
