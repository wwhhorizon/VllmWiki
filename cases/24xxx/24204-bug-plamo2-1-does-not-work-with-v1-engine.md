# vllm-project/vllm#24204: [Bug]: PLaMo2.1 does not work with v1 engine

| 字段 | 值 |
| --- | --- |
| Issue | [#24204](https://github.com/vllm-project/vllm/issues/24204) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: PLaMo2.1 does not work with v1 engine

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running [PLaMo2.1](https://huggingface.co/pfnet/plamo-2.1-2b-cpt) using the recently introduced v1 support fails: ``` $ VLLM_USE_V1=1 vllm serve pfnet/plamo-2.1-2b-cpt --trust-remote-code --max-model-len 32768 --no-enable-prefix-caching ... (EngineCore_0 pid=2647201) Process EngineCore_0: (EngineCore_0 pid=2647201) Traceback (most recent call last): (EngineCore_0 pid=2647201) File "/scratch/micromamba/contrib-vllm/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap (EngineCore_0 pid=2647201) self.run() (EngineCore_0 pid=2647201) File "/scratch/micromamba/contrib-vllm/lib/python3.12/multiprocessing/process.py", line 108, in run (EngineCore_0 pid=2647201) self._target(*self._args, **self._kwargs) (EngineCore_0 pid=2647201) File "/scratch/vllm/vllm/v1/engine/core.py", line 716, in run_engine_core (EngineCore_0 pid=2647201) raise e (EngineCore_0 pid=2647201) File "/scratch/vllm/vllm/v1/engine/core.py", line 703, in run_engine_core (EngineCore_0 pid=2647201) engine_core = EngineCoreProc(*args, **kwargs) (EngineCore_0 pid=2647201) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_0 pid=2647201) File "/scratch/vllm/vllm/v1/eng...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: rrent environment ### 🐛 Describe the bug Running [PLaMo2.1](https://huggingface.co/pfnet/plamo-2.1-2b-cpt) using the recently introduced v1 support fails: ``` $ VLLM_USE_V1=1 vllm serve pfnet/plamo-2.1-2b-cpt --trust-re...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: er. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ct/vllm/pull/23998#issuecomment-3250186500 It seems like the `MambaSpec.page_size_bytes` is half of `SlidingWindowSpec.page_size_bytes` (not sure why, might be related to the model config). I will have to investigate th...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
