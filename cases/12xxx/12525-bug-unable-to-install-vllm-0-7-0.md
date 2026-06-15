# vllm-project/vllm#12525: [Bug]: unable to install `vllm==0.7.0`

| 字段 | 值 |
| --- | --- |
| Issue | [#12525](https://github.com/vllm-project/vllm/issues/12525) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: unable to install `vllm==0.7.0`

### Issue 正文摘录

### Your current environment ### Model Input Dumps n/a ### 🐛 Describe the bug Running an install with `uv` (coming from https://github.com/astral-sh/uv/issues/11038): ```none > uv cache clean --quiet > uv pip install vllm==0.7.0 Resolved 113 packages in 1.28s × Failed to download and build `vllm==0.7.0` ╰─▶ Package metadata version `0.7.0+cpu` does not match given version `0.7.0` ``` Alternately, running this with `pip`: ```none > pip cache purge --quiet > pip install vllm==0.7.0 Collecting vllm==0.7.0 Downloading vllm-0.7.0.tar.gz (5.0 MB) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.0/5.0 MB 24.9 MB/s eta 0:00:00 Installing build dependencies ... done Getting requirements to build wheel ... done Preparing metadata (pyproject.toml) ... done Discarding https://files.pythonhosted.org/packages/fd/1c/602eafc32a1f6ddf66f4700f30fd4039e20c04a9ef9334e32fb18270cda2/vllm-0.7.0.tar.gz (from https://pypi.org/simple/vllm/) (requires-python:>=3.9): Requested vllm==0.7.0 from https://files.pythonhosted.org/packages/fd/1c/602eafc32a1f6ddf66f4700f30fd4039e20c04a9ef9334e32fb18270cda2/vllm-0.7.0.tar.gz has inconsistent version: expected '0.7.0', but metadata has '0.7.0+cpu' ERROR: Ignored the followi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: unable to install `vllm==0.7.0` bug ### Your current environment ### Model Input Dumps n/a ### 🐛 Describe the bug Running an install with `uv` (coming from https://github.com/astral-sh/uv/issues/11038): ```none >...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: m`? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: es in 1.28s × Failed to download and build `vllm==0.7.0` ╰─▶ Package metadata version `0.7.0+cpu` does not match given version `0.7.0` ``` Alternately, running this with `pip`: ```none > pip cache purge --quiet > pip in...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: unable to install `vllm==0.7.0` bug ### Your current environment ### Model Input Dumps n/a ### 🐛 Describe the bug Running an install with `uv` (coming from https://github.com/astral-sh/uv/issues/11038): ```none > uv cac...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: 7.0.tar.gz (from https://pypi.org/simple/vllm/) (requires-python:>=3.9): Requested vllm==0.7.0 from https://files.pythonhosted.org/packages/fd/1c/602eafc32a1f6ddf66f4700f30fd4039e20c04a9ef9334e32fb18270cda2/vllm-0.7.0.t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
