# vllm-project/vllm#6897: [Bug]: Unrecognized keys in `rope_scaling` for 'rope_type'='linear': {'type'}

| 字段 | 值 |
| --- | --- |
| Issue | [#6897](https://github.com/vllm-project/vllm/issues/6897) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Unrecognized keys in `rope_scaling` for 'rope_type'='linear': {'type'}

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug When using vllm 0.5.3 and 0.5.3.post1 to deploy deepseek coder 6.7b, which has a rope_scaling configuration in the config.json, a message appears "Unrecognized keys in `rope_scaling` for 'rope_type'='linear': {'type'}", not sure which script raised it. serve code: /usr/bin/python3 -m vllm.entrypoints.openai.api_server \ --host :: \ --port "${PORT0}" \ --model $SERVER_PATH/"${MODEL_NAME}" \ --served-model-name $SERVED_MODEL_NAME \ --tensor-parallel-size "${GPU_NUM}" \ --tokenizer $SERVER_PATH/"${MODEL_NAME}" \ --max-model-len $MAX_LENGTH \ --gpu-memory-utilization 0.9 \ --speculative-model "[ngram]" \ --ngram-prompt-lookup-max 3 \ --ngram-prompt-lookup-min 1 \ --num-speculative-tokens 5 \ --use-v2-block-manager \ --enable-prefix-caching \ --trust-remote-code \ --dtype auto

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: and 0.5.3.post1 to deploy deepseek coder 6.7b, which has a rope_scaling configuration in the config.json, a message appears "Unrecognized keys in `rope_scaling` for 'rope_type'='linear': {'type'}", not sure which script...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: --enable-prefix-caching \ --trust-remote-code \ --dtype auto
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: mpt-lookup-min 1 \ --num-speculative-tokens 5 \ --use-v2-block-manager \ --enable-prefix-caching \ --trust-remote-code \ --dtype auto
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: model-len $MAX_LENGTH \ --gpu-memory-utilization 0.9 \ --speculative-model "[ngram]" \ --ngram-prompt-lookup-max 3 \ --ngram-prompt-lookup-min 1 \ --num-speculative-tokens 5 \ --use-v2-block-manager \ --enable-prefix-ca...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
