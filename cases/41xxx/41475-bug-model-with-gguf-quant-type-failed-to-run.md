# vllm-project/vllm#41475: [Bug]: model with GGUF quant type failed to run

| 字段 | 值 |
| --- | --- |
| Issue | [#41475](https://github.com/vllm-project/vllm/issues/41475) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: model with GGUF quant type failed to run

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I run docker with follow cmd: docker run -d \ --name vllm \ --gpus all \ --ipc=host \ --shm-size=16g \ -e NCCL_P2P_DISABLE=0 \ -e NCCL_IB_DISABLE=1 \ -e VLLM_USE_MODELSCOPE=True \ -p 5000:5000 \ vllm/vllm-openai:v0.20.0 \ --model hesamation/Qwen3.6-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled-GGUF:Q4_K_M \ --max-model-len 102400 \ --kv-cache-dtype fp8 \ --gpu-memory-utilization 0.9 \ --max-num-seqs 24 \ --max-num-batched-tokens 8192 \ --language-model-only \ --enable-prefix-caching \ --default-chat-template-kwargs '{"enable_thinking":false}' it fails to run. Here is the log: WARNING 05-01 19:13:17 [argparse_utils.py:257] With `vllm serve`, you should provide the model as a positional argument or in a config file instead of via the `--model` option. The `--model` option will be removed in a future version. (APIServer pid=1) INFO 05-01 19:13:17 [utils.py:299] (APIServer pid=1) INFO 05-01 19:13:17 [utils.py:299] █ █ █▄ ▄█ (APIServer pid=1) INFO 05-01 19:13:17 [utils.py:299] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.20.0 (APIServer pid=1) INFO 05-01 19:13:17 [utils.py:299] █▄█▀ █ █ █ █ model hesamation/Qwen3.6-35B-A3B-Claude-4.6-Opus-Reasoning...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: bug ### Your current environment ### 🐛 Describe the bug When I run docker with follow cmd: docker run -d \ --name vllm \ --gpus all \ --ipc=host \ --shm-size=16g \ -e NCCL_P2P_DISABLE=0 \ -e NCCL_IB_DISABLE=1 \ -e VLLM_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: model with GGUF quant type failed to run bug ### Your current environment ### 🐛 Describe the bug When I run docker with follow cmd: docker run -d \ --name vllm \ --gpus all \ --ipc=host \ --shm-size=
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: model with GGUF quant type failed to run bug ### Your current environment ### 🐛 Describe the bug When I run docker with follow cmd: docker run -d \ --name vllm \ --gpus all \ --ipc=host \ --shm-size=16g \ -e NCCL
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: lm/entrypoints/cli/main.py", line 92, in main (APIServer pid=1) args.dispatch_function(args) (APIServer pid=1) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/serve.py", line 122, in cmd (APIServer pi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ven ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
