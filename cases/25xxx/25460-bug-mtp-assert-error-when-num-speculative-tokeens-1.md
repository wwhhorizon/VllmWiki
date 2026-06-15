# vllm-project/vllm#25460: [Bug]: MTP assert error when num_speculative_tokeens > 1

| 字段 | 值 |
| --- | --- |
| Issue | [#25460](https://github.com/vllm-project/vllm/issues/25460) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: MTP assert error when num_speculative_tokeens > 1

### Issue 正文摘录

### Your current environment vllm serve ${MODEL_PATH} \ --trust-remote-code \ --block-size 64 \ --served-model-name deepseek-r1 \ --max-model-len 32184 \ --max-num-seqs 64 \ --gpu-memory-utilization 0.9 \ -tp 8 \ --max-num-batched-tokens 32184 \ --enable-chunked-prefill \ --no-enable-prefix-caching \ --port 8300 \ --load-format "auto" \ --speculative_config '{"num_speculative_tokens":2,"method":"deepseek_mtp"}' ```text By default, DeepSeek use FlashMLA backend, but MTP>1 only support FlashAttn backend. If change FlashMLA to FlashAttn, there are other bugs for MTP > 1. ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ulative_tokeens > 1 bug;stale ### Your current environment vllm serve ${MODEL_PATH} \ --trust-remote-code \ --block-size 64 \ --served-model-name deepseek-r1 \ --max-model-len 32184 \ --max-num-seqs 64 \ --gpu-memory-ut...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: MTP assert error when num_speculative_tokeens > 1 bug;stale ### Your current environment vllm serve ${MODEL_PATH} \ --trust-remote-code \ --block-size 64 \ --served-model-name deepseek-r1 \ --max-model-len 32184...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ":2,"method":"deepseek_mtp"}' ```text By default, DeepSeek use FlashMLA backend, but MTP>1 only support FlashAttn backend. If change FlashMLA to FlashAttn, there are other bugs for MTP > 1. ```
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: environment vllm serve ${MODEL_PATH} \ --trust-remote-code \ --block-size 64 \ --served-model-name deepseek-r1 \ --max-model-len 32184 \ --max-num-seqs 64 \ --gpu-memory-utilization 0.9 \ -tp 8 \ --max-num-batched-token...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
