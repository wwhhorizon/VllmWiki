# vllm-project/vllm#23108: [Usage]: how to use built-in python tool of gpt-oss-20b after starting vllm serve --tool-server demo?

| 字段 | 值 |
| --- | --- |
| Issue | [#23108](https://github.com/vllm-project/vllm/issues/23108) |
| 状态 | closed |
| 标签 | usage;stale;gpt-oss |
| 评论 | 23; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: how to use built-in python tool of gpt-oss-20b after starting vllm serve --tool-server demo?

### Issue 正文摘录

### Your current environment Hi, I'm trying to test gpt-oss with vllm in a H800 GPU. I have successfully installed vllm and relevant dependencies following [gpt-oss vllm usage installation guide](https://github.com/openai/gpt-oss?tab=readme-ov-file#vllm): ```bash pip install --pre vllm==0.10.1+gptoss \ --extra-index-url https://wheels.vllm.ai/gpt-oss/ \ --extra-index-url https://download.pytorch.org/whl/nightly/cu128 ``` Following the [gpt-oss vllm usage guide](https://docs.vllm.ai/projects/recipes/en/latest/OpenAI/GPT-OSS.html#usage), I successfully started the vllm server with the command: ```bash vllm serve openai/gpt-oss-20b --port 38999 --async-scheduling --tool-server demo ``` And the log outputs "Code interpreter tool initialized", which means the built-in python tool has been successfully initialized. Accoding to the [gpt-oss vllm usage guide](https://docs.vllm.ai/projects/recipes/en/latest/OpenAI/GPT-OSS.html#usage), I should call the /v1/responses api. I have successfully tried some cases like: ```bash curl http://localhost:38999/v1/responses -H "Content-Type: application/json" -d '{"model": "openai/gpt-oss-20b", "input": "What is the square root of 9001?"}' ``` The gpt-...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: I'm trying to test gpt-oss with vllm in a H800 GPU. I have successfully installed vllm and relevant dependencies following [gpt-oss vllm usage installation guide](https://github.com/openai/gpt-oss?tab=readme-ov-file#vll...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: how to use built-in python tool of gpt-oss-20b after starting vllm serve --tool-server demo? usage;stale;gpt-oss ### Your current environment Hi, I'm trying to test gpt-oss with vllm in a H800 GPU. I have succe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: tool of gpt-oss-20b after starting vllm serve --tool-server demo? usage;stale;gpt-oss ### Your current environment Hi, I'm trying to test gpt-oss with vllm in a H800 GPU. I have successfully installed vllm and relevant...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ction'\"}}, {'type': 'literal_error', 'loc': ('body', 'tools', 0, 'FileSearchTool', 'type'), 'msg': \"Input should be 'file_search'\", 'input': 'code_interpreter', 'ctx': {'expected': \"'file_search'\"}}, {'type': 'miss...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: emo? usage;stale;gpt-oss ### Your current environment Hi, I'm trying to test gpt-oss with vllm in a H800 GPU. I have successfully installed vllm and relevant dependencies following [gpt-oss vllm usage installation guide...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
