# vllm-project/vllm#1121: AssertionError: Prompt input should have only one seq.

| 字段 | 值 |
| --- | --- |
| Issue | [#1121](https://github.com/vllm-project/vllm/issues/1121) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> AssertionError: Prompt input should have only one seq.

### Issue 正文摘录

- OS: **Ubuntu 22.04** - GPUs: **2x 4090** (2x 24GB) - CUDA: **11.8** - CPU: **Ryzen 3800X** - RAM: **64GB** - vLLM build: **main** `400b8289` Started the API server with this command: ```sh python -O -u -m vllm.entrypoints.api_server \ --host=0.0.0.0 \ --port=8000 \ --model=$HOME/models/WizardLM/WizardCoder-Python-13B-V1.0 \ --tokenizer=hf-internal-testing/llama-tokenizer \ --tensor-parallel-size=2 \ --block-size=16 \ --swap-space=8 ``` After running for a few minutes it crashes with `500 Internal server error`. Error in the log: ``` AssertionError: Prompt input should have only one seq. ``` Please find the full log attached: [vllm-server-error.log.gz](https://github.com/vllm-project/vllm/files/12680614/vllm-server-error.log.gz) I've removed the part with all the successful requests to redact the prompts, but kept the failed request in full. Tested with the latest official version (0.1.7), it worked perfectly for the first attempt with the exact same prompts. However the order may have been different due to running up to 32 generations in parallel. The above error with the custom build happened 3 times in a row, so it does not seem to depend on the order of prompts, however. **UP...

## 现有链接修复摘要

#41606 Bump the minor-update group across 1 directory with 140 updates | #41766 Bump the minor-update group across 1 directory with 141 updates | #41859 Bump the minor-update group across 1 directory with 141 updates | #42056 Bump the minor-update group across 1 directory with 142 updates | #42717 Bump the minor-update group across 1 directory with 143 updates | #43505 Bump the minor-update group across 1 directory with 145 updates | #43993 Bump the minor-update group across 1 directory with 147 updates

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: (2x 24GB) - CUDA: **11.8** - CPU: **Ryzen 3800X** - RAM: **64GB** - vLLM build: **main** `400b8289` Started the API server with this command: ```sh python -O -u -m vllm.entrypoints.api_server \ --host=0.0.0.0 \ --port=8...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: lm.entrypoints.api_server \ --host=0.0.0.0 \ --port=8000 \ --model=$HOME/models/WizardLM/WizardCoder-Python-13B-V1.0 \ --tokenizer=hf-internal-testing/llama-tokenizer \ --tensor-parallel-size=2 \ --block-size=16 \ --swa...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: -internal-testing/llama-tokenizer \ --tensor-parallel-size=2 \ --block-size=16 \ --swap-space=8 ``` After running for a few minutes it crashes with `500 Internal server error`. Error in the log: ``` AssertionError: Prom...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: AssertionError: Prompt input should have only one seq. bug;stale - OS: **Ubuntu 22.04** - GPUs: **2x 4090** (2x 24GB) - CUDA: **11.8** - CPU: **Ryzen 3800X** - RAM: **64GB** - vLLM build: **main** `400b8289` Started the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ne seq. bug;stale - OS: **Ubuntu 22.04** - GPUs: **2x 4090** (2x 24GB) - CUDA: **11.8** - CPU: **Ryzen 3800X** - RAM: **64GB** - vLLM build: **main** `400b8289` Started the API server with this command: ```sh python -O...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41606](https://github.com/vllm-project/vllm/pull/41606) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 140 updates | href="https://redirect.github.com/prometheus/client_python/pull/1121">prometheus/client_python#1121</a></li> <li>fix(multiprocess): avoid double-building child metric names (<a hr… |
| [#41766](https://github.com/vllm-project/vllm/pull/41766) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 141 updates | href="https://redirect.github.com/prometheus/client_python/pull/1121">prometheus/client_python#1121</a></li> <li>fix(multiprocess): avoid double-building child metric names (<a hr… |
| [#41859](https://github.com/vllm-project/vllm/pull/41859) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 141 updates | href="https://redirect.github.com/prometheus/client_python/pull/1121">prometheus/client_python#1121</a></li> <li>fix(multiprocess): avoid double-building child metric names (<a hr… |
| [#42056](https://github.com/vllm-project/vllm/pull/42056) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 142 updates | href="https://redirect.github.com/prometheus/client_python/pull/1121">prometheus/client_python#1121</a></li> <li>fix(multiprocess): avoid double-building child metric names (<a hr… |
| [#42717](https://github.com/vllm-project/vllm/pull/42717) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 143 updates | href="https://redirect.github.com/prometheus/client_python/pull/1121">prometheus/client_python#1121</a></li> <li>fix(multiprocess): avoid double-building child metric names (<a hr… |
| [#43505](https://github.com/vllm-project/vllm/pull/43505) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 145 updates | href="https://redirect.github.com/prometheus/client_python/pull/1121">prometheus/client_python#1121</a></li> <li>fix(multiprocess): avoid double-building child metric names (<a hr… |
| [#43993](https://github.com/vllm-project/vllm/pull/43993) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 147 updates | href="https://redirect.github.com/prometheus/client_python/pull/1121">prometheus/client_python#1121</a></li> <li>fix(multiprocess): avoid double-building child metric names (<a hr… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
