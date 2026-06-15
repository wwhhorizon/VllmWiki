# vllm-project/vllm#7979: [Bug]: run gguf ，the gguf model is only 800M, but why does the GPU memory usage exceed 20G?

| 字段 | 值 |
| --- | --- |
| Issue | [#7979](https://github.com/vllm-project/vllm/issues/7979) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: run gguf ，the gguf model is only 800M, but why does the GPU memory usage exceed 20G?

### Issue 正文摘录

### Your current environment 0.5.5 vllm ### 🐛 Describe the bug CUDA_VISIBLE_DEVICES=1 vllm serve /ai/qwen1.5-1.8b.gguf --host 0.0.0.0 --port 10868 --max-model-len 4096 --trust-remote-code --tensor-parallel-size 1 --dtype=half --quantization gguf --load-format gguf ![image](https://github.com/user-attachments/assets/99f3e7d2-fd15-4afd-b478-cb3458fd8336) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: run gguf ，the gguf model is only 800M, but why does the GPU memory usage exceed 20G? bug ### Your current environment 0.5.5 vllm ### 🐛 Describe the bug CUDA_VISIBLE_DEVICES=1 vllm serve /ai/qwen1.5-1.8b.gguf --ho...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: 8 --max-model-len 4096 --trust-remote-code --tensor-parallel-size 1 --dtype=half --quantization gguf --load-format gguf ![image](https://github.com/user-attachments/assets/99f3e7d2-fd15-4afd-b478-cb3458fd8336) ### Befor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ? bug ### Your current environment 0.5.5 vllm ### 🐛 Describe the bug CUDA_VISIBLE_DEVICES=1 vllm serve /ai/qwen1.5-1.8b.gguf --host 0.0.0.0 --port 10868 --max-model-len 4096 --trust-remote-code --tensor-parallel-size 1...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]: run gguf ，the gguf model is only 800M, but why does the GPU memory usage exceed 20G? bug ### Your current environment 0.5.5 vllm ### 🐛 Describe the bug CUDA_VISIBLE_DEVICES=1 vllm serve /ai/qwen1.5-1.8b.gguf --ho...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
