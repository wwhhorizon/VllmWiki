# vllm-project/vllm#26434: [Bug]: `gpt-oss` dependency disallows vllm usage with python<=3.11

| 字段 | 值 |
| --- | --- |
| Issue | [#26434](https://github.com/vllm-project/vllm/issues/26434) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `gpt-oss` dependency disallows vllm usage with python<=3.11

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm added `gpt-oss>=0.0.7` as a dependency 3 days ago (see [here](https://github.com/vllm-project/vllm/commit/91ac7f764d04e7a9103e3c839244ce241a43b45e#diff-bf1b1fe7bf334bb5f5589d4366b2c17ea1f5a3a45668188aef31c324f2a34f20R52)). `gpt-oss` [requires python>=3.12](https://pypi.org/project/gpt-oss/) for both 0.0.7 and 0.0.8. This breaks vllm compatibility with any python version less than 3.12 Running with `--ignore-requires-python` can circumvent, but without it I get the following error when installing from main on python 3.10 ``` (projects) ➜ vllm git:(main) VLLM_USE_PRECOMPILED=1 uv pip install -e . Using Python 3.10.12 environment at: /home/bdellabe/projects/.venv × No solution found when resolving dependencies: ╰─▶ Because the current Python version (3.10.12) does not satisfy Python>=3.12 and gpt-oss>=0.0.7 depends on Python>=3.12, we can conclude that gpt-oss>=0.0.7 cannot be used. And because only the following versions of gpt-oss are available: gpt-oss =0.0.7, we can conclude that vllm==0.11.1rc1.dev317+g4ba887574.precompiled cannot be used. And because only vllm==0.11.1rc1.dev317+g4ba887574.precompiled is available and you...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: `gpt-oss` dependency disallows vllm usage with python<=3.11 bug ### Your current environment ### 🐛 Describe the bug vllm added `gpt-oss>=0.0.7` as a dependency 3 days ago (see [here](https://github.com/vllm-proje...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: `gpt-oss` dependency disallows vllm usage with python<=3.11 bug ### Your current environment ### 🐛 Describe the bug vllm added `gpt-oss>=0.0.7` as a dependency 3 days ago (see [here](https://github.com/vllm-proje...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: uild;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
