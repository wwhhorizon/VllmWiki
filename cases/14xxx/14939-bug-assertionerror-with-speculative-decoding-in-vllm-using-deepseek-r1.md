# vllm-project/vllm#14939: [Bug]:   AssertionError with Speculative Decoding in vLLM Using DeepSeek R1 Distill Qwen Models

| 字段 | 值 |
| --- | --- |
| Issue | [#14939](https://github.com/vllm-project/vllm/issues/14939) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:   AssertionError with Speculative Decoding in vLLM Using DeepSeek R1 Distill Qwen Models

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When attempting to use speculative decoding in vLLM with the following models: - Main Model: deepseek-ai/DeepSeek-R1-Distill-Qwen-7B - Draft Model: deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B I encounter the following error: ``` assert all(vocab_sizes[0] == vocab_size for vocab_size in vocab_sizes) AssertionError Process SpawnProcess-1? ``` This is the full error code > INFO 03-17 16:21:39 model_runner.py:1115] Loading model weights took 3.3143 GB > INFO 03-17 16:21:40 spec_decode_worker.py:380] [Speculative Decoding] Use batch expansion for scoring proposals. > ERROR 03-17 16:21:40 engine.py:400] > Traceback (most recent call last): > File "/home/api-server/miniconda3/envs/vllm/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 391, in run_mp_engine > engine = MQLLMEngine.from_engine_args(engine_args=engine_args, > File "/home/api-server/miniconda3/envs/vllm/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 124, in from_engine_args > return cls(ipc_path=ipc_path, > File "/home/api-server/miniconda3/envs/vllm/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 76,...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: AssertionError with Speculative Decoding in vLLM Using DeepSeek R1 Distill Qwen Models bug;stale ### Your current environment ### 🐛 Describe the bug When attempting to use speculative decoding in vLLM with the fo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: rypoints/openai/api_server.py", line 947, in run_server > async with build_async_engine_client(args) as engine_client: > File "/home/api-server/miniconda3/envs/vllm/lib/python3.10/contextlib.py", line 199, in __aenter__...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: sertionError with Speculative Decoding in vLLM Using DeepSeek R1 Distill Qwen Models bug;stale ### Your current environment ### 🐛 Describe the bug When attempting to use speculative decoding in vLLM with the following m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: el. ### Before submitting a new issue... - [ ] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: this process. In rare cases this process can exit before this point and block the progress of another member of the process group. This constraint has always been present, but this warning has only been added since PyTo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
