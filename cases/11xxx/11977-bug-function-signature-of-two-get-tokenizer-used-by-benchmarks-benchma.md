# vllm-project/vllm#11977: [Bug]: Function signature of two `get_tokenizer` used by `benchmarks/benchmark_serving.py` is not aligned

| 字段 | 值 |
| --- | --- |
| Issue | [#11977](https://github.com/vllm-project/vllm/issues/11977) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Function signature of two `get_tokenizer` used by `benchmarks/benchmark_serving.py` is not aligned

### Issue 正文摘录

### Your current environment (not related) ### Model Input Dumps _No response_ ### 🐛 Describe the bug Two functions imported by this conditional import has different signature: https://github.com/vllm-project/vllm/blob/d14e98d924724b284dc5eaf8070d935e214e50c0/benchmarks/benchmark_serving.py#L46-L49 https://github.com/vllm-project/vllm/blob/d14e98d924724b284dc5eaf8070d935e214e50c0/vllm/transformers_utils/tokenizer.py#L119-L127 https://github.com/vllm-project/vllm/blob/d14e98d924724b284dc5eaf8070d935e214e50c0/benchmarks/backend_request_func.py#L419-L421 Which cause this error when using benchmark: ```bash (task, pid=5102) Traceback (most recent call last): (task, pid=5102) File "/home/gcpuser/sky_workdir/vllm/benchmarks/benchmark_serving.py", line 1226, in (task, pid=5102) main(args) (task, pid=5102) File "/home/gcpuser/sky_workdir/vllm/benchmarks/benchmark_serving.py", line 793, in main (task, pid=5102) tokenizer = get_tokenizer(tokenizer_id, (task, pid=5102) TypeError: get_tokenizer() got an unexpected keyword argument 'tokenizer_mode' ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: Function signature of two `get_tokenizer` used by `benchmarks/benchmark_serving.py` is not aligned bug ### Your current environment (not related) ### Model Input Dumps _No response_ ### 🐛 Describe the bug Two fun...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: lm-project/vllm/blob/d14e98d924724b284dc5eaf8070d935e214e50c0/benchmarks/backend_request_func.py#L419-L421 Which cause this error when using benchmark: ```bash (task, pid=5102) Traceback (most recent call last): (task,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Model Input Dumps _No response_ ### 🐛 Describe the bug Two functions imported by this conditional import has different signature: https://github.com/vllm-project/vllm/blob/d14e98d924724b284dc5eaf8070d935e214e50c0/benchm...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: .py` is not aligned bug ### Your current environment (not related) ### Model Input Dumps _No response_ ### 🐛 Describe the bug Two functions imported by this conditional import has different signature: https://github.com...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
