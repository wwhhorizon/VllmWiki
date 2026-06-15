# vllm-project/vllm#10643: [Bug]: GPU Memory Accounting Issue with Multiple vLLM Instances

| 字段 | 值 |
| --- | --- |
| Issue | [#10643](https://github.com/vllm-project/vllm/issues/10643) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support |
| 子分类 |  |
| Operator 关键词 | cache;cuda |
| 症状 | mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GPU Memory Accounting Issue with Multiple vLLM Instances

### Issue 正文摘录

### Your current environment ### Model Input Dumps docker run --rm --gpus all \ -p 8000:8000 \ --ipc=host \ -v /llm-store/Llama-3.1-8B-Instruct:/model \ --name vllm-llama \ vllm-nvidia:latest \ --host 0.0.0.0 \ --port 8000 \ --gpu-memory-utilization 0.3 \ --enable_chunked_prefill True \ --enable_prefix_caching \ --max_model_len 16384 \ --max-num-batched-tokens 2048 \ --max_seq_len_to_capture 16384 \ --model /model \ docker run --rm --gpus all \ -p 8001:8000 \ --ipc=host \ -v /llm-store/Qwen2.5-7B-Instruct:/model \ --name vllm-qwen \ vllm-nvidia:latest \ --host 0.0.0.0 \ --port 8000 \ --gpu-memory-utilization 0.3 \ --enable_chunked_prefill True \ --enable_prefix_caching \ --max_model_len 16384 \ --max-num-batched-tokens 2048 \ --max_seq_len_to_capture 16384 \ --model /model \ ### 🐛 Describe the bug When running multiple vLLM instances on the same GPU, the second instance fails to start due to incorrect GPU memory accounting. The second instance appears to include the first instance's memory usage in its calculations, leading to a negative KV cache size and initialization failure. Note: this setup was working fine in version 0.6.3.post1 **First Instance (Works correctly)** ``` Loadi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: LM Instances bug ### Your current environment ### Model Input Dumps docker run --rm --gpus all \ -p 8000:8000 \ --ipc=host \ -v /llm-store/Llama-3.1-8B-Instruct:/model \ --name vllm-llama \ vllm-nvidia:latest \ --host 0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Bug]: GPU Memory Accounting Issue with Multiple vLLM Instances bug ### Your current environment ### Model Input Dumps docker run --rm --gpus all \ -p 8000:8000 \ --ipc=host \ -v /llm-store/Llama-3.1-8B-Instruct:/
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ue with Multiple vLLM Instances bug ### Your current environment ### Model Input Dumps docker run --rm --gpus all \ -p 8000:8000 \ --ipc=host \ -v /llm-store/Llama-3.1-8B-Instruct:/model \ --name vllm-llama \ vllm-nvidi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: Llama-3.1-8B-Instruct:/model \ --name vllm-llama \ vllm-nvidia:latest \ --host 0.0.0.0 \ --port 8000 \ --gpu-memory-utilization 0.3 \ --enable_chunked_prefill True \ --enable_prefix_caching \ --max_model_len 16384 \ --m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
