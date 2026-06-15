# vllm-project/vllm#25227: [Bug]: internVL3.5 38B not working in vlllm 0.10.2

| 字段 | 值 |
| --- | --- |
| Issue | [#25227](https://github.com/vllm-project/vllm/issues/25227) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;gemm;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: internVL3.5 38B not working in vlllm 0.10.2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I was able to start vllm server for InternVL 3.5 38B in 0.10.1; for latest release 0.10.2 (where video support for this model should be working), vllm server crashes: python3 -m vllm.entrypoints.openai.api_server --served-model-name internvl-35-38b --model internvl3538b --tensor-parallel-size 4 --gpu-memory-utilization 0.95 --max-seq-len-to-capture 8192 --trust-remote-code --limit-mm-per-prompt '{"image":5, "video": 1}' --disable-log-requests --enable-chunked-prefill ... ckages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl (Worker_TP0 pid=411) ERROR 09-18 20:37:55 [multiproc_executor.py:654] return self._call_impl(*args, **kwargs) (Worker_TP0 pid=411) ERROR 09-18 20:37:55 [multiproc_executor.py:654] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker_TP0 pid=411) ERROR 09-18 20:37:55 [multiproc_executor.py:654] File "/usr/local/lib/python3.12/dist-packages/torch/nn/modules/module.py", line 1784, in _call_impl (Worker_TP0 pid=411) ERROR 09-18 20:37:55 [multiproc_executor.py:654] return forward_call(*args, **kwargs) (Worker_TP0 pid=411) ERROR 09-18 20:37:55 [multiproc_executor.py:654] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker_TP0...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: internVL3.5 38B not working in vlllm 0.10.2 bug ### Your current environment ### 🐛 Describe the bug I was able to start vllm server for InternVL 3.5 38B in 0.10.1; for latest release 0.10.2 (where video support f...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits attention;cuda;gemm;operator;sampling;tri...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: emote-code --limit-mm-per-prompt '{"image":5, "video": 1}' --disable-log-requests --enable-chunked-prefill ... ckages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl (Worker_TP0 pid=411) ERROR 09-18 20:37:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: use ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: I was able to start vllm server for InternVL 3.5 38B in 0.10.1; for latest release 0.10.2 (where video support for this model should be working), vllm server crashes: python3 -m vllm.entrypoints.openai.api_server --serv...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
