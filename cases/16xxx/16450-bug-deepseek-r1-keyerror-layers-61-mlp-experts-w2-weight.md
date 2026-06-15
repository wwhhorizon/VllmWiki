# vllm-project/vllm#16450: [Bug]: DeepSeek-R1 KeyError: 'layers.61.mlp.experts.w2_weight'

| 字段 | 值 |
| --- | --- |
| Issue | [#16450](https://github.com/vllm-project/vllm/issues/16450) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: DeepSeek-R1 KeyError: 'layers.61.mlp.experts.w2_weight'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug - cmd ```bash export VLLM_USE_V1=0 && export VLLM_PP_LAYER_PARTITION="22,20,19" nohup python3 -m vllm.entrypoints.openai.api_server \ --model=/workspace/dev/hf_models/DeepSeek-R1 \ --dtype=auto \ --block-size 32 \ --tokenizer-mode=slow \ --max-model-len 32768 \ --max-num-batched-tokens 2048 \ --tensor-parallel-size 8 \ --pipeline-parallel-size 3 \ --gpu-memory-utilization 0.90 \ --max-num-seqs 48 \ --trust-remote-code \ --no-enable-prefix-caching \ --enable-chunked-prefill=True \ --disable-custom-all-reduce \ --max-log-len 0 \ --port 8862 > vllm.R1.log.3 2>&1 & ``` - error ```bash quantized or ignored modules [repeated 22x across cluster] (RayWorkerWrapper pid=269885, ip=10.189.109.87) ERROR 04-11 11:26:12 [worker_base.py:620] Error executing method 'load_model'. This might cause deadlock in distributed execution. [repeated 7x across cluster] (RayWorkerWrapper pid=269885, ip=10.189.109.87) ERROR 04-11 11:26:12 [worker_base.py:620] Traceback (most recent call last): [repeated 7x across cluster] (RayWorkerWrapper pid=269885, ip=10.189.109.87) ERROR 04-11 11:26:12 [worker_base.py:620] File "/usr/local/lib/python3.10/dist-packages/vl...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 2,20,19" nohup python3 -m vllm.entrypoints.openai.api_server \ --model=/workspace/dev/hf_models/DeepSeek-R1 \ --dtype=auto \ --block-size 32 \ --tokenizer-mode=slow \ --max-model-len 32768 \ --max-num-batched-tokens 204...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: erver \ --model=/workspace/dev/hf_models/DeepSeek-R1 \ --dtype=auto \ --block-size 32 \ --tokenizer-mode=slow \ --max-model-len 32768 \ --max-num-batched-tokens 2048 \ --tensor-parallel-size 8 \ --pipeline-parallel-size...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ote-code \ --no-enable-prefix-caching \ --enable-chunked-prefill=True \ --disable-custom-all-reduce \ --max-log-len 0 \ --port 8862 > vllm.R1.log.3 2>&1 & ``` - error ```bash quantized or ignored modules [repeated 22x a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: /openai/api_server.py", line 1069, in run_server [rank0]: async with build_async_engine_client(args) as engine_client: [rank0]: File "/usr/lib/python3.10/contextlib.py", line 199, in __aenter__ [rank0]: return await ane...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
