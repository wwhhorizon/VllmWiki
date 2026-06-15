# vllm-project/vllm#14949: [Usage]: Unable to run Phi-4-multimodal-instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#14949](https://github.com/vllm-project/vllm/issues/14949) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Unable to run Phi-4-multimodal-instruct

### Issue 正文摘录

### Your current environment Running VLLM instances on K8S. Instaces with other VL models run succesfully. ### How would you like to use vllm I'm trying to deploy a vLLM image running microsoft/Phi-4-multimodal-instruct: `image: vllm/vllm-openai:latest command: - /bin/sh - '-c' args: - >- vllm serve microsoft/Phi-4-multimodal-instruct --dtype auto --trust-remote-code --gpu-memory-utilization 0.98 --max-model-len 4096 --max-seq-len-to-capture=8192 --enable-lora --max-lora-rank 320 --lora-extra-vocab-size 0 --limit-mm-per-prompt audio=0,image=1 --max-loras 2 --port 8200 ` An error is raised: File "/usr/local/lib/python3.12/dist-packages/vllm/config.py", line 431, in _init_multimodal_config raise ValueError("`limit_mm_per_prompt` is only supported for " ValueError: `limit_mm_per_prompt` is only supported for multimodal models. ERROR 03-17 04:05:57 engine.py:400] `limit_mm_per_prompt` is only supported for multimodal models. Because I've seen other users succesfully running the model, I guess I'm doing something wrong with vLLM arguments. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corn...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: Unable to run Phi-4-multimodal-instruct usage ### Your current environment Running VLLM instances on K8S. Instaces with other VL models run succesfully. ### How would you like to use vllm I'm trying to deploy a...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: - >- vllm serve microsoft/Phi-4-multimodal-instruct --dtype auto --trust-remote-code --gpu-memory-utilization 0.98 --max-model-len 4096 --max-seq-len-to-capture=8192 --enable-lora --max-lora-rank 320 --lora-extra-vocab-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ts. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: running microsoft/Phi-4-multimodal-instruct: `image: vllm/vllm-openai:latest command: - /bin/sh - '-c' args: - >- vllm serve microsoft/Phi-4-multimodal-instruct --dtype auto --trust-remote-code --gpu-memory-utilization...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
