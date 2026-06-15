# vllm-project/vllm#1281: run openai/api_server.py ，load Qwen-7B， AttributeError: 'ModelConfig' object has no attribute 'get_max_model_len'

| 字段 | 值 |
| --- | --- |
| Issue | [#1281](https://github.com/vllm-project/vllm/issues/1281) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> run openai/api_server.py ，load Qwen-7B， AttributeError: 'ModelConfig' object has no attribute 'get_max_model_len'

### Issue 正文摘录

CUDA_VISIBLE_DEVICES=2 python openai/api_server.py --host 0.0.0.0 --port 35300 --model /data/model/Qwen-7B-Chat --trust-remote-code --gpu-memory-utilization 0.8 --served-model-name qwen --max-num-batched-tokens 8192 ![image](https://github.com/vllm-project/vllm/assets/42534237/68e1de3e-7653-4358-9427-71c165e65b4c) vllm 0.2.0 NVIDIA A40 use vllm 0.1.7，no problem。What should I do？

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: run openai/api_server.py ，load Qwen-7B， AttributeError: 'ModelConfig' object has no attribute 'get_max_model_len' CUDA_VISIBLE_DEVICES=2 python openai/api_server.py --host 0.0.0.0 --port 35300 --model /data/model/Qwen-7...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ttributeError: 'ModelConfig' object has no attribute 'get_max_model_len' CUDA_VISIBLE_DEVICES=2 python openai/api_server.py --host 0.0.0.0 --port 35300 --model /data/model/Qwen-7B-Chat --trust-remote-code --gpu-memory-u...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
