# vllm-project/vllm#7857: [Doc]: Why does the GPU utilization fluctuate so much?

| 字段 | 值 |
| --- | --- |
| Issue | [#7857](https://github.com/vllm-project/vllm/issues/7857) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Why does the GPU utilization fluctuate so much?

### Issue 正文摘录

### 📚 The doc issue I'm using 8 A100 GPUs with 40GB each to deploy LLaMA 3 70B. Under high concurrency, the average GPU utilization is only 50%. Here are my launch parameters. '''CUDA_VISIBLE_DEVICES={gpu} RAY_memory_monitor_refresh_ms=0 \ python3 -u -m vllm.entrypoints.api_server --trust-remote-code \ --gpu-memory-utilization 0.98 \ --dtype float16 \ --enforce-eager \ --swap-space 16 --disable-log-requests --host 0.0.0.0 --port {port} --max-num-seqs 512 -tp {tp} --max-model-len 8192\ --model {model_path} ''' ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: zation fluctuate so much? documentation ### 📚 The doc issue I'm using 8 A100 GPUs with 40GB each to deploy LLaMA 3 70B. Under high concurrency, the average GPU utilization is only 50%. Here are my launch parameters. '''...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: i_server --trust-remote-code \ --gpu-memory-utilization 0.98 \ --dtype float16 \ --enforce-eager \ --swap-space 16 --disable-log-requests --host 0.0.0.0 --port {port} --max-num-seqs 512 -tp {tp} --max-model-len 8192\ --...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: tion ### 📚 The doc issue I'm using 8 A100 GPUs with 40GB each to deploy LLaMA 3 70B. Under high concurrency, the average GPU utilization is only 50%. Here are my launch parameters. '''CUDA_VISIBLE_DEVICES={gpu} RAY_memo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: -dtype float16 \ --enforce-eager \ --swap-space 16 --disable-log-requests --host 0.0.0.0 --port {port} --max-num-seqs 512 -tp {tp} --max-model-len 8192\ --model {model_path} ''' ### Suggest a potential alternative/fix _...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
