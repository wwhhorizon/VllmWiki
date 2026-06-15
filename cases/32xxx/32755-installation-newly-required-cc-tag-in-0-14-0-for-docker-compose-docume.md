# vllm-project/vllm#32755: [Installation]: Newly required -cc tag in 0.14.0 for Docker compose -- documentation

| 字段 | 值 |
| --- | --- |
| Issue | [#32755](https://github.com/vllm-project/vllm/issues/32755) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Newly required -cc tag in 0.14.0 for Docker compose -- documentation

### Issue 正文摘录

### The issue https://docs.vllm.ai/en/latest/cli/serve/#vllmconfig Am I missing something? The documentation does not explain how to use `-cc` argument at all. I've been using Docker compose and it just kicked me saying that I need to use `-cc`. I can't seem to find any info on e.g. `-cc='{"mode":3}'` -- what is mode? What is mode 3? The vLLM AI can't seem to cite anything else except for the above link. If every key-value pairs, possible values, and examples are documented, as well as 'default' or 'common' setups, that would be great. ### Your current environment Nvidia Spark ### How you are installing vllm Docker compose -- what used to work, but doesn't work anymore: ``` services: vllm-node: image: vllm/vllm-openai:latest ... privileged: true network_mode: host ipc: host pid: host deploy: resources: reservations: devices: - driver: nvidia count: all capabilities: [gpu] ... command: > bash -c -i "vllm serve openai/gpt-oss-120b --cc '{"mode": "3"}' <<---- newly added line --port 8000 --host 0.0.0.0 --gpu-memory-utilization 0.7 --load-format fastsafetensors ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot livi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Installation]: Newly required -cc tag in 0.14.0 for Docker compose -- documentation installation ### The issue https://docs.vllm.ai/en/latest/cli/serve/#vllmconfig Am I missing something? The documentation does not exp
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: nstallation ### The issue https://docs.vllm.ai/en/latest/cli/serve/#vllmconfig Am I missing something? The documentation does not explain how to use `-cc` argument at all. I've been using Docker compose and it just kick...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: m-project/vllm/issues/32637 to see if I can run `GadflyII/GLM-4.7-Flash-NVFP4`
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: `-cc`, then suggests empty key-value `-cc "{}"`, then suggested `--cc '{"backend": "inductor"}'`, etc. etc., no luck.) ### Unrelated Also looking at the thread https://github.com/vllm-project/vllm/issues/32637 to see if...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
