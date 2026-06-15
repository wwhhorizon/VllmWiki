# vllm-project/vllm#11760: [Misc]: Very High GPU RX/TX using vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#11760](https://github.com/vllm-project/vllm/issues/11760) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Very High GPU RX/TX using vllm

### Issue 正文摘录

### Anything you want to discuss about vllm. I found there are very big size of data transfer to GPU when making a request with 10K tokens. VLLM result a very high TTFT compare to Ollama. I dont think it is a normal data size of 10K tokens. vllm version: v0.6.4.post1 There is how I run vllm ` vllm serve Qwen/Qwen2.5-32B-Instruct-AWQ --pipeline-parallel-size 2 --enable-auto-tool-choice --tool-call-parser hermes --gpu-memory-utilization 0.9 --max_model_len 32000 --max-num-seqs 5 --kv-cache-dtype fp8_e4m3 ` There is my GPU receiving data (over 10GiB/s RX) ![image](https://github.com/user-attachments/assets/87de1545-f7c6-4375-af9e-f99e51ac45f5) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ing a request with 10K tokens. VLLM result a very high TTFT compare to Ollama. I dont think it is a normal data size of 10K tokens. vllm version: v0.6.4.post1 There is how I run vllm ` vllm serve Qwen/Qwen2.5-32B-Instru...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: emory-utilization 0.9 --max_model_len 32000 --max-num-seqs 5 --kv-cache-dtype fp8_e4m3 ` There is my GPU receiving data (over 10GiB/s RX) ![image](https://github.com/user-attachments/assets/87de1545-f7c6-4375-af9e-f99e5...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Misc]: Very High GPU RX/TX using vllm stale ### Anything you want to discuss about vllm. I found there are very big size of data transfer to GPU when making a request with 10K tokens. VLLM result a very high TTFT compa...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: to Ollama. I dont think it is a normal data size of 10K tokens. vllm version: v0.6.4.post1 There is how I run vllm ` vllm serve Qwen/Qwen2.5-32B-Instruct-AWQ --pipeline-parallel-size 2 --enable-auto-tool-choice --tool-c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: f5) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
