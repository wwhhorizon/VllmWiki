# vllm-project/vllm#25842: [Usage]: Problem with concurrency in encoder-based embedder serving with V1 Engine

| 字段 | 值 |
| --- | --- |
| Issue | [#25842](https://github.com/vllm-project/vllm/issues/25842) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Problem with concurrency in encoder-based embedder serving with V1 Engine

### Issue 正文摘录

### Your current environment ### How would you like to use vllm Dear vLLM team : ) I would like to ask a question regarding the embedding model serving, specifically [BAAI/bge-large-en-v1.5](https://huggingface.co/BAAI/bge-large-en-v1.5) model. I served it with cli command: ```bash vllm serve BAAI/bge-large-en-v1.5 --max-model-len 512 --gpu-memory-utilization 0.9 --max-num-batched-tokens 819200 --max-num-seqs 1600 --dtype float32 --override-pooler-config {pooling_type: MEAN, normalize: true} --enforce-eager ``` - `--enforce-eager` I recently discovered that in vLLM 0.10.2, with V1, I have to put this flag to make the engine run for this model. Found it [here](https://github.com/vllm-project/vllm/issues/25060#issuecomment-3302040286) - More importantly, when I perform a k6 load-test on the vllm embedding server, I found the server handle the incoming requests one after another without multiple requests being processed at the same time. I tried tuning the `--max-num-seqs` or `--max-num-batched-tokens`, it didn't help. The only thing helps but not by a lot is the `--api-server-count` argument. I would like to ask what is the correct configurations to handle X incoming requests at the...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: I would like to ask a question regarding the embedding model serving, specifically [BAAI/bge-large-en-v1.5](https://huggingface.co/BAAI/bge-large-en-v1.5) model. I served it with cli command: ```bash vllm serve BAAI/bge...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ar vLLM team : ) I would like to ask a question regarding the embedding model serving, specifically [BAAI/bge-large-en-v1.5](https://huggingface.co/BAAI/bge-large-en-v1.5) model. I served it with cli command: ```bash vl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: with concurrency in encoder-based embedder serving with V1 Engine usage;stale ### Your current environment ### How would you like to use vllm Dear vLLM team : ) I would like to ask a question regarding the embedding mod...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ry-utilization 0.9 --max-num-batched-tokens 819200 --max-num-seqs 1600 --dtype float32 --override-pooler-config {pooling_type: MEAN, normalize: true} --enforce-eager ``` - `--enforce-eager` I recently discovered that in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: : ) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
