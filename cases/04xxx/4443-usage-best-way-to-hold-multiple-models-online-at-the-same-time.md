# vllm-project/vllm#4443: [Usage]: best way to hold multiple models online at the same time?

| 字段 | 值 |
| --- | --- |
| Issue | [#4443](https://github.com/vllm-project/vllm/issues/4443) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: best way to hold multiple models online at the same time?

### Issue 正文摘录

### Your current environment Hi, I'm using vllm and I want to hold two models at the same time. Currently what I am doing is this: CUDA_VISIBLE_DEVICES=1 python -O -u -m vllm.entrypoints.openai.api_server --host=0.0.0.0 --port=8001 --model=/home/jack/model_product/model_20240424 --tokenizer=/home/jack/model_product/model_20240424 --served-model-name=test >/var/log/test.log CUDA_VISIBLE_DEVICES=0 python -O -u -m vllm.entrypoints.openai.api_server --host=0.0.0.0 --port=8000 --model=/home/jack/model_product/model_20240425 --tokenizer=/home/jack/model_product/model_20240425 --served-model-name=test >/var/log/test.log Would this be less efficient since it is running two vllm servers? Could anyone gives me some suggestion on what would be the best practice for holding multiple models at the same time ? ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 0425 --served-model-name=test >/var/log/test.log Would this be less efficient since it is running two vllm servers? Could anyone gives me some suggestion on what would be the best practice for holding multiple models at...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: to hold two models at the same time. Currently what I am doing is this: CUDA_VISIBLE_DEVICES=1 python -O -u -m vllm.entrypoints.openai.api_server --host=0.0.0.0 --port=8001 --model=/home/jack/model_product/model_2024042...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: best way to hold multiple models online at the same time? usage ### Your current environment Hi, I'm using vllm and I want to hold two models at the same time. Currently what I am doing is this: CUDA_VISIBLE_DE...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: --tokenizer=/home/jack/model_product/model_20240424 --served-model-name=test >/var/log/test.log CUDA_VISIBLE_DEVICES=0 python -O -u -m vllm.entrypoints.openai.api_server --host=0.0.0.0 --port=8000 --model=/home/jack/mod...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
