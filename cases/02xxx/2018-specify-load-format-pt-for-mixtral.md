# vllm-project/vllm#2018: Specify `--load-format pt` for Mixtral

| 字段 | 值 |
| --- | --- |
| Issue | [#2018](https://github.com/vllm-project/vllm/issues/2018) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Specify `--load-format pt` for Mixtral

### Issue 正文摘录

As explained [here](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1/discussions/3), HF pushed some changes to the official repo to make it compatible with `transformers==4.36.0.dev0`. Need to double check that this does not break vLLM integration (in particular, we don't want to load weights twice, and model name changed from `mistral` to `mixtral`). https://github.com/vllm-project/vllm/blob/b5f882cc98e2c9c6dde7357dbac2ec0c2c57d8cd/requirements.txt#L10C20-L10C20

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Specify `--load-format pt` for Mixtral As explained [here](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1/discussions/3), HF pushed some changes to the official repo to make it compatible with `transformers==4.36.0....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Specify `--load-format pt` for Mixtral As explained [here](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1/discussions/3), HF pushed some changes to the official repo to make it compatible with `transformers==4.36.0....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
