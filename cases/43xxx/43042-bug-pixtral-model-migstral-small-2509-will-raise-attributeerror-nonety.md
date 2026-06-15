# vllm-project/vllm#43042: [Bug]: Pixtral model(Migstral-Small-2509) will raise AttributeError NoneType Size on graph mode. Eager mode is ok

| 字段 | 值 |
| --- | --- |
| Issue | [#43042](https://github.com/vllm-project/vllm/issues/43042) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Pixtral model(Migstral-Small-2509) will raise AttributeError NoneType Size on graph mode. Eager mode is ok

### Issue 正文摘录

### Your current environment vllm service startup config: vllm serve {model_path} \ --served-model-name "Magistral-Small-2509" \ --load_format mistral --tool-call-parser mistral \ --tokenizer_mode mistral --config_format mistral \ --enable-auto-tool-choice \ --trust-remote-code \ --reasoning-parser mistral \ --limit-mm-per-prompt '{"image":0}' \ --host 0.0.0.0 \ --port 8010 \ --data-parallel-size 1 \ --tensor-parallel-size 4 \ --max-model-len 32768 \ --max-num-batched-tokens 8192 \ --max-num-seqs 16 \ --gpu-memory-utilization 0.94 \ --async-scheduling \ --mm-processor-cache-gb 0 \ --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY","cudagraph_capture_sizes":[1,2,4,8,16]}' \ --additional-config '{"enable_cpu_binding":true, "multistream_overlap_shared_expert": true}' \ #--enforce-eager while on `--enforce-eager` vllm serve start successful and infer successful. But `FULL_DECODE_ONLY` mode will failed! ### 🐛 Describe the bug WorkerProc hit an exception. (Worker_TP0 pid=2019) ERROR 05-12 09:17:24 [multiproc_executor.py:932] Traceback (most recent call last): (Worker_TP0 pid=2019) ERROR 05-12 09:17:24 [multiproc_executor.py:932] File "/usr/local/python3.11.10/lib/python3.11/site...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Pixtral model(Migstral-Small-2509) will raise AttributeError NoneType Size on graph mode. Eager mode is ok bug ### Your current environment vllm service startup config: vllm serve {model_path} \ --served-model-na...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Pixtral model(Migstral-Small-2509) will raise AttributeError NoneType Size on graph mode. Eager mode is ok bug ### Your current environment vllm service startup config: vllm serve {model_path} \ --served-model-na...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: rocessor-cache-gb 0 \ --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY","cudagraph_capture_sizes":[1,2,4,8,16]}' \ --additional-config '{"enable_cpu_binding":true, "multistream_overlap_shared_expert": true}' \...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ile "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/_dynamo/eval_frame.py", line 1044, in _fn (Worker_TP1 pid=2020) ERROR 05-12 09:17:24 [multiproc_executor.py:932] File "/usr/local/python3.11.10/lib/python...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: d=2019) ERROR 05-12 09:17:24 [multiproc_executor.py:932] return TorchCompileWithNoGuardsWrapper.__call__(self, *args, **kwargs) # type: ignore[arg-type] (Worker_TP1 pid=2020) ERROR 05-12 09:17:24 [multiproc_executor.py:...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
