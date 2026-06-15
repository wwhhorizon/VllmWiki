# vllm-project/vllm#40247: [Bug]: Gemma 4 26b-a4b AWQ INT4 is broken in 0.19.1, but working in latest gemma4 tag on Dockerhub

| 字段 | 值 |
| --- | --- |
| Issue | [#40247](https://github.com/vllm-project/vllm/issues/40247) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Gemma 4 26b-a4b AWQ INT4 is broken in 0.19.1, but working in latest gemma4 tag on Dockerhub

### Issue 正文摘录

### Your current environment I was running the Docker images `vllm/vllm-openai:v0.19.1` and `vllm/vllm-openai:gemma4`. ### 🐛 Describe the bug Running https://huggingface.co/cyankiwi/gemma-4-26B-A4B-it-AWQ-4bit works on the `gemma4` tag. Running the same model on `v0.19.1`, we see the following: ``` Loading safetensors checkpoint shards: 0% Completed | 0/4 [00:00<?, ?it/s] (EngineCore pid=272) ERROR 04-18 14:25:37 [core.py:1108] EngineCore failed to start. (EngineCore pid=272) ERROR 04-18 14:25:37 [core.py:1108] Traceback (most recent call last): (EngineCore pid=272) ERROR 04-18 14:25:37 [core.py:1108] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 1082, in run_engine_core (EngineCore pid=272) ERROR 04-18 14:25:37 [core.py:1108] engine_core = EngineCoreProc(*args, engine_index=dp_rank, **kwargs) (EngineCore pid=272) ERROR 04-18 14:25:37 [core.py:1108] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore pid=272) ERROR 04-18 14:25:37 [core.py:1108] File "/usr/local/lib/python3.12/dist-packages/vllm/tracing/otel.py", line 178, in sync_wrapper (EngineCore pid=272) ERROR 04-18 14:25:37 [core.py:1108] return func(*args, **kwargs) (EngineCore pid...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Gemma 4 26b-a4b AWQ INT4 is broken in 0.19.1, but working in latest gemma4 tag on Dockerhub bug ### Your current environment I was running the Docker images `vllm/vllm-openai:v0.19.1` and `vllm/vllm-openai:gemma4...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: Gemma 4 26b-a4b AWQ INT4 is broken in 0.19.1, but working in latest gemma4 tag on Dockerhub bug ### Your current environment I was running the Docker images `vllm/vllm-openai:v0.19.1` and `vllm/vllm-openai:gemma4...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 6b-a4b AWQ INT4 is broken in 0.19.1, but working in latest gemma4 tag on Dockerhub bug ### Your current environment I was running the Docker images `vllm/vllm-openai:v0.19.1` and `vllm/vllm-openai:gemma4`. ### 🐛 Describ...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Bug]: Gemma 4 26b-a4b AWQ INT4 is broken in 0.19.1, but working in latest gemma4 tag on Dockerhub bug ### Your current environment I was running the Docker images `vllm/vllm-openai:v0.19.1` and `vllm/vllm-openai:gemma4...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
