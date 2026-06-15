# vllm-project/vllm#43382: [Bug]: Qwen3.5 397B model occurs assertion error during allocating new blocks

| 字段 | 值 |
| --- | --- |
| Issue | [#43382](https://github.com/vllm-project/vllm/issues/43382) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5 397B model occurs assertion error during allocating new blocks

### Issue 正文摘录

### Your current environment I find this problem in customer‘s code which is base on vllm 0.18.1.dev35+g36ed358b1.empty vllm_ascend 0.1.dev100+gd773192cd It is hard to replicate, i keep the log and try to find what happen in the code. I have some questions: 1、Why mamba don’t need to consider the situation that num_required_blocks ### 🐛 Describe the bug KeyId: [None]. ERROR 2026-05-14 05:25:28.876 [core.py:1123] EngineCore encountered a fatal error. ERROR 2026-05-14 05:25:28.876 [core.py:1123] Traceback (most recent call last): ERROR 2026-05-14 05:25:28.876 [core.py:1123] File "/usr/local/python3.11.14/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 1114, in run_engine_core ERROR 2026-05-14 05:25:28.876 [core.py:1123] engine_core.run_busy_loop() ERROR 2026-05-14 05:25:28.876 [core.py:1123] File "/usr/local/python3.11.14/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 1155, in run_busy_loop ERROR 2026-05-14 05:25:28.876 [core.py:1123] self._process_engine_step() ERROR 2026-05-14 05:25:28.876 [core.py:1123] File "/usr/local/python3.11.14/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 1194, in _process_engine_step ERROR 2026-05-14 05:25:28.876 [core.p...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: 3.11/site-packages/vllm/v1/engine/core.py", line 463, in step_with_batch_queue ERROR 2026-05-14 05:25:28.876 [core.py:1123] scheduler_output = self.scheduler.schedule() ERROR 2026-05-14 05:25:28.876 [core.py:1123] ^^^^^...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen3.5 397B model occurs assertion error during allocating new blocks bug ### Your current environment I find this problem in customer‘s code which is base on vllm 0.18.1.dev35+g36
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [Bug]: Qwen3.5 397B model occurs assertion error during allocating new blocks bug ### Your current environment I find this problem in customer‘s code which is base on vllm 0.18.1.dev35+g36ed358b1.empty vllm_ascend 0.1.d...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: --gpu-memory-utilization 0.90 --compilation-config {"cudagraph_capture_sizes":[4,16,32,64,96,128,160,192,224,256,288,320,352,384,416,448,480,512],"cudagraph_mode":"FULL_DECODE_ONLY"} --speculative-config {"method":"qwen...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: /aicloud/task/otlptrace/otlp/api/v1/traces --token-level-profiling --data-parallel-size 1 --tensor-parallel-size 16 --max-model-len 262144 --max-num-batched-tokens 16384 --max-num-seqs 128

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
