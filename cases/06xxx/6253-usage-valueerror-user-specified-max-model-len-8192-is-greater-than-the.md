# vllm-project/vllm#6253: [Usage]: ValueError: User-specified max_model_len (8192) is greater than the derived max_model_len (sliding_window=4096 or model_max_length=None in model's config.json).

| 字段 | 值 |
| --- | --- |
| Issue | [#6253](https://github.com/vllm-project/vllm/issues/6253) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: ValueError: User-specified max_model_len (8192) is greater than the derived max_model_len (sliding_window=4096 or model_max_length=None in model's config.json).

### Issue 正文摘录

### Your current environment ```text python -m vllm.entrypoints.openai.api_server --model Vigostral-7B-Chat-AWQ --served-model-name Vigostral-7B-Chat-AWQ --max-model-len 8192 --quantization awq --enable-prefix-caching --disable-sliding-window ``` ### How would you like to use vllm I want to launch vllm with Vigostral 7B Chat AWQ by enabling prefix caching. I have to disable at the same time disabling sliding windows to enable prefix caching. This leads to a restriction for the setting of the max model len value, which equals to the default sliding window value, according to this line of code https://github.com/vllm-project/vllm/blob/5d5b4c5fe524c3b62453bba7ad4434a27c81317a/vllm/config.py#L1392 Is it possible to increase max model len above default sliding windows value when enabling prefix caching? Many thanks for your help

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: ValueError: User-specified max_model_len (8192) is greater than the derived max_model_len (sliding_window=4096 or model_max_length=None in model's config.json). usage;stale ### Your current environment ```text...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Usage]: ValueError: User-specified max_model_len (8192) is greater than the derived max_model_len (sliding_window=4096 or model_max_length=None in model's config.json). usage;stale ### Your current environment ```text...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: hat-AWQ --served-model-name Vigostral-7B-Chat-AWQ --max-model-len 8192 --quantization awq --enable-prefix-caching --disable-sliding-window ``` ### How would you like to use vllm I want to launch vllm with Vigostral 7B C...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ding_window=4096 or model_max_length=None in model's config.json). usage;stale ### Your current environment ```text python -m vllm.entrypoints.openai.api_server --model Vigostral-7B-Chat-AWQ --served-model-name Vigostra...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
