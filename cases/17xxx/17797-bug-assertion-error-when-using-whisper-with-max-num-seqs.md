# vllm-project/vllm#17797: [Bug]: Assertion error when using Whisper with `--max-num-seqs`

| 字段 | 值 |
| --- | --- |
| Issue | [#17797](https://github.com/vllm-project/vllm/issues/17797) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Assertion error when using Whisper with `--max-num-seqs`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I encountered memory errors when deploying whisper on my GPU. Following #15216 I tried to change `--max-num-seqs`, but I hit an assertion error. ## Steps to reproduce Create the dockerfile ```docker FROM vllm/vllm-openai:v0.8.5.post1 RUN uv pip install --system vllm[audio]==v0.8.5.post1 ``` and then build and run the image ```bash docker build -t vllm-whisper -f Dockerfile . docker run --gpus all vllm-whisper --model=openai/whisper-large-v3 --task=transcription --max-num-seqs=2 ``` I see this error: ``` File "/usr/local/lib/python3.12/dist-packages/vllm/attention/backends/xformers.py", line 554, in forward assert query.shape[0] == num_prefill_query_tokens ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: -seqs`, but I hit an assertion error. ## Steps to reproduce Create the dockerfile ```docker FROM vllm/vllm-openai:v0.8.5.post1 RUN uv pip install --system vllm[audio]==v0.8.5.post1 ``` and then build and run the image `...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ends/xformers.py", line 554, in forward assert query.shape[0] == num_prefill_query_tokens ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ``` ### Before submitting a new issue... - [x] Make sure you already searched for rele...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: rror: ``` File "/usr/local/lib/python3.12/dist-packages/vllm/attention/backends/xformers.py", line 554, in forward assert query.shape[0] == num_prefill_query_tokens ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ``` ### Bef...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: i_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding attention;cuda;operator;quantization;sampling;triton build_error;crash;nan_inf...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
