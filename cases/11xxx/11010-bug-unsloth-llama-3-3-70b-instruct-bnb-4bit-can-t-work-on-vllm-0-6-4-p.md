# vllm-project/vllm#11010: [Bug]: unsloth/Llama-3.3-70B-Instruct-bnb-4bit can't work on vllm 0.6.4.post1

| 字段 | 值 |
| --- | --- |
| Issue | [#11010](https://github.com/vllm-project/vllm/issues/11010) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: unsloth/Llama-3.3-70B-Instruct-bnb-4bit can't work on vllm 0.6.4.post1

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm using following command to load Llama3.3 on one GPU: ``` CUDA_VISIBLE_DEVICES=1 python3 -m vllm.entrypoints.openai.api_server --model unsloth/Llama-3.3-70B-Instruct-bnb-4bit --host 0.0.0.0 --port 8081 --seed 42 --trust-remote-code --enable-chunked-prefill --tensor-parallel-size 1 --max-model-len 1024 ``` Got error: ``` Loading safetensors checkpoint shards: 0% Completed | 0/8 [00:00<?, ?it/s] ERROR 12-09 00:49:29 engine.py:366] 'layers.0.mlp.down_proj.weight.absmax' ERROR 12-09 00:49:29 engine.py:366] Traceback (most recent call last): ERROR 12-09 00:49:29 engine.py:366] File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/engine.py", line 357, in run_mp_engine ERROR 12-09 00:49:29 engine.py:366] engine = MQLLMEngine.from_engine_args(engine_args=engine_args, ERROR 12-09 00:49:29 engine.py:366] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 12-09 00:49:29 engine.py:366] File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/engine.py", line 119, in from_engine_args ERROR 12-09 00:49:29 engine.py:366] return cls(ipc_path=ipc_path, ERROR 12-...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: be the bug I'm using following command to load Llama3.3 on one GPU: ``` CUDA_VISIBLE_DEVICES=1 python3 -m vllm.entrypoints.openai.api_server --model unsloth/Llama-3.3-70B-Instruct-bnb-4bit --host 0.0.0.0 --port 8081 --s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: unsloth/Llama-3.3-70B-Instruct-bnb-4bit can't work on vllm 0.6.4.post1 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm using following command to load Llama3....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: sloth/Llama-3.3-70B-Instruct-bnb-4bit can't work on vllm 0.6.4.post1 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm using following command to load Llama3.3 on one...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Bug]: unsloth/Llama-3.3-70B-Instruct-bnb-4bit can't work on vllm 0.6.4.post1 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm using following command to load Llama3....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
