# vllm-project/vllm#15751: [Installation]: How to install vllm on an M40 GPU?

| 字段 | 值 |
| --- | --- |
| Issue | [#15751](https://github.com/vllm-project/vllm/issues/15751) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;model_support |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: How to install vllm on an M40 GPU?

### Issue 正文摘录

### Your current environment My GPU is an M40, and the capability value is 5.2. ``` (base) root@7313fb5368b7:/workspace# python -c "import torch; print(torch.cuda.get_device_capability())" (5, 2) ``` Now, I want to install vllm to run the qwen2.5-1.5b model. However, I am unable to successfully install vllm from the source code. The command I used for installation is: `pip install -e .` ### How you are installing vllm ```sh pip install -e . ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Installation]: How to install vllm on an M40 GPU? installation;stale ### Your current environment My GPU is an M40, and the capability value is 5.2. ``` (base) root@7313fb5368b7:/workspace# python -c "import torch; prin
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: stallation;stale ### Your current environment My GPU is an M40, and the capability value is 5.2. ``` (base) root@7313fb5368b7:/workspace# python -c "import torch; print(torch.cuda.get_device_capability())" (5, 2) ``` No...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: _device_capability())" (5, 2) ``` Now, I want to install vllm to run the qwen2.5-1.5b model. However, I am unable to successfully install vllm from the source code. The command I used for installation is: `pip install -...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Installation]: How to install vllm on an M40 GPU? installation;stale ### Your current environment My GPU is an M40, and the capability value is 5.2. ``` (base) root@7313fb5368b7:/workspace# python -c "import torch; pri...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;model_support cuda env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
