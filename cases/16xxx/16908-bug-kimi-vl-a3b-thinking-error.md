# vllm-project/vllm#16908: [Bug]: Kimi-VL-A3B-Thinking Error

| 字段 | 值 |
| --- | --- |
| Issue | [#16908](https://github.com/vllm-project/vllm/issues/16908) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Kimi-VL-A3B-Thinking Error

### Issue 正文摘录

### Your current environment Installation method for vLLM: `pip install vllm --pre --extra-index-url https://wheels.vllm.ai/nightly` Run command: `vllm serve /mnt/model/Kimi-VL-A3B-Thinking/ --port 22345 --tensor-parallel-size 1 --limit-mm-per-prompt image=1 --max-model-len 40000 --dtype bfloat16 --trust-remote-code --served-model-name Kimi-VL-A3B-Thinking` ### 🐛 Describe the bug Using the latest version of vLLM results in the following error: ERROR 04-21 01:55:57 [core.py:392] EngineCore encountered a fatal error. ERROR 04-21 01:55:57 [core.py:392] Traceback (most recent call last): ERROR 04-21 01:55:57 [core.py:392] File "/usr/local/lib/python3.10/dist-packages/vllm/v1/engine/core.py", line 383, in run_engine_core ERROR 04-21 01:55:57 [core.py:392] engine_core.run_busy_loop() ERROR 04-21 01:55:57 [core.py:392] File "/usr/local/lib/python3.10/dist-packages/vllm/v1/engine/core.py", line 407, in run_busy_loop ERROR 04-21 01:55:57 [core.py:392] self._process_engine_step() ERROR 04-21 01:55:57 [core.py:392] File "/usr/local/lib/python3.10/dist-packages/vllm/v1/engine/core.py", line 436, in _process_engine_step ERROR 04-21 01:55:57 [core.py:392] outputs = self.step_fn() ERROR 04-21 01...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Bug]: Kimi-VL-A3B-Thinking Error bug;stale ### Your current environment Installation method for vLLM: `pip install vllm --pre --extra-index-url https://wheels.vllm.ai/nightly` Run command: `vllm serve /mnt/model/Kimi-VL...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: -parallel-size 1 --limit-mm-per-prompt image=1 --max-model-len 40000 --dtype bfloat16 --trust-remote-code --served-model-name Kimi-VL-A3B-Thinking` ### 🐛 Describe the bug Using the latest version of vLLM results in the...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: line 589, in _prepare_inputs ERROR 04-21 01:55:57 [core.py:392] attn_metadata = self.attn_metadata_builder.build( ERROR 04-21 01:55:57 [core.py:392] File "/usr/local/lib/python3.10/dist-packages/vllm/v1/attention/backen...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Kimi-VL-A3B-Thinking Error bug;stale ### Your current environment Installation method for vLLM: `pip install vllm --pre --extra-index-url https://wheels.vllm.ai/nightly` Run command: `vllm serve /mnt/model/Kimi-V...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: y:392] File "/usr/local/lib/python3.10/dist-packages/vllm/v1/attention/backends/mla/common.py", line 508, in build ERROR 04-21 01:55:57 [core.py:392] self.page_size) ERROR 04-21 01:55:57 [core.py:392] AttributeError: 'M...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
