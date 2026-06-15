# vllm-project/vllm#250: Multi-GPU inference and Specify which GPUs to be used during inference

| 字段 | 值 |
| --- | --- |
| Issue | [#250](https://github.com/vllm-project/vllm/issues/250) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Multi-GPU inference and Specify which GPUs to be used during inference

### Issue 正文摘录

I have two questions: 1. I attempted multi-GPU inference (8 GPU inference on A100) on Llama-13B. I followed the steps described in [https://github.com/vllm-project/vllm/issues/188], first running `$ ray start --head` and then `llm = LLM(model= , tensor_parallel_size=8)`. However, I got the following error: (Worker pid=1027546) AssertionError: 32001 is not divisible by 8 [repeated 7x across cluster] Is there any way to resolve this issue? 3. Additionally, is there a way to specify which GPUs are used during inference? I tried using `os.environ["CUDA_VISIBLE_DEVICES"]="2"` but it doesn't seem to work - it continues to use the first GPU. Thanks!

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e two questions: 1. I attempted multi-GPU inference (8 GPU inference on A100) on Llama-13B. I followed the steps described in [https://github.com/vllm-project/vllm/issues/188], first running `$ ray start --head` and the...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: stions: 1. I attempted multi-GPU inference (8 GPU inference on A100) on Llama-13B. I followed the steps described in [https://github.com/vllm-project/vllm/issues/188], first running `$ ray start --head` and then `llm =...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Multi-GPU inference and Specify which GPUs to be used during inference I have two questions: 1. I attempted multi-GPU inference (8 GPU inference on A100) on Llama-13B. I followed the steps described in [https://github.c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
