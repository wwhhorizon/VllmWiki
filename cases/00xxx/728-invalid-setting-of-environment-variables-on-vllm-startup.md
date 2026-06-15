# vllm-project/vllm#728: Invalid setting of environment variables on vllm startup 

| 字段 | 值 |
| --- | --- |
| Issue | [#728](https://github.com/vllm-project/vllm/issues/728) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Invalid setting of environment variables on vllm startup 

### Issue 正文摘录

command: ``` HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m vllm.entrypoints.openai.api_server --model baichuan-inc/Baichuan-13B-Chat --host 0.0.0.0 --port 1234 --trust-remote-code --dtype half ``` I want to make the model run offline, but setting `HF_DATASETS_OFFLINE = 1 TRANSFORMERS_OFFLINE = 1` is invalid. Besides using --model to set the specified directory, is there any other solution? [Reference HF](https://huggingface.co/docs/transformers/installation#offline-mode:~:text=Run%20this%20same%20program%20in%20an%20offline%20instance%20with%3A) @WoosukKwon @zhuohan123

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Invalid setting of environment variables on vllm startup command: ``` HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m vllm.entrypoints.openai.api_server --model baichuan-inc/Baichuan-13B-Chat --host 0.0.0.0 --por...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: RANSFORMERS_OFFLINE = 1` is invalid. Besides using --model to set the specified directory, is there any other solution? [Reference HF](https://huggingface.co/docs/transformers/installation#offline-mode:~:text=Run%20this...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: n-inc/Baichuan-13B-Chat --host 0.0.0.0 --port 1234 --trust-remote-code --dtype half ``` I want to make the model run offline, but setting `HF_DATASETS_OFFLINE = 1 TRANSFORMERS_OFFLINE = 1` is invalid. Besides using --mo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
