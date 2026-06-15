# vllm-project/vllm#15550: [Installation]: Transformer installation requires uv venv --system now

| 字段 | 值 |
| --- | --- |
| Issue | [#15550](https://github.com/vllm-project/vllm/issues/15550) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Transformer installation requires uv venv --system now

### Issue 正文摘录

Hi all, a small one I can take care of is a breaking change introduced in https://github.com/vllm-project/vllm/commit/7ffcccfa5ca3ef6b56c292ad2489e077a5cdd6f5#diff-dd2c0eb6ea5cfc6c4bd4eac30934e2d5746747af48fef6da689e85b752f39557R62 The installation instructions in [here](https://docs.vllm.ai/en/latest/deployment/docker.html#deployment-docker-pre-built-image) should probably include `--system` as in: `RUN uv pip install --system git+https://github.com/huggingface/transformers.git` Thanks for your hard work! ### How you are installing vllm ```sh pip install -vvv vllm ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Installation]: Transformer installation requires uv venv --system now installation Hi all, a small one I can take care of is a breaking change introduced in https://github.com/vllm-project/vllm/commit/7ffcccfa5ca3ef6b5
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: former installation requires uv venv --system now installation Hi all, a small one I can take care of is a breaking change introduced in https://github.com/vllm-project/vllm/commit/7ffcccfa5ca3ef6b56c292ad2489e077a5cdd6...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: e `--system` as in: `RUN uv pip install --system git+https://github.com/huggingface/transformers.git` Thanks for your hard work! ### How you are installing vllm ```sh pip install -vvv vllm ``` ### Before submitting a ne...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: 57R62 The installation instructions in [here](https://docs.vllm.ai/en/latest/deployment/docker.html#deployment-docker-pre-built-image) should probably include `--system` as in: `RUN uv pip install --system git+https://g...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
