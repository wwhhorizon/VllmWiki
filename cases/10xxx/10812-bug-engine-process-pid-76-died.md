# vllm-project/vllm#10812: [Bug]: Engine process (pid 76) died

| 字段 | 值 |
| --- | --- |
| Issue | [#10812](https://github.com/vllm-project/vllm/issues/10812) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Engine process (pid 76) died

### Issue 正文摘录

### Your current environment Engine args on v0.6.4.post1. This happens with/without num scheduler steps setting. "--tensor-parallel-size", "8", "--enable-chunked-prefill", "false", "--enable-prefix-caching", "--num-scheduler-steps", "8", ### Model Input Dumps _No response_ ### 🐛 Describe the bug Upon serving a fp8 model on 8xH100s, it seems like every so often (sometimes every few hours, sometimes sooner) it would crash with this error message: ERROR 12-01 13:05:02 client.py:282] RuntimeError('Engine process (pid 76) died.') ERROR 12-01 13:05:02 client.py:282] NoneType: None CRITICAL 12-01 13:05:02 launcher.py:99] MQLLMEngine is already dead, terminating server process INFO: [10.42.0.118:60606](http://10.42.0.118:60606/) - "POST /v1/completions HTTP/1.1" 500 Internal Server Error INFO: Shutting down INFO: Waiting for connections to close. (CTRL+C to force quit) Engine args on v0.6.4.post1. This happens with/without num scheduler steps setting. "--tensor-parallel-size", "8", "--enable-chunked-prefill", "false", "--enable-prefix-caching", "--num-scheduler-steps", "8", ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Engine process (pid 76) died bug;stale ### Your current environment Engine args on v0.6.4.post1. This happens with/without num scheduler steps setting. "--tensor-parallel-size", "8", "--enable-chunked-prefill",
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ps _No response_ ### 🐛 Describe the bug Upon serving a fp8 model on 8xH100s, it seems like every so often (sometimes every few hours, sometimes sooner) it would crash with this error message: ERROR 12-01 13:05:02 client...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: Model Input Dumps _No response_ ### 🐛 Describe the bug Upon serving a fp8 model on 8xH100s, it seems like every so often (sometimes every few hours, sometimes sooner) it would crash with this error message: ERROR 12-01...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: "8", "--enable-chunked-prefill", "false", "--enable-prefix-caching", "--num-scheduler-steps", "8", ### Model Input Dumps _No response_ ### 🐛 Describe the bug Upon serving a fp8 model on 8xH100s, it seems like e
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: caching", "--num-scheduler-steps", "8", ### Model Input Dumps _No response_ ### 🐛 Describe the bug Upon serving a fp8 model on 8xH100s, it seems like every so often (sometimes every few hours, sometimes sooner) it would...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
