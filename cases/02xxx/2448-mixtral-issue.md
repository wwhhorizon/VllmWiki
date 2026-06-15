# vllm-project/vllm#2448: Mixtral issue

| 字段 | 值 |
| --- | --- |
| Issue | [#2448](https://github.com/vllm-project/vllm/issues/2448) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Mixtral issue

### Issue 正文摘录

vllm version 0.2.7 python -u -m vllm.entrypoints.openai.api_server \ --host 0.0.0.0 \ --port 8008 \ --model /data2/public_file2/LLM_model/Mixtral-8x7B-Instruct-v0.1 \ --tensor-parallel-size 8 \ --load-format pt ValueError: Currently, the 'pt' format is not supported for Mixtral. Please use the 'safetensors' format instead.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: penai.api_server \ --host 0.0.0.0 \ --port 8008 \ --model /data2/public_file2/LLM_model/Mixtral-8x7B-Instruct-v0.1 \ --tensor-parallel-size 8 \ --load-format pt ValueError: Currently, the 'pt' format is not supported fo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Mixtral issue vllm version 0.2.7 python -u -m vllm.entrypoints.openai.api_server \ --host 0.0.0.0 \ --port 8008 \ --model /data2/public_file2/LLM_model/Mixtral-8x7B-Instruct-v0.1 \ --tensor-parallel-size 8 \

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
