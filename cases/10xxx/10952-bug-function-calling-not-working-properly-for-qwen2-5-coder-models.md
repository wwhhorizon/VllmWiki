# vllm-project/vllm#10952: [Bug]: Function calling not working properly for Qwen2.5-Coder models

| 字段 | 值 |
| --- | --- |
| Issue | [#10952](https://github.com/vllm-project/vllm/issues/10952) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Function calling not working properly for Qwen2.5-Coder models

### Issue 正文摘录

### Your current environment Serving `Qwen2.5-Coder-32B-Instruct` with the latest docker image `vllm-openai:v0.6.4.post1`: ``` docker run --gpus all -e VLLM_LOGGING_LEVEL=DEBUG --ipc=host -p 8002:8002 -ti vllm/vllm-openai:v0.6.4.post1 --model "/models/Qwen2.5-Coder-32B-Instruct" --served-model-name "Qwen25-Coder-32B-Instruct" --port 8002 --tensor-parallel-size 4 --enable-auto-tool-choice --tool-call-parser hermes ``` ### Model Input Dumps _No response_ ### 🐛 Describe the bug While running the get_temperature function calling example described in the [qwen documentation ](https://qwen.readthedocs.io/en/latest/framework/function_call.html) the function calls are not properly parsed. What I get from the model generation is the following: ```json { "content": "Sure, I'll get the current temperature in San Francisco and also the temperature for tomorrow.\n\nFirst, let's get the current temperature:\n\n \n{\"name\": \"get_current_temperature\", \"arguments\": {\"location\": \"San Francisco, California, USA\", \"unit\": \"fahrenheit\"}}\n \n\nNext, to get the temperature for tomorrow, I'll need to know the date. Since today is 2024-09-30, tomorrow will be 2024-10-01. Let's get the temper...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Function calling not working properly for Qwen2.5-Coder models bug ### Your current environment Serving `Qwen2.5-Coder-32B-Instruct` with the latest docker image `vllm-openai:v0.6.4.post1`: ``` docker run --gpus...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: urrent environment Serving `Qwen2.5-Coder-32B-Instruct` with the latest docker image `vllm-openai:v0.6.4.post1`: ``` docker run --gpus all -e VLLM_LOGGING_LEVEL=DEBUG --ipc=host -p 8002:8002 -ti vllm/vllm-openai:v0.6.4....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: tool_calls` contains the function call. I'm not sure if this is just a small bug in the tool call parser or if I am suppose to use a different one than `hermes`. Serving the model `qwen2.5-coder:32b` via ollama results...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: our current environment Serving `Qwen2.5-Coder-32B-Instruct` with the latest docker image `vllm-openai:v0.6.4.post1`: ``` docker run --gpus all -e VLLM_LOGGING_LEVEL=DEBUG --ipc=host -p 8002:8002 -ti vllm/vllm-openai:v0...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
