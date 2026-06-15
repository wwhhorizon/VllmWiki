# vllm-project/vllm#10717: [Installation]: on docker swarm in VPS say: RuntimeError: Failed to infer device type

| 字段 | 值 |
| --- | --- |
| Issue | [#10717](https://github.com/vllm-project/vllm/issues/10717) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: on docker swarm in VPS say: RuntimeError: Failed to infer device type

### Issue 正文摘录

### Your current environment I install using docker swarm on dedicated cloud vps on hetzner, I want run a lightweight model "jinaai/jina-embeddings-v3", I assume that the cpu and ram i sufficient in a 16gb ram and 4 dedicated cpu. My docker compose file services: jinna: hostname: jinaai image: vllm/vllm-openai:latest command: "--model jinaai/jina-embeddings-v3 " volumes: - jinaai:/root/.cache/huggingface environment: - HUGGING_FACE_HUB_TOKEN=${secret} networks: - ragflow - bridge volumes: jinaai: driver: local networks: ragflow: external: true bridge: name: bridge external: true ### ERROR INFO 11-27 07:19:27 api_server.py:194] Started engine process with PID 16 Traceback (most recent call last): File " ", line 198, in _run_module_as_main File " ", line 88, in _run_code File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/api_server.py", line 643, in uvloop.run(run_server(args)) File "/usr/local/lib/python3.12/dist-packages/uvloop/__init__.py", line 109, in run return __asyncio.run( ^^^^^^^^^^^^^^ File "/usr/lib/python3.12/asyncio/runners.py", line 194, in run return runner.run(main) ^^^^^^^^^^^^^^^^ File "/usr/lib/python3.12/asyncio/runners.py", line 118, in run r...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Installation]: on docker swarm in VPS say: RuntimeError: Failed to infer device type installation ### Your current environment I install using docker swarm on dedicated cloud vps on hetzner, I want run a lightweight mod
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: docker swarm on dedicated cloud vps on hetzner, I want run a lightweight model "jinaai/jina-embeddings-v3", I assume that the cpu and ram i sufficient in a 16gb ram and 4 dedicated cpu. My docker compose file services:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ompose file services: jinna: hostname: jinaai image: vllm/vllm-openai:latest command: "--model jinaai/jina-embeddings-v3 " volumes: - jinaai:/root/.cache/huggingface environment: - HUGGING_FACE_HUB_TOKEN=${secret} netwo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
