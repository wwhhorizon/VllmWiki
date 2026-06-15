# vllm-project/vllm#23582: [Bug]: vLLM server timeout due to multiprocessing communication error

| 字段 | 值 |
| --- | --- |
| Issue | [#23582](https://github.com/vllm-project/vllm/issues/23582) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;kernel;quantization |
| 症状 | build_error;crash;mismatch;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: vLLM server timeout due to multiprocessing communication error

### Issue 正文摘录

### Your current environment I ran sudo docker pull vllm/vllm-openai:latest ``` sudo docker run -d \ --gpus all \ --name vllm-8b-bf16-b200 \ -p 8000:8000 \ --ipc=host \ -e HF_TOKEN=... \ vllm/vllm-openai:latest \ --model meta-llama/Llama-3.1-8B-Instruct \ --tensor-parallel-size 8 \ --trust-remote-code \ --host 0.0.0.0 \ --port 8000 ``` and tried to perform a sweep across input and output configs using vllm bench serve and ran into below isues ### 🐛 Describe the bug ``` (APIServer pid=1) INFO: 127.0.0.1:42352 - "POST /v1/completions HTTP/1.1" 200 OK (APIServer pid=1) INFO 08-25 12:24:14 [loggers.py:123] Engine 000: Avg prompt throughput: 26298.0 tokens/s, Avg generation throughput: 10103.2 tokens/s, Running: 224 reqs, Waiting: 0 reqs, GPU KV cache usage: 3.2%, Prefix cache hit rate: 6.8% (VllmWorker TP1 pid=406) ERROR 08-25 12:24:17 [multiproc_executor.py:596] WorkerProc hit an exception. (VllmWorker TP1 pid=406) ERROR 08-25 12:24:17 [multiproc_executor.py:596] Traceback (most recent call last): (VllmWorker TP1 pid=406) ERROR 08-25 12:24:17 [multiproc_executor.py:596] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 591, in worker_busy_loo...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #20988 [CI] [Doc]: Add GH Action for auto labeling issues with `rocm` tag

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: Bug]: vLLM server timeout due to multiprocessing communication error bug;stale ### Your current environment I ran sudo docker pull vllm/vllm-openai:latest ``` sudo docker run -d \ --gpus all \ --name vllm-8b-bf16-b200 \...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ommunication error bug;stale ### Your current environment I ran sudo docker pull vllm/vllm-openai:latest ``` sudo docker run -d \ --gpus all \ --name vllm-8b-bf16-b200 \ -p 8000:8000 \ --ipc=host \ -e HF_TOKEN=... \ vll...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: -openai:latest ``` sudo docker run -d \ --gpus all \ --name vllm-8b-bf16-b200 \ -p 8000:8000 \ --ipc=host \ -e HF_TOKEN=... \ vllm/vllm-openai:latest \ --model meta-llama/Llama-3.1-8B-Instruct \ --tensor-parallel-size 8...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ai:latest ``` sudo docker run -d \ --gpus all \ --name vllm-8b-bf16-b200 \ -p 8000:8000 \ --ipc=host \ -e HF_TOKEN=... \ vllm/vllm-openai:latest \ --model meta-llama/Llama-3.1-8B-Instruct \ --tensor-parallel-size 8 \ --...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: all \ --name vllm-8b-bf16-b200 \ -p 8000:8000 \ --ipc=host \ -e HF_TOKEN=... \ vllm/vllm-openai:latest \ --model meta-llama/Llama-3.1-8B-Instruct \ --tensor-parallel-size 8 \ --trust-remote-code \ --host 0.0.0.0 \ --por...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | 53 (0x7fb2379b3253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6) frame #4: <unknown function> + 0x94ac3 (0x7fb2b2602ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6) frame #5: clone + 0x… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | /local/lib/python3.12/dist-packages/torch/lib/libtorch_cuda.so) frame #6: c10d::processgroupnccl::ncclcommwatchdog() + 0x14d (0x7fb247580fdd in /usr/local/lib/python3.12/dist-pack… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | /local/lib/python3.12/dist-packages/torch/lib/libtorch_cuda.so) frame #7: <unknown function> + 0xdc253 (0x7fb2379b3253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6) frame #8: <unkn… |
| [#20988](https://github.com/vllm-project/vllm/pull/20988) | mentioned | 0.6 | [CI] [Doc]: Add GH Action for auto labeling issues with `rocm` tag | 23. #23587: [Bug]: NIXL Crashes if P/D Protocol is off... [bug] 24. #23582: [Bug]: vLLM server timeout due to multiprocessing communicat... [bug] 25. #23581: [Installation]:... [i… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
