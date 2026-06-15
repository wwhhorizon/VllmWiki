# vllm-project/vllm#27256: [Bug]: Qwen3-Embedding-0.6B三种请求方式，数值结果都不一致

| 字段 | 值 |
| --- | --- |
| Issue | [#27256](https://github.com/vllm-project/vllm/issues/27256) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3-Embedding-0.6B三种请求方式，数值结果都不一致

### Issue 正文摘录

### Your current environment vllm=0.9.2 ### 🐛 Describe the bug vllm serve方式启动： `CUDA_VISIBLE_DEVICES=1 vllm serve */Qwen/Qwen3-Embedding-0___6B \ --task embedding \ --host 0.0.0.0 \ --port 8002 \ --dtype auto \ --gpu-memory-utilization 0.2 \ --max-num-seqs 8 \ --max-model-len 8192 \ --trust-remote-code` vllm本地加载： ```python LLM(model=model_path, task="embed", gpu_memory_utilization=0.8, max_model_len=8192, enforce_eager=is_debug) ``` qwen3-embedding原生transformers加载模型方式： ```python AutoModel.from_pretrained(model_path, device_map="auto").eval() ``` 上面三种方式加载向量化模型，输入如下语句，向量化结果不同，这是什么原因？ ![Image](https://github.com/user-attachments/assets/bf768779-e0dd-4439-93ef-81f7e9c1ed82) ![Image](https://github.com/user-attachments/assets/e90286e7-1358-4f94-a0a9-f309eb80522c) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: urrent environment vllm=0.9.2 ### 🐛 Describe the bug vllm serve方式启动： `CUDA_VISIBLE_DEVICES=1 vllm serve */Qwen/Qwen3-Embedding-0___6B \ --task embedding \ --host 0.0.0.0 \ --port 8002 \ --dtype auto \ --gpu-memory-utili...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen3-Embedding-0.6B三种请求方式，数值结果都不一致 bug;stale ### Your current environment vllm=0.9.2 ### 🐛 Describe the bug vllm serve方式启动： `CUDA_VISIBLE_DEVICES=1 vllm serve */Qwen/Qwen3-Embedding-0___6B \ --task embedding \ --
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: 模型方式： ```python AutoModel.from_pretrained(model_path, device_map="auto").eval() ``` 上面三种方式加载向量化模型，输入如下语句，向量化结果不同，这是什么原因？ ![Image](https://github.com/user-attachments/assets/bf768779-e0dd-4439-93ef-81f7e9c1ed82) ![Image]...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ing-0___6B \ --task embedding \ --host 0.0.0.0 \ --port 8002 \ --dtype auto \ --gpu-memory-utilization 0.2 \ --max-num-seqs 8 \ --max-model-len 8192 \ --trust-remote-code` vllm本地加载： ```python LLM(model=model_path, task=...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Qwen3-Embedding-0.6B三种请求方式，数值结果都不一致 bug;stale ### Your current environment vllm=0.9.2 ### 🐛 Describe the bug vllm serve方式启动： `CUDA_VISIBLE_DEVICES=1 vllm serve */Qwen/Qwen3-Embedding-0___6B \ --task embedding \ -...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
