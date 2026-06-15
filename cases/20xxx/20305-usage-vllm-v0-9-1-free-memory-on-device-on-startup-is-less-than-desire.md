# vllm-project/vllm#20305: [Usage]: vLLM v0.9.1 Free Memory on device on startup is less than desired GPU memory utilization

| 字段 | 值 |
| --- | --- |
| Issue | [#20305](https://github.com/vllm-project/vllm/issues/20305) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: vLLM v0.9.1 Free Memory on device on startup is less than desired GPU memory utilization

### Issue 正文摘录

### Your current environment ```text ``` ### How would you like to use vllm I created a container with these arguments by using vLLM v0.9.1 by usnig Dockerode. ```text --gpus all \ --ipc=host \ -p 8000:8000 \ -v /home/openzeka/.cache/huggingface:/root/.cache/huggingface:rw \ -e HF_TOKEN= \ vllm/vllm-openai:v0.9.1 \ --max-model-len 1024 \ --gpu-memory-utilization 0.95 \ --max-num-seqs 1 \ --tensor-parallel-size 2 \ --model deepseek-ai/DeepSeek-R1-Distill-Llama-8B ``` But after that I got an error like. My GPUs are free to use. ```text [multiproc_executor.py:492] ValueError: Free memory on device (31.44/47.38 GiB) on startup is less than desired GPU memory utilization (0.95, 45.01 GiB). Decrease GPU memory utilization or reduce GPU memory used by other processes. ERROR 06-30 13:53:19 [core.py:515] EngineCore failed to start. ERROR 06-30 13:53:19 [core.py:515] Traceback (most recent call last): ERROR 06-30 13:53:19 [core.py:515] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 506, in run_engine_core ERROR 06-30 13:53:19 [core.py:515] engine_core = EngineCoreProc(*args, **kwargs) ERROR 06-30 13:53:19 [core.py:515] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 06-30...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: --gpus all \ --ipc=host \ -p 8000:8000 \ -v /home/openzeka/.cache/huggingface:/root/.cache/huggingface:rw \ -e HF_TOKEN= \ vllm/vllm-openai:v0.9.1 \ --max-model-len 1024 \ --gpu-memory-utilization 0.95 \ --max-num-seqs...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: I created a container with these arguments by using vLLM v0.9.1 by usnig Dockerode. ```text --gpus all \ --ipc=host \ -p 8000:8000 \ -v /home/openzeka/.cache/huggingface:/root/.cache/huggingface:rw \ -e HF_TOKEN= \ vllm...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: sage]: vLLM v0.9.1 Free Memory on device on startup is less than desired GPU memory utilization usage ### Your current environment ```text ``` ### How would you like to use vllm I created a container with these argument...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
