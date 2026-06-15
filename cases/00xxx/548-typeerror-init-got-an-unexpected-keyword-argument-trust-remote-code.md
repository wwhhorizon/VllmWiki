# vllm-project/vllm#548: TypeError: __init__() got an unexpected keyword argument 'trust_remote_code'

| 字段 | 值 |
| --- | --- |
| Issue | [#548](https://github.com/vllm-project/vllm/issues/548) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> TypeError: __init__() got an unexpected keyword argument 'trust_remote_code'

### Issue 正文摘录

I was trying to run benchmark_latency.py but failed. ``` root@99e5b0a5543d:~/share/vllm/benchmarks# python benchmark_latency.py Namespace(batch_size=8, input_len=32, model='facebook/opt-125m', n=1, num_iters=3, output_len=128, tensor_parallel_size=1, tokenizer=None, trust_remote_code=False, use_beam_search=False) Traceback (most recent call last): File "benchmark_latency.py", line 81, in main(args) File "benchmark_latency.py", line 18, in main llm = LLM( File "/usr/local/lib/python3.8/dist-packages/vllm/entrypoints/llm.py", line 53, in __init__ engine_args = EngineArgs( TypeError: __init__() got an unexpected keyword argument 'trust_remote_code' ```

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: t an unexpected keyword argument 'trust_remote_code' I was trying to run benchmark_latency.py but failed. ``` root@99e5b0a5543d:~/share/vllm/benchmarks# python benchmark_latency.py Namespace(batch_size=8, input_len=32,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: sor_parallel_size=1, tokenizer=None, trust_remote_code=False, use_beam_search=False) Traceback (most recent call last): File "benchmark_latency.py", line 81, in main(args) File "benchmark_latency.py", line 18, in main l...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: put_len=128, tensor_parallel_size=1, tokenizer=None, trust_remote_code=False, use_beam_search=False) Traceback (most recent call last): File "benchmark_latency.py", line 81, in main(args) File "benchmark_latency.py", li...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: arks# python benchmark_latency.py Namespace(batch_size=8, input_len=32, model='facebook/opt-125m', n=1, num_iters=3, output_len=128, tensor_parallel_size=1, tokenizer=None, trust_remote_code=False, use_beam_search=False...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
