# vllm-project/vllm#15997: [Bug]: creating helm chart with vllm image and downloaded model throws   raise KeyboardInterrupt("terminated") KeyboardInterrupt: terminated error

| 字段 | 值 |
| --- | --- |
| Issue | [#15997](https://github.com/vllm-project/vllm/issues/15997) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: creating helm chart with vllm image and downloaded model throws   raise KeyboardInterrupt("terminated") KeyboardInterrupt: terminated error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug we have a docker image created out of vllm openapi which is working fine with docker run command but created helm chart for the same image to run via helm chart getting failed with below error please help here to understand this issue and fix. FROM vllm/vllm-openai:latest ENV API_KEY="11611-22722-33833-44944-55055" RUN apt-get update && apt-get install -y git wget vim && rm -rf /var/lib/apt/lists/* COPY ./Meta-Llama-3.1-8B-Instruct-Q8_0.gguf /Meta-Llama-3.1-8B-Instruct-Q8_0.gguf EXPOSE 8000 ENTRYPOINT ["python3", "-m", "vllm.entrypoints.openai.api_server", "--model", "/Meta-Llama-3.1-8B-Instruct-Q8_0.gguf"] You are using the default legacy behaviour of the . This is expected, and simply means that the `legacy` (previous) behavior will be used so nothing changes for you. If you want to use the new behaviour, set `legacy=False`. This should only be set if you understand what it means, and thoroughly read the reason why this was added as explained in https://github.com/huggingface/transformers/pull/24565 - if you loaded a llama tokenizer from a GGUF file you can ignore this message. Traceback (most recent call last): File "/usr/loca...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: stale ### Your current environment ### 🐛 Describe the bug we have a docker image created out of vllm openapi which is working fine with docker run command but created helm chart for the same image to run via helm chart...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: creating helm chart with vllm image and downloaded model throws raise KeyboardInterrupt("terminated") KeyboardInterrupt: terminated error bug;stale ### Your current environment ### 🐛 Describe the bug we have a do...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ase help here to understand this issue and fix. FROM vllm/vllm-openai:latest ENV API_KEY="11611-22722-33833-44944-55055" RUN apt-get update && apt-get install -y git wget vim && rm -rf /var/lib/apt/lists/* COPY ./Meta-L...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 2/dist-packages/vllm/entrypoints/cli/main.py", line 73, in main args.dispatch_function(args) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/serve.py", line 34, in cmd uvloop.run(run_server(args)) Fil...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ted ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
