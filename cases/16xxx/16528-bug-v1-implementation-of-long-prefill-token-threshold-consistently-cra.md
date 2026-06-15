# vllm-project/vllm#16528: [Bug]: V1 implementation of --long-prefill-token-threshold consistently crashes

| 字段 | 值 |
| --- | --- |
| Issue | [#16528](https://github.com/vllm-project/vllm/issues/16528) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: V1 implementation of --long-prefill-token-threshold consistently crashes

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Was trying out this new parameter since I saw it in 0.8.3's changelog. vLLM consistently crashes with `--long-prefill-token-threshold` set to `8192` and this Gutenberg Library sample text file as part of a prompt (~40k tokens): [40k.txt](https://github.com/user-attachments/files/19717747/40k.txt) The crash: ``` INFO 04-11 21:46:13 [async_llm.py:228] Added request chatcmpl-7c3909107865459697d63676b732c53b. INFO: 10.39.171.204:35960 - "POST /v1/chat/completions HTTP/1.1" 200 OK ERROR 04-11 21:46:13 [core.py:390] EngineCore hit an exception: Traceback (most recent call last): ERROR 04-11 21:46:13 [core.py:390] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 383, in run_engine_core ERROR 04-11 21:46:13 [core.py:390] engine_core.run_busy_loop() ERROR 04-11 21:46:13 [core.py:390] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 405, in run_busy_loop ERROR 04-11 21:46:13 [core.py:390] self._process_engine_step() ERROR 04-11 21:46:13 [core.py:390] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 434, in _process_engine_step ERROR 04-11 21:46:13 [core.py:390...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: V1 implementation of --long-prefill-token-threshold consistently crashes bug;stale ### Your current environment ### 🐛 Describe the bug Was trying out this new parameter since I saw it in 0.8.3's changelog. vLLM c...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding cuda;...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: s the crashing from occurring. The rest of our parameters (llama 4 scout FP8 quant): ``` extraVllmArgs: - "\"--enable-chunked-prefill\"" **- "\"--long-prefill-token-threshold\"" - "\"8192\""** - "\"--gpu-memory-utilizat...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: argument stops the crashing from occurring. The rest of our parameters (llama 4 scout FP8 quant): ``` extraVllmArgs: - "\"--enable-chunked-prefill\"" **- "\"--long-prefill-token-threshold\"" - "\"8192\""** - "\"--gpu-me...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
