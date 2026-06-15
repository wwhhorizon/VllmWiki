# vllm-project/vllm#15101: [Bug]: Run DeepSeek-R1-awq model  on AMD MI210 meet an error

| 字段 | 值 |
| --- | --- |
| Issue | [#15101](https://github.com/vllm-project/vllm/issues/15101) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Run DeepSeek-R1-awq model  on AMD MI210 meet an error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug command line code: VLLM_WORKER_MULTIPROC_METHOD=spawn python -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 12345 --max-model-len 65536 --max-num-batched-tokens 65536 --trust-remote-code --tensor-parallel-size 8 --gpu-memory-utilization 0.97 --dtype float16 --served-model-name deepseek-reasoner --model ./deepseek-awq-4/ The DeepSeek R1 model is from https://[huggingface.co](https://huggingface.co/cognitivecomputations/DeepSeek-R1-awq)/cognitivecomputations/DeepSeek-R1-awq the error is assert self.quant_method is not None AssertionError [error.log](https://github.com/user-attachments/files/19334936/error.log) Thanks for your help! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#41606 Bump the minor-update group across 1 directory with 140 updates | #41766 Bump the minor-update group across 1 directory with 141 updates | #41859 Bump the minor-update group across 1 directory with 141 updates | #42056 Bump the minor-update group across 1 directory with 142 updates | #42717 Bump the minor-update group across 1 directory with 143 updates

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;quantization;sampling...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ust-remote-code --tensor-parallel-size 8 --gpu-memory-utilization 0.97 --dtype float16 --served-model-name deepseek-reasoner --model ./deepseek-awq-4/ The DeepSeek R1 model is from https://[huggingface.co](https://huggi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: lp! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Run DeepSeek-R1-awq model on AMD MI210 meet an error bug;stale ### Your current environment ### 🐛 Describe the bug command line code: VLLM_WORKER_MULTIPROC_METHOD=spawn python -m vllm.entrypoints.openai.api_serve...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Run DeepSeek-R1-awq model on AMD MI210 meet an error bug;stale ### Your current environment ### 🐛 Describe the bug command line code: VLLM_WORKER_MULTIPROC_METHOD=spawn python -m vllm.entrypoints.openai.api_serve...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41606](https://github.com/vllm-project/vllm/pull/41606) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 140 updates | s (<a href="https://redirect.github.com/fastapi/fastapi/issues/15101">#15101</a>)</li> <li><a href="https://github.com/fastapi/fastapi/commit/ef1c927b0558d414e199a666833942a6fabb3… |
| [#41766](https://github.com/vllm-project/vllm/pull/41766) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 141 updates | s (<a href="https://redirect.github.com/fastapi/fastapi/issues/15101">#15101</a>)</li> <li><a href="https://github.com/fastapi/fastapi/commit/ef1c927b0558d414e199a666833942a6fabb3… |
| [#41859](https://github.com/vllm-project/vllm/pull/41859) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 141 updates | s (<a href="https://redirect.github.com/fastapi/fastapi/issues/15101">#15101</a>)</li> <li><a href="https://github.com/fastapi/fastapi/commit/ef1c927b0558d414e199a666833942a6fabb3… |
| [#42056](https://github.com/vllm-project/vllm/pull/42056) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 142 updates | s (<a href="https://redirect.github.com/fastapi/fastapi/issues/15101">#15101</a>)</li> <li><a href="https://github.com/fastapi/fastapi/commit/ef1c927b0558d414e199a666833942a6fabb3… |
| [#42717](https://github.com/vllm-project/vllm/pull/42717) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 143 updates | s (<a href="https://redirect.github.com/fastapi/fastapi/issues/15101">#15101</a>)</li> <li><a href="https://github.com/fastapi/fastapi/commit/ef1c927b0558d414e199a666833942a6fabb3… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
