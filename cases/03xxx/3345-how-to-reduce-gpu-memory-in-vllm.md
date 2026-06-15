# vllm-project/vllm#3345: how to reduce gpu memory in vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#3345](https://github.com/vllm-project/vllm/issues/3345) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> how to reduce gpu memory in vllm

### Issue 正文摘录

when i run it with: python -m vllm.entrypoints.openai.api_server --model /home/wanghaikuan/code/LLaMA-Factory/qw7bint4 --trust-remote-code --max-model-len 2046 --host 104.171.202.141 --port 8087 --gpu-memory-utilization 0.15 ![image](https://github.com/vllm-project/vllm/assets/17873056/57094c53-c888-44d5-81e6-808eed52c022) i think 7G is enough, in fact, it need 10G almost. Is there any parameters to reduce gpu memory. Thanks!

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: vllm when i run it with: python -m vllm.entrypoints.openai.api_server --model /home/wanghaikuan/code/LLaMA-Factory/qw7bint4 --trust-remote-code --max-model-len 2046 --host 104.171.202.141 --port 8087 --gpu-memory-utiliz...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: oints.openai.api_server --model /home/wanghaikuan/code/LLaMA-Factory/qw7bint4 --trust-remote-code --max-model-len 2046 --host 104.171.202.141 --port 8087 --gpu-memory-utilization 0.15 ![image](https://github.com/vllm-pr...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: how to reduce gpu memory in vllm when i run it with: python -m vllm.entrypoints.openai.api_server --model /home/wanghaikuan/code/LLaMA-Factory/qw7bint4 --trust-remote-code --max-model-len 2046 --host 104.171.202.141 --p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
